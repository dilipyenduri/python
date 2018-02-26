from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import pandas as pd
import os
import json
from django.contrib.sites.models import Site
from django.db import transaction, IntegrityError
from locations.models import *
from accounts.models import *
from django.contrib.auth.models import Group
from itertools import tee, islice, chain, izip

class Command(BaseCommand):
    help = 'Insert test data'
    def handle(self, *args, **options):
        file_path = settings.MEDIA_ROOT + "/codes"
        file_name = "Facility_Type_codes.csv"
        csv_file_name = file_path+'/'+file_name
        df = pd.read_csv(csv_file_name, index_col=0)
        # District
        for index, row in df.iterrows():
            kwargs = {
            "phc_chc_id" : index,
            "phc_chc_type": row['PHC_CHC_Type'],
            "label_name": row['PHC_CHC_Type'],
            "short_name" : row['ShortName']
            }
            try:
                ftype_obj = FacilityTypes.objects.get(**kwargs)
            except FacilityTypes.DoesNotExist as e:
                ftype_obj = FacilityTypes.objects.create(**kwargs)
                pass