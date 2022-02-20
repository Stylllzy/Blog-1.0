# blog–1.0 (半成品)

Django &amp; Vue &amp; Element -前后端不分离
用到的技术：

django, Vue, ElementUI, axios, 

jQuery, scss, editor-md, 

图：Font_Awesome，bing壁纸，阿里巴巴iconfont

> 已完成功能
## index __主页

- nav(完成)

  - 首页，新闻(可用)，其余#
  - light模式可用，dark模式未开发完
  - 登录，注册可用
    - 普通用户，可发布文章
    - 超级用户，可添加编辑文章
  - 根据屏幕滚动渐变

- main(未完成)

  完成

  - 轮播图
  - 精选文章，分前后端分类排序显示
  - 博客文章
  - 标签云

  未完成

  - 今日热搜
  - 站点信息
  - 意见反馈- 

- footer(完成)

  - 服务器支持
  - 版本
  - 备案
  - 个人QQ，微信，GitHub链接及二维码

## article__文章详情页

- nav 同 index主页

- footer 同 index主页

- main(未完成)

  已完成

  - 文章内容markdown渲染
  - 侧边栏文章点赞，收藏，回到顶部
  - 发布评论
    - 根评论点赞，回复
    - 子评论点赞，回复
    - 删除评论，普通用户删除自己，超级用户所有都可删

  未完成

  - 悬浮目录(半成品)

## backend__个人界面

前端样式完成

完成功能：

- 普通用户
  - 发布文章
- 超级用户
  - 发布文章
  - 编辑文章

> 注：编辑文章暂时只能从 article 文章详情页文章标题边`编辑按钮`进入,该按钮普通用户不可见
>
> <img src="C:\Users\11842\AppData\Roaming\Typora\typora-user-images\image-20220220152356581.png" alt="image-20220220152356581" style="zoom:67%;" />

未完成功能：

- 个人中心信息展示
- 修改密码
- 修改头像
- 收藏文章展示

