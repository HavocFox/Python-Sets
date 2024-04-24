our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
dupe_routes = {}

if our_routes.isdisjoint(competitor_routes):
    print("There are no duplicate destinations.")

else:  
    print("Destinations that both airlines fly to: ")

    print(our_routes.intersection(competitor_routes))

    print("Destinations unique to your airline: ")

    print(our_routes.difference(competitor_routes))

    print("Do these airlines have any destinations that neither shares?")

    neither = []
    for route in our_routes:

        if route in competitor_routes:
            pass
        else:
            neither.append(route)

    for route in competitor_routes:

        if route in our_routes:
            pass
        else:
            neither.append(route)

    if len(neither)>0:
        print(f"Yes. These routes are: {neither}")
    else:
        print("No, they do not.")