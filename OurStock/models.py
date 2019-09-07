from django.db import models
from django.urls import reverse
from django.db import models
from django.forms import ModelForm




class Stock(models.Model):
    stock_name = models.CharField(max_length=200)
    stock_price = models.IntegerField()
    stock_to_sell = models.IntegerField()

    def get_absolute_url(self):
        return reverse('showall')

