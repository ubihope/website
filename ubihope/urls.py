from website.views import ContactView, ThanksView
from django.conf.urls import include, url

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', ContactView.as_view(), name='index'),
    url(r'^thanks/$', ThanksView.as_view()),
]
