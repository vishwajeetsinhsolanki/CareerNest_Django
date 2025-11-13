"""
URL configuration for CareerNest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),  
    
    path('add-department/',views.add_department,name='add-department'),
    path('view-department/',views.view_department,name='view-department'),
    path('del-department/<int:pk>',views.del_department,name='del-department'),
    path('edit-department/<int:pk>',views.edit_department,name='edit-department'),
    path('update-department/',views.update_department,name='update-department'),
    
    path('add-faculty/',views.add_faculty,name='add-faculty'),
    path('all-faculty/',views.all_faculty,name='all-faculty'),
    path('del-faculty/<int:pk>',views.del_faculty,name='del-faculty'),
    # path('edit-faculty/<int:pk>',views.edit_faculty,name='edit-faculty'),
    # path('update-faculty/',views.update_faculty,name='update-faculty'),
    

    path('add-course/',views.add_course,name='add-course'),
    path('view-course/',views.view_course,name='view-course'),
    path('del-course/<int:pk>',views.del_course,name='del-course'),
    path('edit-course/<int:pk>',views.edit_course,name='edit-course'),
    path('update-course/',views.update_course,name='update-course'),

    path('add-student/',views.add_student,name='add-student'),
    path('all-student/',views.all_student,name='all-student'),
    path('del-student/<int:pk>',views.del_student,name='del-student'),

    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('reset-password/',views.reset_password,name='reset-password'),
    
]

