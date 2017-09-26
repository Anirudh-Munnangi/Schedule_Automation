from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',auth_views.login,name='login'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^form_automation/sign_up$',views.sign_up, name='sign_up'),
    url(r'^form_automation/user_index$',views.user_index,name='user_index'),
    url(r'^form_automation/service_index$',views.service_index,name='service_index')
]
