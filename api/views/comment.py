from django.views import View
from django.http import JsonResponse
from app01.models import Comment, Articles
from django.db.models import F
from api.utils.find_root_comment import find_root_comment
from app01.utils.sub_comment import find_root_sub_comment

class CommentView(View):
    # 发布评论
    def post(self, request, nid):
        # /api/article/2/comment
        # 文章id
        # 用户
        # 讨论内容
        res = {
            'msg': '评论已发布',
            'code': 412,
            'self': None
        }
        data = request.data

        # 没登陆
        if not request.user.username:
            res['msg'] = '请登录'
            return JsonResponse(res)

        # 没写内容
        content = data.get('content')
        if not content:
            res['msg'] = '请输入评论内容'
            res['self'] = 'content'
            return JsonResponse(res)

        pid = data.get('pid')

        # 文章评论数+1   F查询找到自己字段
        Articles.objects.filter(nid=nid).update(comment_count=F('comment_count') + 1)

        # 校验通过
        if pid:
            # 有pid的不是根评论
            comment_obj = Comment.objects.create(
                content=content,
                user=request.user,
                article_id=nid,
                parent_comment_id=pid
            )
            # 根评论 回复后括号内数目+1
            # 找最终的根评论
            root_comment_obj = find_root_comment(comment_obj)
            # 找到根评论后自增1
            root_comment_obj.comment_count += 1
            root_comment_obj.save()

        else:
            # 根评论
            Comment.objects.create(
                content=content,
                user=request.user,
                article_id=nid
            )

        res['code'] = 0
        return JsonResponse(res)

    # 删除评论
    def delete(self, request, nid):
        # 普通用户只能删除自己发的评论
        # 超级管理员可以全删
        res = {
            'msg': '评论已删除',
            'code': 412,

        }
        login_user = request.user   # 当前登录用户
        comment_query = Comment.objects.filter(nid=nid)   # 评论信息
        comment_user = comment_query.first().user   # 评论人

        aid = request.data.get('aid')
        # 子评论的最终根评论id
        pid = request.data.get('pid')

        if not (login_user == comment_user or login_user.is_superuser):
            res['msg'] = '用户验证失败'
            return JsonResponse(res)

        # 根评论 删除后括号内数目-1, 文章评论数也要-1
        # 求子评论数量
        list = []
        find_root_sub_comment(comment_query.first(), list)
        # 文章评论数 - 子评论数 - 删的根评论（1）
        Articles.objects.filter(nid=aid).update(comment_count=F('comment_count') - len(list) - 1)

        if pid:
            # 不是根评论
            # 删除该子评论下的子子评论
            Comment.objects.filter(nid=pid).update(comment_count=F('comment_count') - len(list) - 1)

        comment_query.delete()
        res['code'] = 0
        return JsonResponse(res)


class CommentDiggView(View):
    def post(self, request, nid):
        res = {
            'msg': '点赞成功',
            'code': 412,
            'data': 0
        }
        # 判断是否登录
        if not request.user.username:
            res['msg'] = '请登录'
            return JsonResponse(res)

        comment_query = Comment.objects.filter(nid=nid)
        comment_query.update(digg_count=F('digg_count') + 1)

        res['data'] = comment_query.first().digg_count
        res['code'] = 0
        return JsonResponse(res)