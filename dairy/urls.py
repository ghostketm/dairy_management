from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # User URLs
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/update/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),

    # Bull URLs
    path('bulls/', views.bull_list, name='bull_list'),
    path('bulls/create/', views.bull_create, name='bull_create'),
    path('bulls/<uuid:pk>/update/', views.bull_update, name='bull_update'),
    path('bulls/<uuid:pk>/delete/', views.bull_delete, name='bull_delete'),

    # Heifer URLs
    path('heifers/', views.heifer_list, name='heifer_list'),
    path('heifers/create/', views.heifer_create, name='heifer_create'),
    path('heifers/<uuid:pk>/update/', views.heifer_update, name='heifer_update'),
    path('heifers/<uuid:pk>/delete/', views.heifer_delete, name='heifer_delete'),

    # Calf URLs
    path('calves/', views.calf_list, name='calf_list'),
    path('calves/create/', views.calf_create, name='calf_create'),
    path('calves/<uuid:pk>/update/', views.calf_update, name='calf_update'),
    path('calves/<uuid:pk>/delete/', views.calf_delete, name='calf_delete'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<uuid:pk>/update/', views.product_update, name='product_update'),
    path('products/<uuid:pk>/delete/', views.product_delete, name='product_delete'),

    # Health Record URLs
    path('health/', views.health_list, name='health_list'),
    path('health/create/', views.health_create, name='health_create'),
    path('health/<uuid:pk>/update/', views.health_update, name='health_update'),
    path('health/<uuid:pk>/delete/', views.health_delete, name='health_delete'),

    # Reproduction Record URLs
    path('reproduction/', views.reproduction_list, name='reproduction_list'),
    path('reproduction/create/', views.reproduction_create, name='reproduction_create'),
    path('reproduction/<uuid:pk>/update/', views.reproduction_update, name='reproduction_update'),
    path('reproduction/<uuid:pk>/delete/', views.reproduction_delete, name='reproduction_delete'),

    # Sales Record URLs
    path('sales/', views.sales_list, name='sales_list'),
    path('sales/create/', views.sales_create, name='sales_create'),
    path('sales/<uuid:pk>/update/', views.sales_update, name='sales_update'),
    path('sales/<uuid:pk>/delete/', views.sales_delete, name='sales_delete'),

    # Milking Record URLs
    path('milking/', views.milking_list, name='milking_list'),
    path('milking/create/', views.milking_create, name='milking_create'),
    path('milking/<uuid:pk>/update/', views.milking_update, name='milking_update'),
    path('milking/<uuid:pk>/delete/', views.milking_delete, name='milking_delete'),

    # Feeding Record URLs
    path('feeding/', views.feeding_list, name='feeding_list'),
    path('feeding/create/', views.feeding_create, name='feeding_create'),
    path('feeding/<uuid:pk>/update/', views.feeding_update, name='feeding_update'),
    path('feeding/<uuid:pk>/delete/', views.feeding_delete, name='feeding_delete'),
]