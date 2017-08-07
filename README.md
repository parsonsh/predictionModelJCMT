# Prediction Model JCMT



This aim of this python program is to make completion predictions for the Large Programs being observed at the JCMT. This program will need to:

1) gather information from the OMP database about the current status of each of the programs in each weather band and:

* prioritiy of each program
* time remaining / weather band 
* ​

2) gather information from the schedule - **due to be** stored as a file in: data/

3) gather information about the weathe status - as found in data/weather-average.csv



## The structure of the program

* predictionmodel.py : the fie that run's the program
* predictions/ : the module containing all the classes and modules for the program



### Considerations

##### Weather

How to split/allocated the weather for a night - i.e. random number generator for each "unit of time". What do we consider to be a "unit": 

* 1-3 hors?
* \# nights in an observing block?

This unit will need references the weather statistics table

ANSWER: I think that this nees to be on a ~hourly block provided we grab the statistics from a distribution. not all sources are available all the time. It becomes easy then to allocate time for calibrations/overhead - i.e. of the hour in time => 12 mins of E&C (20% of the time) => x minutes for slewing/cals/pointings.

QUESTION: can I define a distribution for each month where I could then grab from - i.e rather than normal distribution or gaussian have a specific wvm distribution that is time (aka month) dependent?

##### Transients

Transents is a cadence observation and so requires thinking about in a slightly different way - I might ignore this for now.



### Caveats of the Prediction Model

The model makes the following assumptions:

* All instruments are avaliable all of the time
* No data is obtained outside f an observing block



