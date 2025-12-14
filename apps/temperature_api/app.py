import datetime
import random
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/temperature/{sensor_id}')
def get_temperature(location: Annotated[str | None, Query] = None, sensor_id=None):
    # If no location is provided, use a default based on sensor ID
    if not location:
        if sensor_id == "1":
            location = "Living Room"
        elif sensor_id == "2":
            location = "Bedroom"
        elif sensor_id == "3":
            location = "Kitchen"
        else:
            location = "Unknown"

    # If no sensor ID is provided, generate one based on location
    if not sensor_id:
        if location == "Living Room":
            sensor_id = "1"
        elif location == "Bedroom":
            sensor_id = "2"
        elif location == "Kitchen":
            sensor_id = "3"
        else:
            sensor_id = "0"
    
    return {
        'value': generate_temperature(),
        'unit': '°C',
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'location': location,
        'status': 'active',
        'sensor_id': sensor_id,
        'sensor_type': 'temperature',
        'description': 'temperature sensor in ' + location
    }

def generate_temperature():
    return round(random.uniform(10.0, 30.0), 2)
