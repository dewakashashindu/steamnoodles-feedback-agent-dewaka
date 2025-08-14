# main_multiagent_runner.py

from agent1_response_generator import detect_sentiment, generate_reply
from agent2_sentiment_visualizer import visualize_sentiments

import csv
from datetime import date

def append_to_csv(review_text, sentiment):
    with open('dataset/Reviews.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([review_text, sentiment, date.today()])

def main():
    while True:
        print("\n=== SteamNoodles Feedback Agent ===")
        print("1. Add new customer feedback (Agent 1)")
        print("2. Visualize sentiment trends (Agent 2)")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            feedback = input("\nEnter customer feedback: ")
            sentiment = detect_sentiment(feedback)
            reply = generate_reply(feedback, sentiment)
            print(f"Sentiment: {sentiment}")
            print(f"Reply: {reply}")
            append_to_csv(feedback, sentiment)
        elif choice == '2':
            print("\nEnter start date (YYYY-MM-DD): ")
            start_date = input().strip()
            print("Enter end date (YYYY-MM-DD): ")
            end_date = input().strip()
            visualize_sentiments(start_date, end_date)
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == '__main__':
    main()
