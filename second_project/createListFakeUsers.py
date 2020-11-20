import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')


import django
django.setup()


## here we'll write Fake pop script

import random
from secondapp.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # New entry 
        user = User.objects.get_or_create(first_name=fake_first_name, last_name= fake_last_name , email= fake_email)


if __name__ == "__main__":
    print("Please Wait ....")
    populate(15)
    print("Population has been Completed !!!")
