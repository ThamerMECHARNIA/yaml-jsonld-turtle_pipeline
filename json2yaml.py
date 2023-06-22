import json
import yaml

def json2yaml(json_file, yaml_file):

    # Read json
    file = open(json_file, 'r')
    json_data = json.load(file)

    # convert to yaml
    yaml_string = yaml.dump(json_data)
    print('The YAML file is:')
    print(yaml_string)
    file.close()

    # Write yaml
    fileOut = open(yaml_file, 'w')
    fileOut.write(yaml_string)
    fileOut.close()


def main():
    json_file = "json2yaml_data/input.jsonld"
    yaml_file = "json2yaml_data/output.yaml"

    # Convert JSON to YAML
    json2yaml(json_file, yaml_file)


if __name__ == '__main__':
    main()