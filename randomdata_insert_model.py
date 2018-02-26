import string
import random
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from accounts.models import User
from accounts.models import Worker
from locations.models import Locations

def random_string_generator(size, type=None):
    if type == "char":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "string":
        chars = chars = string.ascii_uppercase + string.ascii_lowercase
    elif type == "number":
        chars = string.digits
    return ''.join(random.choice(chars) for _ in range(size))    

location_list = Locations.objects.filter(hierarchy_level__name='subfacility')
gender_list = ['Male','Female']
hl_list = [1,2,3,4,5,6]

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('no_anms', type=int)

    def handle(self, *args, **options):
        no_anms = options.get('no_anms')

        user_data={}
        worker_data={}
        for i in range(no_anms):  
            user_data['password'] = random_string_generator(6, 'char').title()
            user_data['username'] = random_string_generator(6, 'char').title()
            user_data['first_name'] = random_string_generator(6, 'char').title()
            user_data['role'] = 'mentor'
            User.objects.create(**user_data)
 
            gender_choice = random.choice(gender_list)
            location_choice = random.choice(location_list) 
            hl_list_choice = random.choice(hl_list)

            worker_data['gender'] = gender_choice
            worker_data['mobile_number'] = random_string_generator(10, 'number')
            worker_data['phone_number'] = random_string_generator(10, 'number')
            worker_data['imei_slot1'] = random_string_generator(4, 'char').title() 
            worker_data['imei_slot2'] = random_string_generator(4, 'char').title() 
            worker_data['mac_address'] = random_string_generator(10, 'char').title() 
            worker_data['office_address'] = random_string_generator(6, 'char').title() 
            worker_data['user'] = User.objects.get(username=user_data['username'])
            worker_data['designation'] = random_string_generator(4, 'char').title() 
            # worker_data['location'] = location_choice
            worker_data['hl_code'] = hl_list_choice
            location_code =Locations.objects.filter(hierarchy_level_id=hl_list_choice)
            worker_data['loc_code'] =  location_code[0].loc_code
            Worker.objects.create(**worker_data)  