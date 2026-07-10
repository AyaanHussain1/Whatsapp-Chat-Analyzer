from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

def fetch_data(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]
    words = []
    num_message = df.shape[0]
    for message in df["msg"]:
        words.extend(message.split())
    # num_media_msg = df[df["msg"] == "<Media omitted>"].shape[0] # for media messages
    url = []
    extractor = URLExtract()
    for message in df["msg"]:
        url.extend(extractor.find_urls(message))

    return num_message,len(words),len(url)

def most_active_users(df):
    x = df["name"].value_counts().head(5) 
    df = round((df["name"].value_counts()/df.shape[0])* 100,2).reset_index().rename(columns={"index":"name","count":"percent"})
    return x,df
            
def create_word_cloud(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]
    wc = WordCloud(width=400,height=400,min_font_size=10,background_color="white")
    df_wc = wc.generate(df["msg"].str.cat(sep=" "))
    return df_wc

def most_common_words(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]

    f = open("stop_english.txt","r")
    stop_words = f.read()
    words = []
    list_of_word = ["<This","message","was","edited>"]
    for msg in df["msg"]:
        for word in msg.lower().split():
            if word not in stop_words and word not in list_of_word:
                words.append(word)

    df = pd.DataFrame(Counter(words).most_common(20))
    return df

def fetching_emojis(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]

    emojis = []
    for message in df["msg"]:
        emojis.extend([c for c in message if emoji.is_emoji(c)])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(emojis)))
    return emoji_df

def monthly_timeline(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]
    timeline = df.groupby(["year","month_num","month"]).count()["msg"].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append((f"{timeline["month"][i]}-{str(timeline["year"][i])}"))
    timeline["time"] = time

    return timeline
    
def daily_timeline(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name] 
    daily_timeline = df.groupby("Every day").count()["msg"].reset_index()

    return daily_timeline

def week_activity(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]
    
    return df["day_name"].value_counts() 

def moth_activity(user_name,df):
    if user_name != "Overall":
        df = df[df["name"] == user_name]
    
    return df["month"].value_counts() 