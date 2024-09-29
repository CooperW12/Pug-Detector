
Pugs2.0 - v2 2024-09-25 9:18pm
==============================

This dataset was exported via roboflow.com on September 25, 2024 at 9:18 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 263 images.
Pugs are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -15 and +15 degrees
* Random shear of between -13° to +13° horizontally and -13° to +13° vertically
* Random brigthness adjustment of between -20 and +20 percent
* Random exposure adjustment of between -14 and +14 percent
* Salt and pepper noise was applied to 1.96 percent of pixels


