from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
#router.register(r'posts', views.PostViewSet)

urlpatterns=[
    url(r'reaction/', views.reflectReaction),
    url(r'', views.Chatbot),
]