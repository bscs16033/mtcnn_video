#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2019 Iván de Paz Centeno
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import cv2
from mtcnn import MTCNN

detector = MTCNN()

videopath = "/content/drive/My Drive/Colab Notebooks/datasets/0-Personally Collected/videos/lawyer.avi"

cap = cv2.VideoCapture(videopath)

out = cv2.VideoWriter('/content/drive/My Drive/Colab Notebooks/mtcnn/mtcnn_video/mtcnn/output/lawyer_output.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 30, (1280,720))

while cap.isOpened(): 
    #Capture frame-by-frame
    #print('entered')
    ret, frame = cap.read()
    #print('entered2')
    #Use MTCNN to detect faces
    
    

    if ret==True:
        result = detector.detect_faces(frame)
        if result != []:
            for person in result:
                bounding_box = person['box']
                keypoints = person['keypoints']
        
                cv2.rectangle(frame,
                              (bounding_box[0], bounding_box[1]),
                              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                              (0,155,255),
                              2)
        
                cv2.circle(frame,(keypoints['left_eye']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['right_eye']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['nose']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['mouth_left']), 2, (0,155,255), 2)
                cv2.circle(frame,(keypoints['mouth_right']), 2, (0,155,255), 2)
        #display resulting frame
        
        # write the flipped frame
        print('hello')
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

print('video writing successful')

#When everything's done, release capture
cap.release()
out.release()
