
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns =[
    path('login/', views.loginPage, name = "login"),
    path('main/', views.main, name = "main"),
    path('',views.searchh, name="searchh"),
    path('results/', views.results, name= "results"),
    path('career/', views.career, name= "career"),
    path('find/', views.find, name = 'find'),
    path('science/', views.science, name= 'science'),
    path('commerce/', views.commerce, name= 'commerce'),
    path('Art/', views.Art, name = 'Art'),
    path('education/', views.education, name = 'education'),
    path('add-Course/', views.addCourse, name = "add-Course"),
     path('update/', views.updateCourse, name = "update"),
    path('delete/', views.delete, name = "delete"),
]
urlpatterns += staticfiles_urlpatterns()