from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# 展示出版社
def publisher_list(request):
    # 从数据库中查询到出版社的信息
    all_publishers = models.Publisher.objects.all().order_by('pk')
    # 返回一个包含出版社信息的页面
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


# 新增出版社
def add_publisher(request):
    # 对请求方式进行判断
    if request.method == 'POST':
        # 处理POST请求
        # 获取到出版社的名称
        publisher_name = request.POST.get('publisher_name')
        # 判断出版社名称是否有重复的
        if models.Publisher.objects.filter(name=publisher_name):
            return render(request, 'add_publisher.html', {'error': '出版社名称已存在'})
        # 判断输入的值是否为空
        if not publisher_name:
            return render(request, 'add_publisher.html', {'error': '不能输入为空'})
        # 使用ORM将数据插入到数据库中
        obj = models.Publisher.objects.create(name=publisher_name)
        # 跳转到展示出版社的页面
        return redirect('/publisher_list/')
    # 返回一个包含form表单的页面
    return render(request, 'add_publisher.html')


# 新增出版社
def add_publisher(request):
    error = ''
    # 对请求方式进行判断
    if request.method == 'POST':
        # 处理POST请求
        # 获取到出版社的名称
        publisher_name = request.POST.get('publisher_name')
        # 判断出版社名称是否有重复的
        if models.Publisher.objects.filter(name=publisher_name):
            error = '出版社名称已存在'
        # 判断输入的值是否为空
        if not publisher_name:
            error = '不能输入为空'
        if not error:
            # 使用ORM将数据插入到数据库中
            obj = models.Publisher.objects.create(name=publisher_name)
            # 跳转到展示出版社的页面
            return redirect('/publisher_list/')
    # 返回一个包含form表单的页面
    return render(request, 'add_publisher.html', {'error': error})


# 删除出版社
def del_publisher(request):
    # 获取要删除的数据
    pk = request.GET.get('id')
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        # 没有要删除的数据
        return HttpResponse('要删除的数据不存在')
    # 删除该数据
    # obj.delete()
    obj_list.delete()
    # 跳转到展示页面
    return redirect('/publisher_list/')


# 编辑出版社
def edit_publisher(request):
    error = ''
    # 查找要编辑的数据
    pk = request.GET.get('id')  # url上携带的参数  不是GET请求提交参数
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        return HttpResponse('要编辑的数据不存在')

    obj = obj_list[0]

    if request.method == 'POST':
        # 处理POST请求
        # 获取新提交的出版的名称
        publisher_name = request.POST.get('publisher_name')

        if models.Publisher.objects.filter(name=publisher_name):
            # 新修改的名称已存在
            error = '新修改的名称已存在'
        if obj.name == publisher_name:
            error = '名称未修改'
        if not publisher_name:
            error = '名称不能为空'

        if not error:
            # 修改数据
            obj.name = publisher_name
            obj.save()  # 保存数据到数据库中
            # 跳转到出版社的展示页面
            return redirect('/publisher_list/')

    # 返回一个包含原始数据的页面
    return render(request, 'edit_publisher.html', {'obj': obj, 'error': error})


# 展示书籍
def book_list(request):
    # 查询所有的书籍
    all_books = models.Book.objects.all()
    # print(all_books)
    # for book in all_books:
    #     print(book)
    #     print(book.id)
    #     print(book.pk)
    #     print(book.title)
    #     print(book.pub,type(book.pub))
    #     print(book.pub_id)
    #     print(book.pub.pk)
    #     print(book.pub.name)
    #
    #     print("*"*32)
    return render(request, 'book_list.html', {'all_books': all_books})


# 添加书籍
def add_book(request):
    if request.method == 'POST':
        # 获取数据
        book_name = request.POST.get('book_name')
        pub_id = request.POST.get('pub_id')
        # 将数据插入到数据库
        # models.Book.objects.create(title=book_name,pub=models.Publisher.objects.get(pk=pub_id))
        models.Book.objects.create(title=book_name, pub_id=pub_id)
        # 跳转到书籍的展示页面
        return redirect('/book_list/')
        # all_books = models.Book.objects.all()
        # return render(request, 'book_list.html', {'all_books': all_books})

    # 查询所有的出版社
    all_publishers = models.Publisher.objects.all()

    return render(request, 'add_book.html', {'all_publishers': all_publishers})


# 删除书籍
def del_book(request):
    # 获取要删除的对象删除
    pk = request.GET.get('id')
    models.Book.objects.filter(pk=pk).delete()
    # 跳转到展示页面
    return redirect('/book_list/')


# 编辑书籍
def edit_book(request):
    # 获取要编辑的书籍对象
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
        # 重定向到展示页面
        return redirect('/book_list/')
    # 查询所有的出版社
    all_publishers = models.Publisher.objects.all()

    return render(request, 'edit_book.html', {'book_obj': book_obj, 'all_publishers': all_publishers})


# 展示作者
def author_list(request):
    # 查询所有的作者
    all_authors = models.Author.objects.all()
    # for author in all_authors:
    #     print(author)
    #     print(author.pk)
    #     print(author.name)
    #     print(author.books,type(author.books)) # 关系管理对象
    #     print(author.books.all(),type(author.books.all()))
    #     print('*'*30)
    return render(request, 'author_list.html', {'all_authors': all_authors})


# 增加作者
def add_author(request):
    if request.method == 'POST':
        # 获取post请求提交数据
        author_name = request.POST.get('author_name')
        books = request.POST.getlist('books')
        # 存入数据库
        author_obj = models.Author.objects.create(name=author_name, )
        author_obj.books.set(books)
        # 跳转到展示页面
        return redirect('/author_list/')

    # 查询所有的书籍
    all_books = models.Book.objects.all()
    return render(request, 'add_author.html', {'all_books': all_books})


# 删除作者
def del_author(request):
    # 获取要删除对象的id
    pk = request.GET.get('pk')
    # 获取要删除的对象 删除
    models.Author.objects.filter(pk=pk).delete()
    # 跳转到展示页面
    return redirect('/author_list/')


# 编辑作者
def edit_author(request):
    # 查询编辑的作者对象
    pk = request.GET.get('pk')
    author_obj = models.Author.objects.get(pk=pk)

    if request.method == 'POST':
        # 获取提交的数据
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