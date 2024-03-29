from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('entry/<str:name>', views.entry, name="entry"),
    path('search/', views.search, name="search"),
    path('new/', views.new, name="new"),
    path('edit/', views.edit, name="edit"),
    path('random/', views.random_ent, name="random")
]
