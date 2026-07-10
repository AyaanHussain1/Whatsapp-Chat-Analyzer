import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re
import preprocess,all_functions
from urlextract import URLExtract
extractor = URLExtract()

st.sidebar.title("Whatsapp Chat Analyzer")
updload_file  = st.sidebar.file_uploader("Choose a file")
if updload_file is not None:
    bytes_data = updload_file.getvalue()
    data = bytes_data.decode("utf-8")
    # st.text(data)

    df = preprocess.preprocess_whatsapp_chat_df(data)
    # st.dataframe(df)

    user_list = df["name"].unique().tolist()
    try:
        user_list.remove("system notifications")
    except:
        pass
    user_list.sort()
    user_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("Show Analysis according to user",user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages,words,links =  all_functions.fetch_data(selected_user,df)
        st.title("Top Statistics")
        col1 , col2 ,col3 ,col4  = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(words)
        with col3:
            st.header("Links Shared")
            st.title(links)

        # timeline
        st.title("Time line")
        timeline = all_functions.monthly_timeline(selected_user,df)
        fig,axs = plt.subplots()
        axs.plot(timeline["time"],timeline["msg"],color="green") 
        st.pyplot(fig)

        # daily timeline

        st.title("Daily Time line")
        daily_time = all_functions.daily_timeline(selected_user,df)
        fig,axs = plt.subplots()
        axs.plot(daily_time["Every day"],daily_time["msg"],color="purple") 
        st.pyplot(fig)
        
        # activity map
        st.title("Activity map")
        col1,col2 = st.columns(2)

        with col1:
            st.header("Most Busy Day")
            busy_day = all_functions.week_activity(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(busy_day.index,busy_day.values)
            st.pyplot(fig)

        with col1:
            st.header("Most Busy Month")
            Month_day = all_functions.moth_activity(selected_user,df)
            fig,ax = plt.subplots()
            ax.bar(Month_day.index,Month_day.values)
            st.pyplot(fig)
        
        # most active users in groups
        
        if selected_user == "Overall":
            st.title("Most Active users")
            x,new_df = all_functions.most_active_users(df)
            col1,col2 = st.columns(2)
            fig,axs = plt.subplots()

            with col1:
                axs.bar(x.index,x.values)
                plt.xticks(rotation="vertical")
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)
        df_wc = all_functions.create_word_cloud(selected_user,df)
        st.title("Word CLoud")
        fig,axs = plt.subplots()
        axs.imshow(df_wc)
        st.pyplot(fig)

        most_common_word = all_functions.most_common_words(selected_user,df)
        # st.dataframe(most_common_word)
        fig ,ax = plt.subplots()
        ax.barh(most_common_word[0],most_common_word[1])
        plt.xticks(rotation="vertical")
        st.title("Most Common Words")
        st.pyplot(fig)

        # emojis
        st.title("Emojis Analysis")
        col1,col2 = st.columns(2)
        emoji_df = all_functions.fetching_emojis(selected_user,df)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig,ax = plt.subplots()
            ax.pie(emoji_df[1],labels=emoji_df[0],autopct="%.2f%%")
            st.pyplot(fig)