from flask import Flask
app = Flask(__name__)

from app.modul.views import index
from app.modul.views import uploading
from app.modul.views import hasilupload
from app.modul.views import hasilpemilihan
from app.modul.views import tokenisasi
from app.modul.views import filtering
from app.modul.views import stemming
from app.modul.views import inputK
from app.modul.views import harmonic

