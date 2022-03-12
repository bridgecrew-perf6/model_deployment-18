from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_null_prediction():
    response = client.post('/v1/prediction',json = {
                                                    'opening_gross':0,
                                                    'screens':0,
                                                    'production_budget':0,
                                                    'title_year':0,
                                                    'aspect_ratio':0,
                                                    'duration':0,
                                                    'cast_total_facebook_likes':0,
                                                    'budget':0,
                                                    'imdb_score':0
                                                })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] == 0

def test_random_prediction():
    response = client.post('/v1/prediction',json = {
                                                    'opening_gross':11212,
                                                    'screens':1231230,
                                                    'production_budget':132123,
                                                    'title_year':1000,
                                                    'aspect_ratio':123,
                                                    'duration':120,
                                                    'cast_total_facebook_likes':1111110,
                                                    'budget':11120,
                                                    'imdb_score':4.2
                                                })
    assert response.status_code == 200
    assert response.json()['worldwide_gross'] > 0