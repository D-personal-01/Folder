import os

if (not os.path.exists("data")):
        os.mkdir("data")

for i in range (0,100):
        if (not os.path.exists(f"data/Days{i}")):
                os.mkdir(f"data/Days{i}")

for i in range (99,-1,-1):
        os.rename(f"data/Days{i}",f"data/Days{i+1}")
    
for i in range (99,-1,-1):
        os.rename(f"data/Days{i+1}",f"data/Days {i+1}")

fols=os.listdir("data")

# printing list of folders
print(fols)
# not looking sorted 21', 'Days 22', 'Days 23', 'Days 24', 'Days 25', 'Days 26', 'Days 27', 'Days 28', 'Days 29', 'Days 3', 'Days 30', 'Days 31', 'Days 32', 'Days 33', 'Days 34', 'Days 35', 'Days 36', 'Days 37', 'Days 38', 'Days 39', 'Days 4', 'Days 40', 'Days 41', 'Days 42', 'Days 43', 'Days 44', 'Days 45', 'Days 46', 'Days 47', 'Days 48', 'Days 49', 'Days 5', 'Days 50', 'Days 51', 'Days 52', 'Days 53', 'Days 54', 'Days 55', 'Days 56', 'Days 57', 'Days 58', 'Days 59', 'Days 6', 'Days 60', 'Days 61', 'Days 62', 'Days 63', 'Days 64', 'Days 65', 'Days 66', 'Days 67', 'Days 68', 'Days 69', 'Days 7', 'Days 70', 'Days 71', 'Days 72', 'Days 73', 'Days 74', 'Days 75', 'Days 76', 'Days 77', 'Days 78', 'Days 79', 'Days 8', 'Days 80', 'Days 81', 'Days 82', 'Days 83', 'Days 84', 'Days 85', 'Days 86', 'Days 87', 'Days 88', 'Days 89', 'Days 9', 'Days 90', 'Days 91', 'Days 92', 'Days 93', 'Days 94', 'Days 95', 'Days 96', 'Days 97', 'Days 98', 'Days 99']

for fol in fols:
        print(fol)
# nither this

#Lets make it organised
for i in range(0, 101):
    old = f"data/Days {i}"
    new = f"data/Days {i:03d}"   # 3-digit padding
    
    if ( os.path.exists(old)):
        os.rename(old, new)

# More organised
fols=os.listdir("data")

print(fols)

for fol in fols:
        print(fol)
