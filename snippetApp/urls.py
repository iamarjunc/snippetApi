from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SnippetViewSet, TagViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'snippets', SnippetViewSet)
router.register(r'tags', TagViewSet)


urlpatterns = [
    
    *router.urls,

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
