# Generated by Django 3.2.12 on 2022-02-11 14:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=16, verbose_name='昵称')),
                ('sign_status', models.IntegerField(choices=[(0, '用户名注册'), (1, '手机号注册'), (2, '邮箱注册'), (3, 'QQ注册')], default=0, verbose_name='注册方式')),
                ('tel', models.CharField(blank=True, max_length=12, null=True, verbose_name='手机号')),
                ('integral', models.IntegerField(default=20, verbose_name='用户积分')),
                ('token', models.CharField(blank=True, max_length=64, null=True, verbose_name='TOKEN')),
            ],
            options={
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, null=True, verbose_name='产品名称')),
                ('href', models.URLField(verbose_name='跳转链接')),
                ('img', models.FileField(blank=True, help_text='单图', null=True, upload_to='advert/', verbose_name='图片地址')),
                ('img_list', models.TextField(blank=True, help_text='上传图片请用线上地址，使用；隔开多张图片', null=True, verbose_name='图片组')),
                ('is_show', models.BooleanField(default=False, verbose_name='是否展示')),
                ('author', models.CharField(blank=True, max_length=32, null=True, verbose_name='广告主')),
                ('abstract', models.CharField(blank=True, max_length=128, null=True, verbose_name='产品简介')),
            ],
            options={
                'verbose_name_plural': '广告',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=32, null=True, verbose_name='标题')),
                ('abstract', models.CharField(blank=True, max_length=128, null=True, verbose_name='文章简介')),
                ('content', models.TextField(blank=True, null=True, verbose_name='文章内容')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='文章发布日期')),
                ('change_date', models.DateTimeField(auto_now=True, null=True, verbose_name='文章修改日期')),
                ('status', models.IntegerField(choices=[(0, '未发布'), (1, '已发布')], verbose_name='文章保存状态')),
                ('recommend', models.BooleanField(default=True, verbose_name='是否上推荐')),
                ('look_count', models.IntegerField(default=0, verbose_name='文章阅读量')),
                ('comment_count', models.IntegerField(default=0, verbose_name='文章评论量')),
                ('digg_count', models.IntegerField(default=0, verbose_name='文章点赞量')),
                ('collects_count', models.IntegerField(default=0, verbose_name='文章收藏数')),
                ('category', models.IntegerField(blank=True, choices=[(0, '前端'), (1, '后端')], null=True, verbose_name='文章分类')),
                ('author', models.CharField(blank=True, max_length=16, null=True, verbose_name='作者')),
                ('source', models.CharField(blank=True, max_length=32, null=True, verbose_name='来源')),
            ],
            options={
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Avatars',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.FileField(upload_to='avatars/', verbose_name='用户头像地址')),
            ],
            options={
                'verbose_name_plural': '用户头像',
            },
        ),
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.FileField(upload_to='article_img/', verbose_name='文章封面地址')),
            ],
            options={
                'verbose_name_plural': '文章封面',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('content', models.TextField(verbose_name='反馈信息')),
                ('status', models.BooleanField(default=False, verbose_name='是否处理')),
                ('processing_content', models.TextField(blank=True, null=True, verbose_name='回复的内容')),
            ],
            options={
                'verbose_name_plural': '用户反馈',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='事件名称')),
                ('content', models.TextField(verbose_name='事件内容')),
                ('create_date', models.DateField(null=True, verbose_name='创建时间')),
                ('drawing', models.TextField(blank=True, null=True, verbose_name='配图组，以;隔开')),
            ],
            options={
                'verbose_name_plural': '回忆录',
            },
        ),
        migrations.CreateModel(
            name='MenuImg',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('url', models.FileField(upload_to='site_bg/', verbose_name='图片地址')),
            ],
            options={
                'verbose_name_plural': '站点背景图',
            },
        ),
        migrations.CreateModel(
            name='MyInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32, verbose_name='名字')),
                ('job', models.CharField(max_length=128, verbose_name='工作')),
                ('email', models.EmailField(max_length=64, verbose_name='邮箱')),
                ('site_url', models.CharField(max_length=32, verbose_name='网站链接')),
                ('addr', models.CharField(max_length=16, verbose_name='地址')),
                ('bilibili_url', models.URLField(verbose_name='哔哩哔哩链接')),
                ('github_url', models.URLField(verbose_name='GitHub链接')),
                ('wechat_img', models.FileField(upload_to='my_info/', verbose_name='微信图片')),
                ('qq_img', models.FileField(upload_to='my_info/', verbose_name='QQ图片')),
            ],
            options={
                'verbose_name_plural': '个人信息',
            },
        ),
        migrations.CreateModel(
            name='NavCategory',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=16, verbose_name='分类标题')),
                ('icon', models.CharField(max_length=32, verbose_name='分类图标')),
            ],
            options={
                'verbose_name_plural': '导航分类',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='获取时间')),
            ],
            options={
                'verbose_name_plural': '新闻爬取',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, verbose_name='网站标题')),
                ('abstract', models.CharField(max_length=128, verbose_name='网站简介')),
                ('key_words', models.CharField(max_length=128, verbose_name='网站关键字')),
                ('record', models.CharField(max_length=32, verbose_name='网站备案号')),
                ('create_date', models.DateTimeField(verbose_name='建站日期')),
                ('version', models.CharField(max_length=16, verbose_name='网站版本号')),
                ('icon', models.FileField(upload_to='site_icon/', verbose_name='网站图标')),
            ],
            options={
                'verbose_name_plural': '网站信息',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=16, verbose_name='标签名字')),
            ],
            options={
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='Navs',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('icon_href', models.URLField(blank=True, help_text='在线链接', null=True, verbose_name='图标链接')),
                ('icon', models.FileField(blank=True, help_text='文件优先级大于在线链接', null=True, upload_to='site_icon/', verbose_name='网站图标')),
                ('title', models.CharField(max_length=32, verbose_name='网站标题')),
                ('abstract', models.CharField(max_length=128, null=True, verbose_name='网站简介')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('href', models.URLField(verbose_name='网站链接')),
                ('status', models.IntegerField(choices=[(0, '待审核'), (1, '已通过'), (2, '被驳回')], default=0, verbose_name='导航状态')),
                ('nav_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.navcategory', verbose_name='网站导航的分类')),
            ],
            options={
                'verbose_name_plural': '网站导航',
            },
        ),
        migrations.CreateModel(
            name='Moods',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, verbose_name='发布人')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('content', models.TextField(verbose_name='心情内容')),
                ('drawing', models.TextField(blank=True, null=True, verbose_name='配图组，以;隔开')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('digg_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.avatars', verbose_name='心情的发布头像')),
            ],
            options={
                'verbose_name_plural': '心情',
            },
        ),
        migrations.CreateModel(
            name='MoodComment',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, null=True, verbose_name='评论人')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('digg_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='评论时间')),
                ('avatar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.avatars', verbose_name='心情的发布头像')),
                ('mood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.moods', verbose_name='评论的心情')),
            ],
            options={
                'verbose_name_plural': '心情评论',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('menu_title', models.CharField(max_length=16, null=True, verbose_name='菜单名称')),
                ('menu_title_en', models.CharField(max_length=32, null=True, verbose_name='菜单英文名称')),
                ('title', models.CharField(max_length=32, null=True, verbose_name='slogan')),
                ('abstract', models.TextField(help_text='多个之间按分号区分', null=True, verbose_name='slogan介绍')),
                ('abstract_time', models.IntegerField(default=8, help_text='单位秒，默认是8秒', verbose_name='slogan切换时间')),
                ('rotation', models.BooleanField(default=True, verbose_name='是否轮播slogan介绍')),
                ('menu_rotation', models.BooleanField(default=False, help_text='多选默认会轮播', verbose_name='是否轮播banner图')),
                ('menu_time', models.IntegerField(default=8, help_text='单位秒，默认是8秒', verbose_name='背景图切换时间')),
                ('menu_url', models.ManyToManyField(help_text='可以多选，多选就会轮播', to='app01.MenuImg', verbose_name='菜单图片')),
            ],
            options={
                'verbose_name_plural': '站点背景',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('digg_count', models.IntegerField(default=0, verbose_name='点赞')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('comment_count', models.IntegerField(default=0, verbose_name='子评论数')),
                ('drawing', models.TextField(blank=True, null=True, verbose_name='配图')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.articles', verbose_name='评论文章')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.comment', verbose_name='是否是父评论')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='评论者')),
            ],
            options={
                'verbose_name_plural': '评论',
            },
        ),
        migrations.AddField(
            model_name='articles',
            name='cover',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.cover', verbose_name='文章封面'),
        ),
        migrations.AddField(
            model_name='articles',
            name='tag',
            field=models.ManyToManyField(blank=True, to='app01.Tags', verbose_name='文章标签'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.avatars', verbose_name='用户头像'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='collects',
            field=models.ManyToManyField(to='app01.Articles', verbose_name='收藏的文章'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
