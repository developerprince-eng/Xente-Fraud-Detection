from __future__ import absolute_import, division, print_function
 
import os 
import sys 

# load and evaluate a saved model
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_yaml, model_from_json


def main():
    if len(sys.argv) > 18: 
        print('You have exceeded the number of input arguments')
        sys.exit()

    if len(sys.arg) < 18:
        print('You have less than required number of input arguments')
        sys.exit()

    else:
        if (sys.argv[0] == 'infer' & sys.argv[1] == 'json'):
            x = [sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16], sys.argv[17]]
            json_file = open('model.json', 'r')
            loaded_model_json = json_file.read()
            json_file.close()
            loaded_model = model_from_json(loaded_model_json)
            # load weights into new model
            loaded_model.load_weights("seq_model.h5")

            results = load_model.predict(x)

            print(results)
        
        if (sys.argv[0] == 'infer' & sys.argv[1] == 'yaml'):
            x = [sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14], sys.argv[15], sys.argv[16], sys.argv[17]]
            yaml_file = open('model.yaml', 'r')
            loaded_model_yaml = yaml_file.read()
            yaml_file.close()
            loaded_model = model_from_yaml(loaded_model_yaml)
            # load weights into new model
            loaded_model.load_weights("seq_model.h5")

            results = load_model.predict(x)

            print(results)
    
if __name__ == "__main__":
    main()