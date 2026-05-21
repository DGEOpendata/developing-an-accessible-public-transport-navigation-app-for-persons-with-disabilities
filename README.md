markdown
# Accessible Public Transport Navigation App

This repository provides the source code for a Flask-based API designed to enable accessible navigation for public transport in Abu Dhabi. The application leverages the 'Public Transport Accessibility Data' dataset to help persons with disabilities find accessible public transport routes and stops.

## Features
- Locates the nearest accessible bus stop based on user location.
- Filters stops for wheelchair accessibility.
- Provides real-time distance information from the user's current location to the nearest stop.

## Requirements
- Python 3.8+
- Flask 2.0+
- pandas 1.3+
- geopy 2.2+

## Installation
1. Clone this repository:
   bash
   git clone https://github.com/yourusername/accessible-transport-navigation.git
   
2. Navigate to the project directory:
   bash
   cd accessible-transport-navigation
   
3. Install dependencies:
   bash
   pip install -r requirements.txt
   
4. Place the `public_transport_accessibility_data.csv` file in the project directory.

## Dataset Format
Ensure your dataset (CSV) includes the following columns:
- `stop_name`: Name of the bus stop.
- `latitude`: Latitude of the bus stop.
- `longitude`: Longitude of the bus stop.
- `wheelchair_accessible`: Boolean indicating wheelchair accessibility.

## Running the Application
1. Start the Flask application:
   bash
   python app.py
   
2. Access the API endpoint:
   
   http://localhost:5000/nearest_stop?lat=<latitude>&lon=<longitude>&wheelchair=<true/false>
   
3. Replace `<latitude>` and `<longitude>` with the user's current coordinates and set `<true/false>` for wheelchair accessibility.

## Example
Request:

GET http://localhost:5000/nearest_stop?lat=24.4539&lon=54.3773&wheelchair=true

Response:

{
  "stop_name": "Corniche Central",
  "location": {
    "latitude": 24.4686,
    "longitude": 54.3657
  },
  "distance": 1.5
}


## Future Enhancements
- Integration with real-time public transport APIs for live schedule updates.
- Multilingual support to cater to diverse users.
- User feedback mechanism for continuous dataset improvement.

## Contributing
We welcome contributions! Please feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License.

