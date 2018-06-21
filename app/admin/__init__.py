from tornado.web import RequestHandler
from ven import app, db
import transaction


@app.route
class Index(RequestHandler):
    def get(self):
        navbarResponsive = [
            {'title': 'Dashboard', 'link': '/admin/index', 'i': 'fa fa-fw fa-dashboard'},
            {'title': 'Charts', 'link': '/admin/charts', 'i': 'fa fa-fw fa-area-chart'},
            {'title': 'Tables', 'link': '/admin/tables', 'i': 'fa fa-fw fa-table'},
            {'title': 'Components', 'link': '/#collapseComponents', 'i': 'fa fa-fw fa-wrench',
             'aclass': 'nav-link-collapse collapsed',
             'collapse': [
                 {'title': 'Navbar', 'link': '/navbar.html'},
                 {'title': 'Cards', 'link': '/Cards.html'},
             ]},
            {'title': 'Example Pages', 'link': '/#collapseExamplePages', 'i': 'fa fa-fw fa-file', 'collapse': [
                {'title': 'login', 'link': '/login'},
                {'title': 'register', 'link': '/register.html'},
                {'title': 'forgot password', 'link': '/forgot-password.html'},
                {'title': 'blank', 'link': '/blank'},
            ]},
            {'title': 'Menu Levels', 'link': '/#collapseMulti', 'i': 'fa fa-fw fa-sitemap', 'collapse': [
                {'title': 'Second Level Item', 'link': '/login'},
                {'title': 'Second Level Item', 'link': '/register.html'},
                {'title': 'Second Level Item', 'link': '/forgot-password.html'},
            ]},
            {'title': 'Link', 'link': '/#', 'i': 'fa fa-fw fa-link'},
            {'title': 'setting', 'link': '/admin/setting', 'i': 'fa fa-fw fa-cog'}
        ]
        # if not db.dbroot.get('navbarResponsive'):
        # db.dbroot['navbarResponsive']=navbarResponsive
        # transaction.commit()
        self.render('index.html', dbroot=db.dbroot)

@app.route
class Setting(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('setting.html',dbroot=db.dbroot)