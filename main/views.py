import logging
import random
from django.shortcuts import render, redirect
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
        logging.error("get")
        all_animals = list(Animal.objects.all())
        self.first_animal = random.choice(all_animals)
        all_animals.remove(self.first_animal)
        self.second_animal = random.choice(all_animals)   
        return render(request, self.template_name, {'first_animal':self.first_animal,
            'second_animal':self.second_animal})

    def post(self, request, *args, **kwargs):
        logging.error(request.POST.items)
        if request.POST.get("first_animal"):
            chosen_animal_id = request.POST.get("first_animal").split('&')[0]
            unchosen_animal_id = request.POST.get("first_animal").split('&')[1]
        else:
            chosen_animal_id = request.POST.get("second_animal").split('&')[0]
            unchosen_animal_id = request.POST.get("second_animal").split('&')[1]
        
        chosen_animal = Animal.objects.get(pk=chosen_animal_id)
        unchosen_animal = Animal.objects.get(pk=unchosen_animal_id)
        chosen_animal.rating, unchosen_animal.rating = new_rating(chosen_animal.rating,
            unchosen_animal.rating)
        chosen_animal.save()
        unchosen_animal.save()

        # For new animals after POST
        all_animals = list(Animal.objects.all())
        self.first_animal = random.choice(all_animals)
        all_animals.remove(self.first_animal)
        self.second_animal = random.choice(all_animals)   
        return render(request, self.template_name, {'first_animal':self.first_animal,
            'second_animal':self.second_animal})
