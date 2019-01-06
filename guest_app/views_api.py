from django.http import JsonResponse, HttpResponseRedirect
from django.contrib import auth

"""
说明：这里面实现的是接口，专门给前端调用
"""

# 验证登录的接口
def login(request):
    if request.method == "POST":
        user = request.POST.get("username", "")
        pawd = request.POST.get("password", "")
        print(user)
        print(pawd)
        if user == "" or pawd == "":
            return JsonResponse({"success":"false",
                                 "message":"用户名或密码为空"})
        user = auth.authenticate(username=user, password=pawd)
        if user is not None:
            return JsonResponse({"success":"true",
                                 "message":"登录成功"})
        else:
            return JsonResponse({"success":"false",
                                 "message":"用户名或密码错误"})
    else:
        return JsonResponse({"success":"false",
                             "message":"请求方法错误"})


"""
浏览器 -->    登录  -->      服务端
浏览器（cookie保存） <-- 信息  <--  服务端
浏览器 （验证身份的东西）  --> cookie    -->  判断是否是合法的

cookie sessionid  针对浏览器器所保存的数据

存折：  存钱，取钱
银行卡： 
"""




