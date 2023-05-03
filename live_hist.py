# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 10:47:50 2023

@author: cosmo
"""

import pandas as pd
import plotly.express as px
import os
import streamlit as st
import pydeck as pdk
import pygwalker as pyg

st.set_page_config(layout="wide", initial_sidebar_state="auto")
st.title("ライブ情報のダッシュボード")

  
    
#df=pd.read_excel(r"D:\Pydoc\MyPythonScripts\streamlit_webapp\live_info\Live info.xlsx")
df=pd.read_excel("Live info.xlsx")

df["year"]=df["date"].str[:4]



#列名のリスト
clm=list(df.columns)

df

pyg.walk(df, env='Streamlit')





df_groupby = df["artist"].value_counts()
df_groupby

fig = px.pie(df_groupby, values="artist")
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')


# Plot!
st.plotly_chart(fig, use_container_width=True)



#TimeStampの変換するかどうか
filter_check = st.checkbox('フィルターしますか')
if filter_check:
    fil=st.selectbox('filter',clm)
    'filterは',fil,'です。'
    selected_erea = st.multiselect('グラフに表示する要素を選択', list(set(list(df[fil]))))
    df = df[(df[fil].isin(selected_erea))]

fig2 = px.treemap(df, path=[px.Constant('artist')])
# Plot!
st.plotly_chart(fig2, use_container_width=True)