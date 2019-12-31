from django.shortcuts import render,redirect,HttpResponse
from app01 import models


# 展示出版社
def publisher_list(request):
    all_publisher = models.Publisher.objects.all().order_by('pk')
    # {'all_publisher':all_publisher} 第一个是html的变量，第二个是查询结果
    return render(request,'publisher_list.html',{'all_publisher':all_publisher})


# 新增出版社
def add_publisher(request):
    error = ''
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        # name 为数据库出版社的name
        if models.Publisher.objects.filter(name=publisher_name):
            error = '出版社名称已存在'
        if not publisher_name:
            error = '不能输入为空'
        if not  error:
            obj = models.Publisher.objects.create(name=publisher_name)
            return redirect('/publisher_list/')
    return render(request,'add_publisher.html',{'error':error})


# 删除出版社
def del_publisher(request):
    pk = request.GET.get('id')
    # obj = models.Publisher.objects.get(pk=pk)
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        return HttpResponse('要删除的数据不存在')
    # obj.delete()
    obj_list.delete()
    return redirect('/publisher_list/')

# 编辑出版社
def edit_publisher(request):
    # 查找要编辑的数据
    error = ''
    pk = request.GET.get('id')
    obj_list = models.Publisher.objects.filter(pk=pk)
    print(obj_list)
    if not obj_list:
        return HttpResponse('要编辑的数据不存在')
    obj = obj_list[0]
    print(obj)

    # 处理POST请求,编辑查找的数据
    if request.method == 'POST':
        publisher_name = request.POST.get('publisher_name')
        if models.Publisher.objects.filter(name=publisher_name):
            error = '新修改的名称已存在'
        if obj.name == publisher_name:
            error = '名称未修改'
        if not publisher_name:
            error = '名称不能为空'
        if not error:
            obj.name = publisher_name
            obj.save()
            return redirect('/publisher_list/')

    return render(request,'edit_publisher.html',{'obj':obj,'error':error})