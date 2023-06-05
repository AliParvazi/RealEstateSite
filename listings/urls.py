from django.urls import path
from . import views


urlpatterns = [
    path('', views.listings, name='listings'),
    path('<int:listing_id>', views._listing, name='listing'),
    path('search', views.search, name='search')
]