import streamlit as st

def render_kpis(df, prev_df=None):
    total_sales   = df["Sales"].sum()
    total_profit  = df["Profit"].sum()
    total_orders  = df["Order ID"].nunique()
    margin        = (total_profit / total_sales * 100) if total_sales else 0

    def delta(curr, prev):
        if prev is None or prev == 0:
            return None
        return f"{((curr - prev) / abs(prev)) * 100:+.1f}%"

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total sales",   f"${total_sales:,.0f}",
              delta(total_sales, prev_df["Sales"].sum() if prev_df is not None else None))
    c2.metric("Total profit",  f"${total_profit:,.0f}",
              delta(total_profit, prev_df["Profit"].sum() if prev_df is not None else None))
    c3.metric("Orders",        f"{total_orders:,}",
              delta(total_orders, prev_df["Order ID"].nunique() if prev_df is not None else None))
    c4.metric("Profit margin", f"{margin:.1f}%")