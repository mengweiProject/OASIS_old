"""
在项目初始化文件中创建app
命名
添加配置文件引入路径
"""

from celery import Celery

app = Celery('tasks_mytest')
# 指定celery配置文件的路径和名称
app.config_from_object('celeryTasks.celeryconfig')