# 🐍 Python Portfolio

This repository highlights some of my Python projects.  
They focus on **data analysis, machine learning, and APIs**.

---

## 📂 Projects

### 1. Kickstarter ML Classifier 🎯
- **Description:** Predicts Kickstarter campaign success using project descriptions.  
- **Methods:**  
  - Text preprocessing with NLTK  
  - Vectorization with CountVectorizer  
  - Models: Neural Network, Decision Tree, KNN  
- **Output:** Model accuracy comparison.  

---

### 2. Wholesale Customers Clustering 🛒
- **Description:** Segments wholesale customers into groups using purchasing patterns.  
- **Methods:**  
  - K-Means clustering (tested multiple K values)  
  - Silhouette score evaluation  
  - Scatterplot visualizations by user-selected features  
- **Output:** Cluster insights + visualization.  

---

### 3. Earthquake Data Collector 🌍
- **Description:** Small ETL pipeline that pulls real-time earthquake data from APIs.  
- **Methods:**  
  - API requests (JSON)  
  - Data cleaning + storage (SQLite/CSV)  
  - Automation with GitHub Actions (scheduled runs)  
- **Output:** Up-to-date earthquake dataset.  

---

## 🚀 How to Run
Clone the repo and run a project script:
```bash
git clone https://github.com/yourusername/python-portfolio.git
cd python-portfolio
python kickstarter_classifier.py
