# Dict : key-value pairs
# it is unordered
#mutable
#cannot contain duplicate keys

d = {
  "name": "Shikha",
  "age" : 29
}

d["name"] #Shikha

# for below two we can use to get the value but the issue is if the key doestn exist
#  then d["city"] givens error where d.get["city"] gives none
d.get("city") #None 
d["city"] = "Delhi"

d.pop("age") # use this for deltee
print(d)
print(d.keys())
print(d.values())
print(d.items())
d.update({"name": "Mradul"})
print(d)
# Loop 
for key, value in d.items():
  print(key, value)

#   {[1,2]: "value"}   # ❌ error
# ✅ Valid
# {(1,2): "value"}   # ✅

#Advanced TRick
from collections import defaultdict

d = defaultdict(int)
d["a"] += 1
d["b"] = "True"
print(d)

# clear
d.clear()
print(d)

new_d = d.copy()
print(new_d)

keys= ["a","b","c"]
new_d1 = dict.fromkeys(keys, 0)
print(new_d1)

# Use Cases
# APIs (JSON = dict)
# Counting
# Mapping
# Caching