# books/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# ルーター設定（自動的にCRUDのURLを生成）
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

# URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
]

# 生成されるURL一覧：
# GET    /api/books/         - 本の一覧取得
# POST   /api/books/         - 本の新規作成
# GET    /api/books/{id}/    - 特定の本の詳細取得
# PUT    /api/books/{id}/    - 特定の本の全更新
# PATCH  /api/books/{id}/    - 特定の本の部分更新
# DELETE /api/books/{id}/    - 特定の本の削除
