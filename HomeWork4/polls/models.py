from django.db import models
import datetime
class Pastes(models.Model):
    text = models.TextField()
    title=models.CharField(max_length=200)
    created_date=models.DateTimeField("Date",default=datetime.date.today)

  
# Create your models here.
