from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^registerProcess$', views.register_process),
	url(r'^loginProcess$', views.login_process),
	url(r'^secretsProcess$', views.secrets_process),
	url(r'^secrets$', views.secrets),
	url(r'^popular$', views.show_popular),
	url(r'^logout$', views.logout),
]

