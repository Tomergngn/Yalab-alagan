import pickle
with open('courseDict.pkl', 'rb') as f:
    info = pickle.load(f)
for i in info["BJJ"]:
    if "972556625345" in i[2]:
        print(info["BJJ"][32])
        print(len(info["BJJ"]))