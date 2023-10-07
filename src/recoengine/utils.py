from faker import Faker
import csv
import datetime
from pprint import pprint
from django.conf import settings

PRODUCT_DATA = settings.DATA_DIR/ "TV_Final.csv"

def validate_date_str(date_text):
    try:
        datatime.datatime.strptime(date_text, "%Y-%m-%d")
    except:
        return None
    return date_text



def load_product_data(limit=1):
    with open(PRODUCT_DATA, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = []
        for i, row in enumerate(reader):
            #pprint(row)
            _id = row.get("id")
            try:
                _id = int(_id)
            except:
                _id =  None
            
            data = {
                "id": _id,
                "brand": row.get('Brand'),
                "resolution": row.get('Resolution'),
                "size": row.get('Size'),
            }
            dataset.append(data)

            if i + 1 > limit:
                break
        return dataset


def get_fake_profile(count=10):
    fake = Faker()
    user_data = []
    for _ in range(count):
        profile = fake.profile()
        
        # Ensure the profile has an email
        if not profile.get('email'):
            profile['email'] = fake.email()

        data = {
            "username": profile.get('username'),
            "email": profile.get('email'),
            "is_active": True
        }
        if 'name' in profile:
            fname, lname = profile.get('name').split(" ")[:2]
            data['first_name'] = fname
            data['last_name'] = lname

        user_data.append(data)
    return user_data
