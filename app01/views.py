from django.shortcuts import render,HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,"user_add.html")

def tpl(request):
    name = "韩超发方法"
    roles = ["管理员", "CEO", "保安"]
    user_info = {"name": "王刚", "salary": 100000, 'role': "CTO"}

    data_list = [
        {"name": "郭智", "salary": 100000, 'role': "CTO"},
        {"name": "卢慧", "salary": 100000, 'role': "CTO"},
        {"name": "赵建先", "salary": 100000, 'role': "CTO"},
    ]
    return render(request, template_name='tpl.html', context={"n1": name, "n2": roles, "n3": user_info, "n4": data_list})

def weather(req):
    import requests
    res = requests.get("https://api.open-meteo.com/v1/forecast?latitude=30.67&longitude=104.07&current=temperature_2m")
    data_list = res.json()
    print(data_list)
    return render(req, template_name='weather.html', context={"weather_list": data_list})
# views.py
from django.shortcuts import render, redirect
from django.http import HttpRequest

def login(request: HttpRequest):
    if request.method == "GET":
        return render(request, "login.html")

    username = request.POST.get("user")
    password = request.POST.get("pwd")

    if username == 'root' and password == '123':
        return redirect("https://www.chinaunicom.com.cn/")

    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})

from app01.models import Department, UserInfo

def orm(request):
    # 1. 新增部门表 Department
    """Department.objects.create(title="销售部")
    Department.objects.create(title="IT部")
    Department.objects.create(title="运营部")
    # 2. 新增用户表 UserInfo
    UserInfo.objects.create(name="武沛齐", password="123", age=19)
    UserInfo.objects.create(name="朱虎飞", password="666", age=29)
    UserInfo.objects.create(name="吴阳军", password="666")

    UserInfo.objects.filter(id=3).delete()
    Department.objects.all().delete()
    data_list = UserInfo.objects.all()
    print(data_list)
        # 循环遍历每一行数据（每一条记录是一个obj对象）
    for obj in data_list:
        print(obj.id, obj.name, obj.password, obj.age)"""

    # 4.更新数据
    # 1.更新表里面【所有数据】，全部password改为999
    UserInfo.objects.all().update(password=999)
    # 2.只更新id=2这一条，age改成999
    UserInfo.objects.filter(id=2).update(age=999)
    # 3.只更新name="朱虎飞"这条数据，age改成999
    UserInfo.objects.filter(name="朱虎飞").update(age=999)
    return HttpResponse("成功")

def info_list(request):
    # 1.获取数据库中所有的用户信息，拿到QuerySet对象列表
    data_list = UserInfo.objects.all()

    # 2.渲染模板，把data_list传给html页面
    return render(request, "info_list.html", context={"data_list": data_list})

def info_add(request):
    # 判断请求方式：GET 就是打开添加页面
    if request.method == "GET":
        # 返回添加用户的网页表单
        return render(request, template_name='info_add.html')

    # ========== POST请求：表单提交，新增数据 ==========
    # 获取前端表单POST提交过来的数据
    user = request.POST.get("user")    # 获取表单name="user"的值
    pwd = request.POST.get("pwd")      # 获取表单name="pwd"的值
    age = request.POST.get("age")      # 获取表单name="age"的值

    # ORM新增：把拿到的数据插入UserInfo数据库表
    UserInfo.objects.create(name=user, password=pwd, age=age)

    # 新增完成后，自动跳转到 用户列表页面 /info/list/
    return redirect("/info/list/")

def info_delete(request):
    # 获取GET传递过来的参数nid（要删除数据的id）
    nid = request.GET.get('nid')
    # ORM：筛选id等于nid的数据，执行删除
    UserInfo.objects.filter(id=nid).delete()
    # 删除完成，重定向跳转到列表页面
    return redirect("/info/list/")