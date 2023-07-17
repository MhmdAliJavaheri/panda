from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from clients.models import Client
# Create your models here.


class Auther(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nick_name

    def serialize(self):
        return dict(
            nickName=self.nick_name,
            modified=self.modified_at
        )


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(unique=False, null=False, blank=False)
    location = models.TextField(null=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            modified=self.modified_at
        )


class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()
    publisher_year = models.DateTimeField(default=timezone.now())
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    auther = models.ForeignKey(
        Auther,
        on_delete=models.CASCADE,
        related_name='books'
    )

    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self) -> str:
        return self.title

    def serialize(self):
        return dict(
            title=self.title,
            created=self.created_at
        )
