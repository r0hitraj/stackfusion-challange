from django.urls import path
from .import views


urlpatterns=[

    path('',views.index, name='index'),   #route of form page
    path('details/',views.details, name='details'),   #route of details page

]