from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Stock
from .forms import StockForm
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings


# def stock(request):
#
#     if request.method != 'POST':
#
#         form = StockForm()
#         dict = {"form":form}
#     else:
#         form = StockForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['stock_name']
#             addiction = form.cleaned_data['stock_price']
#             nickname = form.cleaned_data['stock_to_sell']
#             c1 = Stock()
#             c1.stock_name = name
#             c1.stock_price = price
#             c1.stock_to_sell = quantity
#             c1.save()
#             return HttpResponse("Added")
#
#     return render(request, 'stock.html', dict)


class StockAdd(CreateView):
    model = Stock
    fields = ['stock_name', 'stock_price', 'stock_to_sell']
    template_name = "stock.html"


class StockList(ListView):
    model = Stock
    template_name = "stock.html"
    context_object_name = "stocklist"


class StockUpdate(UpdateView):
    model = Stock
    fields = ['stock_name', '']
    template_name = 'stock.html'


class StockDelete(DeleteView):
    model = Stock
    template_name = 'stock.html'


class StockTemplate(TemplateView):
    template_name = 'index.html'


def email(request):
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sravankrishna03@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("Email sent")
