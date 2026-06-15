capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome"
}

# Nested List in Dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
    "Italy": {
        "cities_visited": ["Rome", "Milan", "Naples"],
        "total_visits": 8
    }
}

# Nested Dictionary


print(travel_log["Germany"]["cities_visited"][1])
