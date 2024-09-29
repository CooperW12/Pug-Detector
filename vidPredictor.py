import cv2
from ultralytics import YOLO

model = YOLO(r"runs\detect\train48\weights\best.pt") #load my model from the best weights

video_path = r"UnseenPugs\uvid03.mov"
cap = cv2.VideoCapture(video_path)

#frame by frame detection
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame,conf=.2,iou=.1)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        smallerFrame = cv2.resize(annotated_frame,(720,1000))
        cv2.imshow("YOLOv8 Inference", smallerFrame)
        
        cv2.resizeWindow("YOLOv8 Inference",720, 1000)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()