from django.test import TestCase

from .models import Animal
from .rating import new_rating
# Create your tests here.

class NewRatingTests(TestCase):

    def test_new_rating(self):
        """
        test_new_rating() returns True if winner rating is greater than loser rating.
        """
        first_animal = Animal(animal='testAnimal1', id=1)
        second_animal = Animal(animal='testAnimal2', id=2)
        first_animal.rating, second_animal.rating = new_rating(first_animal.rating, second_animal.rating)
        self.assertIs(first_animal.rating > second_animal.rating, True)
