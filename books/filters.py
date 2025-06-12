# books/filters.py（新しいファイル）
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # 著者名：完全一致検索
    author = django_filters.CharFilter(lookup_expr='exact')
    
    # タイトル：部分一致検索（大文字小文字を区別しない）
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['author', 'title']