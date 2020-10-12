from django.shortcuts import render
from venture.models import Property
from django.views import View

# Create your views here.


class Venture(View):
    def get(self, request):
        property_list = Property.objects.all()
        template = 'home.html'
        context = {
            'property_list': property_list
        }

        return render(request, template, context)


