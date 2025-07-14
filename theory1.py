import shutil

class Theory_one(): #Father class
    def __init__(cheat,frequent_messages,current_messages):
        cheat.frequent_messages=int(frequent_messages)
        cheat.current_messages=int(current_messages)


class Theory_two(Theory_one): #Mother class
    def __init__(cheat,frequent_messages,current_messages,cfollowing_list,ofollowing_list):
        super().__init__(int(frequent_messages),int(current_messages))
        cheat.cfollowing_list=int(cfollowing_list)
        cheat.ofollowing_list=int(ofollowing_list)


class Theory_three(Theory_two): #Oldest sibling
    def __init__(cheat, frequent_messages, current_messages, cfollowing_list, ofollowing_list,cmeet_freq,omeet_freq):
        super().__init__(int(frequent_messages), int(current_messages), int(cfollowing_list), int(ofollowing_list))
        cheat.cmeet_freq=int(cmeet_freq)
        cheat.omeet_freq=int(omeet_freq)


    def model(cheat):
        count=0
        if cheat.current_messages<cheat.frequent_messages:
            count+=1
        elif cheat.cfollowing_list>cheat.ofollowing_list:
            count+=1
        elif cheat.cmeet_freq<cheat.ofollowing_list:
            count+=1
        
        if count>2:
            print("\nHe might be cheating on you, but give him a chance.")
        elif count>1:
            print("\nMaybe he might be cheating, 'if you're guessing his cheating'")
        elif count>0:
            print("\nYou're safe for... now")

def main():
    size=shutil.get_terminal_size().columns
    print("Only insert numbers like 1-9per day or 1-1000per day")

    fm=input("\n\nHow often did he/she message you in the past per day: ")
    cm=input("How often does he or she message you nowadays: ")
    if fm>cm:
        print("\nChatbot:\nfind GOD my friend\n".rjust(size))
    else:
        print("\nChatbot:\nAlright, You might just still be safe\n".rjust(size))

    cf=input("What is his/her current following count: ")
    of=input("What was their old following count an estimate: ")
    if cf>of:
        print("\nChatbot:\nSee what youve become checking follwer list\n".rjust(size))
    else:
        print("\nChatbot:\nYou might just still be safe\n".rjust(size))

    cm=input("how fequent is she/he meeting up with you now per week: ")
    om=input("how frequent did he/she use to meet up with you per week: ") 
    if cm>om:
        print("\nChatbot:\nSTAND UP this is not you\n".rjust(size))
    else:
        print("\nChatbot:\n...\n")

    questions=Theory_three(fm,cm, cf, of, cm, om,
                          )
    questions.model()
    print("\nHelping others is our mission".center(size))
    
    

if __name__=="__main__":
    main()