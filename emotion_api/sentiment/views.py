import os
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Set NLTK data path to a directory where it can write (e.g., home directory)
nltk_data_dir = os.path.expanduser('~/nltk_data/')
if not os.path.exists(nltk_data_dir):
    os.makedirs(nltk_data_dir)

nltk.data.path.append(nltk_data_dir)

# Try to download the vader_lexicon if not already downloaded
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon', download_dir=nltk_data_dir)

# Create the SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

@api_view(['POST'])
def analyze_sentiment(request):
    """
    API view to analyze sentiment of input text
    """
    text = request.data.get('text', '')  # Get the 'text' field from the request

    if not text:
        return Response({"error": "No text provided"}, status=400)

    # Analyze the sentiment of the text
    sentiment = sia.polarity_scores(text)
    
    # Return the emotional values as a response
    return Response({
        'text': text,
        'positive': sentiment['pos'],
        'neutral': sentiment['neu'],
        'negative': sentiment['neg'],
        'compound': sentiment['compound'],
    })
