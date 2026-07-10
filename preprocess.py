import re
import pandas as pd

def preprocess_whatsapp_chat_df(data):
    pattern = r'^\[\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}:\d{2}\s[A-Z]{2}\]\s'
    
    messages = re.split(pattern,data,flags= re.MULTILINE)[1:]
    dates = re.findall(pattern,data,flags= re.MULTILINE)
    
    clean_dates = [date.strip().strip("[]") for date in dates ]
    df = pd.DataFrame({"date" : clean_dates,"msg":messages})

    df['date'] = pd.to_datetime(df['date'], format="%m/%d/%y, %I:%M:%S %p")
    df["month"] = df["date"].dt.month_name()
    df["day"] = df["date"].dt.day
    df["month_num"] = df["date"].dt.month
    df["Every day"] = df["date"].dt.date
    df["hour"] = df["date"].dt.hour
    df["year"] = df["date"].dt.year
    df["day_name"] = df["date"].dt.day_name()
    
    df["name"] = df["msg"].str.extract(r"^([^:]+):")
    df["msg"] = df["msg"].str.extract(r"^[^:]+:\s*(.*)")
    df["name"] = df["name"].fillna("system notifications")
    
    df[df["name"] == "system notifications"]
    df["msg"] = df["msg"].str.strip("\n")

    return df