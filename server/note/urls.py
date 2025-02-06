from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('all', views.all, name='all'),
    path('create/', views.create_note, name='create'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('edit/<int:note_id>', views.edit_note, name='edit'),
    path('login/', views.login_user, name="login_user"),
    path('signup/', views.signup_user, name="signup")

]   
    

   
    
  