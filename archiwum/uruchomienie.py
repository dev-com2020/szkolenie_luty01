import pywhatkit
import pyttsx3

if __name__ == "__main__":
    # pywhatkit.text_to_handwriting("Tomasz Kaniecki")
    silnik = pyttsx3.init()
    silnik.say('Witam, tutaj bot Anita, chcę sprzedać Ci panele słoneczne')
    silnik.runAndWait()
