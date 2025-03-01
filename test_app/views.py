from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def function_view_test(request):
    return HttpResponse("<h1>Hello, World! Function-based View Tes</h1>")

class ClassViewTest(TemplateView):
    template_name = "test.html"