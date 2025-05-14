import os
if(not os.path.exists("data")):
    os.mkdir("data")
# for i in range(1,5):
#     # os.mkdir(f"data/Day{i}/")
#     os.rename(f"data/Day{i}",f"data/tutorial{i}")
file_path = os.path.join("data/tutorial1", "main.py")
folders=os.listdir("data")
print(folders)