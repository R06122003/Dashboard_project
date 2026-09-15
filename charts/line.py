import plotly.graph_objects as go
import plotly.express as px
from charts.theme import CHART_THEME, PALETTE, SEQ_PALETTE, chart_theme_with

def sales_over_time(df):
    monthly = (
        df.set_index("Order Date")
        .resample("ME")["Sales"].sum()
        .reset_index()
    )
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly["Order Date"], y=monthly["Sales"],
        mode="lines",
        line=dict(color=PALETTE["blue"], width=2.5, shape="spline"),
        fill="tozeroy",
        fillcolor="rgba(77,159,255,0.07)",
        hovertemplate="<b>%{x|%b %Y}</b><br>$%{y:,.0f}<extra></extra>",
        name="Sales",
    ))
    fig.update_layout(
        **chart_theme_with(
            title="Monthly sales trend",
            showlegend=False,
            yaxis=dict(**CHART_THEME["yaxis"], tickprefix="$", tickformat=",.0f"),
        )
    )
    return fig


def category_trend(df):
    monthly = (
        df.groupby(["Category",
                    df["Order Date"].dt.to_period("M").dt.to_timestamp()])["Sales"]
        .sum().reset_index()
    )
    monthly.columns = ["Category", "Month", "Sales"]
    fig = px.line(
        monthly, x="Month", y="Sales", color="Category",
        line_shape="spline",
        color_discrete_sequence=SEQ_PALETTE,
        title="Sales trend by category",
    )
    fig.update_traces(line_width=2)
    fig.update_layout(
        **chart_theme_with(
            yaxis=dict(**CHART_THEME["yaxis"], tickprefix="$", tickformat=",.0f"),
        )
    )
    return fig
