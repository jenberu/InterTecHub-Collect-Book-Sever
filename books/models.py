from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    published_year=models.IntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.titlepy 
