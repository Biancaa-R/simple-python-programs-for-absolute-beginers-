#Assignment3 9.Vowel or consonant
a=input('Enter a character:')
if a.isalpha()==True:
    if a.lower() in 'aeiou':
        print('Vowel')
    else:
        print('Consonant')