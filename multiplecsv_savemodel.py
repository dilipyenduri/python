from django.core.management.base import BaseCommand
from django.conf import settings
from campaign.models import *
import pandas as pd
import os
import numpy as np
import traceback

bucket_name = 'primary_locations'
media_root = settings.MEDIA_ROOT

class Command(BaseCommand):
    help = 'Insert test data'
    
    def handle(self, *args, **options):
        file_path = settings.MEDIA_ROOT + "/new_locations"
        dir_list = [name for name in os.listdir(file_path)]
        input_file_list = set([file for file in os.listdir(file_path) if file.endswith(".xlsx")])
        user_data = {}
        for each_file in list(input_file_list):
 
            file_name = file_path+'/'+each_file
            df = pd.read_excel(file_name)
            for each_user in df.index:
                # print each_user


                user_data['label_name'] = df['label_name'][each_user] 
                user_data['ec_code'] = df['ec_code'][each_user]
                user_data['name'] = df['name'][each_user]  

                print df['_parent_id'][each_user]
                if str(df['_parent_id'][each_user]) == 'nan':
                    user_data['_parent_id'] = None
                else:
                    user_data['_parent_id'] = df['_parent_id'][each_user].astype(np.int64)
                
                print user_data['_parent_id']

                    

                user_data['campaign_id'] = df['campaign_id'][each_user]
                user_data['hierarchy_level_id'] = df['hierarchy_level_id'][each_user]
                print user_data
                Location.objects.create(**user_data)




                    
