from tkinter import *
import speech_recognition as sr
import webbrowser
from PIL import ImageTk, Image
from speak import speakclass


def search_web(input):
    webbrowser.open(f"https://www.google.com/search?q={input}")


def recognize_speech():
    speakclass.speakmethod("What can i search for you ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            speakclass.speakmethod("hold on I'm getting the results")
            text = r.recognize_google(audio)
            search_web(text)
        except sr.UnknownValueError:
            speakclass.speakmethod(
                "Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            label.config(text=f"Error making request: {e}", fg="#ff0000")


def main():
    global label

    # Create main window
    window = Tk()
    window.title("Speech Recognition")
    window.geometry("400x100")

    # Create label and button widgets
    label = Label(text="Listening for input...", font=("Helvetica", 16))
    label.pack(pady=10)

    photo = ImageTk.PhotoImage(Image.open("voice1.png"))

    playbutton = Button(window, font=(
        "Helvetica", 16), image=photo, command=recognize_speech)
    playbutton.pack()
    window.mainloop()


if __name__ == '__main__':
    main()
