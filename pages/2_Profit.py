import streamlit as st
import plotly.express as px
from utils.loader import load_data
from utils.sidebar import render_sidebar
from charts.bar import profit_by_region
from charts.theme import CHART_THEME, SEQ_PALETTE, chart_theme_with

st.set_page_config(page_title="Profit", page_icon="▪", layout="wide")

df       = load_data()
filtered = render_sidebar(df)

# ── Header ────────────────────────────────────────────────────
st.title("Profit analysis")
st.markdown(
    "<p style='color:#aeb6cc;font-size:0.875rem;margin-top:-0.5rem;margin-bottom:1.5rem;'>"
    f"Margin and regional breakdown · {len(filtered):,} orders</p>",
    unsafe_allow_html=True,
)

# ── KPI row ───────────────────────────────────────────────────
total_sales  = filtered["Sales"].sum()
total_profit = filtered["Profit"].sum()
margin       = (total_profit / total_sales * 100) if total_sales else 0
avg_discount = filtered["Discount"].mean() * 100 if "Discount" in filtered.columns else 0

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total profit",  f"${total_profit:,.0f}")
c2.metric("Profit margin", f"{margin:.1f}%")
c3.metric("Total sales",   f"${total_sales:,.0f}")
c4.metric("Avg discount",  f"{avg_discount:.1f}%")

st.markdown("<div style='margin:1.5rem 0'></div>", unsafe_allow_html=True)

# ── Row 1 ─────────────────────────────────────────────────────
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.plotly_chart(profit_by_region(filtered), use_container_width=True)
with col2:
    fig = px.scatter(
        filtered, x="Sales", y="Profit",
        color="Category", size="Quantity",
        opacity=0.7,
        color_discrete_sequence=SEQ_PALETTE,
        title="Sales vs profit",
        hover_data=["Sub-Category", "Region"],
    )
    fig.update_traces(
        marker=dict(line=dict(width=0)),
        hovertemplate="<b>%{customdata[0]}</b><br>Sales: $%{x:,.0f}<br>Profit: $%{y:,.0f}<extra></extra>",
    )
    fig.update_layout(
        **chart_theme_with(
            xaxis=dict(**CHART_THEME["xaxis"], tickprefix="$", tickformat=",.0f"),
            yaxis=dict(**CHART_THEME["yaxis"], tickprefix="$", tickformat=",.0f"),
        )
    )
    st.plotly_chart(fig, use_container_width=True)

# ── Row 2: profit by segment ──────────────────────────────────
seg = filtered.groupby("Segment", as_index=False)["Profit"].sum()
fig2 = px.pie(
    seg, names="Segment", values="Profit",
    color_discrete_sequence=SEQ_PALETTE,
    title="Profit share by segment",
    hole=0.55,
)
fig2.update_traces(
    textfont=dict(size=12, color="#f8fafc", weight=600),
    hovertemplate="<b>%{label}</b><br>$%{value:,.0f}<extra></extra>",
)
fig2.update_layout(**CHART_THEME)

cat = filtered.groupby("Category", as_index=False).agg(
    Sales=("Sales","sum"), Profit=("Profit","sum")
)
cat["Margin"] = cat["Profit"] / cat["Sales"] * 100
fig3 = px.bar(
    cat, x="Category", y="Margin",
    color="Category",
    color_discrete_sequence=SEQ_PALETTE,
    title="Margin % by category",
    text="Margin",
)
fig3.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="outside",
    textfont=dict(color="#8b90a0", size=11),
    marker_line_width=0,
)
fig3.update_layout(
    **chart_theme_with(
        showlegend=False,
        yaxis=dict(**CHART_THEME["yaxis"], ticksuffix="%"),
    )
)

col3, col4 = st.columns(2, gap="medium")
with col3:
    st.plotly_chart(fig2, use_container_width=True)
with col4:
    st.plotly_chart(fig3, use_container_width=True)
