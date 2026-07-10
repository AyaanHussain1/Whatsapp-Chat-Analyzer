# WhatsApp Chat Analyzer

🔗 **Live Demo:** [https://whatsapp-chat-analyzer-sys.streamlit.app/]

An interactive web app that analyzes any exported WhatsApp chat, turning raw conversation exports into statistics, timelines, word clouds, and emoji breakdowns.

## Overview

WhatsApp lets you export any chat as a plain `.txt` file, but that raw export is hard to make sense of at a glance. This app parses that export directly, extracts structured data (sender, timestamp, message content) using regex, and generates a full analytics dashboard — message counts, activity over time, most active users, most common words, and emoji usage — all filterable by individual participant or the whole group.

## How It Works

1. **Parsing** — Takes a raw WhatsApp `.txt` export and uses a regex pattern to split it into individual messages with timestamps, then extracts the sender name and message text from each line.
2. **Feature Extraction** — Derives date-based fields (year, month, day, hour, day of week) from each message's timestamp to support timeline and activity analysis.
3. **Analysis Functions** — A dedicated function library (`all_functions.py`) computes:
   - Total messages, word count, and links shared (per user or overall)
   - Monthly and daily message timelines
   - Most active users in a group chat
   - Busiest days and months
   - Most frequently used words (with a custom Hindi/Urdu + English stopword list to filter out common filler words)
   - Word cloud generation
   - Emoji usage frequency and distribution
4. **Deployment** — Built as a Streamlit app: upload a chat export file, optionally filter by a specific participant, and instantly view all the generated charts and statistics.

## Tech Stack

- **Language:** Python
- **Data Handling:** Pandas, regex
- **Text Analysis:** urlextract, wordcloud, emoji, Counter (collections)
- **Visualization:** Matplotlib, Seaborn
- **App/Deployment:** Streamlit

## Project Structure

```
whatsapp-chat-analyzer/
├── app.py                # Streamlit web app (main entry point)
├── preprocess.py          # Regex-based chat parsing and timestamp feature extraction
├── all_functions.py       # Analysis functions (stats, timelines, word cloud, emojis)
├── stop_english.txt       # Custom stopword list (English + Hindi/Urdu filler words)
└── requirements.txt       # Python dependencies
```

Note: no sample chat file is included in this repo, since chat exports contain private conversation data. To try the app, export any WhatsApp chat (without media) from your phone and upload it directly in the app.

## Installation & Usage

```bash
# Clone the repository
git clone https://github.com/AyaanHussain1/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then upload any WhatsApp chat export (`.txt` file, exported without media) through the sidebar.

## Results

The app successfully parses real-world WhatsApp exports with mixed content (text, emojis, links, system notifications, edited-message markers) and produces a full interactive analytics view without any manual data cleaning required from the user.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This project is built for educational and portfolio purposes. It processes chat data entirely within the user's own session and does not store or transmit uploaded chat files anywhere.
