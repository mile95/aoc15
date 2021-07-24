import hashlib

base_input = "ckczppom"

# Part A
counter = 0
while True:
    input = base_input + str(counter)
    hex_hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    if hex_hash[:5] == "00000":
        break
    counter+= 1
print(counter)

# Part B
counter = 0
while True:
    input = base_input + str(counter)
    hex_hash = hashlib.md5(input.encode('utf-8')).hexdigest()
    if hex_hash[:6] == "000000":
        break
    counter+= 1
print(counter)