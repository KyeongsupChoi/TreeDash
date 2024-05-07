import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

data = pd.read_csv('cmpd.csv')

st.bar_chart(data)