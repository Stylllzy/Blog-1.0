from django.contrib import admin
from app01.models import Articles   # 文章
from app01.models import Tags   # 标签
from app01.models import Cover  # 文章封面
from app01.models import Comment   # 评论
from app01.models import UserInfo   # 用户
from app01.models import Avatars   # 用户头像

# Register your models here.
admin.site.register(Articles)
admin.site.register(Tags)
admin.site.register(Cover)
admin.site.register(Comment)
admin.site.register(UserInfo)
admin.site.register(Avatars)