
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import State, Town


# Template: taxes/state_list.html
class StateListView(ListView):
    model = State


# Template: taxes/state_detail.html
class StateDetailView(DetailView):
    model = State
    slug_field = "name"
    slug_url_kwarg = "state_name"


# Template: taxes/town_list.html
class TownListView(ListView):
    model = Town
    # paginate_by = 20

    # def get_queryset(self):
    #     state_name = self.kwargs.get('state_name')
    #     return Town.objects.filter(state__name=state_name)


# Template: taxes/town_detail.html
class TownDetailView(DetailView):
    model = Town
    slug_field = "name"
    slug_url_kwarg = "town_name"

