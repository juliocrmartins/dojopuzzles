from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.problems, name='problems'),
    url(r'^published$', views.problems_published, name='problems-published'),
    url(r'^random$', views.problems_random, name='problems-random'),
    url(r'^(?P<slug>[\w-]+)$', views.problems_detail, name='problems-detail'),
    url(r'^(?P<slug>[\w-]+)/choose$', views.problems_choose, name='problems-choose'),
]
