from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',auth_views.login,name='login'),
    url(r'^redirectUser/$',views.user_view_redirect,name="user_view_redirect"),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^form_automation/sign_up$',views.sign_up, name='sign_up')
]
