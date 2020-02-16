import json

import falcon
from gpiozero import LED


class PiApiHandler():

    def __init__(self):
        # initialize LED on pin 18
        self.led = LED(18)

    def __del__(self):
        pass

    def on_patch(self, req, resp):
        patch_body = req.media
        if patch_body['on'] == True:
            print("turning PI light ON")

            # activate LED
            self.led.on()

            resp.body = json.dumps({
                "status": "success", 
                "on": True
            })
        elif patch_body['on'] == False:
            print("turning PI light OFF")

            # deactivate LED
            self.led.off()

            resp.body = json.dumps({
                "status": "success", 
                "on": False
            })

# Resources are represented by long-lived class instances
pi_api = PiApiHandler()
# falcon.API instances are callable WSGI apps
app = falcon.API()
# things will handle all requests to the '/things' URL path
app.add_route('/lights/1', pi_api)
