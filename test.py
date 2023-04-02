from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/prediction', json = {
                                                "opening_gross": 0,
                                                "screens": 0,
                                                "production_budget": 0,
                                                "title_year": 0,
                                                "aspect_ratio": 0,
                                                "duration": 0,
                                                "cast_total_facebook_likes": 0,
                                                "budget": 0,
                                                "imdb_score": 0
                                                })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] ==0 


def test_random_prediction():
    response = client.post('/v1/prediction', json = {
                                                "opening_gross": 17435092,
                                                "screens": 3008,
                                                "production_budget": 65000000,
                                                "title_year": 2012,
                                                "aspect_ratio": 2.35,
                                                "duration": 99,
                                                "cast_total_facebook_likes": 813,
                                                "budget": 65000000,
                                                "imdb_score": 6.4                                                
})
    
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] !=0