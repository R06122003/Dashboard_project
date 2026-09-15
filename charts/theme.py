CHART_THEME = dict(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans, sans-serif", color="#8b90a0", size=12),
    title=dict(font=dict(size=14, color="#c8cad4", weight=500), x=0, pad=dict(l=4, b=12)),
    xaxis=dict(
        showgrid=False,
        showline=False,
        tickcolor="#2a3050",
        tickfont=dict(size=11, color="#aeb6cc"),
        zeroline=False,
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="#1a1d27",
        gridwidth=1,
        showline=False,
        tickcolor="#2a3050",
        tickfont=dict(size=11, color="#aeb6cc"),
        zeroline=False,
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        borderwidth=0,
        font=dict(size=11, color="#8b90a0"),
    ),
    margin=dict(l=8, r=8, t=40, b=8),
    hoverlabel=dict(
        bgcolor="#1a1d27",
        bordercolor="#2a3050",
        font=dict(family="DM Sans, sans-serif", size=12, color="#e2e4ea"),
    ),
)

PALETTE = {
    "blue":   "#4d9fff",
    "teal":   "#2dd4bf",
    "amber":  "#f59e0b",
    "coral":  "#f87171",
    "purple": "#a78bfa",
    "green":  "#4ade80",
    "muted":  "#aeb6cc",
}

SEQ_PALETTE = [
    "#4d9fff", "#2dd4bf", "#a78bfa", "#f59e0b", "#f87171", "#4ade80"
]

def chart_theme_with(**overrides):
    theme = CHART_THEME.copy()
    theme.update(overrides)
    return theme
