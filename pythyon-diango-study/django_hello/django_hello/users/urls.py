from django.urls import path

from django_hello.users import views

urlpatterns = [

    # 配置url和视图函数，需要调用url函数，并传入参数
    # 参数1： 匹配url的正则表达式（需要用 ^ 和 $ 匹配开头和结尾）
    # 参数2： url匹配成功执行的视图函数
    path(r'index', views.index),
]
