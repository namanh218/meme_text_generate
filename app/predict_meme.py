import numpy as np
import os
import tensorflow as tf  
import json   
from tensorflow_core.python.keras.api._v2.keras.models import load_model
from tensorflow_core.python.keras.api._v2.keras.preprocessing.sequence import pad_sequences


model_meme = load_model('./models/model_final_2.h5')
print('e')
params = json.load(open('./params.json'))
labels_index = params['labels_index']
int_to_char = {v: k for k, v in labels_index.items()}
SEQUENCE_LENGTH = params['sequence_length']

def char_to_num(text):
    char = []
    for i in text:
        char.append(labels_index[i])
    return char

def predict_meme(text):
    res = text.lower()
    for i in range(300):
        temp = char_to_num(res)
        data = pad_sequences([temp], maxlen=SEQUENCE_LENGTH)[0]
        data = np.expand_dims(data, axis=0)
        y = model_meme.predict(data)
        y = np.argmax(y)
        key = int_to_char[y]
        if key == '>':
            break
        res += key
    print(res)    
    return res





