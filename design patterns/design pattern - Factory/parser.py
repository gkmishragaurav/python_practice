import json
import xml.etree.ElementTree as etree

class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data

class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree

def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)

def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = dataextraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj

def main():
    json_factory = extract_data_from('movie.json')
    json_data = json_factory.parsed_data
    print('Found:', {len(json_data)} )
    for movie in json_data:
        print("Title: ", movie['title'])
        year = movie['year']
        if year:
            print("Year: ", year)
        director = movie['director']
        if director:
            print("Director: ", director)
        genre = movie['genre']
        if genre:
            print("Genre: ", genre)

    xml_factory = extract_data_from('abc.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//person[lastName='Liar']")
    print('found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print('first name: ', firstname)
        lastname = liar.find('lastName').text
        print('last name: ', lastname)



main()