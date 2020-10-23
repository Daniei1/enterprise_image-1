from django.shortcuts import render
from . import extract
from django.http import HttpResponse
import os

from .settings import BASE_DIR


def search(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        if request.POST.get('q'):
            print("1")
            txt = request.POST.get('q')
            Data = extract.extract(txt)
            print("进行抽取...")
            return render(request, 'output.html', {"Data": Data, "txt": txt, })
        elif request.FILES.get("myfile", None):
            print("2")
            file_path = "E:\\github_repository\enterprise_image\djangoProject\data"
            myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
            if not myFile:
                return HttpResponse("no files for upload!")
            destination = open(os.path.join(file_path, myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
            for chunk in myFile.chunks():  # 分块写入文件
                destination.write(chunk)
            destination.close()
            # 文件已经存到data文件夹下，下面进行读取然后提取
            with open('E:\github_repository\enterprise_image\djangoProject\data\\'+myFile.name, 'r', encoding='UTF-8') as f:
                data = f.read()
            Data = extract.extract(data)
            print("进行抽取...")
            return render(request, 'output.html', {"Data": Data, "txt": data, })
        else:
            print("3")
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')