import logging
import random
from django.shortcuts import render
from django.views import generic

from .models import Animal
# Create your views here.
#pylint: disable=E1101

class IndexView(generic.View):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        firstAnimal = random.choice(Animal.objects.all())
        secondAnimal = random.choice(Animal.objects.all())
        return render(request, self.template_name, {'firstAnimal':firstAnimal,
            'secondAnimal':secondAnimal})

    def post(self, request, *args, **kwargs):
        firstAnimal = random.choice(Animal.objects.all())
        secondAnimal = random.choice(Animal.objects.all())
        logging.error(request.POST)
        return render(request, self.template_name, {'firstAnimal':firstAnimal,
            'secondAnimal':secondAnimal})
