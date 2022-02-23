import os
import sys
import apache_beam as beam
from utils.filename import generate_filename

class load_data(beam.DoFn):
    def process(self, element, config):
        # read configurations
        path = config['path']

        file_name = f'{generate_filename()}.txt'
        file = os.path.join(path, file_name)
        try:

            with open(file, "w") as f:
                f.write(element)
                f.close()
        except:
            print("cannot write data into file")
            sys.exit(1)
