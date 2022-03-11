
list_of_dates = []                         # Creating the lists
list_of_prices = []
list_of_volumes = []

def data_cleaning():        # this is for exercise 1d)

    #a) Read data from .txt file and store in 3 lists
    raw_data = "oil_raw_data.txt"       # storing the text file in a variable
    data_opened = open(raw_data,"r")    # Opening the data in read mode
    lines = data_opened.readlines()     # Storing the Data in a variable
    data_opened.close()                 # closing the file
    lines.pop(0)                        # removing the first line of oil_raw_data.txt: "date,oil,volume"

    list_of_dates = []                         # Clear the lists for reusing within the function, see line 6
    list_of_prices = []
    list_of_volumes = []

    for line in lines:                  #Looping over the lines and adding the data
        data = line.split(',')          # split iterartes over every line and recognizes every comma and than seperates the data in between the commas into individual strings
        list_of_dates.append(data[0])            # the first [0] element of data now contains the date, the second [1] element the price and the third [2] the volumes
        list_of_prices.append(data[1])             # now appending the list with the positional statements [0],[1],[2]
        list_of_volumes.append(data[2])


    #1B.) The date format is not very good. It contains several blank spaces. Remove these.

    for i in range(len(list_of_dates)):                     #Using the range funtion to introduce list counter (=19 lines in oil_raw_data.txt)
         list_of_dates[i] = list_of_dates[i].strip()        #iterating over every line [i] and removing blanks with .strip and storing the result back into list_of_dates

    for i in range(len(list_of_volumes)):                   #same thing to get rid of /n in list of volumes
        list_of_volumes[i] = list_of_volumes[i].strip()

    # 1B.) Also, the format is day/month/year. Change it to year/month/day.

    list_of_dates_changed = []                              #new variable for the new order of dates with empty list
    for old_date_string in list_of_dates:                   #it
        month = old_date_string[0:2]                          #creating variable for day and storing the position of day in it
        day = old_date_string[3:5]                        #creating variable for month and storing the position of month in it
        year = old_date_string[6:10]                        #...
        new_date_order = year + "/" + month + "/" + day     #storing the variables for day month and year in a variable in the right order and adding /
        list_of_dates_changed.append(new_date_order)        #appending new order into list_of_dates_changed

    print(list_of_dates_changed)                            #printing the lists to check for mistakes
    print(list_of_dates)                                    #actually did that all the time while trying new code
    print(list_of_prices)
    print(list_of_volumes)

    #c.) write the lists to a file called "oil.txt" for you to have data on a proper format in a text file.
    # The columns of data must be comma separated (date, oil, volume).

    list_length = len(list_of_dates)      # the number of lines in the list (=19)

    list_total = []                     #creating new list to collect all data
    for i in range(list_length):        #iterate over every index of lines in the list, so from line 1 to line 19
        line = list_of_dates_changed[i] + ", " + list_of_prices[i] + ", " + list_of_volumes[i]     # new Variable line that concatenates all strings of the 19 lines
        list_total.append(line)         ## appending all lines to new list

    output_file = open("oil.txt", "w")      # creating output file
    for line in list_total:                 # iterating over every line of the new list
        output_file.write(line)             # adding line to file
        output_file.write("\n")             # adding \n to every line
    output_file.close()                     #closing the file
    #d.) Place the code for parts a), b), and c) in a function.
    # Line 6 introduces the function