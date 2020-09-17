from flask import Flask 

mota_app = Flask(__name__)

@mota_app.route('/')
def ping():
    return "Pong! Project Mota is Online"


mota_app.run()