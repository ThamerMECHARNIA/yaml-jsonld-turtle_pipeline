import json
import yaml

def yaml2json(yaml_file, json_file):

    with open(yaml_file, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main():
    json_file = "yaml2json_data/output.jsonld"
    yaml_file = "yaml2json_data/input.yaml"

    # Convert JSON to YAML
    yaml2json(yaml_file, json_file)


if __name__ == '__main__':
    main()