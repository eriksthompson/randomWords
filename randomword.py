import random
consontants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'

length = input('Enter length of word')
num_words = input('Enter number of words to generate:')
def random_letter(random_word):
    global is_vowel
    global const_in_a_row
    if is_vowel:
        const_in_a_row = 0
        random_word += random.choice(vowels)
        is_vowel = False
    else:
        random_word += random.choice(consontants)
        
    return random_word


const_in_a_row = 0
is_vowel = random.choice([True, False])
i = 0
while(i < int(num_words)):
    i+=1
    random_word = ''
    is_vowel = random.choice([True, False])
    while len(random_word) < int(length):
        if is_vowel:
            const_in_a_row = 0
            
            random_word = random_letter(random_word)
        else:
            random_word = random_letter(random_word)
            const_in_a_row += 1
            is_vowel = random.choice([True, False])
            if const_in_a_row > 1:
                is_vowel = True
    print(random_word)