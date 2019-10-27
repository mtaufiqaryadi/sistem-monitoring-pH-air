from flask import Flask, abort, request
import json

app = Flask(__name__)

data_ph = [
    {
        "id" : 1,
        "ph" : "8",
    }
]

@app.route('/ph', methods=['GET'])
def index():
    str_ph = json.dumps(data_ph)
    return(str_ph)

@app.route('/ph/<int:id>', methods=['GET'])
def get_ph(id):
    ph = None
    for m in data_ph:
        if m["id"] == id :
            ph = m
            break

    if ph is None :
        abort(404)
        
    str_ph = json.dumps(ph)
    return(str_ph)


@app.route('/ph', methods=['POST'])
def create_ph():
    ph = request.form.get('ph')
    idbaru = (data_ph[-1]["id"])+1
    
    ph_baru = {
        "id" : idbaru,
        "ph" : ph
    }

    data_ph.append(ph_baru)
    return("OK")
             
app.run(port=9998, debug=True)