from django.conf.urls import  url
from django.contrib import  admin
from api import views

urlpatterns = [
    url(r'^(?P<version>[v1|v2|v3]+)/questions/$',views.QuestionsView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/login/$',views.UserLoginView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/errorin/$', views.ErrorinView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/errorout/$', views.ErroroutView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/edituser/$', views.UserInfoView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/saveuser/$', views.SaveUserView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/results/$',views.ResultsView.as_view()),
]
