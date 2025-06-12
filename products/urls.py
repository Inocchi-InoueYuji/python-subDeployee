# products/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# ルーター設定（自動的にCRUDのURLを生成）
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]

# 生成されるURL一覧：
# GET    /api/products/         - 商品の一覧取得
# POST   /api/products/         - 商品の新規作成
# GET    /api/products/{id}/    - 特定の商品の詳細取得
# PUT    /api/products/{id}/    - 特定の商品の全更新
# PATCH  /api/products/{id}/    - 特定の商品の部分更新
# DELETE /api/products/{id}/    - 特定の商品の削除
