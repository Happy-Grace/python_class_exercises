# 27th Feb, 2025: Thursday Class

info = {1: "uno", 2: "dos", 3: "tres"}

# print(info.fromkeys(info[, "uniform"]))

print(info.get(5)) #The key 5 does not exist, defaultly set to 'None'.

print(info.get(5, "Unknown")) # the key 5 doesn't exist, sets to unknown

# print(info.hash_key(1))

print("")
print(info.setdefault(5)) #Defaultly sets to None as the 'key 5' does no exist.
print(info.setdefault(5, "cinq")) # Creates and sets the 'key 5' that initially did not exist.
