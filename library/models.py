from django.db import models


# Create your models here.
class Library(models.Model):
    NAME = (
        ('1', 'library number 1'),
        ('2', 'library number 2'),
        ('3', 'library number 3'),
        ('4', 'library number 4'),
        ('5', 'library number 5'),
        ('6', 'library number 6'),
        ('7', 'library number 7'),
        ('8', 'library number 8'),
        ('9', 'library number 9'),
        ('10', 'library number 10'),
    )
    name = models.IntegerField(
        choices=NAME
    )

    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def organization():
        libraries_list = []
        for i in Library.NAME:
            a = dict(
                name=i[0],
                value=i[1]
            )
            libraries_list.append(a)
        return libraries_list

    def serialize(self):
        return dict(
            id=self.id,
            name=dict(
                id=self.name,
                value=self.get_name_display()
            ),
            created=self.created_at
        )
