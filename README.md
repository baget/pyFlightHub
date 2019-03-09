# pyFlightHub - Get Microsoft Windows Insider Build Flighting info
Python Script to get Microsoft Windows Insider Build Flighting info 

Main Resource: [Flight Hub](https://docs.microsoft.com/en-us/windows-insider/flight-hub/)

Using [Beautiful](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Soup 4 to parse Microsoft Flight Hub tables.


### License: [Apache License 2.0](https://github.com/baget/pyFlightHub/blob/master/LICENSE)

### Screenshot:
![Powershell Screenshot](https://github.com/baget/pyFlightHub/raw/master/screenshots/screenshot1.jpg "Powershell screenshot")

### Using:
+ Clone the repo
+ Goto into the workspace of repo
+ Create venv: `python -m venv <whatever>` e.g. `python -m venv flighthub`
+ Activate venv: e.g `source ./flighthub/bin/activate` or `flighthub\Scripts\Activate.ps1`
+ Install depedncy packages using pip: `pip install -r requirements.txt`
+ Run the script: `./src/pyFlightHub.py`

### TODO:
1. Add an option to display only a particular version or build.
2. Add an option to export to csv.
3. Add an option to do queries.


