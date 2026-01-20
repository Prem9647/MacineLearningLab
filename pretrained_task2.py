from transformers import pipeline

# Load pretrained sentiment analysis model
classifier = pipeline("sentiment-analysis")

# Test sentence
text = "This product is good"

result = classifier(text)
print(result)
