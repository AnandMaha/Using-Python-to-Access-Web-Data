import urllib.request
import xml.etree.ElementTree as ET

url = input("Enter url - ")
url_h = urllib.request.urlopen(url)
data = url_h.read()
tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print(results)
count = 0
sum = 0
for item in results:
    x = int(item.find('count').text)
    count =count+1
    sum = sum+x

print("Count:", count)
print("Sum:", sum)