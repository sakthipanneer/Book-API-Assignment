from django.test import TestCase
from books.models import Book
from books.views import ExternalBookView
from rest_framework.test import APIRequestFactory

# Create your tests here.

book_data = {
    "name": "Book 2",
    "isbn": "123-1212-2122",
    "authors": ["User1", "User2"],
    "number_of_pages": 350,
    "publisher": "XYZ Publishers",
    "country": "Europe",
    "release_date": "2018-06-01"

}

factory = APIRequestFactory()

class BookModelTest(TestCase):
    """ Test module for Books model """

    def setUp(self):
        Book.objects.create(
            name="Book 1",
            isbn="123-122-2122",
            authors=["User1", "User2"],
            number_of_pages=250,
            publisher="ABC Publishers",
            country="India",
            release_date="2018-06-01"
        )

    def test_book_publishers(self):
        book_data = Book.objects.get(name='Book 1')
        self.assertEqual(book_data.publisher, 'ABC Publishers')


class BookExternalAPITest(TestCase):
    """ Test module for Books External API views """

    def test_success(self):
        request = factory.get('/api/external-books/?name=A Game of Thrones')
        response = ExternalBookView().get(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'][0]['name'], "A Game of Thrones")

    def test_empty(self):
        request = factory.get('/api/external-books/?name=A Game of')
        response = ExternalBookView().get(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['data'], [])