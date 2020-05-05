data = [] # 100m reviews
count = 0
with open('original.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Files ended, there are', len(data), 'in total.')

#count len
sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)
print('The average numbers of words per reply is:', sum_len / len(data))


#filter 100 words
new = [] # 21XXX reviews (filtered)
for d in data:
	if len(d) < 100:
		new.append(d)
print('There are', len(new),'reviews that are less than 100 words.')
print(new[12])


#filter good
good = [] # 162550 reviews (filtered)
for d in data:
	if 'good' in d:
		good.append(d)
print('There are', len(good),'reviews that are containing the words "good" in their content.')		
print(good[1])

#filter bad
bad = [] # bad = ['bad' in d for d in data]
for d in data:
		bad.append('bad' in d)

print(bad)








print(data[0])

# word count

wc = {} # word_count
for d in data: 
	words = d.split()
	for word in words: # nested for loop
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # add new key to wc

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word]) # wc[word] is the key with searching function, word is the key itself

print(len(wc))
print(wc['Sunny'])

while True:
	word = input('Please enter the word you want to search: ')
	if word == 'q':
		break
	if word in wc:
		print('The word', word, 'has appeared', wc[word], 'times.')
	else:
		print('This word does not appeared in the comment!')
print('Thanks for using the search engine.') 



