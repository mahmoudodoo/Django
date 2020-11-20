import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')


import django
django.setup()


## here we'll write Fake pop script

import random
from secondapp.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News','Games']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N):

    for entry in range(N):

        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company() 
        # Create a new Webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create a fake access record
        acc_record = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == "__main__":
    print("POpulating script !!!")
    populate(15)
    print("Population Complete !!")