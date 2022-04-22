'''

This is a Group Assignment for the Introduction to Programming course, Spring 2022.

Lecturer: Erik Smith-Meyer

Prepared by: Robert-Erik Lars Wilm Kollenbaum, Hessel Jan van Lier Lels and Aleksejs Popovs (Group 14).

'''

import oilmodule as om #import the oilmodule with necessary functions

print('This program provides several tools to analyse oil prices.') #explain the main aspects of the program to the user 
print('The data needed for the operation of the program is stored in the file oil_raw_data.txt.')

om.data_cleaning() #import the data from oil_raw_data.txt, clean it and create a file oil.txt with cleaned data
list_of_dates, list_of_prices, list_of_values = om.info_to_dicitonary() #import the cleaned data, create a dictionary oil_dicit where dates, prices and volumes are stored and store the data in lists

end = False #initalize a boolean variable for the menu while loop

while end != True: #menu while loop
    
    print('\n\nMENU') #print a primitive menu with different option
    print('-'*50) #print a line of dashes
    print('Enter 1 to re-import data from oil_raw_data.txt, clean it and create a file oil.txt with cleaned data.') #explain the options to the user
    print('Enter 2 to get the highest or the lowest oil price in USD.')
    print('Enter 3 to get the oil price in USD or the number of traded oil contracts for a specified date.')
    
    entry = input('Enter 1, 2, 3 or press ENTER to exit: ') #ask for user input to choose one of the options
    print('-'*50) #print a line of dashes
    
    if entry == "": #if the user presses ENTER... 
        end = True  #...change the value of the boolean variable to stop the program
    
    elif entry == "1": #if the user chooses the 1st option... 
        om.data_cleaning() #re-import the data from oil_raw_data.txt, clean it and create a file oil.txt with cleaned data
        om.info_to_dicitonary() #re-import the cleaned data and create a dictionary oil_dicit where dates, prices and volumes are stored
    
    elif entry == "2": #if the user chooses the 2nd option... 
        om.highlow(list_of_dates, list_of_prices) #activate the function which returns the highest or the lowest oil price in USD
        
    elif entry == "3": #if the user chooses the 3rd option... 
        om.display() #activate the function which prints the price or volume for a specified date
    
    else: #in case of invalid input...
        print('Invalid input. Please enter 1, 2 or 3. To exit the program press ENTER.') #print an error message
     
print('\nThank you for using this program!') #print a goodbye message