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
df=df.sort_values("date", ascending=False)
df["year"]=df["date"].str[:4]


#artistのデータフレーム
df_0=df.loc[:,['artist', 'date',"year","title"]]

df_1=df.loc[:,['artist1', 'date',"year","title"]]
df_1=df_1.rename(columns={"artist1":"artist"})
df_1=df_1.dropna(subset=['artist'])

df_2=df.loc[:,['artist2', 'date',"year","title"]]
df_2=df_2.rename(columns={"artist2":"artist"})
df_2=df_2.dropna(subset=['artist'])

df_3=df.loc[:,['artist3', 'date',"year","title"]]
df_3=df_3.rename(columns={"artist3":"artist"})
df_3=df_3.dropna(subset=['artist'])

df_artist = pd.concat([df_0, df_1,df_2,df_3], ignore_index=True)


#列名のリスト
clm=list(df.columns)

df

#集計結果表示
df_groupby = df_artist["artist"].value_counts()
df_groupby

df_year=df["year"].value_counts()
df_year

#フィルターするかどうか
filter_check = st.checkbox('フィルターしますか')
if filter_check:
    fil=st.selectbox('filter',clm)
    'filterは',fil,'です。'
    selected_erea = st.multiselect('表示する要素を選択', list(set(list(df[fil]))))
    df_fil = df[(df[fil].isin(selected_erea))]

df_fil

#集計結果表示
df_groupby_fil = df_fil["artist"].value_counts()
df_groupby_fil

df_year_fil=df_fil["year"].value_counts()
df_year_fil

st.bar_chart(df_year)


pyg.walk(df, env='Streamlit')






fig = px.pie(df_groupby, values="artist")
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')


# Plot!
st.plotly_chart(fig, use_container_width=True)

