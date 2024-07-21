import speech_recognition as sr
def main():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("please say something")
        audio=r.listen(source)
        print("Recoginizing Now......")
        # recoginize using google
        try:
            print("you have said|n"+ r.recognize_google(audio))
            print("Audio recorded sucessfully \n")
        except Exception as e:
            print("Error: "+str(e))
        # write audio
        with open("recorded.wav","wb") as f:
            f.write(audio.get_wav_data())
if __name__ == "__main__":
    main()

        