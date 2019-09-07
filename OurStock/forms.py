from django import forms

class StockForm(forms.Form):
    stock_name = forms.CharField(max_length=200)
    stock_price = forms.CharField(max_length=200)
    stock_ = forms.CharField(max_length=200)
