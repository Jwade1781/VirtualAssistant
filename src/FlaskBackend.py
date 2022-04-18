#######################################################################
#
# Purpose:
# Purpose of this file is to communicate the frontend with the backend
#
# Extra Info:
# Uses Celery to distribute the work between worker threads
#
# Run:
# --
#
#######################################################################
from flask import Flask
#from CeleryWorker import make_celery
#import celery as Celery

app = Flask(__name__)
#app.config["CELERY_BROKER_URL"] = "localhost//"
#app.config["CELERY_BACKEND"]
# The main entry point into the backend 
@app.route('/python_process')
def backendMain():
    #Will need to introduce a method to add workers and split the work async
    # Added SpeechTask for now to evaluate functionality
    return SpeechTask()


#@Celery.task()
def SpeechTask():
    import SpeechRecognition as SpeechRecognition
    SR = SpeechRecognition.SpeechRecognition(0)
    return SR.RunSpeechRecognition()
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)



        