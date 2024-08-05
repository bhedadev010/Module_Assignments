#12. Write a Python program to convert a list of tuples into a dictionary

data = [(1, 'sravan',3), (2, 'ojaswi',1), (3, 'bobby',True), (4, 'rohith',"ok"), (5, 'gnanesh',23)]
di = dict()

for i in range(0,len(data)):
    di[i] = data[i]

print(di)