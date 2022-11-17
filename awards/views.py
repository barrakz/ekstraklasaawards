from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from awards.models import Category, Nomination


class CategoryList(ListView):
    model = Category
    context_object_name = 'category_list'

    template_name = 'awards/category_list.html'


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nomination_list'] = Nomination.objects.filter(category=self.object)
        return context


class NominationsList(ListView):
    model = Nomination
    context_object_name = 'nominations'
    template_name = 'awards/nomination_list.html'


class NominationDetail(DetailView):
    model = Nomination
    context_object_name = 'nomination'
    queryset = Nomination.objects.all()
