from django.urls import path

from .views import *

urlpatterns = [
    path('', Index.as_view(), name="main_page"),
    path('categories/', categories, name="categories"),
    path('profile/', user_pesonal, name="profile"),
    path('book/<int:book_id>/', BookPage.as_view(), name="book_page"),
    path('book/reserve/<int:book_id>', book_reservation, name="reservation"),
    path('register/', RegisterUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout')
]
