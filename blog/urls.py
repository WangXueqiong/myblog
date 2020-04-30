from django.urls import path

from . import views
# 设置app_name,html中配置url使用
app_name = 'blog'
# 配置二级url，路径，方法，name
urlpatterns = [
    path('index/', views.index),
    path('article/<int:article_id>/', views.article_page, name='article_page'),
    path('edit/', views.edit_page, name='edit_page'),
    path('index/action/', views.edit_action, name='edit_action'),
    path('update/<int:article_id>', views.update_action, name='update_action')
]