import json
import yaml

def json2yaml(json_file, yaml_file):
    file = open(json_file, 'r')
    python_dict = json.load(file)
    yaml_string = yaml.dump(python_dict)
    print('The YAML file is:')
    print(yaml_string)
    file.close()
    fileOut = open(yaml_file, 'w')
    fileOut.write(yaml_string)
    fileOut.close()


def main():
    json_file = 'input.json'
    yaml_file = 'output.yaml'

    # Convert JSON to YAML
    json2yaml(json_file, yaml_file)


if __name__ == '__main__':
    main()