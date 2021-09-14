from imageai.Detection import ObjectDetection
import os

class Detection():
    def detect(image_name):
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = ""
        image_path = "media/"+image_name
        detected_url = "media/detected-"+image_name
        execution_path = os.getcwd()
        detector = ObjectDetection()
        detector.setModelTypeAsYOLOv3()
        detector.setModelPath( os.path.join(execution_path , "pretrained-yolov3.h5"))
        detector.loadModel()
        print("reached here so far")
        print(os.path.join(execution_path , image_path))
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_path), 
                output_image_path=os.path.join(execution_path , detected_url), input_type="file", output_type="file")
        return "/"+image_path, "/"+detected_url
# for eachObject in detections:
#     print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
