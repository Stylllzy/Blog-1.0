# 中间件
from django.utils.deprecation import MiddlewareMixin
import json

# 解析post请求
class Md1(MiddlewareMixin):
    # 请求中间件
    def process_request(self, request):
        # if 后面的判断解决admin登录不了的情况
        if request.method != 'GET' and request.META.get('CONTENT_TYPE') == 'application/json':
            data = json.loads(request.body, encoding='utf8')  # 反序列化
            request.data = data


    # # 响应中间件
    def process_response(self, request, response):
        return response
