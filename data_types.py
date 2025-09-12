# --- Lists ---
numbers = [1, 2, 3]
numbers.append(4)        
print("After append:", numbers)
numbers.pop()              
print("After pop:", numbers)
print("Slicing:", numbers[0:2])  #

# --- Dictionaries ---
person = {"name": "Ankita", "age": 23}
print("Name:", person["name"])
person["city"] = "Kathmandu"
print("Updated Dictionary:", person)

# --- Tuples ---
coordinates = (27.7, 85.3)
print("Coordinates:", coordinates)
# coordinates[0] = 30  # ❌ would throw error (immutable)

# --- Sets ---
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))
