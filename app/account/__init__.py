from ven import BaseHandler,app

@app.route
class Login(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        # 这里补充一个，获取用户输入
        # self.get_argument("name")

        self.set_secure_cookie("mail", self.get_argument("mail"))
        redirect = self.get_argument("next",'/')
        self.redirect(redirect)