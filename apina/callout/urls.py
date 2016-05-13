from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from callout import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^beacons/$', views.BeaconList.as_view()),
    url(r'^beacons/(?P<pk>[0-9]+)/$', views.BeaconDetail.as_view()),
    url(r'^workspaces/$', views.WorkspaceList.as_view()),
    url(r'^workspaces/(?P<pk>[0-9]+)/$', views.WorkspaceDetail.as_view()),
    url(r'^statuses/$', views.StatusList.as_view()),
    url(r'^statuses/(?P<pk>[0-9]+)/$', views.StatusDetail.as_view()),
    url(r'^subscriptions/$', views.SubscriptionList.as_view()),
    url(r'^subscriptions/(?P<pk>[0-9]+)/$', views.SubscriptionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
