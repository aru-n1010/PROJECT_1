#Step 1 
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

you_win=''' ____  ____                              _            
|_  _||_  _|                            (_)           
  \ \  / / .--.   __   _    _   _   __  __   _ .--.   
   \ \/ // .'`\ \[  | | |  [ \ [ \ [  ][  | [ `.-. |  
   _|  |_| \__. | | \_/ |,  \ \/\ \/ /  | |  | | | |  
  |______|'.__.'  '.__.'_/   \__/\__/  [___][___||__]
  '''

you_lose=''' _____.___.              .____                        
\__  |   | ____  __ __  |    |    ____  ______ ____  
 /   |   |/  _ \|  |  \ |    |   /  _ \/  ___// __ \ 
 \____   (  <_> )  |  / |    |__(  <_> )___ \\  ___/ 
 / ______|\____/|____/  |_______ \____/____  >\___  >
 \/                             \/         \/     \/ 
'''                                     

word_list = ["aardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
word_len = len(chosen_word)
lives=6
display=[]

for _ in range(word_len):
  display+="_"
print(display)

# print("\n")
end_game=False
while not end_game:
  guess=input("\nguess a letter : ").lower()
  for index in range(word_len):
    letter=chosen_word[index]
    if letter == guess:
      display[index]=letter
  # print(display)
  
  if guess not in chosen_word:
    lives-=1
    if lives==0:
      end_game=True
      print(you_lose)

  print(f"{''.join(display)}")

    
  if "_" not in display:
      end_game=True
      print(you_win)
    
  print(stages[lives])
  
