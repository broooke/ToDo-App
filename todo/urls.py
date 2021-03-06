"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from viewtasks import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('add/', views.add, name='add'),
    path('update/<int:task_id>/', views.update, name='update'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('deletecomp/<int:task_id>/', views.deletecompleted, name='deletecompleted'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.loginout, name='logout'),
]
