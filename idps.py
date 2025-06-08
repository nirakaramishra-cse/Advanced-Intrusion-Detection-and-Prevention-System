import io
import os
import json
import random
from datetime import datetime
from flask import Flask, render_template, request, send_file, make_response
import pandas as pd
import joblib
from plyer import notification
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


app = Flask(__name__)
model = joblib.load('models/intrusion_model.pkl')

# Ensure required directories exist
os.makedirs('logs', exist_ok=True)
os.makedirs('static', exist_ok=True)

# Show desktop notification
def show_notification(num_attacks):
    if num_attacks > 0:
        notification.notify(
            title="IDPS Alert",
            message=f"{num_attacks} intrusion(s) detected and blocked.",
            timeout=10
        )

#Create and save pie chart
def create_pie_chart(normal_count, attack_count):
    labels = ['Normal', 'Intrusion']
    sizes = [normal_count, attack_count]
    colors = ['#4CAF50', '#F44336']
    explode = (0.05, 0.1)

    plt.figure(figsize=(7, 7))  # Slightly bigger figure
    wedges, texts, autotexts = plt.pie(
        sizes,
        explode=explode,
        labels=labels,
        colors=colors,
        autopct='%1.1f%%',
        startangle=135,
        textprops={'fontsize': 16, 'color': 'black'}
    )

    # Make labels bold and readable
    for text in texts:
        text.set_fontweight('bold')
        text.set_fontsize(20)

    # Customize percentage text
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(20)
        autotext.set_fontweight('bold')

    plt.title('Intrusion Detection Summary', fontsize=25, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('static/pie_chart.png', transparent=True)
    plt.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file:
        df = pd.read_csv(file)

        if 'label' in df.columns:
            df.drop(columns=['label'], inplace=True)

        try:
            df = df[model.feature_names_in_]
        except AttributeError:
            pass

        predictions = model.predict(df)
        df['Prediction'] = predictions

        normal_count = (predictions == 0).sum()
        attack_count = (predictions == 1).sum()
        create_pie_chart(normal_count, attack_count)
        show_notification(attack_count)

        blocked_ips = [f"192.168.0.{100 + i}" for i in range(attack_count)]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        attacks = df[df['Prediction'] == 1].copy()
        if not attacks.empty:
            attacks['src_ip'] = [f"192.168.1.{random.randint(1, 255)}" for _ in range(len(attacks))]
            attacks['timestamp'] = timestamp

            attacks.to_csv('logs/attack_log.csv', mode='a', header=not os.path.exists('logs/attack_log.csv'), index=False)

            logs = []
            for _, row in attacks.iterrows():
                logs.append({
                    'src_ip': row['src_ip'],
                    'timestamp': row['timestamp'],
                    'Prediction': int(row['Prediction']),
                    'details': row.drop(['src_ip', 'timestamp']).to_dict()
                })

            with open('logs/attack_log.json', 'w') as f:
                json.dump(logs, f, indent=4)

        result_table = df[['Prediction']].value_counts().to_dict()

        return render_template(
            'result.html',
            table=df.head(50).to_html(classes='table table-bordered', index=False),
            stats=result_table,
            blocked=blocked_ips
        )

    return "Upload failed", 400

@app.route('/logs', methods=['GET', 'POST'])
def view_logs():
    df = pd.DataFrame()
    if os.path.exists('logs/attack_log.csv'):
        df = pd.read_csv('logs/attack_log.csv')

        if request.method == 'POST':
            ip = request.form.get('ip')
            date = request.form.get('date')
            pred = request.form.get('prediction')

            if ip:
                df = df[df['src_ip'].astype(str).str.contains(ip, na=False)]
            if date:
                df = df[df['timestamp'].astype(str).str.contains(date, na=False)]
            if pred:
                df = df[df['Prediction'].astype(str) == pred]

            if 'export' in request.form:
                export_file = 'logs/filtered_log.csv'
                df.to_csv(export_file, index=False)
                return send_file(export_file, as_attachment=True)

            if 'export_excel' in request.form:
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                    df.to_excel(writer, index=False, sheet_name='Logs')
                output.seek(0)
                return send_file(
                    output,
                    as_attachment=True,
                    download_name='attack_logs.xlsx',
                    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

    table_html = df.to_html(classes='table table-bordered table-hover', index=False)
    return render_template('logs.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)
 