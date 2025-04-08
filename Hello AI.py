print("Hello, I am the Python Chatbot. What is you name?:")
name= input()
print("Nice to meet you", name, "How are you feeling today?:")
mood= input().lower()
if mood=="good":
    print("That's great! I am so glad that you are feeling okay.")
elif mood=="bad":
    print("Oh no! I am sorry to hear that.")
else:
    print("I understand it is hard to put your emotions into words.")    