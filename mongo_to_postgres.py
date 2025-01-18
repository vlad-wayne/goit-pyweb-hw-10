from pymongo import MongoClient
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes_site.settings')
django.setup()

from quotes.models import Author, Quote


client = MongoClient("mongodb://localhost:27017/")
db = client['quotes_db']


for mongo_author in db.authors.find():
    author, _ = Author.objects.get_or_create(
        fullname=mongo_author['fullname'],
        born_date=mongo_author.get('born_date'),
        born_location=mongo_author.get('born_location'),
        description=mongo_author.get('description')
    )


for mongo_quote in db.quotes.find():
    author = Author.objects.get(fullname=mongo_quote['author'])
    Quote.objects.create(
        text=mongo_quote['quote'],
        tags=mongo_quote['tags'],
        author=author
    )
