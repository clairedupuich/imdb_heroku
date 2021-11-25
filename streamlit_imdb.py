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
datasait_object = st.container()   #通过with st.beta_container():，可以Book一个组件模块, 将一个不可见的容器插入到你的应用程序中，可以用来保存多个元素。

#st.subheader("choice a actor who you like")
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
        list_type = ["Comedy","Horror","Drama"]
        type_var = st.sidebar.selectbox("which type exactly?",  list_type, key=None)
        if type_var == "Comedy":
            masque = imdb["genre"].str.contains("Comedy") 
            new_list = imdb[masque].sort_values(by="note",ascending=False)
            film_comedy = new_list['title'].values
            type_hor = st.sidebar.selectbox("which fime horror?",  film_comedy, key=None)
            st.subheader("Here are all our comedy films")
            st.dataframe(new_list, height = 450)
        if type_var == "Horror":
            masque = imdb["genre"].str.contains("Horror") 
            new_list = imdb[masque].sort_values(by="note",ascending=False)
            film_horror = new_list['title'].values
            type_hor = st.sidebar.selectbox("which fime horror?",  film_horror, key=None)
            st.subheader("Here are all our horror films")
            st.dataframe(new_list, height = 450)
        if type_var == "Drama":
            masque = imdb["genre"].str.contains("Drama") 
            new_list = imdb[masque].sort_values(by="note",ascending=False)
            film_drama = new_list['title'].values
            type_hor = st.sidebar.selectbox("which fime horror?",  film_drama, key=None)
            st.subheader("Here are all our drama films")
            st.dataframe(new_list, height = 450)
    if result == "actor":
    
            imdb["actors_list"] = imdb["actors"].str.split(",")
            
            list_actors = imdb.explode("actors_list")["actors_list"].unique()            
            select_actor = st.sidebar.selectbox("which actor?",  list_actors, key=None)
            st.dataframe(imdb[imdb["actors"].str.contains(select_actor)])
            
            
            


           
        
        
        
        
# note = st.slider(
# ...     'Select a range of note',
# ...     ,  )
# >>> st.write('Values:', values)       
        
        
        
# # boutton pour montrer tous les films par note

# def get_table():
#     datatable = imdb.sort_values(by="note", ascending=False)
#     return datatable
# datatable = get_table()
# st.markdown("### Here to show you all of our movies by scrot")
# # with st.echo():用来同时在网页上显示代码和效果。
# # st.botton('<style>boutton{color:blue;}</style>',unsafe_allow_html=True)
# if st.button('Click Me for all our film by scort'):
#     st.dataframe(datatable) # will display the dataframe
#     #st.table(datatable)# will display the table
    
# #choice the film by type
# list_type = ["Horror","Comedy","Drama"]
# st.sidebar.selectbox("choice the tpye of film", list_type, index=0, key=None)
# masque = imdb["genre"].str.contains("Drama") #直接在文件的数据列表里创建一个masque，用来分别显示genre里的值
# imdb[masque]
# new_list = imdb[masque].sort_values(by="note").head(3)
# film_dramatic_3 = new_list['title'].values
# str(film_dramatic_3)







