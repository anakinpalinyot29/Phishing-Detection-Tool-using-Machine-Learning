# 🔐 Phishing Detection Tool Using Machine Learning

This project is part of the **CSS453: Cyber Crimes and Digital Forensics** course and aims to combat phishing threats using machine learning. It leverages a dataset of labeled URLs to train and deploy models that can identify phishing websites in real time.

> 🎯 **Final Model Accuracy: 96.67%**

---

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Project Pipeline](#-project-pipeline)
- [Technologies Used](#-technologies-used)
- [How It Works](#-how-it-works)
- [Model Performance](#-model-performance)
- [Demo](#-demo)
- [Getting Started](#-getting-started)
- [Team Contributions](#-team-contributions)
- [License](#-license)

---

## 🧠 About the Project

Phishing is a widespread cybercrime tactic where attackers use fake websites or emails to steal sensitive data. Our project introduces a **machine learning-based phishing detection tool** capable of analyzing and classifying URLs as *malicious* or *legitimate*.

---

## 🔄 Project Pipeline

The system follows a structured machine learning workflow:

1. **Data Collection**  
   - Over 500,000 labeled URLs from trusted datasets (e.g., Kaggle)
2. **Data Preprocessing**  
   - Regex-based tokenization and stemming using NLTK  
   - URL cleaning and standardization
3. **Model Training**  
   - Logistic Regression and Multinomial Naive Bayes models
4. **Prediction Engine**  
   - Real-time classification with confidence scores
5. **Model Deployment**  
   - FastAPI backend for easy integration

📌 *Consider adding a flowchart or architecture diagram here (e.g., `images/pipeline.png`).*

---

## 🛠️ Technologies Used

- **Python 3.x**
- **scikit-learn**
- **NLTK**
- **BeautifulSoup**
- **Edge WebDriver**
- **FastAPI**

---

## ⚙️ How It Works

- The input URL is **tokenized** and **stemmed** to extract relevant features.
- The model (preferably **Logistic Regression**) then predicts whether the URL is *good* or *bad*.
- Optionally, a **confidence score** is returned to aid decision-making.

---

## 📊 Model Performance

| Model                    | Train Accuracy | Test Accuracy |
|--------------------------|----------------|----------------|
| Logistic Regression      | 98.10%         | 96.68%         |
| Multinomial Naive Bayes  | 97.42%         | 95.73%         |

🟢 Logistic Regression performs better and is recommended for deployment.

📌 *You can add performance charts here (e.g., `images/accuracy_comparison.png`, `images/confusion_matrix.png`).*

---

## 🚀 Demo

A simple FastAPI app is deployed for real-time predictions.

📌 *Insert screenshots or GIF here: `images/demo.gif` or `images/ui.png`.*

---

## 🧑‍🤝‍🧑 Team Contributions

| Name                     | Student ID     | Contributions |
|--------------------------|----------------|----------------|
| Supawit Nakprame         | 6422770287     | Report, Presentation, Methodology, Evaluation |
| Surabordin Sungchai      | 6422782514     | Report, Model Visualization, Reference |
| Panpatchara Naneplai     | 6422782522     | Report, Presentation, Software Testing |
| Anakin Palinyot          | 6422782530     | ML Development, System Integration, Presentation |

---

## 📥 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/phishing-detector.git
2. Install requirements:
 ```bash
   pip install -r requirements.txt
