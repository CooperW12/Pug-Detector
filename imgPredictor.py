from ultralytics import YOLO


model = YOLO(r"runs\detect\train48\weights\best.pt") #load my model from best weights 
results = model.predict(['UnseenPugs/upug01.jpg','UnseenPugs/upug02.jpg','UnseenPugs/upug03.jpg'], conf=.2, iou=.3)

#process results list
for result in results:
    result.show()  # display to screen
    
    