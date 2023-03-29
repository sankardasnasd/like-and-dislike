from django.urls import path
from.import views

urlpatterns =[
    path("index",views.index,name='index'),
    path('',views.home,name='homepage'),
    path('login',views.loginView,name='loginView'),
    path('register',views.registerView,name='registerView'),
    path('like/<int:id/>,',views.like),
    path('dislike/<int:id>/',views.dislike)
    
]