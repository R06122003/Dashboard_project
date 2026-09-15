import streamlit as st

def render_sidebar(df):
    """Renders filters in the sidebar and returns the filtered dataframe."""
    with st.sidebar:
        st.markdown("### Filters")
        st.markdown("---")

        regions = st.multiselect(
            "Region",
            options=sorted(df["Region"].unique()),
            default=sorted(df["Region"].unique()),
        )
        years = st.multiselect(
            "Year",
            options=sorted(df["Order Date"].dt.year.unique()),
            default=sorted(df["Order Date"].dt.year.unique()),
        )
        categories = st.multiselect(
            "Category",
            options=sorted(df["Category"].unique()),
            default=sorted(df["Category"].unique()),
        )
        segments = st.multiselect(
            "Segment",
            options=sorted(df["Segment"].unique()),
            default=sorted(df["Segment"].unique()),
        )

        st.markdown("---")
        n = len(df[
            df["Region"].isin(regions) &
            df["Order Date"].dt.year.isin(years) &
            df["Category"].isin(categories) &
            df["Segment"].isin(segments)
        ])
        st.caption(f"{n:,} rows match current filters")

    filtered = df[
        df["Region"].isin(regions) &
        df["Order Date"].dt.year.isin(years) &
        df["Category"].isin(categories) &
        df["Segment"].isin(segments)
    ]
    return filtered