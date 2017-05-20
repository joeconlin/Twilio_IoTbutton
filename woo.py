import base64
import json
import os
import urllib
from urllib import request, parse

# Put the number of the person who will be called when you hit the button
TO_NUMBER = '+1xxxxxxxxxx'
# Put your Twilio from number here
FROM_NUMBER = '+1yyyyyyyyyy'

TWILIO_VOICE_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Calls.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


def lambda_handler(event, context):
    to_number = TO_NUMBER
    from_number = FROM_NUMBER
    # Feel free to use your own TwiML here
    url = 'https://s3.amazonaws.com/iotbuttoncaller/woo.xml'

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not url:
        return "The function needs a 'Url' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_VOICE_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Url": url, "Method": "Get"}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    return "Call sent successfully!"
