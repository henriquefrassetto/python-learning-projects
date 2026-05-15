# Current weather
# Forecast
# Search historic
# Favorites
# Unit conversion
# Cache
# Limit 100 request/min
# Authentication

from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from collections import deque
from dotenv import load_dotenv
import os
import datetime
import redis
import json
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def fetch_weather_current(city: str, unit: str):

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"

    params = {
        "key": WEATHER_API_KEY,
        "unitGroup": unit,
        "include": "current"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")

    data = response.json()

    return {
        "city": data["resolvedAddress"],
        "temperature": data["currentConditions"]["temp"],
        "wind": data["currentConditions"]["windspeed"],
        "sensation": data["currentConditions"]["feelslike"],
        "condition": data["currentConditions"]["conditions"]
    }

def fetch_weather_forecast(city: str, unit: str, days: int = 7):

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"

    params = {
        "key": WEATHER_API_KEY,
        "unitGroup": unit,
        "include": "days"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="City not found")

    data = response.json()

    forecast = []

    for day in data["days"][:days]:

        forecast.append({
            "date": day["datetime"],
            "temperature": day["temp"],
            "wind": day["windspeed"],
            "condition": day["conditions"]

        })

    return {"city": data["resolvedAddress"], "forecast": forecast}


historic = deque(maxlen=10)

favorites = []

def rate_limit(request: Request):
    ip = request.client.host
    key = f"limit:{ip}"

    count = r.get(key)

    if count is None:
        r.set(key, 1, ex=60)
        return

    if int(str(count)) >= 100:
        raise HTTPException(status_code=429, detail="Too many requests")

    r.incr(key)

def auth(request: Request):
    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    
# dependencies=[Depends(auth), Depends(rate_limit)]

app = FastAPI(dependencies=[Depends(rate_limit)])
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request = request,
        name = "index.html",
        context = {}
    )

@app.get("/weather/current")
def get_current_weather(city: str, request: Request, unit: str = "us"):

    if unit not in ["us", "metric"]:
        raise HTTPException(status_code=400, detail="Invalid unit")

    city = city.strip().lower()

    cached_key = f"current:{city}:{unit}"
    cached_current = r.get(cached_key)

    if cached_current:
        weather = json.loads(cached_current)
    else:
        weather = fetch_weather_current(city, unit)
        r.set(cached_key, json.dumps(weather), ex=300)

    historic.append({
        "city": weather["city"],
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": request.client.host,
    })

    return {"city": weather["city"], "weather": weather}

@app.get("/weather/forecast")
def get_forecast_weather(city: str, request: Request, unit: str = "us"):

    if unit not in ["us", "metric"]:
        raise HTTPException(status_code=400, detail="Invalid unit")

    city = city.strip().lower()

    cached_key = f"forecast:{city}:{unit}"
    cached_forecast = r.get(cached_key)

    if cached_forecast:
        weather = json.loads(cached_forecast)
    else:
        weather = fetch_weather_forecast(city, unit)
        r.set(cached_key, json.dumps(weather), ex=300)

    historic.append({
        "city": weather["city"],
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": request.client.host,
    })

    return {"city": weather["city"], "weather": weather}

@app.get("/historic")
def get_historic():

    if len(historic) == 0:
        raise HTTPException(status_code=400, detail="Historic is empty")

    return {"historic": historic}

@app.delete("/historic")
def delete_historic():

    if len(historic) == 0:
        raise HTTPException(status_code=400, detail="Historic is empty")

    historic.clear()

    return {"msg": "Historic cleaned!", "historic": historic}

@app.post("/favorites")
def add_favorites(city: str):

    if city in favorites:
        raise HTTPException(status_code=400, detail="Favorite already exists")

    if len(favorites) >= 5:
        raise HTTPException(status_code=400, detail="Favorite list is full!")

    fetch_weather_current(city, unit = "us")

    favorites.append(city)

    return {"msg": "Favorite added!", "favorites": favorites}

@app.get("/favorites")
def get_favorites():

    if len(favorites) == 0:
        raise HTTPException(status_code=400, detail="Favorite list is empty")

    return {"favorites": favorites}

@app.delete("/favorites")
def delete_favorites(city: str):

    if len(favorites) == 0:
        raise HTTPException(status_code=400, detail="Favorite list is empty")

    if city not in favorites:
        raise HTTPException(status_code=400, detail="Favorite not found")

    favorites.remove(city)

    return {"msg": "Favorite excluded!", "favorites": favorites}
