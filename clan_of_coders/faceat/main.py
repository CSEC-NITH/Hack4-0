
import pickle
import os
import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display
from absl import app
from absl import flags

FLAGS = flags.FLAGS
flags.DEFINE_string("image", None, "Test Image")
flags.DEFINE_string("mode",None,"operation Mode: final or init_enc_calc")

def init_calc_enc():
    known_face_encodings=[]
    known_face_names=[]
    path1="temp/"
    listing=os.listdir(path1)
    for file in listing:
        im=face_recognition.load_image_file(path1+file)
        im_encoding=face_recognition.face_encodings(im)[0]
        known_face_encodings.append([im_encoding,file])
    pickle.dump(known_face_encodings,open("known_encoding","wb"))
    print("Encoding of Images done Successfully")



def final_foo():
    unknown_image = face_recognition.load_image_file(FLAGS.image)
    face_enc = face_recognition.face_encodings(unknown_image)[0]
    known_face_encodings=pickle.load(open("known_encoding","rb"))


    identified=[]
    # In[5]:
    for our_enc in known_face_encodings:
        if(face_recognition.compare_faces([our_enc[0]],face_enc)==[True]):
            identified.append([True,our_enc[1]])
            break
        else:
            pass
    if(len(identified)>0):
        return(identified[0][1])
    else:
        return("Match Not Found, Please Try Again!!")


def main(_argv):
    if(FLAGS.mode=="final"):
        print(final_foo())
    elif(FLAGS.mode=="init_enc_calc"):
        init_calc_enc()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass