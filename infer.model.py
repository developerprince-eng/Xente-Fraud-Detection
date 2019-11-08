from __future__ import absolute_import, division, print_function

# load and evaluate a saved model
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_yaml, model_from_json

def main(x):
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model_1 = model_from_json(loaded_model_json)
    # load weights into new model


    # load YAML and create model
    yaml_file = open('model.yaml', 'r')
    loaded_model_yaml = yaml_file.read()
    yaml_file.close()
    loaded_model_2 = model_from_yaml(loaded_model_yaml)


    # load weights into new model
    loaded_model_1.load_weights("model.h5") #json
    # loaded_model_2.load_weights("model.h5") #yaml
    print("Loaded model from disk")


    results = load_model.predict(x)

    print(results)

if __name__ == "__main__":
    main()