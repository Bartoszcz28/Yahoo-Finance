import streamlit as st
import pandas as pd
import plost
import psycopg2 
import time 

#####################################################################################
# Conection to database


conn = psycopg2.connect(user="postgres", password="postgres", host="db", port="5432", database="postgres")
cur = conn.cursor()

query = "SELECT * FROM crypto;"
cur.execute(query)
crypto = cur.fetchall()
crypto_df = pd.DataFrame(crypto)
columns = ["id", "name", "price", "change", "percent_change", "market_cap", "total_volume", "circulate_supply", "date"]
crypto_df.columns = columns

####################################################################################
etc = crypto_df[crypto_df["name"] == "Ethereum USD"]
btc = crypto_df[crypto_df["name"] == "Bitcoin USD"]


st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Dashboard `version 2`')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')


# plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
# selected_crypto = st.sidebar.selectbox('Select cryptocurrency', ['BTC', 'ETC'])# Select data for the line chart
selected_crypto = st.sidebar.selectbox('Select cryptocurrency', ["TrueUSD USD", "Shiba Inu USD", "Avalanche USD", "Polygon USD",
                                                                "Tether USDt USD", "Cardano USD", "USD Coin USD", "Bitcoin USD",
                                                                "Bitcoin Cash USD", "TRON USD", "UNUS SED LEO USD", "Dai USD",
                                                                "Polkadot USD", "Solana USD", "XRP USD", "Stellar USD",
                                                                "Wrapped Bitcoin USD", "Lido Staked ETH USD", "Wrapped Kava USD",
                                                                "Toncoin USD", "Dogecoin USD", "BNB USD", "Chainlink USD",
                                                                "Litecoin USD", "Wrapped TRON USD", "Ethereum USD"])


plot_data = st.sidebar.multiselect('Select data', ["price", "change", "percent_change"], ["price", "change"])

plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

st.sidebar.markdown('''
---
Created by Bartosz Czarnecki
''')


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
    
with c2:
    st.markdown('### Donut chart')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='company',
        legend='bottom', 
        use_container_width=True)

# # Row C
st.markdown('### Line chart')
# st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)

# if selected_crypto == 'BTC':
#     st.line_chart(btc.set_index('date')[plot_data].rename(columns={'price': 'BTC Price', 'change': 'BTC Change'}),
#                   use_container_width=True)
# elif selected_crypto == 'ETC':
#     st.line_chart(etc.set_index('date')[plot_data].rename(columns={'price': 'ETC Price', 'change': 'ETC Change'}),
#                   use_container_width=True)
    
selected_crypto_data = crypto_df[crypto_df['name'] == selected_crypto]

st.line_chart(selected_crypto_data.set_index('date')[plot_data].rename(columns={'price': f'{selected_crypto} Price',
                                                                                 'change': f'{selected_crypto} Change'}),
              use_container_width=True)