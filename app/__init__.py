from flask import Flask
app = Flask (__name__)

from app.modul.views import upload
from app.modul.views import upload_hasil
from app.modul.views import hasil_select
from app.modul.views import Dataframe
from app.modul.views import Coba
from app.modul.views import Index
from app.modul.views import Text_filtering
from app.modul.views import Load_data
from app.modul.views import Tokenizing
from app.modul.views import Filtering
from app.modul.views import Stemming
