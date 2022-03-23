"""

This module contains functions for oil price analysis.

Available functions
-------------------

data_cleaning() 
    Imports the data from "oil_raw_data.txt", cleans it and creates a "oil.txt" file.
    
info_to_dictionary()
    Imports the data from "oil.txt" and stores the information in a dictionary oil_dicit.
    
highlow(list_of_dates_changed, list_of_prices)
    Prints the date for the highest or the lowest oil price.
    
display()
    Displays either the price or the volume for a specified date.

"""


oil_dicit = {}                      #dictionary for exercise F) 

def data_cleaning():        # this is for exercise 1d)
    """    
    This function imports the data from "oil_raw_data.txt", cleans it, transforms the date format and creates a "oil.txt" file with cleaned data, separated by a comma. 
                
    """

    #a) Read data from .txt file and store in 3 lists
    raw_data = "oil_raw_data.txt"       # storing the text file in a variable
    data_opened = open(raw_data,"r")    # Opening the data in read mode
    lines = data_opened.readlines()     # Storing the Data in a variable
    data_opened.close()                 # closing the file
    lines.pop(0)                        # removing the first line of oil_raw_data.txt: "date,oil,volume"

    list_of_dates = []                  # Clear the lists for reusing within the function, see line 6
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
        month = old_date_string[0:2]                        #creating variable for day and storing the position of day in it
        day = old_date_string[3:5]                          #creating variable for month and storing the position of month in it
        year = old_date_string[6:10]                        #...
        new_date_order = year + "/" + month + "/" + day     #storing the variables for day month and year in a variable in the right order and adding /
        list_of_dates_changed.append(new_date_order)        #appending new order into list_of_dates_changed

#    print(list_of_dates)                                    #printing the lists to check for mistakes
#    print(list_of_dates_changed)                            #actually did that all the time while trying new code
#    print(list_of_prices)
#    print(list_of_volumes)

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
    # Line 3 introduces the function
    


# f) Make a function which imports the text in "oil.txt" and stores the information in a dictionary. The date is the key in the key-value pair and the price and volume is the value in the key-value pair. Make sure to check for invalid input from the user.            
            
def info_to_dicitonary():
    """    
    This function imports the data from "oil.txt", stores the information in a dictionary oil_dicit and returns lists of dates, volumes and prices. 
    
    Returns
    -------
    list_of_dates: list
    A list of dates for which oil prices are available.  

    list_of_prices: list
    A list of oil prices in USD on a specific day.

    list_of_volumes: list
    A list of numbers of traded oil contracts in a day.  
       
    """
    
    data = "oil.txt"                    # storing the text file in a variable
    data_opened = open(data,"r")        # Opening the data in read mode
    lines = data_opened.readlines()     # Storing the Data in a variable
    data_opened.close()                 # closing the file
    
    list_of_dates = []                  # Clear the lists for reusing within the function, see line 6
    list_of_prices = []
    list_of_volumes = []

    for line in lines:                  #Looping over the lines and adding the data
        data = line.split(',')          # split iterartes over every line and recognizes every comma and than seperates the data in between the commas into individual strings
        list_of_dates.append(data[0])            # the first [0] element of data now contains the date, the second [1] element the price and the third [2] the volumes
        list_of_prices.append(float(data[1]))             # now appending the list with the positional statements [0],[1],[2]
        list_of_volumes.append(int(data[2]))
 
    counter = 0                                   #Counter for checking if every line as been read
    while counter != len(list_of_dates):          #While to keep the code running until a lines have been read and added
        oil_dicit[list_of_dates[counter]] = list_of_prices[counter], list_of_volumes[counter]  #Add values to dictionary
        counter = counter + 1                     #Add 1 to counter
    
    return list_of_dates, list_of_prices, list_of_volumes 
    

# e) Write a function which displays the date of the highest or lowest oil price, including the price. The user has to specify whether the maximum or minimum price should be displayed. Make sure to check for invalid input from the user.

def highlow(list_of_dates, list_of_prices):   # this is for exercise 1e)
    """    
    This function prints the date for the highest or the lowest oil price from the available data. 
    
    Parameters
    ----------
    list_of_dates: list
    A list of dates for which oil prices are available.   
    
    list_of_prices: list
    A list of oil prices in USD on a specific day.     
    """
    
    list_of_prices_float = []                      #Create new list where prices are in floats
    for item in list_of_prices:                    #Iterate over every index of lines in the list
        list_of_prices_float.append(float(item))   #Appending all lines to new list
    
    
    print("Show highest or lowest oil price.")     #Print to make user clear what is going to happen
    user_input = input("Type in 'highest' or 'lowest': ") #User input
    
    while user_input != "":                                #While to keep the code running until a right input is given
        if user_input == "highest":                        #When input is "highest"
            max_price = max(list_of_prices_float)          #Function to find the maximum price
            maxpos = list_of_prices_float.index(max_price) #Function to find the position of maximum 
            max_price_date = list_of_dates[maxpos] #Function to find the corrosponding date in list

            print("\nThe highest oil price is: " + str(max_price) + ", on the date of " +str(max_price_date)) #print all data
            user_input = ""                                #To make the while function stop
            
        elif user_input == "lowest":                       #When input is "lowest"
            min_price = min(list_of_prices_float)          #Function to find the maximum price
            minpos = list_of_prices_float.index(min_price) #Function to find the position of maximum 
            min_price_date = list_of_dates[minpos] #Function to find the corrosponding date in list

            print("\nThe lowest oil price is: " + str(min_price) + ", on the date of " +str(min_price_date)) #print all data
            user_input = ""                                #To make the while function stop
            
        else:
            print("Not a correct input.")                  #To make the user clear a not correct input was given
            user_input = input("Please type in 'highest' or 'lowest': ") #Asking for correct input. When given, the while loop will start over

            
            


        
        
# G) Make a function which asks for a date and displays either the date and price, or the date and volume. Make sure to check for invalid input from the user.

def display():
    """    
    This function asks for a date and displays either the date and price, or the date and volume, depending on user input.
                
    """
    
    print("Give a date to display either the price or volume.")  #Give user information
    date = input("Input must be 'yyyy/mm/dd': ")                 #Let user give input date
    
    stop = 1                                         #Variable to stop while loop
    
    while stop != 0 :                                #While to keep the code running until a right input is given
        
        try:
            if date[:4].isdigit() and date[4] == "/" and date[5:7].isdigit() and date[7] == "/" and date[-2:].isdigit(): #Check if input has the right format

                if date in oil_dicit:                                   #Date is in dictionary
                    print("\nDo you want to see the price or volume?")  #Ask user what he/she wants to see 
                    price_volume = input("Type 'price' or 'volume': ")  #Let user give input
                    price_volume = price_volume.lower()                 #Lower all characters, just to be sure

                    if price_volume == "price":                                          #Input is "price"                
                        for k, v in oil_dicit.items():                                   #Go over lines all keys and values in oil_dicit
                            if k == date:                                                #Check where "date" is located
                                print("\nThe price on " + k + " was " + str(v[0]) + ".")  #Print date and price
                                stop = 0


                    elif price_volume == "volume":                                       #Input is "price"                   
                        for k, v in oil_dicit.items():                                   #Go over lines all keys and values in oil_dicit
                            if k == date:                                                #Check where "date" is located
                                print("\nThe volume on " + k + " was " + str(v[1]) + ".")  #Print date and volume
                                stop = 0                                                 #Make the while function stop


                    else:                                                   #User input is not "price" or "volume"
                        print("Input was not 'price' or 'volume'.")         #Tell user to correct input has not been given


                else:                                                  #User input is not in the dictionary
                    print("\nDate is not in dictionary.")              #Tell user date is not in dictionary
                    date = input("Try another date, 'yyyy/mm/dd': ")   #Let user try again
                     
            else:                                                   #User input is not in the right order
                print("\nCorrect date order has not been given.")   #Tell user to correct input has not been given
                date = input("Input must be 'yyyy/mm/dd': ")        #Let user try again

        except:                                            #User input is not in the right order
            print("\nInput is not a date.")                #Tell user to correct input has not been given
            date = input("Input must be 'yyyy/mm/dd': ")   #Let user try again   