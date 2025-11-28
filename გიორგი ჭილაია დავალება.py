from datetime import datetime
from django.utils import timezone
from django.db.models import Length
from .models import Article, Comment


class ArticleRepository:

    @staticmethod
    def get_all():
        return Article.objects.all()

    @staticmethod
    def get_by_id(article_id: int):
        return Article.objects.filter(id=article_id).first()

    @staticmethod
    def get_by_title_exact(title: str):
        return Article.objects.filter(title=title)

    @staticmethod
    def search_by_title(title_part: str):
        return Article.objects.filter(title__icontains=title_part)

    @staticmethod
    def get_before_date(dt: datetime):
        return Article.objects.filter(date__lt=dt)

    @staticmethod
    def get_after_date(dt: datetime):
        return Article.objects.filter(date__gt=dt)

    @staticmethod
    def get_between_dates(start: datetime, end: datetime):
        return Article.objects.filter(date__range=(start, end))

    @staticmethod
    def get_ordered_by_date_desc():
        return Article.objects.order_by('-date')

    @staticmethod
    def get_latest(limit: int = 5):
        return Article.objects.order_by('-date')[:limit]

    @staticmethod
    def get_by_title_starts_with(prefix: str):
        return Article.objects.filter(title__startswith=prefix)

    @staticmethod
    def get_by_title_ends_with(suffix: str):
        return Article.objects.filter(title__endswith=suffix)

    @staticmethod
    def get_content_longer_than(length: int):
        # content__length lookup Django 4.1+
        return Article.objects.filter(content__length__gt=length)

    @staticmethod
    def get_today_articles():
        return Article.objects.filter(date__date=timezone.localdate())

    @staticmethod
    def exclude_title(title: str):
        return Article.objects.exclude(title=title)
