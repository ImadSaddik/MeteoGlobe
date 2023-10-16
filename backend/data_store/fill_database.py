import os
from tqdm import tqdm

import sys
sys.path.append('/home/imad/Projects/Meteorites/website/backend')

from django import setup
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
setup()

import pandas as pd
from data_store.models import Meteorite


data_path = os.path.join(settings.BASE_DIR, 'data_store/data/data_with_countries.csv')
data = pd.read_csv(data_path)

for index, row in tqdm(data.iterrows(), total=data.shape[0]):
    meteorite = Meteorite(
        mass=row['mass'],
        latitude=row['latitude'],
        longitude=row['longitude'],
        name=row['name'],
        year=row['year'],
        country=row['country'],
        name_type=row['name_type'],
        recorded_class=row['recorded_class'],
        discovery_type=row['discovery_type']
    )
    meteorite.save()
    
print('Done filling database.')
    