import pandas as pd
import matplotlib.pyplot as plt
import re


df = pd.read_csv("dataset/Reviews.csv")

def clean_review_date(date_str):
    
    if pd.isna(date_str):
        return None
    match = re.search(r'([A-Za-z]+ \d{4})', str(date_str))
    return match.group(1) if match else None

def filter_reviews_by_date(df, start_date, end_date):
    
    df['Cleaned Review Date'] = df['Review Date'].apply(clean_review_date)
    df['Parsed Review Date'] = pd.to_datetime(df['Cleaned Review Date'], format='%b %Y', errors='coerce')
    print("Parsed Review Dates:\n", df['Parsed Review Date'])
    mask = (df['Parsed Review Date'] >= pd.to_datetime(start_date)) & (df['Parsed Review Date'] <= pd.to_datetime(end_date))
    filtered = df.loc[mask]
    print("Filtered DataFrame:\n", filtered)
    return filtered

def count_sentiments_per_day(filtered_df):
    
    filtered_df['Sentiment'] = filtered_df['Sentiment'].str.capitalize()
    counts = filtered_df.groupby([filtered_df['Parsed Review Date'].dt.date, 'Sentiment']).size().unstack(fill_value=0)
    print("Counts DataFrame:\n", counts)
    return counts

def plot_sentiment_trend(count_df):
    if count_df.empty:
        print("No data to plot for the selected date range.")
        return
    count_df.plot(kind='bar', stacked=True, figsize=(10,6))
    plt.title("Sentiment Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Reviews")
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()


def visualize_sentiments(start_date, end_date):
    filtered = filter_reviews_by_date(df, start_date, end_date)
    counts = count_sentiments_per_day(filtered)
    plot_sentiment_trend(counts)


if __name__ == "__main__":
    start = "2023-01-01"
    end = "2024-12-31"
    visualize_sentiments(start, end)
