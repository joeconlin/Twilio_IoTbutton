# Twilio IoT Button

This is a python lambda script that will respond to the push of an IoT button to call you via Twilio voice.
Conceptually, you could use this similar to a "silent alarm" where your IoT button is mounted under your desk and if you're looking to get out of a tough conversation, tap the button and take that important call!

* Deploy this as a python 3 lambda function

* set the Twilio Environment variables based on your Twilio API credentials

* configure the "to" and "from" numbers in this python script

* If you want to tweak the message, replace the "url" link with the TwiML file of your choice

 * Note, if using an S3 bucket, make sure you set your CORS policy to allow the GET method

* Load up your IoT button in your phone app and follow the instructions to register

* select this lambda function

* Launch and go!

