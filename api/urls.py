from django.urls import path
from .views import (
    SignupView,
    CustomLoginView,
    CustomTokenRefreshView,
    LogoutView,
    ProductListCreateView,
    ProductDetailView,
)

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
