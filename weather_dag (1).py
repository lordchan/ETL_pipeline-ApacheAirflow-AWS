from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import json
import pandas as pd

def transformer_func(task_instance):
    data = task_instance.xcom_pull(task_ids = 'extract_weather_Data')
    city = data["name"]
    weather_description = data["weather"][0]['description']
    temperature = data["main"]["temp"]-273.15
    feels_like = data["main"]["feels_like"]-273.15
    min_temp = data["main"]["temp_min"]-273.15
    max_temp = data["main"]["temp_max"]-273.15
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    data_dict = {
        "city": city,
        "weather_description":weather_description,
        "temperature": temperature,
        "Feels Like": feels_like,
        "Minimun Temp":min_temp,
        "Maximum Temp": max_temp,
        "Pressure": pressure,
        "Humidty": humidity,
        "Wind Speed": wind_speed,
        "Time of Record": time_of_record,
        "Sunrise (Local Time)":sunrise_time,
        "Sunset (Local Time)": sunset_time
    }
    df = pd.DataFrame([data_dict])
    now = datetime.now()
    name_of_file = now.strftime('%d%b%Y%H%M%S')
    
    aws_credentials = {"key": "ASIASOX4CZJYLFLYBSHE", "secret": "27R55w7OAexKpNdi3/kaCE2gOmd/0vY6sZny093D", "token": "FwoGZXIvYXdzEM///////////wEaDMORjgoLzY+rtuNi1iJqBRWPG3oI/yfpL6597mtTOHi4EyiZw/QagPxEIkjjxaG9/Z/9kr5TYSC7D7uJBIsT40qWtMZXGd6HilrStC3LQvzbUMfPwtykLwbfuvjjJGT3hEEaZYc3kXPKeil3AJdI+kWeGYZ3zhniiCjZyPimBjIosAqJNexp+LT4YnLQZussncpjlzwgpPCzxjANzv3xAcWUWshj9JaWOQ=="}
    df.to_csv(f"s3://airflowweatherapichanakya/{name_of_file}.csv",index = False, storage_options = aws_credentials)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023,1,8),
    'email': ['chinni030899@gmail.com'],
    'email_on_failure':True,
    'email_on_retry':False,
    'retries':2,
    'retry_delay':timedelta(minutes = 2)}

with DAG('weather_dag', default_args = default_args, schedule_interval = '@daily', catchup = False) as dag:
    is_weather_api_ready = HttpSensor(task_id = 'is_weather_api_ready',http_conn_id = 'weathermap_api',
                                      endpoint = '/data/2.5/weather?q=Bengaluru&appid=b6664bd8da5f07840161dd4424e8ab59')
    extract_weather_Data = SimpleHttpOperator(task_id = 'extract_weather_Data', http_conn_id = 'weathermap_api', 
                                              endpoint = '/data/2.5/weather?q=Bengaluru&appid=b6664bd8da5f07840161dd4424e8ab59',
                                              method = 'GET',
                                              response_filter = lambda r : json.loads(r.text),
                                              log_response = True)
    transform_load_weather_Data = PythonOperator(task_id = 'transform_load_weather_Data', python_callable = transformer_func)
    
    is_weather_api_ready>>extract_weather_Data>>transform_load_weather_Data