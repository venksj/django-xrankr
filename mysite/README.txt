In your templates, either hardcode the url like /static/my_app/example.jpg or, preferably, use the static template tag to build the URL for the given relative path by using the configured STATICFILES_STORAGE storage (this makes it much easier when you want to switch to a content delivery network (CDN) for serving static files).

{% load static %}
<img src="{% static "my_app/example.jpg" %}" alt="My image"/>
