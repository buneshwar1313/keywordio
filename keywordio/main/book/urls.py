
from django.urls import path
from . import views
from .views import *
urlpatterns = [
   path('register/',UserRegistration.as_view()),
   path('login/',LoginView.as_view()),
   path('logout/',LoginView.as_view()),
   path('bookall/',BookView.as_view()),
   path('Bookupdate/<int:pk>/',BookUpdateDelete.as_view()),

   path('book/', Book.as_view(), name='Book'),
   path('book/<int:id>/', Book.as_view(), name='vehicle_fit'),
]
