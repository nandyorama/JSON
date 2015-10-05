import json

#JSON File Name
fileName = "test.json"

lst=[]
#Adding dictionary elements to List
for item in range(5):
	dct={}
	#Adding Elements to Dictionary
	dct[item+1]="SOMEDATA"+str(item)
	#Adding Dictionary to List
	lst.append(dct)

#Dumping List of Dictionary to JSON File
out_file = open(fileName,"a")
json.dump(lst,out_file, indent=4)                                    
out_file.close()

#Loading JSON FILE using Json File Name
with open(fileName) as dataFile:
	data = json.load(dataFile)

#Iterate through the Loaded list Object and then each dictionary elements
for item in data:
	for k,v in item.items():
		print(k+"----"+v)

