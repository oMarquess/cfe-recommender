from . models import Products
from celery import shared_task

@shared_task(task_calculate_product_ratings)
def task_calculate_product_ratings(all=False, count =  None):
    '''
    task_calculate_product_ratings(all=False, count =  None)

    #celery tasks

    task_calculate_product_ratings.delay(all=False, count =  None)

    task_calculate_product_ratings.apply_async(kwargs = {"all":False, "count": 12}, countdown = 30)

    
    '''
    qs = Products.objects.needs_updating()
    if all:
        qs = Products.objects.all()
    qs = qs.order_by('rating_last_updated')
    if isinstance(count, int):
        qs = qs[:count]
    
    for obj in qs:
        obj.calculate_rating(save=True)


# def task_calculate_product_rating_all():
#     qs = Products.objects.all()
#     for obj in qs:
#         obj.calculate_rating(save=True)


# def task_calculate_product_rating_needs_updating():
#     qs = Products.objects.needs_updating()
#     for obj in qs:
#         obj.calculate_rating(save=True)