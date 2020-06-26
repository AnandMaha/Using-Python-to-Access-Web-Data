import urllib.request
import json
#get url handle from json data
url = input('Enter url: ')
url_data = urllib.request.urlopen(url).read().decode()
#compute and print out the sum of the counts in comments
print('Retrieved', len(url_data))
data_json = json.loads(url_data)
count = 0
sum = 0
for item in data_json["comments"]:
	print(item)
	count = count + 1
	print("Current name:", item["name"])
	sum = sum + item["count"] 

print("Count:", count)
print("Sum:", sum)