import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="▪",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Sales Dashboard")
st.markdown(
    "<p style='color:#b8bfd2;font-size:0.95rem;margin-top:-0.5rem;'>"
    "Superstore · Interactive analytics</p>",
    unsafe_allow_html=True,
)

st.markdown("---")

c1, c2, c3 = st.columns(3)
with c1:
    st.page_link("pages/1_Sales.py", label="Sales", icon="📊")
    st.markdown(
        "<p style='color:#aeb6cc;font-size:0.85rem;'>"
        "KPIs, trends, and category breakdown</p>",
        unsafe_allow_html=True,
    )
with c2:
    st.page_link("pages/2_Profit.py", label="Profit", icon="💰")
    st.markdown(
        "<p style='color:#aeb6cc;font-size:0.85rem;'>"
        "Regional profit analysis and scatter view</p>",
        unsafe_allow_html=True,
    )
with c3:
    st.page_link("pages/3_Orders.py", label="Orders", icon="📦")
    st.markdown(
        "<p style='color:#aeb6cc;font-size:0.85rem;'>"
        "Sub-category breakdown and raw data</p>",
        unsafe_allow_html=True,
    )

st.markdown("---")
st.caption("Use the sidebar to navigate between pages. All filters apply globally per page.")
