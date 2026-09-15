import streamlit as st
from utils.loader import load_data
from utils.sidebar import render_sidebar
from charts.kpi import render_kpis
from charts.bar import sales_by_category
from charts.line import sales_over_time, category_trend

st.set_page_config(page_title="Sales", page_icon="▪", layout="wide")

df       = load_data()
filtered = render_sidebar(df)

# ── Header ────────────────────────────────────────────────────
st.title("Sales overview")
st.markdown(
    "<p style='color:#aeb6cc;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem;'>"
    f"{len(filtered):,} orders · filtered view</p>",
    unsafe_allow_html=True,
)

# ── KPIs ──────────────────────────────────────────────────────
render_kpis(filtered)

st.markdown("<div style='margin:1.5rem 0'></div>", unsafe_allow_html=True)

# ── Row 1: trend + category ───────────────────────────────────
col1, col2 = st.columns([3, 2], gap="medium")
with col1:
    st.plotly_chart(sales_over_time(filtered), use_container_width=True)
with col2:
    st.plotly_chart(sales_by_category(filtered), use_container_width=True)

# ── Row 2: category trend ─────────────────────────────────────
st.plotly_chart(category_trend(filtered), use_container_width=True)

# ── Raw data ──────────────────────────────────────────────────
with st.expander("View raw data", expanded=False):
    cols = ["Order Date", "Category", "Sub-Category", "Region", "Segment", "Sales", "Profit", "Quantity"]
    st.dataframe(
        filtered[cols].sort_values("Order Date", ascending=False),
        use_container_width=True,
        height=320,
    )
    st.download_button(
        "Download CSV",
        data=filtered[cols].to_csv(index=False),
        file_name="sales_filtered.csv",
        mime="text/csv",
    )
