worldcapitals = {
    "Ireland":"Dublin",
    "India":"New Delhi",
    "South Africa":"Cape town",
    "Brazil": "Brasília"
}

worldcapitals ["Germany"] = "Berlin"

worldcapitals.pop("South Africa")


print(worldcapitals["India"])
print(worldcapitals)

for i in worldcapitals:
    print(i)

for value in worldcapitals.values():
    print(value)

for key,value in worldcapitals.items():
    print(f"{key}:{value}")

print(len(worldcapitals))   