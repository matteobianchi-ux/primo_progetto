from django.urls import path
from .views import home, ArticoloDetailView

app_name='news'

urlpatterns=[
    path('', home, name="homeview"),
    path("articoloi/<int:pk", ArticoloDetailView, name="articolo_detail")
]