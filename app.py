import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.cluster import KMeans

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Customer Segmentation Studio",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

INC = "Annual Income (k$)"
SPD = "Spending Score (1-100)"
COLORS = ["#6366f1", "#22d3ee", "#f59e0b", "#ec4899", "#10b981"]


def html(s: str) -> str:
    """Strip indentation so Streamlit doesn't treat HTML as a code block."""
    return "".join(line.strip() for line in s.splitlines())


# ---------------------------------------------------
# Custom CSS (dark theme + 3D depth)
# ---------------------------------------------------
st.markdown(html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;600;800&display=swap');

html, body, [class*="css"], .stApp { font-family: 'Sora', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 15% 10%, rgba(99,102,241,.25), transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(34,211,238,.18), transparent 40%),
        linear-gradient(160deg, #0b1020 0%, #111936 100%);
    color: #e2e8f0;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 2rem; max-width: 1250px; }
[data-testid="stWidgetLabel"] p { color: #cbd5e1; font-weight: 600; }
section[data-testid="stSidebar"] { background: #0a0f1f; border-right: 1px solid rgba(255,255,255,.06); }
section[data-testid="stSidebar"] * { color: #cbd5e1; }

/* Hero */
.hero { text-align: center; padding: 20px 0 10px; perspective: 800px; }
.hero h1 {
    font-size: 54px; font-weight: 800; margin: 0; letter-spacing: -1px;
    background: linear-gradient(90deg, #a5b4fc, #67e8f9 50%, #f0abfc);
    -webkit-background-clip: text; background-clip: text; color: transparent;
    text-shadow: 0 10px 30px rgba(99,102,241,.35);
    transform: rotateX(14deg); display: inline-block;
}
.hero p { color: #94a3b8; font-size: 17px; margin-top: 10px; }

/* 3D cards */
.scene { perspective: 1000px; }
.card3d {
    background: linear-gradient(145deg, rgba(255,255,255,.09), rgba(255,255,255,.03));
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 20px; padding: 22px; backdrop-filter: blur(12px);
    box-shadow: 0 2px 0 rgba(255,255,255,.08) inset, 0 20px 40px rgba(0,0,0,.45), 0 0 0 1px rgba(0,0,0,.2);
    transform: rotateX(4deg) rotateY(-4deg);
    transition: transform .35s ease, box-shadow .35s ease;
    height: 100%;
}
.card3d:hover {
    transform: rotateX(0deg) rotateY(0deg) translateY(-8px) scale(1.02);
    box-shadow: 0 2px 0 rgba(255,255,255,.12) inset, 0 32px 60px rgba(99,102,241,.35);
}
.metric-label { color: #94a3b8; font-size: 14px; }
.metric-value { font-size: 36px; font-weight: 800; color: #fff; }
.section-title { font-size: 24px; font-weight: 700; margin: 34px 0 6px; color: #f1f5f9; }
.section-sub { color: #94a3b8; margin-bottom: 16px; }

/* Segment cards */
.seg-name { font-size: 17px; font-weight: 700; color: #fff; }
.seg-stat { color: #94a3b8; font-size: 13px; line-height: 1.7; }
.seg-dot { width: 12px; height: 12px; border-radius: 50%; display: inline-block; margin-right: 8px;
           box-shadow: 0 0 12px currentColor; }

/* Prediction box */
.result3d {
    background: linear-gradient(135deg, #6366f1, #8b5cf6 55%, #ec4899);
    border-radius: 24px; padding: 32px; text-align: center; color: #fff;
    transform: perspective(900px) rotateX(6deg);
    box-shadow: 0 30px 60px rgba(99,102,241,.45), 0 -2px 0 rgba(255,255,255,.3) inset;
    transition: transform .4s ease;
}
.result3d:hover { transform: perspective(900px) rotateX(0deg) translateY(-6px); }
.result-emoji { font-size: 54px; }
.result-name { font-size: 32px; font-weight: 800; margin: 4px 0; }
.result-desc { opacity: .92; font-size: 15px; }
.result-badge { display: inline-block; margin-top: 14px; padding: 6px 16px; border-radius: 999px;
                background: rgba(255,255,255,.2); font-weight: 600; }

/* Button */
.stButton > button {
    width: 100%; height: 54px; border-radius: 14px; border: none; font-weight: 700; font-size: 17px;
    color: #fff; background: linear-gradient(135deg, #6366f1, #22d3ee);
    box-shadow: 0 8px 0 #3730a3, 0 14px 24px rgba(0,0,0,.4);
    transition: all .15s ease;
}
.stButton > button:hover { transform: translateY(-2px); color: #fff; }
.stButton > button:active { transform: translateY(6px); box-shadow: 0 2px 0 #3730a3, 0 6px 12px rgba(0,0,0,.4); }

@media (prefers-reduced-motion: reduce) { .card3d, .result3d, .hero h1 { transition: none; transform: none; } }
</style>
"""), unsafe_allow_html=True)


# ---------------------------------------------------
# Model
# ---------------------------------------------------
def describe_segment(inc: float, spd: float):
    hi_i, lo_i = inc >= 70, inc <= 40
    hi_s, lo_s = spd >= 60, spd <= 40
    if hi_i and hi_s:
        return "Premium Spenders", "💎", "High income and high spending. Your most valuable customers."
    if hi_i and lo_s:
        return "Careful Savers", "🧠", "High income but low spending. Target with quality and value offers."
    if lo_i and hi_s:
        return "Impulsive Buyers", "🎁", "Lower income but high spending. Respond well to deals and trends."
    if lo_i and lo_s:
        return "Budget Customers", "🏷️", "Lower income and low spending. Price-sensitive shoppers."
    return "Standard Customers", "🛒", "Average income and spending. The steady core of your customer base."


@st.cache_resource
def train_model():
    df = pd.read_excel("Mall Customers.xlsx")
    model = KMeans(n_clusters=5, random_state=42, n_init=10).fit(df[[INC, SPD]])
    df["Cluster"] = model.labels_
    return model, df


model, df = train_model()
centers = model.cluster_centers_
segments = {i: describe_segment(*centers[i]) for i in range(5)}


# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
with st.sidebar:
    st.markdown("## 🛍️ Segmentation Studio")
    st.markdown("---")
    st.markdown(
        "**About**\n\nThis app groups mall customers with **K-Means Clustering** "
        "using annual income and spending score.\n\n"
        "**Type:** Unsupervised Learning"
    )
    st.markdown("---")
    st.caption("Week 4 Capstone Project")


# ---------------------------------------------------
# Hero
# ---------------------------------------------------
st.markdown(html("""
<div class="hero">
  <h1>Customer Segmentation</h1>
  <p>Discover who your customers are from their income and spending behavior.</p>
</div>
"""), unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# ---------------------------------------------------
# Metrics
# ---------------------------------------------------
metrics = [
    ("👥 Total customers", f"{len(df)}"),
    ("🔵 Segments", "5"),
    ("💰 Avg. income", f"${df[INC].mean():.0f}k"),
    ("🛒 Avg. spending score", f"{df[SPD].mean():.0f}"),
]
for col, (label, value) in zip(st.columns(4), metrics):
    col.markdown(html(f"""
    <div class="scene"><div class="card3d">
      <div class="metric-label">{label}</div>
      <div class="metric-value">{value}</div>
    </div></div>
    """), unsafe_allow_html=True)


# ---------------------------------------------------
# Input + Prediction
# ---------------------------------------------------
st.markdown('<div class="section-title">🎯 Predict a customer segment</div>'
            '<div class="section-sub">Enter income and spending score, then press the button.</div>',
            unsafe_allow_html=True)

left, right = st.columns([1, 1.1], gap="large")

with left:
    income = st.slider(INC.replace("(k$)", "(k$)"), float(df[INC].min()), float(df[INC].max()), 60.0, 1.0)
    spending = st.slider(SPD, float(df[SPD].min()), float(df[SPD].max()), 50.0, 1.0)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔮 Predict segment"):
        cluster = int(model.predict(pd.DataFrame([[income, spending]], columns=[INC, SPD]))[0])
        st.session_state["result"] = (cluster, income, spending)

with right:
    if "result" in st.session_state:
        cluster, _, _ = st.session_state["result"]
        name, emoji, desc = segments[cluster]
        st.markdown(html(f"""
        <div class="result3d">
          <div class="result-emoji">{emoji}</div>
          <div class="result-name">{name}</div>
          <div class="result-desc">{desc}</div>
          <div class="result-badge">Cluster {cluster}</div>
        </div>
        """), unsafe_allow_html=True)
    else:
        st.markdown(html("""
        <div class="scene"><div class="card3d" style="text-align:center;padding:48px 22px;">
          <div style="font-size:44px;">🔮</div>
          <div class="seg-name" style="margin-top:8px;">Your result will appear here</div>
          <div class="seg-stat">Set the two sliders and press Predict segment.</div>
        </div></div>
        """), unsafe_allow_html=True)


# ---------------------------------------------------
# 3D Cluster Chart
# ---------------------------------------------------
st.markdown('<div class="section-title">🌐 3D cluster explorer</div>'
            '<div class="section-sub">Drag to rotate, scroll to zoom. '
            'Age is shown only as a third axis for visualization; the model uses income and spending.</div>',
            unsafe_allow_html=True)

z_col = "Age" if "Age" in df.columns else None
fig = go.Figure()
for i in range(5):
    sub = df[df["Cluster"] == i]
    fig.add_trace(go.Scatter3d(
        x=sub[INC], y=sub[SPD], z=sub[z_col] if z_col else [0] * len(sub),
        mode="markers", name=f"{segments[i][1]} {segments[i][0]}",
        marker=dict(size=5, color=COLORS[i], opacity=0.85, line=dict(width=0.5, color="white")),
    ))

if "result" in st.session_state:
    _, ri, rs = st.session_state["result"]
    fig.add_trace(go.Scatter3d(
        x=[ri], y=[rs], z=[df[z_col].median() if z_col else 0],
        mode="markers", name="⭐ New customer",
        marker=dict(size=14, color="#ffffff", symbol="diamond", line=dict(width=2, color="#f43f5e")),
    ))

axis = dict(backgroundcolor="rgba(0,0,0,0)", gridcolor="rgba(255,255,255,.12)", color="#cbd5e1")
fig.update_layout(
    height=620, margin=dict(l=0, r=0, t=10, b=0),
    paper_bgcolor="rgba(0,0,0,0)", font=dict(color="#e2e8f0", family="Sora"),
    legend=dict(bgcolor="rgba(255,255,255,.06)", bordercolor="rgba(255,255,255,.12)", borderwidth=1),
    scene=dict(
        xaxis=dict(title="Annual income (k$)", **axis),
        yaxis=dict(title="Spending score", **axis),
        zaxis=dict(title=z_col or "", **axis),
        camera=dict(eye=dict(x=1.6, y=1.6, z=0.9)),
    ),
)
st.plotly_chart(fig, use_container_width=True)


# ---------------------------------------------------
# Segment Overview
# ---------------------------------------------------
st.markdown('<div class="section-title">📊 Segment overview</div>'
            '<div class="section-sub">What each cluster looks like on average.</div>',
            unsafe_allow_html=True)

for i, col in enumerate(st.columns(5)):
    sub = df[df["Cluster"] == i]
    name, emoji, _ = segments[i]
    col.markdown(html(f"""
    <div class="scene"><div class="card3d">
      <div class="seg-name"><span class="seg-dot" style="background:{COLORS[i]};color:{COLORS[i]};"></span>{emoji} {name}</div>
      <div class="seg-stat">
        Cluster {i}<br>
        Customers: <b>{len(sub)}</b><br>
        Avg. income: <b>${sub[INC].mean():.0f}k</b><br>
        Avg. spending: <b>{sub[SPD].mean():.0f}</b>
      </div>
    </div></div>
    """), unsafe_allow_html=True)


# ---------------------------------------------------
# Dataset Preview
# ---------------------------------------------------
st.markdown('<div class="section-title">📋 Dataset preview</div>'
            '<div class="section-sub">First 10 rows of the data used to train the model.</div>',
            unsafe_allow_html=True)
st.dataframe(df.head(10), use_container_width=True, hide_index=True)

st.markdown("---")
st.markdown(
    "<center style='color:#64748b'>Built with 🐍 Python • 🤖 Scikit-learn • 🎈 Streamlit • 📈 Plotly</center>",
    unsafe_allow_html=True,
)