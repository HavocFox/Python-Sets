our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
dupe_routes = {}

if our_routes.isdisjoint(competitor_routes):
    print("There are no duplicate destinations.")

else:  
    print("Destinations that both airlines fly to: ")

    print(our_routes.intersection(competitor_routes))