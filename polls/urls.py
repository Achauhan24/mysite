from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:question_id>', views.detail, name='detail'),
    path('<slug:question_id>/vote', views.vote, name='vote'),
    path('<slug:question_id>/results', views.results, name='results'),

]