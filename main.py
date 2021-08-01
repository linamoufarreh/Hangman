def update(word, guess, state):
    if guess in word:
        for i in range(0, len(word)):
            if guess==word[i]:
                state[i]= guess
        return True
    return False

def main(word):
    string_lines=""
    count=0
    
    for k in range(0,len(word)):
        string_lines= string_lines + " _"
    print(string_lines)
    string_to_list= string_lines.split(" ")
    current_state= string_to_list[1:len(word)+1]

    while True:
        letter= input("Guess a letter:")

        if len(letter)>1:
            print("Enter only 1 letter")
            
        elif len(letter)==1:
            update(word, letter, current_state)
            if update(word, letter, current_state)== True:
                print(" ".join(current_state))
                if "_" not in current_state:
                    print("You solved it!")
                    break
            else:
                count= count+1
                print("Incorrect! Number of tries:", count)
                print(current_state)
                if count>5 or count==5:
                    print("Sorry you did not win")
                    break
                
            
main("python")
