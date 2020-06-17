# 创建蓝图
from flask import Blueprint

passport = Blueprint('passport', __name__, url_prefix='/passport')
from . import views

