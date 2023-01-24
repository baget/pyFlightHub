from urllib.request import urlopen
from bs4 import BeautifulSoup
from enum import Enum
from enum import auto

VER = "0.1"
MS_FLIGHTHUB_URL = "https://docs.microsoft.com/en-us/windows-insider/flight-hub/"

###
# Windows 10 Versions
###


class Win10Version(Enum):
    vRS4 = auto()
    vRS5 = auto()
    v19H1 = auto()
    #v19H2 = auto()
    v20H1 = auto()
    v21H1 = auto()
    v21H2 = auto()
    v22H2 = auto()
    
    def __str__(self):
        return self.name[1:]

###
# Get Os Table from flight hub using bs4
###


def getOSTable(os: Win10Version):
    html = urlopen(MS_FLIGHTHUB_URL)  # Insert your URL to extract
    bsObj = BeautifulSoup(html.read(), features="lxml")

    data = []
    divList = bsObj.find_all('h2')
    if (divList is None):
        return []

    found = False
    for div in divList:
        try:
            if (str(os).lower() in div['id']):
                found = True
                break
        except:
            continue


    if (found == False):
        return []

    buildTables = div.find_next_sibling('table')

    # Adding Header
    table_header = buildTables.find('thead')
    cols = table_header.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    header = [ele for ele in cols if ele]
    data.append(header)  # Get rid of empty values

    # Adding Build Data
    table_body = buildTables.find('tbody')
    rows = table_body.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]

        buildData = [ele for ele in cols if ele]

        dataToAppend = []
        for i in range(0, len(header)):

            dataStr = ''
            if (i < len(buildData)):
                dataStr = buildData[i]

            dataToAppend.insert(i, dataStr)

        data.append(dataToAppend)  # Get rid of empty values

    return data

###
# Print data as formated Table
###


def printTable(data):
    for row in data:
        for col in row:
            print(f' {col:10} |', end='')

        print('')

    print('')

#
# Main Function
#


def main():
    print(f"pyFlightHub v{VER}")
    print(f"===================\n")

    for osVer in reversed(Win10Version):
        print(f"Builds for Windows 10 - {osVer:4}:")
        print("-----------------------------")
        data = getOSTable(osVer)

        printTable(data)


if __name__ == "__main__":
    main()
