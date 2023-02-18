from flask import Flask, request, jsonify
#from waitress import serve
import util
import json
#%run util.ipynb

app = Flask(__name__)

@app.route('/hi')
def hi():
    return util.areas()


@app.route('/locations')
def locations():
    response = jsonify({
        'locations': util.locations()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price')
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    size = int(request.form['size'])
    bath = int(request.form['bath'])
    area_type = request.form['area_type']
    balcony = int(request.form['balcony'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(area_type, location, size, total_sqft, bath, balcony)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('python flask started')
    app.run()
    #serve(app, host='0.0.0.0', port=50100, threads=1)
