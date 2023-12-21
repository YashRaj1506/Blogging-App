from django.db import models

class Details(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"




