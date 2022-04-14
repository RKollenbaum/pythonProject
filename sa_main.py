'''

This is the Semester Assignment for the Introduction to Programming course, Spring 2022.

Lecturer: Erik Smith-Meyer

Prepared by: Robert-Erik Lars Wilm Kollenbaum, Hessel Jan van Lier Lels and Aleksejs Popovs (Group 14).

'''

import pandas as pd
import matplotlib.pyplot as plt

def prepare_dataset(): 
    """
    This function imports the data from 'sp500_marketvalues.csv' and 'sp500_survey.csv', merges two datasets, drops NaNs and creates a 'Returns' row.

    Returns
    -------
    sp500 : DataFrame
        Contains information about S&P500 companies (IT, Industrial and Financial Sectors): their market values, yearly stock returns and product strategy/business model scores.

    """
    
    filename1 = 'sp500_marketvalues.csv'
    filename2 = 'sp500_survey.csv'
    
    try: #import the file with market values...
        market_values = pd.read_csv(filename1)    
    except: #...or return an error message if it is not available
        print('{} is not available!'.format(filename1))

    try: #import the file with market values...
        survey = pd.read_csv(filename2)    
    except: #...or return an error message if it is not available
        print('{} is not available!'.format(filename2))
    
    sp500 = market_values.merge(survey, on = 'Symbol') #merge together both datasets using the company code as a common column

    sp500.dropna(inplace = True) #drop rows with missing data

    sp500['Returns'] = (sp500['FirmV2022'] / sp500['FirmV2017']) ** 0.2 - 1 #calculate yearly stock returns of each firm from April 2017 to April 2022

    return sp500


def print_descriptives(sp500):
    """
    This function presents the descriptive statistics for the dataset SP500.

    Parameters
    ----------
    sp500 : DataFrame
        Contains information about S&P500 companies (IT, Industrial and Financial Sectors): their market values, yearly stock returns and product strategy/business model scores.

    Returns
    -------
    None.
    
    """
    
    print('-'*70) #present descriptive statistics of market values and returns
    print("These are the descriptive statistics of companies' market values and returns: \n")
    print(round(sp500.describe()[['FirmV2017', 'FirmV2022', 'Returns']], 2))
    print('-'*70)

    print('-'*70) #present descriptive statistics of product strategy and business model scores
    print("These are the descriptive statistics of companies' product strategy and business model scores: \n")
    print(round(sp500.describe()[['Differentiation', 'Cost leadership', 'Efficiency', 'Novelty']], 2))
    print('-'*70)


def plot_returns_scores(sp500):
    """
    This function plots 4 scatter plots where "returns" are on the y-axis and differentiation, cost leadership, efficiency, and novelty scores - on the x-axis.

    Parameters
    ----------
    sp500 : DataFrame
        Contains information about S&P500 companies (IT, Industrial and Financial Sectors): their market values, yearly stock returns and product strategy/business model scores.

    Returns
    -------
    None.

    """
    
    fig, axs = plt.subplots(nrows = 2, ncols = 2, figsize = (16, 10)) #create a figure and an array of subplots
    
    X = ['Differentiation', 'Cost leadership', 'Efficiency', 'Novelty'] #an array of scores on X-axis
    colours = ['blue', 'red', 'orange', 'green']
    row = 0 #row index
    column = 0 #column index
    
    for i in X: #iterate for all parametres in array X
        
        axs[row][column].scatter(sp500[i], sp500['Returns'], s = 15, marker = 'o', c = colours[X.index(i)], alpha = 0.7) #draw the scatter plot
        axs[row][column].set_xlim(15, 100) #specify the limits of the X axis
        axs[row][column].set_xlabel(i, fontsize = 16, fontweight = 'bold') #name the X axis
        axs[row][column].tick_params(axis='x', labelsize= 14) #set the size of the ticks font on the X axis
        axs[row][column].set_ylabel('Returns', fontsize = 16) #name the Y axis
        axs[row][column].tick_params(axis='y', labelsize= 14) #set the size of the ticks font on the Y axis
        axs[row][column].set_title('Correlation coefficient = ' + str(round(sp500.corr().loc[i, 'Returns'], 2)), fontsize = 16, horizontalalignment = 'left') #put the correlation coefficient in the subplot titles   
        
        if row == 0: #if the first row is drawn...
            row += 1 #...draw the second row
        else: #if the first column is drawn...
            row = 0 #...draw the second one
            column += 1
    
    fig.suptitle('Product strategy and Business model scores VS Returns \n S&P500 (Financials, Industrials, IT)', fontsize = 20, y = 0.96) #set the title of the whole figure
    fig.tight_layout(pad = 3) #adjust the space between and around subplots.
    plt.show() #show the plot




print('-'*70)
print('This program provides data analysis that helps inspect the effect of different business models and product strategies on firm performance.')
print('It uses the data of S&P500 companies from 3 sectors: Financials, Industrials and Information Technology.\n')

sp500 = prepare_dataset() #create the sp500 DataFrame with necessary information

print_descriptives(sp500) #present the descriptive statistics of the dataset

plot_returns_scores(sp500) #plot a figure where returns are on the y-axis 
                           # and differentiation, cost leadership, efficiency, and novelty - on the x-axis.                           