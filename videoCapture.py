import cv2 # import opencv


cap = cv2.VideoCapture(0) # Starting capturing and specifying which camera to use
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Frame width
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Frame height

# # Saving the video
writer = cv2.VideoWriter('testvideo123.mpeg', # where to save the video and its name
                          cv2.VideoWriter_fourcc('M','P','E','G'), # Video code
                          cv2.CAP_PROP_FRAME_COUNT, # Frames number
                          (width,height))


while True:
    ret,frame = cap.read() # Read the frame
    cv2.imshow('frame', frame) # Displaying the frame
    writer.write(frame) # Write new frame
    
    # Exit when pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Stop capturing
