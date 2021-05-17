def longest_substring(word):
	words ={}
	max_length =0
	ref = 0
	tobe_deleted=[]
	if len(set(word)) <=2 :
		return len(set(word))
	if len(word) <=2 :
		return len(word)
	else:
		for idx, letter in enumerate(word):
			if letter not in words:
				words[letter] = idx
				if len(words) > max_length:
					max_length= len(words)
			else:
				ref=words[letter]
				words[letter] =idx
				tobe_deleted=[]
				for char,value in words.items():
					if value < ref:
						tobe_deleted.append(char)
				for item in tobe_deleted:
  					del words[item]
	return max_length

strings = ['', 'a','aaaa','↕᭡᭡᭡↕↕᭡↕','ab','abc','abbc','srescripting','abc398c03nc-101']

for item in strings:
	print(longest_substring(item), item)