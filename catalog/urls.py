from django.urls import path

from . import views
from .views import BookDetailView,BookListView,AuthorListView,AuthorDetailView
# BookListView,

urlpatterns = [
    path('',views.index,name='index'),
    path('books/',BookListView.as_view(),name='books'),
    path('book/<int:pk>',views.BookDetailView.as_view(),name='book_detail'),
    path('authors/',AuthorListView.as_view()),
    path('author/<int:pk>',views.AuthorDetailView.as_view(),name='author_detail'),
    # path('accounts/login/',views.login,name='login'),
    path("login/", views.login, name="login"),
    path("logout/", views.logout_request, name="logout"),
]
