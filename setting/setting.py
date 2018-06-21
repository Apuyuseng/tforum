"""
这里的设置将会传到　tornado.web.Application
"""
import os
base_path = os.path.dirname(os.path.dirname(__file__))
# 静态文件路径
static_path = os.path.join(base_path, "static")
# cookie 签名．需要签名的数据用set_secure_cookie，get_secure_cookie 设置和获取
cookie_secret = "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo="
# 登陆设置
login_url = "/login"
# XSRF 认证开启，防止跨站攻击
xsrf_cookies = True
# 开发模式
debug = True
