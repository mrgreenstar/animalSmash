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

    @classmethod
    def random_animals(cls):
        '''
            ClassMethod for generate new pair of animals.
        '''
        cls.all_animals = list(Animal.objects.all())
        if cls.all_animals:
            cls.first_animal = random.choice(cls.all_animals)
            cls.all_animals.remove(cls.first_animal)
            cls.second_animal = random.choice(cls.all_animals)
        else:
            logging.error("Empty animal list")

    def get(self, request, *args, **kwargs):
        IndexView.random_animals()
        return render(request, self.template_name, {'first_animal':IndexView.first_animal,
            'second_animal':IndexView.second_animal})

    def post(self, request, *args, **kwargs):
        if request.POST.get("first_animal"):
            chosen_animal = Animal.objects.get(pk=request.POST.get("first_animal"))
            unchosen_animal = IndexView.second_animal
        else:
            chosen_animal = Animal.objects.get(pk=request.POST.get("second_animal"))
            unchosen_animal = IndexView.first_animal
        
        chosen_animal.rating, unchosen_animal.rating = new_rating(chosen_animal.rating,
            unchosen_animal.rating)
        chosen_animal.save()
        unchosen_animal.save()

        IndexView.random_animals()
        return render(request, self.template_name, {'first_animal':IndexView.first_animal,
            'second_animal':IndexView.second_animal})

class RatingView(generic.ListView):
    template_name = "main/rating.html"
    context_object_name = 'animal_list'

    def get_queryset(self):
        '''
            Return the top of animals.
        '''
        return Animal.objects.order_by('-rating')
    