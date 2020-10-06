from django.shortcuts import render
from . import extract
from django.http import HttpResponse

def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q'] :
        txt = request.GET['q']
        Data = extract.extract(txt)
        print("进行抽取...")
        views_list = ["菜鸟教程", "菜鸟教程1", "菜鸟教程2", "菜鸟教程3", ]
        return render(request, 'output.html', {"Data": Data, "txt": txt, })
    else:
        print("没有内容！！！")
        return render(request, 'search.html')
