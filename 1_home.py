import webbrowser
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt

st.set_page_config(layout = 'wide')
link_dataset = 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data'

if 'data' not in st.session_state:
    df_data = pd.read_csv('data/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data.loc[df_data['Contract Valid Until'] >= dt.datetime.today().year]
    df_data = df_data.loc[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by=['Overall'], ascending = False)
    st.session_state['data'] = df_data

st.write('# FIFA23 OFFICIAL DATASET !')
st.subheader('')
btn = st.button('Acesse os dados do Kaggle')

if btn:
    webbrowser.open_new_tab(link_dataset)

