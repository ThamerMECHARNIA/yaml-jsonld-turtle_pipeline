# yaml-jsonld-turtle_pipeline

## Requirments

- Python 3.7+
- Run `pip install -r requirements.txt` to install the requirements (`pyyaml` and `rdflib`)

## Steps to utilize pipeline actions

- Begin by forking the repository.
- Activate the Actions feature for the repository under the 'Action' tab
- Locally clone the project.
- Place the files that need conversion into their respective directories, such as 'json2yaml_data\input' to convert json file to yaml, 'jsonld2turtle_data\input' to convert jsonld to turtle, and so on.
- Commit and push the changes.
- The transformed files content will be accessible in the action's log, for example:
```
Run jsonld2turtle to convert all files in 'jsonld2turtle_data/input'

Run python3 json2yaml.py

The input file:  json2yaml_data/input/test1.jsonld  converted to:
 '@context':
  '@vocab': http://schema.org/
  countries: http://publication.europa.eu/resource/authority/country/
'@graph':
- '@id': countries:ITA
- '@id': http://people.example/Homer
  country:
    '@id': countries:ITA
  full_name: Homer Simpson
- '@id': http://people.example/Lisa
  country:
    '@id': countries:ITA
  full_name: Lisa Simpson
 
------------------------------
```