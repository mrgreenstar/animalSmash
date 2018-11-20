from django.db import models

# Create your models here.

class Animal(models.Model):
    animal = models.CharField(max_length=200)
    rating = models.FloatField(default=400)

    def __repr__(self):
        return '<Animal> animal: {}, rating {}'.format(self.animal, self.rating)
