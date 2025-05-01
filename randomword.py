import random
consontants = 'qwrtpsdfghjklzxcvbnm'
vowels = 'aeiou'

#length = random.choice([3,4,5,6,7,8,9])
num_words = input('Enter number of words to generate:')
def log_to_file(filename, randomly_generated_words):
    """
    Appends the question and answer to the specified text file.

    Args:
        filename (str): The name of the text file.
        context (str): The context or textbook section given for the question.
        question (str): The user's question.
        answer (str): The chatbot's answer.
    """
    with open(filename, "a") as file:
        for i, s in enumerate(randomly_generated_words):
            file.write(f": {i+1, s}\n")
        file.write("\n")  # Add a blank line for better readability

const_in_a_row = 0
is_vowel = random.choice([True, False])
i = 0
words = []
while(i < int(num_words)):
    length = random.choice([3,4,5,6,7,8,9])
    i+=1
    random_word = ''
    is_vowel = random.choice([True, False])
    while len(random_word) < int(length):
        if is_vowel:
            const_in_a_row = 0
            random_word += random.choice(vowels)
            is_vowel = False
        else:
            random_word += random.choice(consontants) 
            const_in_a_row += 1
            is_vowel = random.choice([True, False])
            if const_in_a_row > 1:
                is_vowel = True
    words.append(random_word)
log_to_file('computer science practice/randomlist.txt', words)