# Prediction Model JCMT



This aim of this python program is to make completion predictions for the Large Programs being observed at the JCMT. This program will need to:

1) gather information from the OMP database about the current status of each of the programs in each weather band and:

* prioritiy of each program
* time remaining / weather band 

2) gather information from the schedule - currently I have a "test" file stored as a file in: data/Band3_remaining_from_LAP_page_edited.ascii

3) gather information about the weathe status - as found in data/weather-average.csv

## Current Structure of the program

PredictionGenerator - using the jupyter notebook



## The future structure of the program

* predictionmodel.py : the fie that run's the program
* predictions/ : the module containing all the classes and modules for the program



### Considerations

##### Weather

How to split/allocated the weather for a night - i.e. random number generator for each "unit of time". What do we consider to be a "unit": 

* for simplicity I assume each night is only assigned one weather band
*  use schedule and weather stats

##### Transients

Transents is a cadence observation and so requires thinking about in a slightly different way - Ignore this for now (I will skim off the top for this program later)

**Overheads** 

pointing, focus, slew time, E&C,

- easiest might be to simpyl add on a percentage to every program observed i.e. 20% (I can ask Mark if we have a good number for this)

### Caveats of the Prediction Model

The model makes the following assumptions:

* All instruments are avaliable all of the time
* No data is obtained outside of a LAP observing block
* Gaps of time will be filled in by PI queu and we will not flex to a worse weatherband



