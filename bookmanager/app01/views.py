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
    if not obj_list:
        return HttpResponse('要编辑的数据不存在')
    obj = obj_list[0]

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


# 展示书籍
def book_list(request):
    all_books = models.Book.objects.all()
    return render(request,'book_list.html',{'all_books':all_books})


# 添加书籍
def add_book(request):
    # 添加书籍
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        # models.Book.objects.create(title=book_name,pub=models.Publisher.objects.get(pk=pub_id))  <=>
        models.Book.objects.create(title=book_name,pub_id=pub_id)
        return redirect('/book_list/')

    # 查询所有的出版社
    all_publishers = models.Publisher.objects.all()
    return render(request, 'add_book.html', {'all_publishers': all_publishers})


# 删除书籍
def del_book(request):
    pk = request.GET.get('id')
    models.Book.objects.filter(pk=pk).delete()
    return redirect('/book_list/')


# 编辑书籍
def edit_book(request):
    pk = request.GET.get('id')
    book_obj = models.Book.objects.get(pk=pk)

    if request.method == 'POST':
        # 获取提交的数据
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        # 修改数据
        book_obj.title = book_name
        # book_obj.pub_id = pub_id
        book_obj.pub = models.Publisher.objects.get(pk=pub_id)
        book_obj.save()
        return redirect('/book_list/')
    # 查询所有的出版社
    all_publishers = models.Publisher.objects.all()

    return render(request, 'edit_book.html', {'book_obj': book_obj, 'all_publishers': all_publishers})



# 展示作者
def author_list(request):
    all_authors = models.Author.objects.all()
    return render(request, 'author_list.html', {'all_authors': all_authors})


# 增加作者
def add_author(request):
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        print(request.POST)
        print(books)
        print(author_name)
        author_obj = models.Author.objects.create(name=author_name,)
        author_obj.books.set(books)
        return redirect('/author_list/')

    all_books = models.Book.objects.all()
    return render(request,'add_author.html',{'all_books': all_books})


# 删除作者
def del_author(request):
    pk = request.GET.get('pk')
    models.Author.objects.filter(pk=pk).delete()
    return redirect('/author_list/')


# 编辑作者
def edit_author(request):
    # 查询编辑的作者对象
    pk = request.GET.get('pk')
    author_obj = models.Author.objects.get(pk=pk)

    if request.method == 'POST':
        name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        # 修改对象的数据
        author_obj.name = name
        author_obj.save()
        # 多对多的关系
        author_obj.books.set(books)  #  每次重新设置
        # 重定向
        return  redirect('/author_list/')

    # 查询所有的书籍
    all_books = models.Book.objects.all()
    return render(request, 'edit_author.html', {'author_obj': author_obj, 'all_books': all_books})