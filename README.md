# Virtual-Paint
An openCV and Python project to paint in different colors virtually on webcam.

The VirtualPaint.py file contains the contour detection and drawing part by using the circles function of cv2.
To add more colors to the given project, you can run the colorDetection.py and then callibrate the hsv according to the color you want to add such that whole background is black and the required color is white in the mmask.
Then note down the hue, sat, val (min,max) and put into the myColors array in the VirtualPaint.py and add a color to draw in myColorValues corresponding to the color detected (i.e. same Index)
