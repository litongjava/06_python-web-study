"""django_hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from django_hello import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 配置路由和视图: http://127.0.0.1:8000/users/index
    # 参数1： 匹配url的正则表达式
    # 参数2： 匹配成功后由Django框架调用的视图函数
    path('hello_django/', views.hello_django, name='hello_django'),
    path('hello_view/', views.hello_view, name='hello_view'),
    # 参数1： 匹配url的正则表达式
    # 参数2： 调用 inclucde 函数，包含users模块下的urls.py
    path('users/', include('django_hello.users.urls')),
    path('news/<int:category_id>/<int:page>/', views.news, name='news'),
    path(r'news2', views.news2),
    path(r'news3', views.news3),
    path(r'news4', views.news4),
]
