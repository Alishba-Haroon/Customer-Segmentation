# Customer Segmentation using K-Means

## Project Purpose
This Week 4 capstone project uses K-Means clustering to group mall customers according to annual income and spending behavior.

## Problem
A business may have customer data but no predefined customer categories. The project discovers groups of similar customers without using labeled target values.

## Input
- Annual Income (k$)
- Spending Score (1-100)

## Output
A K-Means cluster assigned to each customer. The cluster is then interpreted using its average income and spending score.

## Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit

## ML Technique
K-Means Clustering (unsupervised learning)

## Evaluation / Cluster Selection
- Elbow Method
- Silhouette Score

## Files
- `Customer_Segmentation.ipynb` — complete capstone notebook
- `app.py` — Streamlit demo
- `Mall Customers.xlsx` — dataset
- `requirements.txt` — dependencies
- `customer_segments.csv` — generated output after running the notebook

## How to Run the Notebook
1. Open `Customer_Segmentation.ipynb` in Google Colab.
2. Upload `Mall Customers.xlsx`.
3. Run the cells from top to bottom.

## How to Run the Streamlit App

```bash
pip install -r requirements.txt
streamlit run app.py
```

Keep `Mall Customers.xlsx` in the same folder as `app.py`.

## Business Purpose
The resulting customer segments can help a business understand customer behavior and design different marketing strategies for different groups. The clustering model itself does not decide business actions; the segments must be interpreted by the business team.
# Customer-Segmentation
