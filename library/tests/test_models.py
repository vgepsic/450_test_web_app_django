import pytest

from django.test import Client
from library.models import Book

@pytest.mark.django_db
def test_book_model_str():
    Book.objects.create(author = "Dominique Roques", title = "Pico Bogue")
    book = Book.objects.get(id=1)
    expected_value = "Dominique Roques | Pico Bogue"
    
    assert str(book) == expected_value
