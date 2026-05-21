python
from flask import Flask, jsonify, request
import pandas as pd
import geopy.distance

app = Flask(__name__)

# Load the dataset - replace with your actual dataset path
data = pd.read_csv('public_transport_accessibility_data.csv')

# Example function to find nearest accessible bus stop
def find_nearest_accessible_stop(user_location, wheelchair_access=True):
    min_distance = float('inf')
    nearest_stop = None

    for index, row in data.iterrows():
        if wheelchair_access and not row['wheelchair_accessible']:
            continue

        stop_location = (row['latitude'], row['longitude'])
        distance = geopy.distance.distance(user_location, stop_location).km

        if distance < min_distance:
            min_distance = distance
            nearest_stop = row

    return nearest_stop

@app.route('/nearest_stop', methods=['GET'])
def get_nearest_stop():
    user_lat = float(request.args.get('lat'))
    user_lon = float(request.args.get('lon'))
    wheelchair_access = request.args.get('wheelchair', 'true').lower() == 'true'

    user_location = (user_lat, user_lon)
    nearest_stop = find_nearest_accessible_stop(user_location, wheelchair_access)

    if nearest_stop is None:
        return jsonify({"error": "No accessible stops found."}), 404

    return jsonify({
        "stop_name": nearest_stop['stop_name'],
        "location": {
            "latitude": nearest_stop['latitude'],
            "longitude": nearest_stop['longitude']
        },
        "distance": geopy.distance.distance(user_location, (nearest_stop['latitude'], nearest_stop['longitude'])).km
    })

if __name__ == '__main__':
    app.run(debug=True)
