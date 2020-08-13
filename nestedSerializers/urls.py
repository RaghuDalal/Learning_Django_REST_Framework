from django.urls import path
from nestedSerializers import views

urlpatterns = [
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>', views.AuthorDetailView.as_view()),
    path('book/', views.BookListView.as_view()),
    path('book/<int:pk>', views.BookDetailView.as_view()),
]
