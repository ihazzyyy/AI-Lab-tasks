from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ride_queue = []
completed_rides = []

def predict_fare(distance):
    return distance * 2.5

def request_ride(source, destination):
    distances = {'A': {'B': 5, 'C': 10}, 'B': {'A': 5, 'C': 7}, 'C': {'A': 10, 'B': 7}}
    return distances.get(source, {}).get(destination, 0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book_ride():
    data = request.get_json()
    source = data['source'].upper()
    destination = data['destination'].upper()

    distance = request_ride(source, destination)
    if distance == 0:
        return "Invalid route. Please try again.", 400

    fare = predict_fare(distance)
    ride = {
        'from': source,
        'to': destination,
        'fare': round(fare, 2)
    }

    ride_queue.append(ride)
    return jsonify({'message': 'Ride booked successfully!'})

@app.route('/serve', methods=['POST'])
def serve_ride():
    if not ride_queue:
        return "No rides to serve.", 400

    ride = ride_queue.pop(0)
    completed_rides.append(ride)
    return jsonify({'message': 'Ride served successfully!'})

@app.route('/history', methods=['GET'])
def view_completed_rides():
    return jsonify(completed_rides)

if __name__ == '__main__':
    app.run(debug=True)