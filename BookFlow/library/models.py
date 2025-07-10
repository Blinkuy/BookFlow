from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import EmailValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=255, null=True)
    email = models.CharField(
        max_length=254,
        unique=True,
        validators=[EmailValidator()]
    )
    phone = models.CharField(
        max_length=20,
        unique=True,
    )


User.groups.field.related_name = 'library_users'
User.user_permissions.field.related_name = 'library_users_permissions'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    publisher = models.CharField(max_length=255)
    available_copies = models.IntegerField()
    total_copies = models.IntegerField()

    cover = models.ImageField(upload_to="photos/%Y/%m/%d")
    describe = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        if self.available_copies < 0:
            raise ValidationError("Количество доступных книг не может быть отрицательным")
        if self.available_copies > self.total_copies:
            raise ValidationError("Доступных книг не может быть больше общего количества")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Книги"
        ordering = ["-id"]


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активна'),
        ('completed', 'Завершена'),
        ('cancelled', 'Отменена'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
    )

    reservation_code = models.CharField(max_length=20, unique=True, null=True)

    def clean(self):
        if self.book.available_copies <= 0:
            raise ValidationError("Нет доступных книг для резервации")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.clean()
            self.book.available_copies -= 1
            self.book.save()
        super().save(*args, **kwargs)


@receiver(pre_save, sender=Reservation)
def set_expiration(sender, instance, **kwargs):
    if not instance.expiration_date:
        instance.expiration_date = instance.reservation_date + timedelta(days=30)
