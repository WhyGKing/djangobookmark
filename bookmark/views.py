from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')     #대신에 get_absolute_url을 정의하여 사용하기도 함
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_confirm_delete'