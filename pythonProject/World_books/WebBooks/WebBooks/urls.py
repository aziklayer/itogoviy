from django.urls import path, include
from django.contrib import admin
from catalog import views
from django.urls import re_path as url             #с Джанго 4.0 url- не работает поэтому -re_path as url



urlpatterns = [
    path('', views.index, name='index'),

    path('admin/', admin.site.urls),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
]
# Добавление URL-адреса для входа в систему
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


