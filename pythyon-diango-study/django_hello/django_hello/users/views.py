from django.http import HttpResponse


def index(request):
    """访问首页的视图"""
    return HttpResponse("users index")


def news(request, a, b):
    return HttpResponse("显示新闻：%s %s" % (a, b))
