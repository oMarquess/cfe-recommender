from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Products
from recoengine import utils as recoengine_utils

User = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("count", nargs='?', default=10, type=int)
        parser.add_argument("--show-total", action='store_true', default=False)
        parser.add_argument("--products", action='store_true', default=False)
        parser.add_argument("--users", action='store_true', default=False)

    def handle(self, *args, **options):
        count = options.get('count')
        show_total = options.get('show_total')
        load_products = options.get('products')
        generate_users = options.get('users')

        if load_products:
            products_dataset = recoengine_utils.load_product_data(limit=count)
            products_new = [Products(**x) for x in products_dataset]
            
            # Save products one by one
            saved_products_count = 0
            for product in products_new:
                try:
                    product.save()
                    saved_products_count += 1
                except Exception as e:
                    print(f"Error saving product: {product}. Error: {e}")

            print(f"New products: {saved_products_count}")
            if show_total:
                print(f"Total products: {Products.objects.count()}")

        if generate_users:
            profiles = recoengine_utils.get_fake_profile(count=count)
            new_users = [User(**profile) for profile in profiles]
            
            # Save users one by one
            saved_users_count = 0
            for user in new_users:
                try:
                    user.save()
                    saved_users_count += 1
                except Exception as e:
                    print(f"Error saving user: {user}. Error: {e}")

            print(f"New users created: {saved_users_count}")
            if show_total:
                print(f"Total users: {User.objects.count()}")
