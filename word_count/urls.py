
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('Jatin',views.jj),
    path('first web page',views.dhingra,name='my_first_web_page'),
    path('count_the _word/',views.count,name='count')
]