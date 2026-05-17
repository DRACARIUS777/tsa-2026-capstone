import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide')

st.title('TSA 2026 Capstone Dashboard')

portfolio_df = pd.read_csv('outputs/tables/portfolio_allocation.csv')
metrics_df = pd.read_csv('outputs/tables/model_metrics.csv')

st.header('Portfolio Allocation')

fig = px.pie(
    portfolio_df,
    values='Allocated Amount',
    names='Stock'
)

st.plotly_chart(fig, use_container_width=True)

st.header('Model Metrics')
st.dataframe(metrics_df)

st.header('Portfolio Table')
st.dataframe(portfolio_df)
