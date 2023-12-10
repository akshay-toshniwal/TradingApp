from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_csv, name='upload_csv'),
    ]