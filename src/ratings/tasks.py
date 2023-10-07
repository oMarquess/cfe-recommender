import random
from django.contrib.auth import get_user_model
from products.models import Products
from django.contrib.contenttypes.models import ContentType

from .models import Rating, RatingChoice


User = get_user_model()

def generate_fake_reviews(count=10, users=10, null_avg = False):
    user_s = User.objects.first()
    user_e = User.objects.last()
    random_user_ids = random.sample(range(user_s.id, user_e.id), users)
    users = User.objects.filter(id__in=random_user_ids)
    products = Products.objects.all().order_by("?")[:count]
    #product_ctype = ContentType.objects.get_for_model(Products)
    if null_avg:
        products = Products.objects.filter(rating_avg__isnull=True).order_by("?")[:count]
    n_rating = products.count()
    rating_choices = [x for x in RatingChoice.values if x is not None]
    user_ratings = [random.choice(rating_choices) for _ in range(0, n_rating)]
    new_ratings = []
    for product in products:
        rating_obj = Rating.objects.create(
            content_obj=product,
            # content_type=product_ctype,
            # object_id=products.id,
            value=user_ratings.pop(),
            user = random.choice(users)
        )
        new_ratings.append(rating_obj.id)
    return new_ratings
    