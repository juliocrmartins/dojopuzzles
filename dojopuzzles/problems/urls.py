from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ProblemsList.as_view(), name='problems'),
    url(r'^published$', views.PublishedProblemsList.as_view(), name='problems-published'),
    url(r'^random$', views.problems_random, name='problems-random'),
    url(r'^(?P<slug>[\w-]+)$', views.ProblemsDetail.as_view(), name='problems-detail'),
    url(r'^(?P<slug>[\w-]+)/choose$', views.ProblemsDetail.as_view(), name='problems-choose'),
]
