import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes": 721, "name": "Spongebob the movie", "views": 12341432},
        {"likes": 1415, "name": "How to make REST API", "views": 10132400},
        {"likes": 1312312312321, "name": "Shrek", "views": 1039393939393}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.patch(BASE + "video/2", {"views": 99, "likes": 190213231231311})
print(response.json())
