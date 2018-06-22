from tornado.web import RequestHandler,authenticated
from ven import app, db
from ven import BaseHandler
import transaction



@app.route
class Index(BaseHandler):
    @authenticated
    def get(self):
        navbarResponsive = [
            {'title': '移盘表', 'link': '/admin/index', 'i': 'fa fa-fw fa-dashboard'},
            {'title': '图表', 'link': '/admin/charts', 'i': 'fa fa-fw fa-area-chart'},
            {'title': '表格', 'link': '/admin/tables', 'i': 'fa fa-fw fa-table'},
            {'title': '设置', 'link': '#collapseComponents', 'i': 'fa fa-fw fa-wrench',
             'aclass': 'nav-link-collapse collapsed',
             'collapse': [
                 {'title': '主题设置', 'link': '/admin/navbar'},
                 {'title': '菜单配置', 'link': '/admin/setting'},
                 {'title': 'Cards', 'link': '/Cards.html'},
             ]},
            {'title': '页面', 'link': '#collapseExamplePages', 'i': 'fa fa-fw fa-file',
             'aclass': 'nav-link-collapse collapsed',
             'collapse': [
                {'title': '登陆', 'link': '/login'},
                {'title': '注销', 'link': '/register.html'},
                {'title': '忘记密码', 'link': '/forgot-password.html'},
                {'title': 'blank', 'link': '/blank'},
            ]},
            {'title': '架构', 'link': '#collapseMulti', 'i': 'fa fa-fw fa-sitemap',
             'aclass': 'nav-link-collapse collapsed',
             'collapse': [
                {'title': 'Second Level Item', 'link': '/login'},
                {'title': 'Second Level Item', 'link': '/register.html'},
                {'title': 'Second Level Item', 'link': '/forgot-password.html'},
            ]},
            {'title': '链接', 'link': '/#', 'i': 'fa fa-fw fa-link'},
        ]

        alerts = [
            {'level':'danger', 'msg_id':'xzz','title':'状态更新', 'i':'fa fa-long-arrow-up fa-fw',
             'time':'11:21 下午','msg':'更新出现一些小问题，不过不影响正常使用'
             },
            {'level': 'success', 'msg_id': 'xzz', 'title': '获取文章', 'i': 'fa fa-long-arrow-up fa-fw',
             'time': '11:21 上午', 'msg': '获取散文100章，1000则笑话．'
             },
            {'level': 'danger', 'msg_id': 'xzz', 'title': 'QQ机器人', 'i': 'fa fa-long-arrow-up fa-fw',
             'time': '10:21 上午', 'msg': 'QQ 机器人已经被玩坏了．'
             },
        ]
        messages = [
            {'title':'小龙女','time':'10:21 上午', 'msg':'我想过儿了', 'msg_id':'zxxc'},
            {'title':'郭靖','time':'10:21 上午', 'msg':'武林大会即将开始，快来襄阳帮助郭伯父吧．', 'msg_id':'zxxc'},
            {'title':'郭襄','time':'10:21 上午', 'msg':'快要过生日了，神雕大侠会来么', 'msg_id':'zxxc'},
        ]

        # if not db.dbroot.get('navbarResponsive'):
        db.dbroot['navbarResponsive']=navbarResponsive
        db.dbroot['alerts'] = alerts
        db.dbroot['messages'] = messages
        db.dbroot._p_changed = 1
        transaction.commit()
        self.render('index.html', dbroot=db.dbroot)

@app.route
class Setting(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('setting.html',dbroot=db.dbroot)

@app.route
class Navbar(RequestHandler):
    def get(self):
        self.render('navbar.html',dbroot=db.dbroot)