import plotly.express as px
import plotly.graph_objects as go
from charts.theme import CHART_THEME, SEQ_PALETTE, PALETTE, chart_theme_with


def sales_by_category(df):
    grouped = df.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales")
    fig = px.bar(
        grouped, x="Sales", y="Category", orientation="h",
        color="Category",
        color_discrete_sequence=SEQ_PALETTE,
        text="Sales",
        title="Sales by category",
    )
    fig.update_traces(
        texttemplate="$%{x:,.0f}",
        textposition="outside",
        textfont=dict(size=11, color="#8b90a0"),
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Sales: $%{x:,.0f}<extra></extra>",
    )
    fig.update_layout(
        **chart_theme_with(
            showlegend=False,
            xaxis=dict(**CHART_THEME["xaxis"], tickprefix="$", tickformat=",.0f"),
        )
    )
    return fig


def profit_by_region(df):
    grouped = df.groupby("Region", as_index=False)["Profit"].sum().sort_values("Profit")
    colors  = [PALETTE["coral"] if v < 0 else PALETTE["teal"] for v in grouped["Profit"]]
    fig = go.Figure(go.Bar(
        x=grouped["Profit"], y=grouped["Region"],
        orientation="h",
        marker_color=colors,
        marker_line_width=0,
        hovertemplate="<b>%{y}</b><br>Profit: $%{x:,.0f}<extra></extra>",
    ))
    fig.update_layout(
        **chart_theme_with(
            title="Profit by region",
            xaxis=dict(**CHART_THEME["xaxis"], tickprefix="$", tickformat=",.0f"),
        )
    )
    return fig


def sales_by_subcategory(df):
    grouped = (df.groupby("Sub-Category", as_index=False)["Sales"]
               .sum().sort_values("Sales", ascending=False).head(10))
    fig = px.bar(
        grouped, x="Sub-Category", y="Sales",
        color="Sales",
        color_continuous_scale=[[0, "#1a1d27"], [1, PALETTE["blue"]]],
        title="Top 10 sub-categories",
    )
    fig.update_traces(
        marker_line_width=0,
        hovertemplate="<b>%{x}</b><br>Sales: $%{y:,.0f}<extra></extra>",
    )
    fig.update_layout(
        **chart_theme_with(
            coloraxis_showscale=False,
            xaxis=dict(**CHART_THEME["xaxis"], tickangle=-30),
        )
    )
    return fig
