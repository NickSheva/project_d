from django.urls import path
from .views import function_view_test, ClassViewTest

urlpatterns = [
    path("test-function/", function_view_test),
    path("test-class/", ClassViewTest.as_view()),
]