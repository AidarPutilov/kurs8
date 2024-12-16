from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.permissions import AllowAny
from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDeleteAPIView,
    UserListAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)


app_name = UsersConfig.name

urlpatterns = [
    # Маршруты для модели User
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("list/", UserListAPIView.as_view(), name="user_list"),
    path("view/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_detail"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("delete/<int:pk>/", UserDeleteAPIView.as_view(), name="user_delete"),
    # Маршруты для работы с JWT-токенами
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="login",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
