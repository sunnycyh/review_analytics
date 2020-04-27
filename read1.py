data = [] # 100m reviews
count = 0

with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Files ended, there are', len(data), 'in total.')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)
	
average = sum_len / len(data)
print('The average numbers of words per reply is:', average)

new = [] # 21XXX reviews (filtered)
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new),'reviews that are less than 100 words.')
print(new[12])