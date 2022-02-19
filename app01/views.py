from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import auth
from app01.models import Articles, Tags, Cover, Comment
from app01.utils.sub_comment import sub_comment_list

import json
# Create your views here.

# 主页
def index(request):
    article_list = Articles.objects.filter(status=1).order_by('change_date')
    qianduan_list = Articles.objects.filter(category=1)[:6]
    houduan_list = Articles.objects.filter(category=2)[:6]
    return render(request, 'index.html', locals())

# 新闻
def news(request):
    return render(request, 'news.html')

# 文章
def article(request, nid):
    article_query = Articles.objects.filter(nid=nid)
    if not article_query:
        return redirect('/')
    article = article_query.first()

    # 评论列表
    comment_list = sub_comment_list(nid)

    return render(request, 'article.html', locals())

# 登录
def login(request):
    return render(request, 'login.html')
# 注册
def sign(request):
    return render(request, 'sign.html')
# 注销
def logout(request):
    auth.logout(request)
    return redirect('/')

# 后台
def backend(request):
    if not request.user.username:
        # 没有登录
        return redirect('/')
    return  render(request, 'backend/backend.html', locals())

# 后台修改密码
def re_password(request):
    return render(request, 'backend/re_password.html', locals())

# 后台修改头像
def re_headlike(request):
    return render(request, 'backend/re_headlike.html', locals())

# 后台增加文章
def add_article(request):
    # 拿到所有标签，分类
    tag_list = Tags.objects.all()
    category_list = Articles.category_choice
    # 拿到所有的封面
    cover_list = Cover.objects.all()
    c_l = []
    for cover in cover_list:
        c_l.append({
            "url": cover.url.url,
            'nid': cover.nid
        })
    return render(request, 'backend/add_article.html', locals())

# 后台编辑文章
def edit_article(request, nid):
    article_obj = Articles.objects.get(nid=nid)
    tags = [str(tag.nid) for tag in article_obj.tag.all()]

    # 拿到所有标签,分类
    tag_list = Tags.objects.all()
    category_list = Articles.category_choice
    # 拿到所有的封面
    cover_list = Cover.objects.all()
    c_l = []
    for cover in cover_list:
        c_l.append({
            "url": cover.url.url,
            'nid': cover.nid
        })
    return render(request, 'backend/edit_article.html', locals())

