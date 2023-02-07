from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'msg': 'API Working'}


# get date for two cities
def test_current_datetimes():
    response = client.get("/current_datetimes",
                          params={'city1': 'Chicago, IL', 'city2': 'New York, NY'})
    assert response.status_code == 200
    data = response.json()[0]
    assert 'date' in data
    assert 'Chicago, IL' in data['date']
    assert 'New York, NY' in data['date']


def test_current_datetimes_temp():
    response = client.get("/current_datetimes_temp",
                          params={'city1': 'Chicago, IL', 'city2': 'New York, NY'})
    assert response.status_code == 200
    data = response.json()[0]
    assert 'info' in data
    assert 'Chicago, IL' in data['info']
    assert 'New York, NY' in data['info']
