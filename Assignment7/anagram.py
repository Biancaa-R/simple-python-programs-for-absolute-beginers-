'''Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram(s1,s2) that takes two strings and returns True if they are anagrams:Example: School master = The classroomListen = Silent
A gentleman = Elegant man'''

def is_anagram(s1,s2):
	s1=list(s1)
	s2=list(s2)
	if len(s1)==len(s2):
		for i in s1:
			if i in s2:
				pass
			else:
				return False
		return True
	else:
		return False

x=is_anagram("elegantman","agentleman")
print(x)
