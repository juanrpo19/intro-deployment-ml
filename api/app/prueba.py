# import joblib
from utils import get_model
import pandas as pd

json_pred = {
                                                "opening_gross": 0,
                                                "screens": 0,
                                                "production_budget": 0,
                                                "title_year": 0,
                                                "aspect_ratio": 0,
                                                "duration": 0,
                                                "cast_total_facebook_likes": 0,
                                                "budget": 0,
                                                "imdb_score": 0
                                                }

model = get_model()

df = pd.DataFrame([json_pred])
# print(df)
# breakpoint()
print(float(model.predict(df)))