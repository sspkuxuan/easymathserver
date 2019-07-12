from django.conf.urls import  url
from django.contrib import  admin
from pinpinpin import views

urlpatterns = [
    url(r'^(?P<version>[v1|v2|v3]+)/submit/$',views.SubmitView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/information/$',views.InformationsView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/myinfo/$',views.MyinfoView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/login/$',views.PinUserLoginView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/delete/$', views.DeleteView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/saveuser/$', views.SaveUserView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/edituser/$', views.UserInfoView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/sort/$', views.SortView.as_view()),
    url(r'^(?P<version>[v1|v2|v3]+)/isuser/$', views.IsUserView.as_view()),



]