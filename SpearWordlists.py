import itertools
import os
import time
import math

#Terminal Text

print("""
   _______  _______   ___ _      ______  ___  ___  __   ______________         
  / __/ _ \/ __/ _ | / _ \ | /| / / __ \/ _ \/ _ \/ /  /  _/ __/_  __/__  __ __
 _\ \/ ___/ _// __ |/ , _/ |/ |/ / /_/ / , _/ // / /___/ /_\ \  / / / _ \/ // /
/___/_/  /___/_/ |_/_/|_||__/|__/\____/_/|_/____/____/___/___/ /_(_) .__/\_, / 
                                                                  /_/   /___/  
             __       ___         ___       __        ___   __     __          
  ___________\ \     / _ )__ __  / _ )___ _/ /  __ __/ _ | / /__  / /  ___ _   
 /___/___/___/> >   / _  / // / / _  / _ `/ _ \/ // / __ |/ / _ \/ _ \/ _ `/   
/___/___/___//_/   /____/\_, / /____/\_,_/_.__/\_, /_/ |_/_/ .__/_//_/\_,_/    
                        /___/                 /___/       /_/                  
""")

print("\nDisclaimer: This script is for educational purposes only. Use responsibly and ethically.")
print("\nThis is the first version, so it still has some flaws. It Generates a lot of Passwords so I would keep the Input words down\nPlanning to add Word Filters so it dosent generate that many.\nType -Help for a Help Menu\nEnjoy ")


input_raw = input("\n\nEnter a List of Words, wich are Likley to be used in the Targets Password.\n(Example:Tom 98 7.5 Berlin Arsenal ...)\n")
if input_raw.strip().lower() == "-help":
    print("""
Help - SpearWordlist.py

Space seperated words are expected as input.
Example: Tom 98 7.5 Berlin Arsenal

Generates Passwords with 6 to 9 Characters.

Adds Special Characters to the Passwords.

The script will create a file named 'SpearWordlist.txt' in the current directory containing the generated passwords.
          
Dicrectory only works on Windows, but the file can be found in the same directory as this script on other systems.
""")
    exit()
input_words = input_raw.split()

#List Editing
Characters = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", ";", "=", "?", "@", "_","|",]

#Remove Bullshit
input_words = [w.replace('.', '') for w in input_words]
input_words = [w.replace(' ', '') for w in input_words]
input_words = [w.replace(',', '') for w in input_words]
input_words = [w.replace(':', '') for w in input_words]

#Animation
animation = ["===>"    , " ===>   | ", "  ===>  | ", "   ===> | ", "    ===>| ", "     ===|>"]

#Upper and Lowercase Versions
expanded_words = []
for w in input_words:
    if w:
        expanded_words.append(w.capitalize())
        expanded_words.append(w[0].lower() + w[1:])

#Generator code
print("Throwing the Spear...\n")
with open("SpearWordlist.txt", "w") as file:
    anim_index = 0
    word_count = 0
    for r in range(1, len(expanded_words)+1):
        for perm in itertools.permutations(expanded_words, r):
            combo = ''.join(perm)
            if 6 <= len(combo) <= 8:
                file.write(combo + '\n')
            for char in Characters:
                for i in range(r+1):
                    combo_with_char = ''.join(perm[:i]) + char + ''.join(perm[i:])
                    if 6 <= len(combo_with_char) <= 9:
                        file.write(combo_with_char + '\n')
            word_count += 1 + len(Characters) * (r+1)
            if word_count % 1000 == 0:
                print(animation[anim_index % len(animation)], end='\r')
                anim_index += 1
                time.sleep(0.2)




# Finished file
file_path = os.path.abspath("SpearWordlist.txt")
print(f"\nYour Wordlist has been completed: {file_path}\n")

#windows file location
os.startfile(os.path.dirname(file_path))