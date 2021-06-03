import web 
import RPi.GPIO as GPIO 

GPIO.setmode(GPIO.BCM)
LedSeq = [4,17,22,10,9,11] 
GPIO.setup(LedSeq, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
status = [0]
render = web.template.render('/home/pi/WebLedController/')
urls = ('/','index')

def gpio_state():    
    LedBuzzerState = [4,17,22,10,9,11,8]
    stateofgpio = [GPIO.input(x) for x in LedBuzzerState]
    print(type(stateofgpio))
    return stateofgpio

class index:
    
    def __init__(self):
        self.hello = "Hello World!"

    def GET(self):
        returnLED = []
        OnOffStatus = 'Off'
        gpiostate = gpio_state()
        LedT = {1:4, 2:17, 3:22, 4:10, 5:9, 6:11, 7:8}
        getInput = web.input(turn="")
        command = getInput.turn
    
        try:
            commandint = (int(str(command)))
            GpioNumber = LedT.pop(commandint)
             
            if status[0] == 0:
                status[0] = 1
                GPIO.output(GpioNumber, GPIO.HIGH)
                returnLED = commandint
                OnOffStatus = 'On'                
                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
            
            elif status[0] == 1:
                status[0] = 0
                GPIO.output(GpioNumber, GPIO.LOW)               
                returnLED = commandint
                OnOffStatus = 'Off'               
                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)

            else:
                print ('Error')
                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
            
        except ValueError:
            pass
        
        return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
                          
if __name__ == "__main__":
        app = web.application(urls,globals())
        app.run()
        
        
        



            
            
