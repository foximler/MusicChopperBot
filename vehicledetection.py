from PIL import Image
import mss
import mss.tools
import numpy as np
import cv2 as cv
import os
### 
import sys
 
# web library
import http.client
playing = 0
def send( message ):
 
    # your webhook URL
    webhookurl = "https://discordapp.com/api/webhooks/"
 
    # compile the form data (BOUNDARY can be anything)
    formdata = "------:::BOUNDARY:::\r\nContent-Disposition: form-data; name=\"content\"\r\n\r\n" + message + "\r\n------:::BOUNDARY:::--"
  
    # get the connection and make the request
    connection = http.client.HTTPSConnection("discordapp.com")
    connection.request("POST", webhookurl, formdata, {
        'content-type': "multipart/form-data; boundary=----:::BOUNDARY:::",
        'cache-control': "no-cache",
        })
  
    # get the response
    response = connection.getresponse()
    result = response.read()
  
    # return back to the calling function with the result
    return result.decode("utf-8")


while True:
	sct = mss.mss()
	# The screen part to capture
	monitor = {"top": 1250, "left": 1000, "width": 160, "height": 135}
	output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

	# Grab the data
	sct_img = np.array(sct.grab(monitor))
	#img = np.array(sct.grab(cords))
	#frame = Image.frombytes(sct_img)
	#frame = np.array(frame)

	img_gray = cv.cvtColor(sct_img, cv.COLOR_BGRA2GRAY)
	template = cv.imread('f.png',0)
	w, h = template.shape[::-1]
	res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
	threshold = 0.6
	loc = np.where( res >= threshold)

	if loc[0] != [] and playing == 0:
		send('!AMAK')
		print('starting music')
		playing = 1
	if loc[0] != [] and playing == 1:
		None

	else:
		if playing == 1:
			send(',leave')
			print('stopping music')
			playing = 0

	for pt in zip(*loc[::-1]):
		cv.rectangle(sct_img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

	cv.imshow('a crop of the screen',sct_img)
	if cv.waitKey(1) & 0xff == ord('q'):
		cv.destroyAllWindows()