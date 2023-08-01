from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

api = "https://api.openweathermap.org/data/2.5/weather?q=" + "delhi" + "&416b13dc795dbaabb813c8744f4f2e8e"

json_data = requests.get(api).json()
print(json_data)