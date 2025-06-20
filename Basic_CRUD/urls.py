from django.contrib import admin
from django.urls import path
from CRUDapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', read, name='read'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
