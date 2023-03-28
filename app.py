from flask import Flask, request

app = Flask(__name__) #__name__ is spatial variable

flights = [
    {"from_city": "London",
     "to_city": "Helsinki",
     "days": [1, 3, 5, 7],
     "captain": {'name': 'Neil',
                 'surname': 'Bonn'},
     "duration_min": 92,
     "capacity": 100,
     "booked": 10,
     "available": 90,
     "flight_id": 555},

    {"from_city": "Manchester",
     "to_city": "Oslo",
     "days": [2, 4],
     "captain": {'name': 'Jorgen',
                 'surname': 'Kopff'},
     "duration_min": 55,
     "capacity": 80,
     "booked": 62,
     "available":  18,
     "flight_id": 1818},
]

@app.route("/") #dynamic URLs
def home_page():
    return "Welcome to my Page"


@app.route("/page/<string:name>") #dynamic URLs
#rerouting URLs
def page(name):
    #return "Let's Build APIs"
    return f"Hello, {name}"

@app.get("/flights")
def get_flights():
    return {"flights": flights}

#post something

@app.post("/flights") #allows you to post new data anywhere, even if you use it
def post_flight():
    request_data = request.get_json()
    new_flight = {"from_city": request_data["from_city"], "to_city": request_data["to_city"],
                  "days": request_data["days"], "captain": {}
                  }
    flights.append(request_data)
    return request_data

@app.get("/flights/<int:flight_id>")
def get_flight(flight_id):
    for flight in flights:
        if flight['flight_id'] == flight_id:
            return flight
    return {'message': "Sorry not found"}, 404

@app.get("/flights/edit/<int:flight_id>")
def edit_flights(flight_id):
    for flight in flights:
        if flight['flight_id'] == flight_id:
            flight['booked'] == 500
            return flight
    return {'message': "Sorry not found"}, 404

# #BAD REQUEST WHEN ORDER IS NOT CORRECT:
# {
# 			"available": 15,
# 			"booked": 10,
# 			"capacity": 120,
# 			"captain": {
# 				"name": "Sarah",
# 				"surname": "Peterson"
# 			},
# 			"days": [
# 				1,
# 				2,
# 				5,
# 				8
# 			],
# 			"duration_min": 55,
# 			"flight_id": 555,
# 			"from_city": "London",
# 			"to_city": "Paris"
# 		}