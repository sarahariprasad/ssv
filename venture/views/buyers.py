from django.views import View
from django.shortcuts import render
from venture.models.buyers import Buyer
from venture.models.video import Video


class Buyers(View):
    def get(self, request):
       reviews = Buyer.objects.all()
       files = Video.objects.all()
       dates = Buyer.objects.filter(date__range=["2020-01-01", "2020-01-31"])
       template = 'buyers.html'
       context = {
           'reviews': reviews,
           'files': files,
           'dates': dates
       }
       return render(request, template, context)

