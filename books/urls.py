from django.urls import path, include
from rest_framework import routers

from books import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)


urlpatterns = [
    path('external-books/', views.ExternalBookView.as_view(), name='External Books'),
    path('v1/', include(router.urls), name='Books')
]