from django.http import HttpResponse
from django.shortcuts import render


def hello_django(request):
    """访问首页的视图"""
    return HttpResponse("hello django")


def hello_view(request):
    # render返回的是HttpResponse对象
    return render(request, 'hello.html')


def news(request, category_id, page):
    return HttpResponse(f"Category: {category_id}, Page: {page}")


def news2(request):
    category = request.GET.get('category')
    page = request.GET.get('page')

    # ?category=1&page=2&a=3&a=4
    # a = request.GET.getlist('a')  # 一键多值通过 getlist 获取

    text = '获取查询字符串：<br/> category=%s, page=%s' % (category, page)
    return HttpResponse(text)


def news3(request):
    category = request.POST.get('category')
    page = request.POST.get('page')

    # 一键多值通过从POST中用 getlist 获取
    # ?category=1&page=2&a=3&a=4
    # a = request.POST.getlist('a')

    text = '获取body中的键值对:<br/>　category=%s, page=%s' % (category, page)
    return HttpResponse(text)


import json


def news4(request):
    # 获取json字符串
    json_str = request.body
    json_str = json_str.decode()  # python3.6 无需执行此步

    # 解析json
    dict_data = json.loads(json_str)
    category = dict_data.get('category')
    page = dict_data.get('page')

    text = '获取body中的json数据:　category=%s, page=%s' % (category, page)
    return HttpResponse(text)
