import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
# Download NLTK resources on first run
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('omw-1.4', quiet=True)
STOPWORDS = set(stopwords.words('english'))
LEMMATIZER = WordNetLemmatizer()
URL_PATTERN = re.compile(r'https?://\S+|www\.\S+')
NON_ALPHANUM = re.compile(r'[^a-zA-Z0-9\s]')
MULTI_SPACE = re.compile(r'\s+')
def clean_text(text: str) -> str:
"""Basic text cleaning: lowercase, remove URLs, punctuation, stopwords
and lemmatize."""
if not isinstance(text, str):
return ''
text = text.lower()
text = URL_PATTERN.sub(' ', text)
text = NON_ALPHANUM.sub(' ', text)
text = MULTI_SPACE.sub(' ', text).strip()
tokens = [t for t in text.split() if t not in STOPWORDS]
lemmas = [LEMMATIZER.lemmatize(t) for t in tokens]
return ' '.join(lemmas)
