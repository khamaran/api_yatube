from rest_framework import routers

from rest_framework.authtoken import views
from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename='posts')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments/', CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token, name='url_api_token'),
]

