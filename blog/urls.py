from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.blog, name="index"),
    url(r'^trash$', views.trash, name="trash"),
    url(r'^(?P<question_id>[0-9]+)$', views.detail, name="detail"),
    url(r'^home$', views.home, name="home"),
    url(r'^add$', views.add, name="add"),
    url(r'^(?P<category>[\w]+)$', views.category, name="category"),
    url(r'^(?P<question_id>[0-9]+)/edit$', views.edit, name="edit"),
    url(r'^(?P<question_id>[0-9]+)/delete$', views.delete, name="delete"),
    url(r'^(?P<question_id>[0-9]+)/comment$', views.comment, name="comment"),
    url(r'^(?P<question_id>[0-9]+)/like$', views.like, name="like"),
    url(r'^(?P<question_id>[0-9]+)/share$', views.share, name="share"),
    url(r'^edit_comment/(?P<comment_id>[0-9]+)$', views.edit_comment, name="edit_comment"),
    url(r'^del_comment/(?P<comment_id>[0-9]+)$', views.del_comment, name="del_comment"),
]
