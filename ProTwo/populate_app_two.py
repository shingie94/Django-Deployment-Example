import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from app_two.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):


        #Create the fake data for that entry
        fk_name = fakegen.name().split()
        fake_name = fk_name[0]
        fake_last_name = fk_name[1]
        fake_email = fakegen.email()


        #Create the new User entry
        user_entry = User.objects.get_or_create(first_name=fake_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
