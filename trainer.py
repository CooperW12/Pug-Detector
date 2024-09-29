from ultralytics import YOLO

model = YOLO("yolov8n.yaml").load(r'runs\detect\train48\weights\best.pt') #create model and load with previous runs weights to improve
model.train(data="data.yaml", epochs=5, imgsz=640) #train
results = model.predict(['pugs/pug03.jpg'], conf=.5) #test on image

#showing and saving stuff (works for list of predictions too)
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk