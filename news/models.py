from django.db import models

# Create your models here.

class Breaking_news(models.Model):
    title=models.TextField()
    created_date = models.DateField(auto_now_add=True)
    class Meta:
        db_table = "Breaking_news"