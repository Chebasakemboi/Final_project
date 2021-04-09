import keras

from PIL import Image

from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

def getPrediction(filename):

    model =  model = keras.models.load_model("trained.h5")
    image = Image.open('uploads/'+filename)
    image=image.resize((224, 224))
    image = img_to_array(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
   
    image = preprocess_input(image)
    yhat = model.predict(image)
    label=yhat[0]
 
    return label