import requests
import apache_beam as beam

class extract_data_from_api(beam.DoFn):
    def process(self, element, config):
        # read configurations
        rest_url = config['rest_url']
        lon = config['lon']
        lat = config['lat']
        product = config['product']

        # request data from rest api by url based on parameters
        url = f'{rest_url}?lon={lon}&lat={lat}&product={product}&output=json'
        res = requests.get(url).text
        return [res]
