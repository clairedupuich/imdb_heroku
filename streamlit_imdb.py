# Créer des outils de recherche : 
# ● par nom 
# ● par acteur(s) 
# ● par genre 
# ● par durée (ajoutez une fonction pour sélectionner un film inférieur à x durées) ● par note (note minimale) 

import streamlit as st
import pandas as pd
import time


imdb = pd.read_csv("datafilm_clean.csv")
st.header("welcome in IMBD_sea of films")


# boutton pour montrer tous les films par note
datatable = imdb.sort_values(by="note", ascending=False)
st.markdown("<h4 style='color: blue; text-shadow: 5px 5px 5px gray;'>Here to show you all of our movies by scort</h4>", unsafe_allow_html=True)
# st.markdown("#### Here to show you all of our movies by scort")
# with st.echo():用来同时在网页上显示代码和效果。
# st.button("<style>button{color: blue;}</style>",unsafe_allow_html=True)
if st.button('Click Me for all our film by scort'):
    st.dataframe(datatable) # will display the dataframe
#     #st.table(datatable)# will display the table

datasait_object = st.container()   #通过with st.beta_container():，可以Book一个组件模块, 将一个不可见的容器插入到你的应用程序中，可以用来保存多个元素。
st.sidebar.title("select the parameters to find the good film")
with datasait_object:
    options = ["name","actor","type","runtime"]
    result = st.sidebar.selectbox("How would you like to choose your film ?", options, key=None)
    # choose film by name
    if result == "name":
        title_var = st.sidebar.selectbox("write or choice the name of film", imdb["title"].unique(), key=None)  #?????????.unique()
        st.dataframe(data = imdb[imdb["title"] == title_var], height = 450)
    # choose film by type
    if result == "type":
        imdb["genre_list"] = imdb["genre"].str.split(",")
        list_genre = imdb.explode("genre_list")["genre_list"].unique()   #去除重复的genre         
        select_genre = st.sidebar.selectbox("which genre excatly?",  list_genre, key=None)
        st.dataframe(imdb[imdb["genre"].str.contains(select_genre)]) #显示带有这个genre的所有电影
    if result == "actor":   
        imdb["actors_list"] = imdb["actors"].str.split(",")    
        list_actors = imdb.explode("actors_list")["actors_list"].unique()   #去除重复的演员名字         
        select_actor = st.sidebar.selectbox("which actor?",  list_actors, key=None)
        st.dataframe(imdb[imdb["actors"].str.contains(select_actor)]) #显示带有这个演员名字的所有电影
    #choose film by scort
    if result == "runtime":
        scort = st.slider('choose diffrent scrot', imdb["note"].min(), imdb["note"].max(), imdb["note"].mean())
        #st.dataframe(imdb[imdb["note"].str.contains(scort)]) 不能运行，也许是因为有些scort值在列表中不存在
        masque = imdb["note"] > scort
        st.dataframe(imdb[masque])