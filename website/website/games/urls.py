from django.urls import path
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='phaser_test_game.html'), name='games'),
]