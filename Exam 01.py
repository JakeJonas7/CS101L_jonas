def word_count(text):
    #wordlist = []
    #text = input()
    #wordlist = text.split()
    wordlist = text.split() #splits input into a list of words, separated by spaces
    #print(wordlist)
    numofwords = len(wordlist)
    return numofwords
'''Takes the list of words and returns the number of elements'''
def find_longest_word(text):
    #wordlist = []
    #text = input()
    #wordlist = usertext.split()
    wordlist = text.split() #splits input into a list of words, separated by spaces
    longword = ''
    for i in wordlist:
        if len(i) > len(longword):
            longword = i
    return longword
'''Takes the list of words and returns the longest word'''
def count_substring(text,substring):
    #substring = input()
    wordlist = text.split() #splits input into a list of words, separated by spaces
    subcount = wordlist.count(substring) #counts number of times substring is in wordlist
    return subcount
'''Takes the substring input and returns the number of occurrences in the list of words'''
def extract_unique_words(text):
    wordlist = text.split() #splits input into a list of words, separated by spaces
    uniquewords = []
    for i in wordlist:
        #if wordlist.count(i) == 1:
        #uniquewords.append(i)
        if uniquewords.count(i) < 1:
            uniquewords.append(i)
        else:
            if uniquewords.count(i) > 1:
                continue        
    return uniquewords
'''Takes the list of words and if they are unique, it adds them to a new list and returns the new list'''

def main():
    print('Welcome to the Text Processing Program!')
    print()
    text = input('Enter a text: ')
    print()
    wordlist = text.split() #splits input into a list of words, separated by spaces
    print('Original Text:')
    print(text)
    user_input = 0
    #print(wordlist)
    numofwords = 0
    longword =  ''
    uniquewords = []
    while user_input != 5:
        print()
        print('Text Analysis Options:')
        print('1. Word Count')
        print('2. Longest Word')
        print('3. Count of Substring')
        print('4. Unique Words')
        print('5. Exit')
        user_input = int(input('Enter the number of the analysis option (1-5): '))
        if user_input == 1:
            #word_count(text)
            print()
            print('Word Count:', word_count(text))
        elif user_input == 2:
            #find_longest_word(text)
            print()
            print('Longest Word:', find_longest_word(text))
        elif user_input == 3:
            substring = input('Enter a substring to count: ')
            print(f"Count of Substring '{substring}': {count_substring(text,substring)}")
        elif user_input == 4:
            #extract_unique_words(text)
            print()
            print('Unique Words:', extract_unique_words(text))
            
        elif user_input == 5:
            break
            #print('Thank you for using the Text Processing Program!')
    print()
    print('Thank you for using the Text Processing Program!')
'''Takes the user input, prints it and then runs a loop for the user until they enter 5 that includes all the previous functions.'''

main()
          
            
                         

    
    
