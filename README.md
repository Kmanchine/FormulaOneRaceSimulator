# Formula One Race Simulator

Simulate a Formula One Grand Prix using data from a race weekend's practice session, qualifying, and drivers' overall career statistics.

## Description

Inspired by [F1Metric's Race Simulator (2014)](https://f1metrics.wordpress.com/2014/10/03/building-a-race-simulator/), this project aims to recreate a modern version of F1Metric's simulator
by feeding up-to-date information and historic data, and improve scalability using [FastF1](https://theoehrly.github.io/Fast-F1/) Python Package as main source of data.

## Features
- Free Practice Analysis: dive into Free Practice 2 to analyse how drivers prepare for Sunday's Grand Prix by analysing long runs and lap times.
- Qualifying Battle: After each Qualifying session, the session is analysed through teammate head-to-head comparison and drivers' one-lap pace.
- Strategy Predictions: Predict each driver's optimal race strategy based on their Free Practice and Qualifying performance. 
- Up-to-date information supplied by FastF1 Python Package
- And more!


### Upcoming Features
- Simulate a one-car race and a complete Grand Prix with overtaking, pit strategies and random accidents
- Optimize strategy based on starting grid positions and maximize overcut and undercut potentials
- Adding weather forecast and track conditions as predictors for race strategies

## Getting Started

### Dependencies

* [FastF1](https://theoehrly.github.io/Fast-F1/)
* [Jupyter Notebook](https://jupyter.org/)

### Installing

#### For Users who want to simulate their own race:
1. Fork a copy to your own branch.
2. Use PyCharm or equivalent IDEs to open the project.
3. Install Jupyter Notebook (or Jupyter Hub) via your terminal
4. Launch JupyterHub in PyCharm's (or your IDE's) terminal using this command: ```jupyter notebook```

#### For Users who want to read the analysis and predictions:
1. Simply open the ipynb files on GitHub and read the text descriptions and diagrams.

## Help

If you encounter any issues with Jupyter Notebook or any of the code in .py files, please restart to see if the issue is resolved. 

Note that some functions can only be run once or errors will be thrown. A clean re-run will be needed. This will be fixed in upcoming patches.

If the issue is terminal, please leave a detailed description in the "issues" tab on GitHub to let me know.

## Authors

[Tyler-CY](https://github.com/Tyler-CY)

## Version History

* 0.1
    * Initial Release (text description not completed)

## Acknowledgments

* [F1Metric's Race Simulator (2014)](https://f1metrics.wordpress.com/2014/10/03/building-a-race-simulator/)
* [FastF1](https://theoehrly.github.io/Fast-F1/)


