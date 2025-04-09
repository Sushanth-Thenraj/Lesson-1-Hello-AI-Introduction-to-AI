#Import required functions
import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

p_m= 0
ne_m=0
n_m=0

#Welcome user
print(f"{Fore.CYAN}Welcome to the Sentiment Spy system!🕵️‍♂️{Style.RESET_ALL}")

history= []

#Ask users name and introduce them to topic
name= input(f"{Fore.CYAN}May I have your name? {Style.RESET_ALL}")
print(f"{Fore.CYAN}❓Hello agent ", name, f", today you will submit a sentence of your choice and I will derive the sentiment out of it.❓{Style.RESET_ALL}")

#Take sentence from user and check for possibilities
while True:
    sentence= input(f"{Fore.CYAN}Enter a sentence of you choice. Write {Fore.YELLOW}reset {Fore.CYAN}to delete history {Fore.RED}or {Fore.YELLOW}exit {Fore.CYAN}to stop program. You can also say {Fore.YELLOW}history {Fore.CYAN}to view chat log. {Style.RESET_ALL}").strip()
    #Check if user says "exit"
    if sentence.lower()== "exit":
        #Say goodbye
        print(f"\n{Fore.CYAN} Exiting Sentiment Spy. Farwell, Agent {name}👋!{Style.RESET_ALL}")
        #Print summary
        print(f"{Fore.GREEN} Mission Report📜:"
              f"\n{Fore.GREEN} Positive Messages: {p_m}"
              f"\n{Fore.GREEN} Negative Messages: {ne_m}"
              f"\n{Fore.GREEN} Neutral Messages: {n_m}{Style.RESET_ALL}")
        break
    #Check if user says "reset"
    elif sentence.lower()== "reset":
        #Reset history
        history.clear()
        print(f"{Fore.CYAN} 🎉All conversation history cleared!🎉{Style.RESET_ALL}")
        continue
    #Check if user says "history"
    elif sentence.lower()== "history":
        #If history not there, state there is no history
        if not history:
            print(f"{Fore.YELLOW} No conversation history yet.{Style.RESET_ALL}")
        #Print history if there
        else:
            print(f"{Fore.CYAN} 📜Conversation History📜:{Style.RESET_ALL}")
            for idx,(text,polarity,sentiment) in enumerate(history, start=1):
                if sentiment=="Positive":
                    color= Fore.GREEN
                    emoji="😄"
                elif sentiment=="Negative":
                    color= Fore.RED
                    emoji="😢"
                else:
                    color= Fore.YELLOW
                    emoji="😐"
                print(f"{idx}. {color}{emoji}{text}"
                       f"(Polarity: {polarity:.2f}, {sentiment}){Style.RESET_ALL}")
        continue 

    #Determine polarity value and check user sentence
    polarity= TextBlob(sentence).sentiment.polarity 
    if polarity>0.25:
        sentiment="Positive"
        color= Fore.GREEN
        emoji="😄"
        p_m=p_m+1
    elif polarity<-0.25:
        sentiment="Negative"
        color= Fore.RED
        emoji="😢"
        ne_m=ne_m+1                
    else:
        sentiment="Neutral"
        color= Fore.YELLOW
        emoji="😐"
        n_m=n_m+1
    
    #Add to history
    history.append((sentence,polarity,sentiment))

    #Print sentiment
    print(f"{color}{emoji}{sentiment} sentiment detected!👨‍💻"
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")