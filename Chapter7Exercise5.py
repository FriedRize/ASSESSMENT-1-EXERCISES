def describe_city(city, country="Philippines"):
    """Display a simple sentence about a city and its country."""
    print(f"{city} is in {country}.")

describe_city("Manila")  # Uses the default country
describe_city("Cebu")    # Uses the default country
describe_city("Tokyo", "Japan")  # Overrides the default country