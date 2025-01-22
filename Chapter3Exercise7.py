locations = ["Tokyo", "Kyoto, ""Paris", "Seoul", "London"]

print("Original list:", locations)

print("Alphabetical order:", sorted(locations))

print("Original list after sorted:", locations)

print("Reverse alphabetical order:", sorted(locations, reverse=True))

print("Original list after reverse sorted:", locations)

locations.reverse()
print("List after reverse:", locations)

locations.reverse()
print("List after reversing again:", locations)

locations.sort()
print("List after sort (alphabetical):", locations)

locations.sort(reverse=True)
print("List after sort(reverse=True):", locations)
