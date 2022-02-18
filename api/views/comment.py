from django.views import View
from django.http import JsonResponse
from app01.models import Comment, Articles
from django.db.models import F
from api.utils.find_root_comment import find_root_comment

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
            # Comment.objects.filter(nid=pid).update(comment_count=F('comment_count') + 1)

        else:
            # 根评论
            Comment.objects.create(
                content=content,
                user=request.user,
                article_id=nid
            )

        res['code'] = 0
        return JsonResponse(res)
