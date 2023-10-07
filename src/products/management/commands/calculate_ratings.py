from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.tasks import task_calculate_product_ratings

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=100, type=int)
        parser.add_argument("--all", action='store_true', default=False)

    def handle(self, *args, **options ):
        all = options.get('all')
        count = options.get('count')
        task_calculate_product_ratings(all=all, count=count)
       