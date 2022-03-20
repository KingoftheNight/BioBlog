# BioBlog下载安装与使用

BioBlog是一款方便的个人博客网站，用户只需简单的调整即可享受优质的个人博客创作与管理服务。



## 1. 下载BioBlog

![mark](http://img.frankgene.top/blog/20220319/iJQfXfgiketN.png)

用户可在[GitHub](http://https://github.com/KingoftheNight/BioBlog/ "GitHub")下载网站安装包。



## 2. 安装Django与BioBlog

用户解压安装包后可得到网站Django前端与后端完整代码，在使用之前，用户需确保当前环境已经安装Django。



### 2.1 安装Django

若用户未安装Django，则可根据以下代码自行安装：

```bash

# 使用pip安装Django，国内用户可使用镜像源加速

$pip install django -i https://pypi.mirrors.ustc.edu.cn/simple/

```



### 2.2 启动BioBlog网站

Django安装完成后，用户需要将当前目录切换至解压文件夹内：

![mark](http://img.frankgene.top/blog/20220319/K2Dqz2Ogniwl.png)

为了方便演示，作者这里使用VScode进行配置：

![mark](http://img.frankgene.top/blog/20220319/6e5AUXrU7Gaf.png)

在命令行中输入以下代码启动网站：

```bash

$python manage.py runserver

```

![mark](http://img.frankgene.top/blog/20220319/7lLWEmsy3gu8.png)

此时用户即可在浏览器中打开提示网址进行查看(注意在网址后边添加/bioblog)：

![mark](http://img.frankgene.top/blog/20220319/6L5oEIb175J5.png)



## 3. 网站配置

在正式使用之前，用户可以根据需求对网站进行配置。



### 3.1 修改头像

网站默认无法更改用户头像，用户可以在./static/browser/img下选择替换user.png进行头像替换：

![mark](http://img.frankgene.top/blog/20220319/GCi91ukrxIsT.png)



### 3.2 登录账户密码设置

网站默认无法更改用户账户密码，用户可以在./browser/views.py中的第47行进行账户和密码修改(用户名必须为纯英文，推荐使用邮箱等复杂账户密码)。此外，用户可以在第49行进行Cookie设置，自定义账户登录缓存时长，单位为秒。

![mark](http://img.frankgene.top/blog/20220319/mbUAy13YaGlx.png)



### 3.3 服务器指定端口广播

Django默认在8080端口广播，用户可以指定端口广播，防止网站侵占端口(0.0.0.0表示所有IP均可以访问网站，80为指定端口)。

```bash

$python manage.py runserver 0.0.0.0:80

```



## 4. 网站使用教程

在完成上述配置后，用户可以点击登录开始使用网站。



### 4.1 登录网站

在未登录状态下，主页导航栏仅包含“我的主页”和“登录/退出”按钮。在登录后，主页导航栏添加了“开始创作”和“用户管理”按钮：

![mark](http://img.frankgene.top/blog/20220319/bajE8Tt9TxDc.png)

![mark](http://img.frankgene.top/blog/20220319/zdsNkh2rx3lu.png)



### 4.2 浏览文章

在主页会显示用户撰写的文章，按照日期由近到远排列，并支持根据文章标题搜索功能，可支持多词共同搜索，以空格隔开；左侧为用户个人信息和推荐阅读列表。在点击文章后将会跳转到对应文章具体内容：

![mark](http://img.frankgene.top/blog/20220320/3BRjBpaXUimn.png)



### 4.3 开始创作

点击开始创作，将会跳转到网站论文撰写页面。该页面由富文本编辑器构成，支持markdown格式写作，并可以同步浏览。在完成写作后，点击右下角提交，填写必要信息后即可发表：

![mark](http://img.frankgene.top/blog/20220320/1aO8mcIuxbev.png)

![mark](http://img.frankgene.top/blog/20220320/Vk8i3WfC6C0P.png)

![mark](http://img.frankgene.top/blog/20220320/uU3dp7XwjMkF.png)

![mark](http://img.frankgene.top/blog/20220320/KUv08OiTSCud.png)



### 4.4 用户管理

用户可以在管理页面查看并修改当前昵称和简介，并可决定当前按推荐文章内容。此外，右侧还添加了文章简要数据和网站使用日历图：

![mark](http://img.frankgene.top/blog/20220320/Ed0gQhrLLVEL.png)



### 4.6 图片引用与图床

为了使得文章更加稳定，我们使用图床进行文献图片储存，默认使用七牛云进行数据保存，本地应用软件可通过主页链接下载。



## 5. 使用注意事项

- 网站为防止用户错误删除文章，只会清除数据记录，并不会真的删除文章，并且用户可以在static/browser/uploads内找到。

![mark](http://img.frankgene.top/blog/20220320/4lQOYeoXKkel.png)
