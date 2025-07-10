from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterFormUser, LoginUserForm
from .models import *


class Index(ListView):
    model = Book
    template_name = "library/main_page.html"
    context_object_name = "books"
    extra_context = {"title": "Главная страница"}

    paginate_by = 3

def categories(request):
    return render(request, "library/categories.html")


class BookPage(DetailView):
    model = Book
    template_name = "library/book_page.html"
    pk_url_kwarg = "book_id"

def book_page(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        "book": book
    }
    return render(request, "library/book_page.html", context)

def user_pesonal(request):
    local_user = request.user
    user_reservations = Reservation.objects.filter(user=local_user.pk)

    context = {
        "user": local_user,
        "rentals": user_reservations
    }
    return render(request, "library/user_profile.html", context)


class RegisterUser(CreateView):
    form_class = RegisterFormUser
    template_name = "library/register_page.html"
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "library/login_page.html"

    def get_success_url(self):
        return reverse_lazy('main_page')

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def book_reservation(request, book_id):
    if request.method == "POST":
        return redirect("main_page")
    book = Book.objects.get(pk=book_id)
    return render(request, "library/book_reservation.html",{"book":book})
