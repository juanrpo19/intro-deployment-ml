# import joblib
from utils import get_model
import pandas as pd

json_pred = {"opening_gross": 17435092, "screens": 3008, "production_budget": 65000000, "title_year": 2012, "aspect_ratio": 2.35, "duration": 99, "cast_total_facebook_likes": 1375, "budget": 65000000, "imdb_score": 6.4}

model = get_model()

df = pd.DataFrame([json_pred])
print(df)
# breakpoint()
print(model.predict(df))