Pipeline for wind information loading from REST API http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json
by timepoint_id (entered as a parameter in conf.json file).
The result is loaded into folder  "output" into txt files as a json
The project has the next folder and files:
  - \pipeline.py: main file of the pipeline, enter point
  - \config\: there are config files, can be created for each env. (dev, qa, prod)
  - \modules\: extracting, loading and transforming implementing
  - \output\: folder with resulted txt files
  - \utils\: aditional functions for pipeline (config parsing etc)

The pipeline running example:
    "python pipeline.py --config_file  conf.json"
or  "python pipeline.py" (conf.json is default parameter for this pipeline)
