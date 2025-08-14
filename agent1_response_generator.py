from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
import torch


sentiment_model = pipeline("sentiment-analysis")


text_gen = pipeline(
    "text-generation",
    model="microsoft/DialoGPT-small",
    device=0 if torch.cuda.is_available() else -1,
    pad_token_id=50256  
)

llm = HuggingFacePipeline(pipeline=text_gen)

def detect_sentiment(text):
    result = sentiment_model(text)[0]
    return result['label'].lower()

def generate_reply(feedback_text, sentiment):
    prompt = (
        f"Customer feedback: \"{feedback_text}\"\n"
        f"Sentiment: {sentiment}\n"
        "Write a polite, brief, and context-aware response as a restaurant representative."
    )
    generated = llm.invoke(prompt)
    reply = generated.replace(prompt, "").strip()


    if len(reply) < 20 or reply.lower().startswith("customer feedback"):
        return {
            "positive": "Thank you for your kind words! We're glad you enjoyed your visit.",
            "negative": "Thank you for your feedback. We're sorry for your experience and will work to improve.",
            "neutral": "Thank you for your feedback! We appreciate your input."
        }.get(sentiment, "Thank you for your feedback!")

    return reply

if __name__ == "__main__":
    feedback = input("Enter feedback: ")
    sentiment = detect_sentiment(feedback)
    reply = generate_reply(feedback, sentiment)
    print("Sentiment:", sentiment)
    print("Reply:", reply)
