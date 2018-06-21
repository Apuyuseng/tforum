import tornado.ioloop
import tornado.web
import os
from setting.setting import base_path
from importlib import import_module
from inspect import getabsfile,getmodule
from setting import settings

class RouterConfig:
    def __init__(self):
        self.Application = tornado.web.Application(**settings)  # 创建路由对象
    def route(self, handler):
        if hasattr(handler,'URL'):
            uri = handler.URL
        else:
            package = getmodule(handler).__package__.lower().split('.')[1:]
            package.append(handler.__name__.lower())
            uri = '/'+"/".join(package)
        self.Application.add_handlers('.*$', [(uri, handler)])  # 路有关系映射添加到路由表中

app = RouterConfig()  # 创建路由

def load_app(model_name='app'):
    instance = import_module(model_name)
    model_path = getabsfile(instance)
    if model_path.endswith('__init__.py'):
        dir_path = os.path.dirname(model_path)
        for _dir in os.listdir(dir_path):
            if '__pycache__'==_dir or '__init__.py'==_dir:
                continue
            if _dir.find('.html')>0:
                continue
            _model_name = _dir.rstrip('.py').rstrip('.pyc')
            load_app('.'.join([model_name,_model_name]))
