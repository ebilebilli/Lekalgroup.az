from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect


__all__ = [
    'HomeView',
    'BlogView',
    'AboutView'
]


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')
    

class BlogView(View):
    def get(self, request):
        return render(request, 'blog.html')


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')