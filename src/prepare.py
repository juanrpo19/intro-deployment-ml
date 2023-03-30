import pandas as pd
from io import StringIO
import sys
import logging
from dvc import api


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logging = logging.getLogger(__name__)

logging.info('Fetching data...')

movie_data_path = api.read('../dataset/movies.csv.dvc', remote='dataset-track')
financial_data_path = api.read('../dataset/financials.csv.dvc', remote='dataset-track')
opening_data_path = api.read('../dataset/opening_gross.csv.dvc', remote='dataset-track')

fin_data = pd.read_csv(StringIO(financial_data_path))
movie_data = pd.read_csv(StringIO(movie_data_path))
opening_data = pd.read_csv(StringIO(opening_data_path))

breakpoint()
