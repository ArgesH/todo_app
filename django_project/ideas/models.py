from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


class Idea(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=90)
    created_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


