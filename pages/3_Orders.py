import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.sidebar import render_sidebar
from charts.bar import sales_by_subcategory
from charts.theme import CHART_THEME, SEQ_PALETTE, PALETTE, chart_theme_with

st.set_page_config(page_title="Orders", page_icon="▪", layout="wide")

df       = load_data()
filtered = render_sidebar(df)

# ── Header ────────────────────────────────────────────────────
st.title("Orders breakdown")
st.markdown(
    "<p style='color:#aeb6cc;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem;'>"
    f"Sub-category and shipping analysis · {len(filtered):,} orders</p>",
    unsafe_allow_html=True,
)

# ── KPIs ─────────────────────────────────────────────────────
total_orders = filtered["Order ID"].nunique()
avg_qty      = filtered["Quantity"].mean()
avg_days     = (filtered["Ship Date"] - filtered["Order Date"]).dt.days.mean() if "Ship Date" in filtered.columns else 0
total_qty    = filtered["Quantity"].sum()

c1, c2, c3, c4 = st.columns(4)
c1.metric("Unique orders",   f"{total_orders:,}")
c2.metric("Total units",     f"{total_qty:,}")
c3.metric("Avg qty/order",   f"{avg_qty:.1f}")
c4.metric("Avg ship days",   f"{avg_days:.1f}d" if avg_days else "—")

st.markdown("<div style='margin:1.5rem 0'></div>", unsafe_allow_html=True)

# ── Row 1 ─────────────────────────────────────────────────────
col1, col2 = st.columns([3, 2], gap="medium")
with col1:
    st.plotly_chart(sales_by_subcategory(filtered), use_container_width=True)
with col2:
    ship = filtered.groupby("Ship Mode", as_index=False)["Order ID"].nunique()
    ship.columns = ["Ship Mode", "Orders"]
    fig = px.pie(
        ship, names="Ship Mode", values="Orders",
        color_discrete_sequence=SEQ_PALETTE,
        title="Orders by ship mode",
        hole=0.55,
    )
    fig.update_traces(
        textfont=dict(size=12, color="#f8fafc", weight=600),
        hovertemplate="<b>%{label}</b><br>%{value:,} orders<extra></extra>",
    )
    fig.update_layout(**CHART_THEME)
    st.plotly_chart(fig, use_container_width=True)

# ── Row 2: monthly order count ────────────────────────────────
import plotly.graph_objects as go
monthly = (
    filtered.groupby(filtered["Order Date"].dt.to_period("M").dt.to_timestamp())
    ["Order ID"].nunique().reset_index()
)
monthly.columns = ["Month", "Orders"]
fig2 = go.Figure(go.Bar(
    x=monthly["Month"], y=monthly["Orders"],
    marker_color=PALETTE["blue"],
    marker_line_width=0,
    hovertemplate="<b>%{x|%b %Y}</b><br>%{y} orders<extra></extra>",
))
fig2.update_layout(**chart_theme_with(title="Monthly order volume"))
st.plotly_chart(fig2, use_container_width=True)

# ── Data table ────────────────────────────────────────────────
st.markdown("<p style='color:#aeb6cc;font-size:0.75rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;margin-bottom:.5rem'>Raw data</p>", unsafe_allow_html=True)
cols = ["Order Date", "Ship Date", "Ship Mode", "Category", "Sub-Category",
        "Region", "Segment", "Sales", "Quantity", "Profit"]
available = [c for c in cols if c in filtered.columns]
st.dataframe(
    filtered[available].sort_values("Order Date", ascending=False),
    use_container_width=True,
    height=360,
)
st.download_button(
    "Download CSV",
    data=filtered[available].to_csv(index=False),
    file_name="orders_filtered.csv",
    mime="text/csv",
)
