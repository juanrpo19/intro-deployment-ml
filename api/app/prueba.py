import joblib
import pandas as pd

model = joblib.load('./model/model.pkl')


json_pred = {"opening_gross": 17435092.0, "screens": 3008.0, "production_budget": 65000000, "title_year": 2012.0, "aspect_ratio": 2.35, "duration": 99.0, "cast_total_facebook_likes": 1375, "budget": 65000000.0, "imdb_score": 6.4}

df = pd.DataFrame(json_pred)

model.predict(df)