#Chatbot introduces itself and asks name of user
print("Hello, I am the Python Chatbot. What is you name?:")
name= input()

#Chatbot responds to name and asks user about mood
print("Nice to meet you", name, "How are you feeling today?:")
mood= input().lower()

#Chatbot gives fitting reply based on user's answer
if mood=="good":
    print("That's great! I am so glad that you are feeling okay.")
elif mood=="bad":
    print("Oh no! I am sorry to hear that.")
else:
    print("I understand it is hard to put your emotions into words.")

#Chatbot asks about user's favourite food based on options
print("What type of food do you enjoy?: Continental, Indian, or Food at home:")
food= input().lower()

#Chatbot relates with user based on answer
if food=="continental":
    print("I see that you are adventurous and willing to try something out of the box!")
elif food=="indian":
    print("I see you like to dare more inside the box but also testing out different cultures!")
elif food=="at home":
    print("I mean, food at home is best, especially when cooked with love!")
else:
    print("I am sure that is also very good food!") 

#Chatbot asks user on favourite season
print("Tell me your favourite season. I'm sure we can relate!:")
season= input().lower()

#Chatbot replies to favourite season
if season=="summer":
    print("Of course! Summer offers a fresh variety of fruits to eat and provide great weather for vacationing")
elif season=="rainy" // season=="fall" // season=="autumn":
    print("I see you enjoy the colourful and cool times of this season")
elif season=="spring":
    print("Of course! Spring is one of the most beautiful seasons of the year, with its colourful flowers and fragrant smells")
elif season=="winter":
    print("Sitting on a chair while sipping on some hot drink while watching snow fall down is one of the most calming senses in the world") 
else:
    print("I'm not quite sure if that is a real season...")   

#Chatbot asks about favourite colour
print("Tell me what your favourite colur is! Red, Blue, Green, or Yellow:")
colour= input().lower()

#Chatbot replies to favourite colour
if colour=="red":
    print("Red represents fiery instincts and angst, I'm sure you like it!")
elif colour=="blue":
    print("Although it represents sadness, it also represent a cool atmosphere and safety in some countries!")
elif colour=="yellow":
    print("This colour represent caution and happiness and is a sure favourite for some!")
elif colour=="green":
    print("The symbol of safety and nature, this colour is very cool!") 
else:
    print("That is also a very good colour too!") 

print("Tell me your favourite season. I'm sure we can relate!")
season= input().lower()

#Chatbot asks user about favourite icecream flavour
print("Tell me what your favourite icecream is! Chocolate, Strawberry, Vannila, or Mango:")
icecream= input().lower()

#Chatbot replies to favourite icecream flavour
if icecream=="chocolate":
    print("I mean, it's the general favourite for everyone, but still a good flavour nonetheless")
elif icecream=="strawberry":
    print("The most unconvential of the three but still a nice flavour")
elif icecream=="vannila":
    print("This flavour is the most classic of the three and an inexpensive favourite")
elif icecream=="mango":
    print("A new and fun flavour with creamy deliciousness, perfect for the summer time woes") 
else:
    print("That is also a very good ice cream flavour too!")

#Chatbot asks user about favourite hobby
print("What is you favourite hobby? I'm sure you like something! Drawing, Watching tv, Playing, Nothing")
hobby= input().lower()

#Chatbot replies to favourite hobby
if hobby=="drawing":
    print("I too sometimes like to draw and express my feelings")
elif hobby=="watching tv" // hobby=="tv":
    print("I don't think that counts as a hobyy and is the lazy answer to this question")
elif hobby=="playing":
    print("Going out to play is a great way to socialize and stay healthy at the same time")
elif hobby=="nothing":
    print("I'm sure you have something. You don't have to be shy") 
else:
    print("I like doing that too!")

#Chatbot says goodbye to user
print("We had such a fun time today, but I have to go now. I hope we can meet another time. See you soon!")
