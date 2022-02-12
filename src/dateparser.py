import datetime as dt

def dateparser(x):
    newDates = []
    for dates in x:
        #Splitting string to have just YYYY-MM-DD
        parsedate = dates[:dates.find("T")]
        #Convert to Datetime type with format mentioned
        datetimeformat = dt.datetime.strptime(parsedate, '%Y-%m-%d')
        #Convert to gregorian time
        gregorian = datetimeformat.toordinal()
        newDates.append(gregorian)
    return newDates
