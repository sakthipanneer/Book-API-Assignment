from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests, json
from requests.exceptions import HTTPError
from django_filters.rest_framework import DjangoFilterBackend

from books.serializers import BooksSerializer, ExternalBookSerializer
from books.models import Book

# Create your views here.

class ExternalBookView(APIView):
    """
    Query the Ice and Fire API & serialize the received data
    """
    def get(self, request):
        try:
            queryset = request.GET.get('name') #Get the query params value
            if queryset:
                url = "https://www.anapioficeandfire.com/api/books?name=" + queryset # construct the request url
            else:
                url = "https://www.anapioficeandfire.com/api/books"  # construct the request url

            response = requests.get(url) # querying the request url with requested query params
            serializer = ExternalBookSerializer(data=json.loads(response.text), many=True) # serializing the response data
            serializer.is_valid()
            return Response({
                "status_code": status.HTTP_200_OK,
                "status": "success",
                "data": serializer.data})
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6

"""
Book viewset which is having all the REST API methods.
"""
class BookViewSet(viewsets.ModelViewSet):

    """
    create:
    Create the Book.

    retrieve:
    Retrieve the particular Book.

    list:
    Retrieve all the Book.

    partial_update:
    Partial update the Book.

    destroy:
    Delete the Book.
    """

    serializer_class = BooksSerializer
    queryset = Book.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name', 'country', 'publisher', 'release_date')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({
            "status_code": status.HTTP_201_CREATED,
            "status": "success",
            "data": [{'book':serializer.data}]})

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "status_code": status.HTTP_200_OK,
            "status": "success",
            "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        book_name = instance.name
        self.perform_destroy(instance)
        return Response({
            "status_code": status.HTTP_200_OK,
            "status": "success",
            "message": "The book "+ book_name +" was deleted successfully",
            "data": []})
