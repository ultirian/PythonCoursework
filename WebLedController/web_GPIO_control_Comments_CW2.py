# Import required libaries
import web

#import RPi.GPIO as GPIO 
import RPISim as GPIO
# Set GPIO pin modes.
GPIO.setmode(GPIO.BCM)

# Led GPIO LIST FOR GPIO SETUP.
LedSeq = [4,17,22,10,9,11]

# Gpio LED Setup LedSeq initialises all GPIO pins out.
GPIO.setup(LedSeq, GPIO.OUT)

# Buzzer on GPIO8
GPIO.setup(8, GPIO.OUT)
        

# set status vairble and initally set it to 0 for off
status = [0]

# For return values.
render = web.template.render('/home/pi/WebLedController/')
urls = ('/','index')

# Function to output current GPIO state.

def gpio_state():
    
    # Defines GPIO pins so that the for loop iterates over all set GPIO pins.
    LedBuzzerState = [4,17,22,10,9,11,8]
    
    #reads GPIO.input for on/off state of GPIO pins and outputs it as 0 or 1's
    
    stateofgpio = [GPIO.input(x) for x in LedBuzzerState]
    
    #checking var for type
    print(type(stateofgpio))
    
    #return list of GPIO states
    return stateofgpio

# Create a template for the objects of index.
class index:
    
    # Is the constructor that Initialises the atrributes of the class and Web.py
    def __init__(self):
        self.hello = "Hello World!"

    
    # GET function call.
    def GET(self):
        
        # Inital values and empty lists.
        returnLED = []
        OnOffStatus = 'Off'
        
        #calls function GpioState() to fill local varible with GPIO state list.
        gpiostate = gpio_state()
        
        # Dictonary to be used to convert turn numbers into GPIO output number.
        LedT = {1:4, 2:17, 3:22, 4:10, 5:9, 6:11, 7:8}
        
        #reads GET request from web.py for the string after turn= assigns to getInput
        getInput = web.input(turn="")
        
        # Debugging
        print(f" GetInput IS: {getInput}")
        command = getInput.turn
    
        # Redundency for initall loop.
        try:
            # Convert command to int from string
            commandint = (int(str(command)))
            # Fetch LedT Dictonary value, uses commandint as key and stores value to be used for dynamic GPIO number.
            GpioNumber = LedT.pop(commandint)
            
            # Checks status 
            if status[0] == 0:
                # Toggle LED or Buzzer on
                status[0] = 1
                GPIO.output(GpioNumber, GPIO.HIGH)
                
                # Sets commandint as different varible for return
                returnLED = commandint
                
                # Sets OnOffStatus ON for return.
                OnOffStatus = 'On'
                
                # As output of gpio state, returns gpio state to index as positional arguiments (*args) index 0-6 to be called by
                # $def with (LED1, LED2, LED3, LED4, LED5, LED6, Buzzer1, status, returnLED, OnOffStatus)
                # and converting 0/1 values to Off/on with a if else and for loop.
                
                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
            
            # Actions to exicute if LED ON and STATUS = 1 turns off current LED
            elif status[0] == 1:
                status[0] = 0
                GPIO.output(GpioNumber, GPIO.LOW)
                
                returnLED = commandint
                OnOffStatus = 'Off'
                
                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
            #Error redundency
            else:
                print ('Error')

                return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)
        #bypasses inital empty value in varible command / commandint / Gpio Number.    
        except ValueError:
            pass
        
        #default
        #has to start by visiting /?turn=on 
        return render.index(*['Off' if x == 0 else 'On' for x in gpiostate], status, returnLED, OnOffStatus)

                          
if __name__ == "__main__":
        app = web.application(urls,globals())
        app.run()
        
        
        



            
            