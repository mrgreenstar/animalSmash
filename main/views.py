import logging
import random
from django.shortcuts import render
from django.views import generic

from .models import Animal
# Create your views here.
#pylint: disable=E1101

class IndexView(generic.View):
    template_name = 'main/index.html'
    firstAnimal = random.choice(Animal.objects.all())
    secondAnimal = random.choice(Animal.objects.all())
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'firstAnimal':self.firstAnimal.animal,
            'secondAnimal':self.secondAnimal.animal})

    def post(self, request, *args, **kwargs):
        logging.debug(request, args, kwargs)
        return render(request, self.template_name, {'firstAnimal':self.firstAnimal.animal,
            'secondAnimal':self.secondAnimal.animal})
