# Django Emotion API

This project is a Django-based API that analyzes the emotional value of text using the VADER sentiment analysis tool. The API is built with Django and can be deployed using Firebase Cloud Functions or other platforms like Heroku or Google Cloud.

## Prerequisites

Before running this project, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [NLTK](https://www.nltk.org/)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/django-emotion-api.git
   cd django-emotion-api

Create and Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

Install Dependencies

pip install -r requirements.txt

Ensure the vader_lexicon is available for NLTK:
import nltk
nltk.download('vader_lexicon')

To start the Django development server:
python manage.py runserver

You can now access the API at http://127.0.0.1:8000/api/analyze/

API Usage
POST http://127.0.0.1:8000/api/analyze/

Request Body
{
  "text": "Your text goes here"
}

Response

{
  "text": "Your text goes here",
  "positive": 0.68,
  "neutral": 0.32,
  "negative": 0.0,
  "compound": 0.87
}
