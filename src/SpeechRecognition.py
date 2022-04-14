#######################################################################
#
# Purpose:
# The purpose of this program is to serve as the speech recognition for the assistant
#
# Extra Info:
# Currently, this uses 3rd party recognizers. Will want to extend this later to include
# a custom script option if able to find a sufficient dataset and model.
#
# Required Modules:
# SpeechRecognition
# pocketsphinx
# PyAudio
# Run:
# --
#
#######################################################################

class SpeechRecognition:
    def __init__(self, moduleNumber: int):
        def GoogleRecognizer(sr, audio):
            print("Using Google recognizer")
            return sr.Recognizer().recognize_google(audio)
        
        def SphinxRecognizer(sr, audio):
            print("Using Sphinx Recognizer")
            return sr.Recognizer().recognize_sphinx(audio)
        
        self.SetRecognizerModule(moduleNumber)
        self.recognizers = {    
                                0 : GoogleRecognizer,
                                1 : SphinxRecognizer
                            }
        
    def GetTotalRecognizers(self):
        return len(self.recognizers) 
        
    def SetRecognizerModule(self, moduleNumber: int):
        self.moduleNumber = moduleNumber
        
    def RunSpeechRecognition(self):
        import speech_recognition as sr 
        
        with sr.Microphone() as source:
            sr.Recognizer().adjust_for_ambient_noise(source)
            print("Speech Recognition Listening")                                                                                   
            audio = sr.Recognizer().listen(source)   

        try:
            print("You said " + self.recognizers[self.moduleNumber](sr, audio))
            
        except sr.UnknownValueError:
            print("Not able to Translate Audio")
            
        except sr.RequestError as e:
            print("Speech Recognition Exception; {0}".format(e))
    
    
        