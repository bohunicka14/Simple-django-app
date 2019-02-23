from django.urls import path, include
from django.views.generic.base import TemplateView
from results import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="results/main.html"), name='result_main'),
    path('list', views.ResultList.as_view(), name='result_list'),
]