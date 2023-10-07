from . models import Products

def task_calculate_product_rating_all():
    qs = Products.objects.all()
    for obj in qs:
        obj.calculate_rating(save=True)


def task_calculate_product_rating_needs_updating():
    qs = Products.objects.all()
    for obj in qs:
        obj.calculate_rating(save=True)