from django import template

register = template.Library()

# 自定义过滤器
@register.filter
# def add1(item):
#     return int(item) + 1

@register.inclusion_tag("my_tag/headers.html")
def banner(menu_name, article=None):
    img_list = [
        "http://127.0.0.1:8000/media/site_bg/1.jpg",
        "http://127.0.0.1:8000/media/site_bg/2.jpg",
        "http://127.0.0.1:8000/media/site_bg/3.jpg",
        "http://127.0.0.1:8000/media/site_bg/4.jpg",
        "http://127.0.0.1:8000/media/site_bg/5.jpg",
    ]
    if article:
        # 说明是文章详情页面
        # 拿到文章封面
        cover = article.cover.url.url
        img_list = [cover]
        print(article)
        pass
    return {"img_list": img_list}
