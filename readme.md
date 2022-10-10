Super face detector.

This application can recognize the human face in photo.

For using photo, you need to put full path of image into console. Then, by using neural network, this application find human faces in photo and insert it coordinates in console.
Finally, it saves the photo of last face into your computer and show it.
 
Developed and tested on Manjaro Linux KDE 5.25.5


This app using libraries: datetime for saving images by actual datetime, cv2 for open photos, face_recognition and PIL for photo picking and face recognize of your photo.

The application in action:



1. Putting image url
![](../../Изображения/1.png)
2. Recognizing photo, show coordinates of face, show face
![](../../Изображения/2.png)