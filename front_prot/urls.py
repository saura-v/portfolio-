from django.urls import path 
from .import views


urlpatterns=[
    path('',views.index,name='index'),
    # path('',views.components,name='component'),
    path('contact/',views.Contact,name='contact')
]