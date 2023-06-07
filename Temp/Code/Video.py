# Read & Save a video.
import cv2
import numpy as np

# Read 

video = cv2.VideoCapture("Video/Sample-1.mp4")

if (video.isOpened() == False): 
  print("Unable to read video file.")

frame_width = int(video.get(3))
frame_height = int(video.get(4))

out = cv2.VideoWriter("Video/Sample-2.mp4",cv2.VideoWriter_fourcc('M','J','P','G'), 60, (frame_width,frame_height))

while(True):
  ret, frame = video.read()
  if ret == True: 
    out.write(frame)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break 

video.release()
out.release()

cv2.destroyAllWindows()
