from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/' , include('polls.urls') ),
    path('polls2/', include('polls2.urls')),
    path('admin/' , admin.site.urls       ),
]
