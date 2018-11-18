import logging
from django.shortcuts import render
from django.views import generic

from .models import Animal
from .forms import ChooseForm
# Create your views here.

class IndexView(generic.View):
    template_name = 'main/index.html'
    form_class = ChooseForm
    def get(self, request, *args, **kwargs):
        form = ChooseForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        logging.error(request, args, kwargs)
        form = self.form_class(request.POST)
        return render(request, self.template_name, {'form':form})
