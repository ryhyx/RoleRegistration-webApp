from urllib import request
from .conection import Register
from django.shortcuts import render


def index(request):
    print('Read')
    # print('result = ', result)
    # print('len result = ', len(result))
    print('______________________________________')
    data = Register()
    result = data.read()
    return render(request, 'temp.html', {'result': result})


def save(request):
    if request.method == 'POST':
        post = request.POST
        print('########################################')
        flag_condition = False
        try:
            id_hidden = int(post.get('id_hidden'))
            flag_condition = type(id_hidden) is int and id_hidden > 0
        except:
            id_hidden = None

        if flag_condition:
            FirstName = post.get('firstName')
            LastName = post.get('lastName')
            password_ = post.get('password')
            acc = post.get('accessPermission')
            db = Register()
            print(id_hidden,FirstName,LastName,password_,acc)
            db.update(id_hidden, FirstName, LastName, password_, acc)

        else:

            FirstName = post.get('firstName')
            LastName = post.get('lastName')
            password_ = post.get('password')
            acc = post.get('accessPermission')
            print(FirstName, LastName, password_, acc)

            # Assuming Register is the model for your database
            db = Register()
            db.insert(FirstName, LastName, password_, acc)
            print('View create has been done')
        data = Register()
        result = data.read()
        return render(request, 'temp.html', {'result': result})


def update(request):
    data = Register()
    result = data.read()

    if request.method == 'POST':
        post = request.POST

        ID = post.get('UserId')
        FirstName = post.get('FirstName')
        LastName = post.get('LastName')
        password_ = post.get('password')
        acc = post.get('accessPermission')
        db = Register()
        db.update(ID, FirstName, LastName, password_, acc)
        print('view create has been done')
    if request.method == 'GET':
        data = request.GET
        user_id = data.get('user_id')
        print(user_id)

        result_per_user = Register().read_by_user(user_id)
        print("!@#!@#!@#")

        return render(request, 'temp.html', {'result': result, 'result_per_user': result_per_user})
        print("wow@@@")
    return render(request, 'temp.html', {'result': result})


def delete(request):
    if request.method == 'POST':
        post = request.POST
        ID = post.get('deleteUserId')
        print(ID)
        db = Register()
        db.delete(ID)
        print('finish in view ')
    data = Register()
    result = data.read()
    return render(request, 'temp.html', {'result': result})
