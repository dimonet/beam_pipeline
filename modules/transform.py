import apache_beam as beam
import json

class convert_json_to_dic(beam.DoFn):
    def process(self, element):
        #Converts line into dictionary
        res = json.loads(element)
        return [res]

class get_wind_by_timepoint(beam.DoFn):
    def process(self, element, config):
        # read configurations
        timepoint_id = config['timepoint_id']

        # extract timepoints from json, get only requested timepoint and read its wind data
        timepoints = element['dataseries']      # get only timepoint data
        for timepoint in timepoints:
            if timepoint['timepoint'] == timepoint_id:
                #res = json.dumps(timepoint['wind10m'], indent=4)
                res = timepoint['wind10m']      # get wind data for a requested timepoint
        return [res]

class convert_json_to_str(beam.DoFn):
    def process(self, element):
        # Converts json into dictionary
        res = json.dumps(element, indent=4)
        return [res]
