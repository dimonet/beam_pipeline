import apache_beam as beam

from utils.parameters import get_options
from utils.parameters import read_config_file
from utils.filename import generate_filename

from modules.extract import extract_data_from_api
from modules.transform import convert_json_to_dic
from modules.transform import get_wind_by_timepoint
from modules.transform import convert_json_to_str
from modules.load import load_data


def run(argv=None):

    options = get_options()
    config_file = options['config_file']
    config = read_config_file(config_file)

    file = "{path}{file_name}".format(path=config['load']['path'],
                                       file_name=generate_filename())


    with beam.Pipeline() as p:
        (
            p
                | 'Create' >> beam.Create(['Start'])
                | 'extract from api' >> beam.ParDo(extract_data_from_api(), config['extract'])
                | 'convert to dic' >> beam.ParDo(convert_json_to_dic())
                | 'get wind by timepoint' >> beam.ParDo(get_wind_by_timepoint(), config['transform'])
                | 'convert to str' >> beam.ParDo(convert_json_to_str())
                #| 'load' >> beam.io.WriteToText(file_path_prefix=file, file_name_suffix='.txt')
                | 'load' >> beam.ParDo(load_data(), config['load'])
        )

if __name__ == '__main__':
    run()