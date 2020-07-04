

from django.urls import path, re_path
from onboarding_form import views
from django.conf.urls import url

urlpatterns = [
    re_path(r'^api/onboarding_form/$', views.onboarding_form_list),
    re_path(
        r'^api/onboarding_form/(?P<pk>[0-9]+)$', views.onboarding_form_detail)
]
