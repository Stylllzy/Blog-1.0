import random

from django import forms
from django.contrib import auth
from django.http import JsonResponse

from app01.models import UserInfo, Avatars
from django.views import View

# 放登录注册公共的方法
class LoginBaseForm(forms.Form):
    name = forms.CharField(error_messages={'required': '请输入用户名'})
    pwd = forms.CharField(error_messages={'required': '请输入密码'})
    # 重写init方法
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

# 登录的字段验证
class LoginForm(LoginBaseForm):

    # 局部钩子
    # def clean_code(self):
    #     code = self.cleaned_data.get('code')
    #     return self.cleaned_data

    # 全局钩子
    def clean(self):
        name = self.cleaned_data.get('name')
        pwd = self.cleaned_data.get('pwd')

        user = auth.authenticate(username=name, password=pwd)
        if not user:
            # 为字段添加错误信息
            self.add_error('pwd', '用户名或密码错误')
            return self.cleaned_data

        # 把用户对象放到clean_data中
        self.cleaned_data['user'] = user
        return self.cleaned_data

# 注册的字段验证
class SignForm(LoginBaseForm):
    re_pwd = forms.CharField(error_messages={'required': '请输入确认密码'})

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')
        if pwd != re_pwd:
            self.add_error('re_pwd', '两次输入密码不一致')
        return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        user_query = UserInfo.objects.filter(username=name)
        if user_query:
            self.add_error('name', '该用户已注册')


# 登录失败的可复用代码
def clean_form(form):
    # 验证不通过
    err_dict: dict = form.errors
    # 拿到所有字段的字段名字
    err_valid = list(err_dict.keys())[0]
    # 拿到第一个字段的第一个错误信息
    err_msg = err_dict[err_valid][0]
    return err_valid, err_msg

# CBV
class LoginView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': '登录成功',
            'self': None
        }
        data = request.data

        form = LoginForm(data, request=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 登录成功
        user = form.cleaned_data.get('user')

        auth.login(request, user)
        res['code'] = 0
        return JsonResponse(res)

class SignView(View):
    def post(self, request):
        res = {
            'code': 425,
            'msg': '注册成功',
            'self': None
        }
        form = SignForm(request.data, renderer=request)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 注册成功
        user = UserInfo.objects.create_user(
            username=request.data.get('name'),
            password=request.data.get('pwd')
        )

        # 给注册用户随机选择头像
        avatar_list = [i.nid for i in Avatars.objects.all()]
        user.avatar_id = random.choice(avatar_list)
        print(user.avatar_id)
        user.save()

        # 注册之后直接登录
        auth.login(request, user)
        res['code'] = 0
        return JsonResponse(res)