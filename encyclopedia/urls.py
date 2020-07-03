from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('newpage', views.newpage, name='newpage'),
    path('upload', views.upload, name='upload'),
    path('editpage/<str:entry>', views.editpage, name='editpage'),
    path('savechanges', views.editpage, name='savechanges'),
    path('<str:entry>', views.entry, name='entry'),
]
