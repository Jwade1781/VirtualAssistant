#######################################################################
#
# Purpose:
# Purpose of this file is to test the general functionality of the Speech Recognition
#
# Extra Info:
# --
#
#
# Run:
# --
#
#######################################################################
def main():
    import sys
    sys.path.append('../src') # Quick and dirty way to import, testing just functionality
    
    
    import SpeechRecognition as SpeechRecognition
    speech = SpeechRecognition.SpeechRecognition(0)

    # Iterate through all of the recognizers to test individually
    for recognizer in range(speech.GetTotalRecognizers()):
        speech.SetRecognizerModule(recognizer)
        speech.RunSpeechRecognition()
    return
    
    
main()
