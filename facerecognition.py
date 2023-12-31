import face_recognition 
import cv2
import os
print(cv2.__version__)

Encodings=[]
name=[]
j=0

image_dir='/home/pjm/desktop/Pypro/faceRecognition/demoImh/known"
for root,dirs,files in os.walk(image_dir):
    print(files)
    for file in files:
        path=os.path.join(root,file)
        print(path)
        name=os.path.splitext(file)[0]
        print(name)
        person=face_recognition.load_image_file(path)
        encoding=face_recognition.face_encoding(person)[0]
        Name.append(name)
print(Name)

font=cv2.FONT_HERSHEY_SIMPLEX
image_dir='/home/pjm/desktop/Pypro/faceRecognition/demoImh/unknownknown"
for root,dirs, files in ox.walk(image_dir):
    for file in files:
        print(root)
        print(file)
        testImagePath=os.path.join(root,file)

        testImage=face_recognition.load_image_file(testimagePath)
        facePositions=face_recognition.face_location(testImage)
        allEncodings=face_recognition.face_encoding(testImage,facePositions)
        testImage=cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)
        
        for(top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
            name='Unknown Person'
            matches=face_recognition.compare_faces(Encoding,face_encoding)
            if True in matches:
               first_match_index=matches.index(true)
               name=Names[first_match_index]
            cv2.rectangle(testImage,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(testImage,name,(left,top-6),font,.75,(0,255,255),2)
        cv2.imshow('Picture',testImage)
        cv2.moveWindow('picture',0,0)
        if cv2.waitkey(0)==ord('q'):
           cv2.destroyAllWindows()