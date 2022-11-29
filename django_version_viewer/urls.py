from . import views

try:
    # django 3.2+
    from django.urls import re_path
    urlpatterns = [
        re_path(r'^$', views.DjangoVersionViewer.as_view(), name='django_version_viewer'),
        re_path(r'^csv/$', views.DjangoVersionViewerCSV.as_view(), name='django_version_viewer_csv'),
        re_path(r'^toolbar/$', views.DjangoVersionViewerToolBar.as_view(), name='django_version_viewer_toolbar'),  # noqa
    ]
except ImportError:
    # django <3.2
    from django.conf.urls import url
    urlpatterns = [
        url(r'^$', views.DjangoVersionViewer.as_view(), name='django_version_viewer'),
        url(r'^csv/$', views.DjangoVersionViewerCSV.as_view(), name='django_version_viewer_csv'),
        url(r'^toolbar/$', views.DjangoVersionViewerToolBar.as_view(), name='django_version_viewer_toolbar'),  # noqa
    ]
