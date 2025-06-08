
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def preprocess_data(input_file, output_file):
    # Load column names
    col_names = [
        'duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent',
        'hot','num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root',
        'num_file_creations','num_shells','num_access_files','num_outbound_cmds','is_host_login',
        'is_guest_login','count','srv_count','serror_rate','srv_serror_rate','rerror_rate','srv_rerror_rate',
        'same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count',
        'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate',
        'dst_host_srv_diff_host_rate','dst_host_serror_rate','dst_host_srv_serror_rate',
        'dst_host_rerror_rate','dst_host_srv_rerror_rate','label', 'difficulty'
]
    # Load the dataset
    data = pd.read_csv(input_file, names=col_names, header=None, sep=",")
    print(f"✅ Loaded data from {input_file} | Shape: {data.shape}")

    # Strip whitespace
    for col in data.columns:
        data[col] = data[col].astype(str).str.strip()

    # Convert label to binary
    data['label'] = data['label'].apply(lambda x: 0 if x.lower() == 'normal' else 1)

    # Encode categorical columns
    cat_cols = ['protocol_type', 'service', 'flag']
    for col in cat_cols:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])

    # Convert all remaining columns to numeric
    numeric_cols = data.columns.drop('label')
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce')

    # Print non-numeric check
    non_numeric = data[numeric_cols].select_dtypes(exclude=['number']).columns.tolist()
    if non_numeric:
        print(f"❌ Still non-numeric columns: {non_numeric}")
    else:
        print("✅ All features are numeric.")

    print(f"🔍 Shape before dropna: {data.shape}")
    data.dropna(inplace=True)
    print(f"🔍 Shape after dropna: {data.shape}")

    if data.empty:
        print("❌ No valid rows left after cleaning. Please recheck the dataset formatting.")
        return

    # Normalize
    scaler = MinMaxScaler()
    features = data.drop('label', axis=1)
    data[features.columns] = scaler.fit_transform(features)

    # Save processed file
    data.to_csv(output_file, index=False)
    print(f"✅ Saved preprocessed file to {output_file}")

if __name__ == "__main__":
    preprocess_data('dataset/KDDTrain+.txt', 'dataset/processed_train.csv')
    preprocess_data('dataset/KDDTest+.txt', 'dataset/processed_test.csv')
