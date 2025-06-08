
# *🔐 Advanced Intrusion Detection and Prevention System (IDPS) using AI/ML*


## 📌 Overview

This project is a smart AI/ML-powered Intrusion Detection and Prevention System (IDPS) that monitors and classifies network traffic as normal or malicious. Built using **Python**, **Flask**, and trained on the **NSL-KDD dataset**, it provides real-time predictions, attack logging, and visual analytics through a clean web dashboard.

---


## 🗂️ Table of Contents

- [Overview](#-overview)  
- [Features](#-features)
- [Key Features (Detailed)](#-key-features-detailed)       
- [Technologies Used](#-technologies-used)  
- [How to Run](#-how-to-run)  
- [Dataset](#-dataset)  
- [ML Model](#-ml-model)  
- [Screenshots](#-screenshots)
- [Testing and Results](#-testing-and-results) 
- [Future Improvements](#-future-improvements) 
- [Contributing](#-contributing)
- [Contact](#-contact) 

---

## ✨ Features

- 📁 Upload CSV file of network traffic  
- 🤖 Real-time prediction using a trained Random Forest model  
- 📊 Interactive pie chart of attack categories  
- 📂 Logs saved in both CSV and JSON formats  
- 🧠 Built using the NSL-KDD dataset  
- 🧾 Log Analyzer with search, filter, and export to Excel  
- 🖥️ Clean UI powered by Flask, HTML, and CSS  
- 🕵️ Attack logs include IP address and timestamp  

---

## 🔑 Key Features (Detailed)

| 🔹 Feature                          | 📌 Description                                                            |
| ---------------------------------- | ------------------------------------------------------------------------- |
| ⚡ **Real-time Threat Detection**   | Detects attacks instantly using trained ML models (e.g., Random Forest).  |
| 🌐 **Interactive Web Dashboard**   | Built with Flask – lets you upload files, view results, and monitor logs. |
| 📋 **Attack Log Analyzer**         | Search, filter, and review past predictions with timestamp and IP.        |
| 📤 **Export to CSV/Excel**         | Export prediction logs with one click for reporting.                      |
| 📊 **Pie Chart Analytics**         | Graphical summary of attack vs normal traffic.                            |
| 💾 **Dual Log Formats**            | Stores logs in both CSV and JSON for versatility.                         |
| 🔁 **Model Training & Reusability**| Preprocess, train, and reuse models with `.pkl` serialization.            |

---

## 🧰 Technologies Used

| 🧪 Technology                        | 🛠️ Purpose                                          |
|--------------------------------------|-----------------------------------------------------|
| 🐍 **Python 3.8+**                   | Core backend programming and ML logic               |
| 🌐 **Flask**                         | Web framework for dashboard and routing             |
| 🤖 **Scikit-learn**                  | ML algorithms for intrusion detection               |
| 🧮 **Pandas & NumPy**                | Data handling and numerical operations              |
| 💼 **Joblib**                        | Saving/loading trained ML models                    |
| 📈 **Matplotlib / Seaborn / Plotly** | Data visualization (charts, graphs)                 |
| 🗃️ **SQLite (optional)**             | Lightweight database for structured storage         |
| 🧱 **HTML/CSS/JS**                   | Front-end interface styling and layout              |
| 🧑‍💻 **VS Code / Jupyter**             | Development and model experimentation               |
| 🌿 **Git**                           | Version control and collaboration                   |


---

## 🚀 How to Run

### 🔧 Step-by-Step Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System
```

#### 2️⃣ (Optional) Create Virtual Environment

```bash
python -m venv venv  
source venv/bin/activate
# On Windows: venv\Scripts\activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the Flask Application

```bash
python idps.py
```

#### 5️⃣ Open in Browser

```bash
Visit: http://127.0.0.1:5000
```

---

## 📚 Dataset

* **Name:** NSL-KDD
* **Description:** Labeled network traffic dataset used to train the machine learning model.
* **Contains:** Normal traffic and several types of network intrusions.
* **Source:** [NSL-KDD Dataset](https://www.unb.ca/cic/datasets/nsl.html)


## 🧠 ML Model

* **Algorithm:** Random Forest Classifier
* **Preprocessing:** Label encoding, feature scaling, and selection
* **Output:** Classifies each row as either Normal or an Attack Category

---

## 📷 Screenshots

### Home Page

![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Home%20Page%20of%20the%20Web%20Interface.png).

## Upload CSV file

![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/CSV%20File%20Upload%20Page.png).

## Pie Chart of Prediction Result

![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Generated%20summary.png).


![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Blocked%20IPs%20Details.png).


![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Prediction%20Output%20Table.png).

## Attack Log Viewer of (filter/search/export)

![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Log%20Analyzer%20interface.png).

---

## 📈 Testing and Results

The system was tested using the NSL-KDD dataset. Performance metrics:

| Metric       | Score |
| -------------| ----- |
| ✅ Accuracy  | 98%   |
| ✅ Precision | 97%   |
| ✅ Recall    | 95%   |
| ✅ F1 Score  | 96%   |


## Confusion Matrix
- The Confusion Matrix illustrates the performance of the machine learning model by showing the counts of True Positives (TP), False Positives (FP), True Negatives (TN), and False Negatives (FN). It helps evaluate classification accuracy.


![Alt Text](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/Confusion%20Matrix.png).

## ROC Curve
- The ROC (Receiver Operating Characteristic) Curve visualizes the model’s ability to distinguish between normal and attack traffic by plotting the True Positive Rate (TPR) against the False Positive Rate (FPR). A higher area under the curve (AUC) indicates better performance.

![Text All](https://github.com/nirakaramishra-cse/Advanced-Intrusion-Detection-and-Prevention-System/blob/1f58de64eaf12448ae4953df0dbd8fd2208d23a7/Images/ROC%20Curve.png).

---

## 🔧 Future Improvements

- 🌐 Real-time traffic integration using packet sniffing (e.g., Scapy)

- 🤖 Experiment with Deep Learning models like CNN, RNN

- 📊 Add advanced visualizations (e.g., heatmaps, line graphs)

- 🛡️ Role-based user authentication and session handling

- 📦 Dockerize the application for easier deployment

---

## 🤝 Contributing
We welcome contributions!

- Fork the repo
- Create a new branch
- Make your changes
- Submit a pull request


## 📬 Contact

- **Developer:**  Nirakara Mishra
- **Email:**  [nirakaramishra.cse@gmail.com]
- **GitHub:**  https://github.com/nirakaramishra-cse
- **LinkedIn:**  https://www.linkedin.com/in/nirakaramishra-cse




