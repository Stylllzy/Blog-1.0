from django.contrib import admin
from django.urls import path, re_path,include
from django.conf import settings
from django.views.static import serve
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),  # 首页
    path('news/', views.news),  # 新闻
    path('login/', views.login),   # 登录
    path('sign/', views.sign),  # 注册
    path('logout/', views.logout),  # 注销

    path('backend/', views.backend),   # 后台个人中心
    path('backend/re_headlike', views.backend),   # 后台修改头像
    path('backend/re_password', views.backend),   # 后台修改密码
    path('backend/add_article/', views.add_article),   # 后台添加文章

    re_path(r'^backend/edit_article/(?P<nid>\d+)/', views.edit_article),  # 编辑文章

    re_path(r'^api/', include('api.urls')),  # 路由分发 以api开头的请求分发到api的url

    re_path(r'^article/(?P<nid>\d+)/', views.article),  # 文章详情页


    # media配置( 请求图片 )
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
