# Django Version Viewer

The pip package version viewer plugin allows a queryable endpoint to display a list of dicts representing all installed pip packages in the environment that django is running in. It also allows the insertion of a template tag to any template to display a link which calls up a pop up modal displaying all installed pip packages. You may also configure which users have access to the link and endpoint.

---------------------------------------
## Installation
---------------------------------------

Add the following to `INSTALLED_APPS` in `settings.py`

	INSTALLED_APPS = [
		'django_version_viewer'
	]

## Add django_version_viewer urls and extend `admin/index.html`


Django Version Viewer needs to extend the `admin/index.html` and append it's urls to your `urls.py`. In your `urls.py` add:

	admin.site.index_template = 'admin/custom_index.html'
	admin.autodiscover()

	urlpatterns = [
		...
		url(r'^django_version_viewer/', include('django_version_viewer.urls')),
		...
	]

In your `templates` dir, create a `custom_index.html`.

	<!-- custom_index.html -->
	{% extends "admin/index.html" %}

	{% load i18n admin_static pip_version_viewer_tags %}

	{% block content %}
	{% show_pip_package_versions %}
	{{ block.super }}
	{% endblock %}


	<!-- only add this if you are NOT using djangoCMS -->
	{% block extrahead %}
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	{% endblock %}

If you are using DjangoCMS the added style sheet and js might interfere with DjangoCMS's styling. In this case you should
create a file called `admin/inc/userlinks.html` inside your `templates` directory.

	<!-- userlinks.html -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.0/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>


## Permissions

You can set your own access permissions on the template tag and route by defining your own
`Accessor` class. This class must have a `allow_access` method that returns a `boolean`. By defualt,
django_version_viewer only allows superusers access to the route and template tag.

	# Django Version Viewer settings:
	# default class only allows superusers access
	ACCESSOR_CLASS_PATH = 'mypathto.my.AccessorClass'
