# from django.urls import path, include
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
# router.register(r'que', views.QuestionViewSet)

urlpatterns = [
    # url('^', include(router.urls)),
    url(r'^que/$', views.QuestionList.as_view()),
    url(r'^que/(?P<pk>[0-9]+)/$', views.QuestionDetail.as_view()),
]
