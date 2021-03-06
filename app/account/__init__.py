from django.conf.urls import patterns, url
from django.conf import settings
import actions
import actions_fixture

if settings.USE_FIXTURE:
        urlpatterns = [
                url(r'^login', actions_fixture.actionLogin),
                url(r'^logout', actions_fixture.actionLogout),
                url(r'^profile/update', actions_fixture.actionProfileUpdate)
        ]
else:
        urlpatterns = [
                url(r'^login', actions.actionLogin),
                url(r'^logout', actions.actionLogout),
                url(r'^profile/update', actions.actionProfileUpdate)
        ]
