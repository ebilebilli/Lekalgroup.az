from django.views import View
from django.http import HttpResponse
from django.shortcuts import render


__all__ = [
    'HomeView',
]


class HomeView(View):
    def get(self, request):
        return render(request, 'blog.html')