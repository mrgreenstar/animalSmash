from django.test import TestCase
from django.urls import reverse

from .models import Animal
from .rating import new_rating
from .views import IndexView
# Create your tests here.

class NewRatingTests(TestCase):
    def test_new_rating(self):
        """
        Returns True if winner rating is greater than loser rating.
        """
        first_animal = Animal(animal='testAnimal1', id=1)
        second_animal = Animal(animal='testAnimal2', id=2)
        first_animal.rating, second_animal.rating = new_rating(first_animal.rating, second_animal.rating)
        self.assertIs(first_animal.rating > second_animal.rating, True)

class IndexTestView(TestCase):
    def test_is_different_animals(self):
        """
            Returns True if first animal and second animal are different animals
        """
        IndexView.all_animals = [Animal(animal='testAnimal1', id=1), Animal(animal='testAnimal2', id=2)]
        IndexView.first_animal = Animal(animal='testAnimal1', id=1)
        IndexView.second_animal = Animal(animal='testAnimal2', id=2)
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIsNot(IndexView.first_animal, IndexView.second_animal)
