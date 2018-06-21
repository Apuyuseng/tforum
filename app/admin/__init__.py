from tornado.web import RequestHandler
from ven import app

@app.route
class Index(RequestHandler):
    def get(self):
        navbarResponsive = [
            {'title':'Dashboard','link':'/admin/index','i':'fa fa-fw fa-dashboard'},
            {'title':'Charts','link':'/admin/charts','i':'fa fa-fw fa-area-chart'},
            {'title':'Tables','link':'/admin/tables','i':'fa fa-fw fa-table'},
            {'title':'Components','link':'/#collapseComponents','i':'a fa-fw fa-wrench','aclass':'nav-link-collapse collapsed',
             'collapse':[
                 {'title':'Navbar', 'link':'/navbar.html'},
                 {'title':'Cards', 'link':'/Cards.html'},
             ]},
            {'title':'Example Pages','link':'/#collapseExamplePages','i':'fa fa-fw fa-file','collapse':[
                {'title': 'login', 'link': '/login'},
                {'title': 'register', 'link': '/register.html'},
                {'title': 'forgot password', 'link': '/forgot-password.html'},
                {'title': 'blank', 'link': '/blank'},
            ]},
            {'title':'Menu Levels','link':'/#collapseMulti','i':'fa fa-fw fa-sitemap','collapse':[
                {'title': 'Second Level Item', 'link': '/login'},
                {'title': 'Second Level Item', 'link': '/register.html'},
                {'title': 'Second Level Item', 'link': '/forgot-password.html'},
            ]},
            {'title': 'Link', 'link': '/#', 'i': 'fa fa-fw fa-link'},
        ]
        site_name = "tornado 博客管理"
        self.render('index.html', site_name=site_name,navbarResponsive=navbarResponsive)