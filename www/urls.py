__author__ = 'yang xian'

import logging, os, re, time, base64, hashlib

from transwarp.web import get, view, post, ctx, interceptor, seeother, notfound
from apis import api, APIError, APIValueError, APIPermissionError, APIResourceNotFoundError
from models import User, Blog, Comment

@view('blogs.html')
@get('/')
def index():
    blogs = Blog.find_all()
    user = User.find_first('where email=?', 'admin@example.com')
    return dict(blogs=blogs, user=user)

@api
@get('/api/users')
def api_get_users():
    users = User.find_by('order by created_at desc')
    for u in users:
        u.password = '******'
    return dict(users=users)