from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.

""" ************* This class includes list of fields in Book table ************* """

class Book(models.Model):
    name = models.TextField(max_length=100)
    isbn = models.TextField()
    authors = ArrayField(models.TextField())
    number_of_pages = models.PositiveIntegerField()
    publisher = models.TextField()
    country = models.TextField()
    release_date = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)

    # ************* Function for specifying custom table name *************
    class Meta:
        db_table = 'books_details'