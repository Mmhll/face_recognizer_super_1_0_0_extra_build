Super face detector.

This application can recognize the human face in photo.

For using photo, you need to put full path of image into console. Then, by using neural network, this application find human faces in photo and insert it coordinates in console.
Finally, it saves the photo of last face into your computer and show it.
 
Developed and tested on Manjaro Linux KDE 5.25.5


This app using libraries: datetime for saving images by actual datetime, cv2 for open photos, face_recognition and PIL for photo picking and face recognize of your photo.

The application in action:


1. Putting image url
![1](https://user-images.githubusercontent.com/71172539/194830971-bc90efb8-cad5-4a6a-8b78-bdda9fedb876.png)

2. Recognizing photo, show coordinates of face, show face
![2](https://user-images.githubusercontent.com/71172539/194830979-47afd8a1-4c0b-47b5-ac4e-8241bd4b1f99.png)
