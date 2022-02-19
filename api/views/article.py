import random
from django import forms
from api.views.login import clean_form
from django.views import View
from django.http import JsonResponse
from markdown import markdown
from pyquery import PyQuery
from app01.models import Cover, Articles, Tags
from django.db.models import F


# 添加文章字段验证
class AddArticleForm(forms.Form):
    title = forms.CharField(error_messages={'required': '请输入文章标题'})
    content = forms.CharField(error_messages={'required': '请输入文章内容'})
    abstract = forms.CharField(required=False)      # 不进行为空验证
    cover_id = forms.IntegerField(required=False)


    category = forms.IntegerField(required=False)
    pwd = forms.CharField(required=False)
    recommend = forms.BooleanField(required=False)
    status = forms.IntegerField(required=False)
    author = forms.CharField(required=False)
    source = forms.CharField(required=False)

    # 全局钩子
    def clean(self):
        author = self.cleaned_data['author']
        if not author:
            self.cleaned_data.pop('author')

        category = self.cleaned_data['category']
        if not category:
            self.cleaned_data.pop('category')

        pwd = self.cleaned_data['pwd']
        if not pwd:
            self.cleaned_data.pop('pwd')

    # 文章简介
    def clean_abstract(self):
        abstract = self.cleaned_data['abstract']
        if abstract:
            return abstract

        # 截取文章正文前30个字符
        # content = self.cleaned_data['content']
        # if content:
        #     abstract = PyQuery(markdown(content)).text()[:15]
        #     return abstract

    # 文章封面
    def clean_cover_id(self):
        cover_id = self.cleaned_data['cover_id']
        if cover_id:
            return cover_id
        cover_set = Cover.objects.all().values('nid')
        cover_id = random.choice(cover_set)['nid']     # 随机选择一张封面
        return cover_id



# 给文章添加标签
def add_article_tags(tags, article_obj):
    for tag in tags:
        if tag.isdigit():
            # 存在添加
            article_obj.tag.add(tag)
        else:
            # 先创建，再多对多关联
            tag_obj = Tags.objects.create(title=tag)
            article_obj.tag.add(tag_obj.nid)

class ArticleView(View):
    # 添加文章
    def post(self, request):
        res = {
            'msg': '文章发布成功！',
            'code': 412,
            'data': None
        }
        data = request.data
        data['status'] = 1
        form = AddArticleForm(data)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 验证通过
        form.cleaned_data['source'] = '互联网'
        article_obj = Articles.objects.create(**form.cleaned_data)
        tags = data.get('tags')
        add_article_tags(tags, article_obj)

        res['code'] = 0
        res['data'] = article_obj.nid
        return JsonResponse(res)

    # 编辑文章
    def put(self, request, nid):
        res = {
            'msg': '文章编辑成功！',
            'code': 412,
            'data': None
        }
        article_query = Articles.objects.filter(nid=nid)
        if not article_query:
            res['msg'] = '请求错误'
            return JsonResponse(res)

        data = request.data
        data['status'] = 1
        form = AddArticleForm(data)
        if not form.is_valid():
            # 验证不通过
            res['self'], res['msg'] = clean_form(form)
            return JsonResponse(res)

        # 验证通过
        form.cleaned_data['source'] = '互联网'
        article_query.update(**form.cleaned_data)   # 更新

        tags = data.get('tags')
        # 标签修改
        article_query.first().tag.clear()    # 清空所有标签
        add_article_tags(tags, article_query.first())

        res['code'] = 0
        res['data'] = article_query.first().nid
        return JsonResponse(res)


# 文章点赞
class ArticleDiggView(View):
    def post(self, request, nid):
        # nid 评论id
        res = {
            'msg': '点赞成功',
            'code': 412,
            'data': 0
        }
        if not request.user.username:
            res['msg'] = '请登录'
            return JsonResponse(res)

        comment_query = Articles.objects.filter(nid=nid)
        comment_query.update(digg_count=F('digg_count') + 1)

        digg_count = comment_query.first().digg_count

        res['code'] = 0
        res['data'] = digg_count
        return JsonResponse(res)

# 文章收藏
class ArticleCollectView(View):
    def post(self, request, nid):
        # 文章只能收藏或取消收藏
        res = {
            'msg': '收藏成功',
            'code': 412,
            'data': 0,
            'iscollect': True    # 默认未收藏
        }
        if not request.user.username:
            res['msg'] = '请登录'
            return JsonResponse(res)

        # 判断用户是否收藏
        flag = request.user.collects.filter(nid=nid)
        num = 1     # 未收藏默认1
        res['code'] = 0

        if flag:
            # 已经收藏，点击取消收藏
            res['msg'] = '取消收藏成功'
            res['iscollect'] = False
            request.user.collects.remove(nid)
            num = -1  # 收藏改为-1
        else:
            # 没有收藏
            request.user.collects.add(nid)

        article_query = Articles.objects.filter(nid=nid)
        article_query.update(collects_count=F('collects_count') + num)
        collects_count = article_query.first().collects_count

        res['data'] = collects_count
        return JsonResponse(res)