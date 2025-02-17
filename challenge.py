import random

vocab = {
    '3.14': 'the current version of Python',
    'input': 'Information or signals entered into a computer system.',
    'output': 'Information or signals produced or delivered by a computer system.',
    'syntax': 'The set of rules that defines the combinations of symbols that are considered to be correctly structured in that language.',
    'abstraction': 'A technique or process that manages complexity in a program or computer system, “hiding” details or removes duplication.',
    'index': 'The position of an item in a list.',
    'algorithm': 'a set of instructions'
}

# this will be the users response
ans = ''
while ans != 'q': # typing 'q' will quit the game
    print("\n-----------------")
    print("here are the terms:")
    # TODO display the vocabulary terms
    
    
    
    # TODO choose a random vocabulary word
    
    
    print("\nhere is the definition:")
    # TODO display the definition for that word
    


    # allow the user to guess the correct term (use the variable 'ans')
    ans = input("\n Enter your guess: ").lower()

    # TODO use an if-else conditional to determine if they were correct
    
    