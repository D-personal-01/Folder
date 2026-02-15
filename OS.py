import os

if (not os.path.exists("data")):
        os.mkdir("data")

for i in range (0,100):
        if (not os.path.exists(f"data/Days{i}")):
                os.mkdir(f"data/Days{i}")


for i in range (99,-1,-1):

        os.rename(f"data/Days{i}",f"data/Days{i+1}")
    
