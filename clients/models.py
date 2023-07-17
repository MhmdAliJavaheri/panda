from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    passworld = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name}'

    def serialize(self):
        return dict(
            id=self.id,
            firstName=self.first_name,
            lastName=self.last_name,
        )
