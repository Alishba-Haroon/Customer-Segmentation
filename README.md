# Customer Segmentation using K-Means

A complete Machine Learning capstone project that applies **K-Means Clustering** to segment mall customers based on their **annual income** and **spending behavior**. The project includes data preprocessing, exploratory analysis, cluster selection, visualization, model training, customer segment interpretation, and an interactive Streamlit application.

## 🚀 Live Demo

**Streamlit App:**
https://customer-segmentation-quqj27qyxjfnaysgaaqfbg.streamlit.app/

---

## 📌 Project Overview

Customer segmentation helps businesses identify groups of customers with similar characteristics and behaviors.

In this project, **K-Means Clustering**, an unsupervised machine learning algorithm, is used to discover natural customer groups from mall customer data without predefined labels.

The resulting clusters can then be analyzed according to their average income and spending behavior.

---

## 🎯 Problem Statement

A business has customer information but does not have predefined customer categories.

The objective of this project is to:

* Analyze customer income and spending behavior.
* Identify naturally occurring customer groups.
* Determine an appropriate number of clusters.
* Assign each customer to a cluster.
* Interpret the characteristics of each customer segment.
* Provide an interactive interface for exploring customer segments.

---

## 📥 Input Features

The clustering model uses two main features:

| Feature                    | Description                                         |
| -------------------------- | --------------------------------------------------- |
| **Annual Income (k$)**     | Customer's annual income in thousands of dollars    |
| **Spending Score (1–100)** | Score representing the customer's spending behavior |

There is **no target variable**, because this is an unsupervised learning problem.

---

## 📤 Output

The model assigns each customer to a **K-Means cluster**.

Each cluster is then interpreted using:

* Average annual income
* Average spending score
* Number of customers
* Customer behavior patterns

For example, clusters may represent groups such as:

* High income / high spending
* High income / low spending
* Low income / high spending
* Low income / low spending

These descriptions are interpretations of the discovered clusters rather than predefined labels.

---

## 🧠 Machine Learning Technique

### K-Means Clustering

**K-Means** is an unsupervised machine learning algorithm that divides data into a predefined number of clusters.

The algorithm works by:

1. Selecting the number of clusters `K`.
2. Initializing cluster centroids.
3. Assigning customers to their nearest centroid.
4. Updating the centroid of each cluster.
5. Repeating the process until the clusters stabilize.

The objective is to minimize the distance between customers and their assigned cluster centroids.

---

## 📊 Cluster Selection & Evaluation

Two techniques are used to determine and evaluate the appropriate number of clusters.

### 1. Elbow Method

The Elbow Method evaluates the **Within-Cluster Sum of Squares (WCSS)** for different values of `K`.

The point where adding more clusters produces relatively smaller improvements can indicate a suitable value of `K`.

### 2. Silhouette Score

The Silhouette Score measures how well customers fit within their assigned clusters compared with other clusters.

A higher score generally indicates better separation and cohesion between clusters.

Both methods are considered together when selecting the clustering configuration.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Exploration
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Feature Scaling
   ↓
Elbow Method
   ↓
Silhouette Score
   ↓
K-Means Clustering
   ↓
Cluster Visualization
   ↓
Cluster Interpretation
   ↓
Customer Segment Output
   ↓
Streamlit Deployment
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Streamlit**
* **Jupyter Notebook / Google Colab**

---

## 📂 Project Structure

```text
Customer-Segmentation/
│
├── Customer_Segmentation.ipynb
├── app.py
├── Mall Customers.xlsx
├── customer_segments.csv
├── requirements.txt
└── README.md
```

### File Description

| File                          | Description                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------- |
| `Customer_Segmentation.ipynb` | Complete ML workflow including preprocessing, analysis, clustering, evaluation, and visualization |
| `app.py`                      | Streamlit application for interactive customer segmentation                                       |
| `Mall Customers.xlsx`         | Original customer dataset                                                                         |
| `customer_segments.csv`       | Generated dataset containing customer cluster assignments                                         |
| `requirements.txt`            | Required Python dependencies                                                                      |
| `README.md`                   | Project documentation                                                                             |

---

## 💻 How to Run the Notebook

### Using Google Colab

1. Open `Customer_Segmentation.ipynb` in Google Colab.
2. Upload `Mall Customers.xlsx`.
3. Run the notebook cells from top to bottom.
4. The clustering analysis and visualizations will be generated.
5. The resulting customer segments can be exported to `customer_segments.csv`.

---

## 🌐 Run the Streamlit Application Locally

First, clone the repository:

```bash
git clone https://github.com/Alishba-Haroon/Customer-Segmentation.git
```

Navigate to the project directory:

```bash
cd Customer-Segmentation
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in your browser.

Make sure `Mall Customers.xlsx` is available in the same project directory if the application loads the dataset locally.

---

## 📈 Streamlit Application

The deployed application provides an interactive way to explore customer segmentation.

### Live Application

🔗 **https://customer-segmentation-quqj27qyxjfnaysgaaqfbg.streamlit.app/**

The application demonstrates how the trained clustering approach can be used to assign and visualize customer segments.

---

## 💼 Business Use Case

Customer segmentation can help businesses understand different customer behavior patterns.

For example, after identifying clusters, a business team could investigate:

* Which customers have high spending behavior?
* Which customers have high income but relatively low spending?
* Which groups may respond differently to marketing campaigns?
* How large is each customer segment?
* What characteristics distinguish one segment from another?

The clustering model itself **does not decide business actions**. The discovered segments must be interpreted by the business team according to the organization's objectives.

---

## 🔍 Key Learning Outcomes

Through this project, the following Machine Learning concepts were practiced:

* Unsupervised Learning
* K-Means Clustering
* Feature Selection
* Feature Scaling
* Centroids
* Elbow Method
* WCSS
* Silhouette Score
* Cluster Visualization
* Customer Segment Interpretation
* Streamlit Deployment
* End-to-End ML Project Workflow

---

## 📌 Project Highlights

* ✅ End-to-end Machine Learning project
* ✅ Unsupervised learning implementation
* ✅ K-Means clustering
* ✅ Elbow Method for cluster selection
* ✅ Silhouette Score evaluation
* ✅ Customer segment visualization
* ✅ CSV output generation
* ✅ Interactive Streamlit application
* ✅ Deployed web application

---

## 👩‍💻 Author

**Alishba Haroon**


---

## 📄 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for the complete license text.

