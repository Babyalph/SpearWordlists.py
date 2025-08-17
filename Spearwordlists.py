import itertools
import os
import time
import math

#variables
Characters = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", ";", "=", "?", "@", "_","|",]
oneword1 = ["123456", "password", "qwerty", "abc123", "letmein", "welcome", "iloveyou", "654321", "12345678", "87654321", "user", "test","123", "321", "1234", "4321",]


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
print("\nThis is the first version, so it still has some flaws. It Generates a lot of Passwords so I would keep the Input words down\nPlanning to add Word Filters so it dosent generate that many.\nType -Help for a Help Menu\nPlease Star it on Github\nEnjoy ")

while True:
    version = input(
        "Choose '1' for the one word version or '2' for the multi word version:\n"
        "(Type '?' for explanation)\n"
    )

    if version == '?':
        print("""
        Version 1: One Word Version
        - Generates passwords based on a single word input.
        - Adds common Strings like '123456', 'password', etc.
        - Searches for the word in the Rockyou.txt Wordlist to include those passwords.
        !!Download Rockyou.txt from Releaeses or elswhere and put it in the same directory as this script.!!

        Version 2: Multi Word Version
        - Generates passwords based on multiple words input.
        - Allows for more complex combinations and variations between the words but doesn't add common Strings.
        
        Both add Special Characters to the Passwords.
        """)
        continue  

    # One word version
    if version == '1':
        input_raw = input("\n\nEnter a Word, which is likely to be used in the target's password.\n(Example: Tom)\n")
        input_words = input_raw.split()
        break  

    # Multi word version
    elif version == '2':
        input_raw = input("\n\nEnter a list of words likely used in the target's password.\n(Example: Tom 98 7.5 Berlin Arsenal ...)\n")

        if input_raw.strip().lower() == "-help":
            print("""
            Help - SpearWordlist.py

            Space-separated words are expected as input.
            Example: Tom 98 7.5 Berlin Arsenal

            Generates passwords with 6 to 9 characters.

            Adds special characters to the passwords.

            You can add more customization by answering 'y' when prompted.

            The script will create a file named 'SpearWordlist.txt' in the current directory containing the generated passwords.
                    
            Directory only works on Windows, but the file can be found in the same directory as this script on other systems.
            """)
            continue  

        input_words = input_raw.split()
        break  
    elif version == "-help":
            print("""
            Help - SpearWordlist.py
                  
            Download Rockyou.txt from Releaeses or elswhere and put it in the same directory as this script.
                  
            Space-separated words are expected as input.
                  
            Example: Tom 98 7.5 Berlin Arsenal

            Generates passwords with 6 to 9 characters.

            Adds special characters to the passwords.

            You can add more customization by answering 'y' when prompted.

            The script will create a file named 'SpearWordlist.txt' in the current directory containing the generated passwords.
                    
            Directory only works on Windows, but the file can be found in the same directory as this script on other systems.
            """)
            continue  

    else:
        print("Invalid input, please try again.")



#Remove Bullshit
input_words = [w.replace('.', '') for w in input_words]
input_words = [w.replace(' ', '') for w in input_words]
input_words = [w.replace(',', '') for w in input_words]
input_words = [w.replace(':', '') for w in input_words]

#Upper and Lowercase Versions
expanded_words = []
for w in input_words:
    if w:
        expanded_words.append(w.capitalize())
        expanded_words.append(w[0].lower() + w[1:])


#fuhrter customization
y_n = input("Do you want to Add more customization? (y/n): ")
if y_n == 'y':
    #Password Length
    mini = int(input("Enter the Minimum Length of the Passwords (recommended: 6): "))
    maxi = int(input("Enter the Maximum Length of the Passwords (recommended: 9): "))
else:
    mini = 6
    maxi = 9


#Rockyou Search
if version == "1":
    print("Searching the word in the Rockyou.txt file...")
    with open("rockyou.txt", "r") as file:
     for line in file:
        for word in line.split():
             if any(w in word for w in input_words):
                rockyou_word = word.strip()    
                print("Passwords from Rockyou.txt added")
                break
        else:
            continue

        break
     else:
        rockyou_word = ""
        print("No matching word found in Rockyou.txt. Proceeding without it.")  
 


#Animation
animation = ["===>"    , " ===>   | ", "  ===>  | ", "   ===> | ", "    ===>| ", "     ===|>"]



#Generator code
print("Throwing the Spear...\n")
with open("SpearWordlist.txt", "w") as file:
    anim_index = 0
    word_count = 0
    for r in range(1, len(expanded_words)+1):
        for perm in itertools.permutations(expanded_words, r):
            combo = ''.join(perm)
            if mini <= len(combo) <= maxi- 1:
                file.write(combo + '\n')
            for char in Characters:
                for i in range(r+1):
                    combo_with_char = ''.join(perm[:i]) + char + ''.join(perm[i:])
                    if mini <= len(combo_with_char) <= maxi:
                        file.write(combo_with_char + '\n')
            if version == "1":
             for word in oneword1:
                 for i in range(r + 1):
                     combo_with_word = ''.join(perm[:i]) + word + ''.join(perm[i:])
                     if mini <= len(combo_with_word) <= maxi:
                         file.write(combo_with_word + '\n')
            word_count += 1 + len(Characters) * (r + 1) + len(oneword1) * (r + 1)
            if word_count % 1000 == 0:
                print(animation[anim_index % len(animation)], end='\r')
                anim_index += 1
                time.sleep(0.2)


if version == "1":
    with open("SpearWordlist.txt", "r") as file:
     withoutRockyou = file.read()


    with open("SpearwordlistWithRockyouWords.txt", "w") as file:
     file.write(rockyou_word + withoutRockyou)

  



# Finished file
file_path = os.path.abspath("SpearWordlist.txt")
print(f"\nYour Wordlist has been completed: {file_path}\n")

#windows file location
os.startfile(os.path.dirname(file_path))




input("\nPress Enter to exit...")
