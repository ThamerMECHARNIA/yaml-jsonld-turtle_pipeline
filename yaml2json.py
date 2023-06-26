import json
import os

import yaml

def yaml2json(yaml_file, json_file):

    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        yaml_file.close()

    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        json_file.close()

        return data


def main():
    input_path = 'yaml2json_data/input/'
    output_path = 'yaml2json_data/output/'

    # get a list of all files in the input dir 'yaml2json_data/input'
    files = os.listdir(input_path)

    for file in files:
        input_file = input_path + file
        output_file = output_path + file[:file.find('.')] + '.jsonld'

        # Convert JSON to YAML
        json_data = yaml2json(input_file, output_file)
        print('The input file: ', input_file, ' converted to:\n', json_data, '\n------------------------------')



    # json_file = "yaml2json_data/output.jsonld"
    # yaml_file = "yaml2json_data/input.yaml"
    #
    # # Convert JSON to YAML
    # yaml2json(yaml_file, json_file)


if __name__ == '__main__':
    main()