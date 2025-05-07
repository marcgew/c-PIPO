from audio import audio_input, audio_output 
from llm import client
from display import face

from llm import client

def main():
    while True:  
        user_input = input("Sag etwas: ")
        if user_input.lower() == 'exit':  
            print("Beende das Programm...")
            break
        reply = client.send_to_llm(user_input)
        print("🤖 Antwort:", reply)

if __name__ == "__main__":
    main()