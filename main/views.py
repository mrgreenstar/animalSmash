import logging
import random
from django.shortcuts import render
from django.views import generic

from .models import Animal
from .rating import new_rating
# Create your views here.
#pylint: disable=E1101

class IndexView(generic.View):
    template_name = 'main/index.html'
    
    all_animals = list(Animal.objects.all())
    first_animal = random.choice(all_animals)
    all_animals.remove(first_animal)
    second_animal = random.choice(all_animals)
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'first_animal':self.first_animal,
            'second_animal':self.second_animal})

    def post(self, request, *args, **kwargs):
        if str(self.first_animal.id) == request.POST.get('first_animal'):
            logging.error('first')
            chosen_animal = self.first_animal
            unchosen_animal = self.second_animal
        else:
            logging.error('second')
            chosen_animal = self.second_animal
            unchosen_animal = self.first_animal
        
        chosen_animal.rating, unchosen_animal.rating = new_rating(chosen_animal.rating,
            unchosen_animal.rating)
        chosen_animal.save()
        unchosen_animal.save()

        all_animals = list(Animal.objects.all())
        self.first_animal = random.choice(all_animals)
        all_animals.remove(self.first_animal)
        self.second_animal = random.choice(all_animals)
        return render(request, self.template_name, {'first_animal':self.first_animal,
            'second_animal':self.second_animal})
