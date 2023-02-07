from fastapi import FastAPI, HTTPException
from world_weather import get_timezone, get_weather

app = FastAPI()

@app.get("/")
def read_main():
    return {'msg': 'API Working'}

@app.get("/current_datetimes")
def current_datetimes(city1, city2):
    if city1 == city2:
        raise HTTPException(status_code=400, detail='Both cities should be unique')

    cities = [city1, city2]
    date = {}
    for city in cities:
        data = get_timezone(city)
        if data['time_zone']:
            date[city] = data['time_zone'][0]['localtime']
        elif 'error' in data:
            raise HTTPException(status_code=400, detail=data['error'][0]['msg'])
        else:
            raise HTTPException(status_code=400, detail="Error occurred while processing {}".format(city))

    return [{"date": date}]


@app.get("/current_datetimes_temp")
def current_datetimes_temp(city1, city2):
    if city1 == city2:
        raise HTTPException(status_code=400, detail='Both cities should be unique')

    cities = [city1, city2]
    info = {}
    for city in cities:
        data = get_weather(city)
        if 'current_condition' in data:
            condition = data['current_condition'][0]
            info[city] = {
                'date': condition['observation_time'],
                'temperature': f'{condition["temp_F"]}F'
            }
        elif 'error' in data:
            raise HTTPException(status_code=400, detail=data['error'][0]['msg'])
        else:
            raise HTTPException(status_code=400, detail="Error occurred while processing {}".format(city))

    return [{'info': info}]
