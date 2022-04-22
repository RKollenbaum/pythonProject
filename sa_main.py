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
    descriptives = sp500.describe() #create an array of descriptive statistics for the dataset
    
    print('-'*70) #present descriptive statistics of market values and returns
    print("These are the descriptive statistics of companies' market values and returns: \n")
    print(round(descriptives[['FirmV2017', 'FirmV2022', 'Returns']], 2))
    
    skewness = sp500.skew(axis = 0, numeric_only = True)['Returns'] #calculate the skewness coefficient
    kurtosis = sp500.kurt(axis = 0, numeric_only = True)['Returns'] #calculate the kurtosis coefficient
    print('\nThe skewness coefficient of Returns is {:.2f}, the kurtosis coefficient - {:.2f}.'.format(skewness, kurtosis)) #print the coefficients
    print('-'*70)

    print('-'*70) #present descriptive statistics of product strategy and business model scores
    print("These are the descriptive statistics of companies' product strategy and business model scores: \n")
    print(round(descriptives[['Differentiation', 'Cost leadership', 'Efficiency', 'Novelty']], 2))
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
    
    for i in X: #iterate for all values in array X
        
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
    plt.savefig('S&P500_ScoresReturnsCorr.png', bbox_inches='tight') #save the plot as a png file
    plt.show() #show the plot
    

def plot_distributions(sp500):
    """
    This function plots 4 histograms with different score distributions.

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
    
    for i in X: #iterate for all values in array X
        
        axs[row][column].hist(sp500[i], bins = 30, rwidth = 0.8, color = colours[X.index(i)], alpha = 0.7) #draw the scatter plot
        axs[row][column].set_xlim(0, 100) #specify the limits of the X axis
        axs[row][column].set_ylim(0, 25)
        axs[row][column].set_xlabel(i, fontsize = 16, fontweight = 'bold') #name the X axis
        axs[row][column].tick_params(axis='x', labelsize= 14) #set the size of the ticks font on the X axis
        axs[row][column].set_ylabel('Count', fontsize = 16) #name the Y axis
        axs[row][column].tick_params(axis='y', labelsize= 14) #set the size of the ticks font on the Y axis
        
        if row == 0: #if the first row is drawn...
            row += 1 #...draw the second row
        else: #if the first column is drawn...
            row = 0 #...draw the second one
            column += 1
    
    fig.suptitle('Distributions of Business model/Product strategy scores', fontsize = 25, y = 0.96) #set the title of the whole figure
    fig.tight_layout(pad = 3) #adjust the space between and around subplots.
    plt.savefig('S&P500_ScoresDistributions.png', bbox_inches='tight') #save the plot as a png file
    plt.show() #show the plot

 def plot_sectors_histogram(sp500):
    """
    This function plots three bar plots where the each sector yearly returns histogram are on the y-axis of each the historgram amount is located on the x-axis.

    Parameters
    ----------
    sp500 : DataFrame
        Contains information about S&P500 companies (IT, Industrial and Financial Sectors): their market values, yearly stock returns and product strategy/business model scores.

    Returns
    -------
    None.

    """

    financials = sp500[sp500['Sector'] == 'Financials']     #Filter sp500 for only 'Financials' Sector
    industrials = sp500[sp500['Sector'] == 'Industrials']   #Filter sp500 for only 'Industrials' Sector
    it = sp500[sp500['Sector'] == 'Information Technology'] #Filter sp500 for only 'Information Technology' Sector

    fig, ax = plt.subplots(nrows = 1, ncols = 3, figsize = (20, 5)) #create a figure and an array of subplots

    ax[0].hist(financials['Returns'], bins = 20, color='red', alpha = 0.5)   #draw histogram plot 0
    ax[1].hist(industrials['Returns'], bins = 20, color='blue', alpha = 0.5) #draw histogram plot 1
    ax[2].hist(it['Returns'], bins = 20, color='orange', alpha = 0.5)        #draw histogram plot 2


    ax[0].set_title('Yearly return by financials', fontsize = 16)             #Set title for plot 0
    ax[1].set_title('Yearly return by industrials', fontsize = 16)            #Set title for plot 1
    ax[2].set_title('Yearly return by information technology', fontsize = 16) #Set title for plot 2

    fig.suptitle('Histogram of the yearly returns within each sector \n S&P500 (Financials, Industrials, IT)', fontsize = 20, y = 1.20) #set the title of the whole figure
    
    plt.show() #show the plot
    
    
def regression_model(sp500):
    """
    This function presents three variation in returns. The first one is the returns from the sp500. 
    The second and third are expected returns with made up: Differentiation, Cost leadership, Efficiency, Novelty.

    Parameters
    ----------
    sp500 : DataFrame
        Contains information about S&P500 companies (IT, Industrial and Financial Sectors): their market values, yearly stock returns and product strategy/business model scores.

    Returns
    -------
    None.

    """
    
    X = sp500[['Differentiation', 'Cost leadership', 'Efficiency', 'Novelty']] # Get 𝛽1𝐷𝑖𝑓𝑓𝑒𝑟𝑒𝑛𝑡𝑖𝑎𝑡𝑖𝑜𝑛 + 𝛽2𝐶𝑜𝑠𝑡 𝑙𝑒𝑎𝑑𝑒𝑟𝑠h𝑖𝑝 + 𝛽3𝐸𝑓𝑓𝑖𝑐𝑖𝑒𝑛𝑐𝑦 + 𝛽 𝑁𝑜𝑣𝑒𝑙𝑡𝑦
    Y = sp500['Returns'] # Get Returns
    
    reg_res = sm.OLS(Y, sm.add_constant(X)).fit() # add constant to X and fit model
    
    r_sqrd = reg_res.rsquared_adj #Adjusted R-squared.
    
    print('-'*70)
    
    #present variation in returns
    print('Differentiation, Cost leadership, Efficiency and Novelty explain ' +str(round(100*r_sqrd,1)) +' % of the variation in Returns.\n')
    
    #present expected variation in returns with fake company
    print('If a company in the financial sector has a score of: \nDifferentiation: 54 Cost leadership: 61 Efficiency: 57 Novelty: 42.')
    print('The expected returns would be: ' + str(reg_res.predict([1, 54, 61, 57, 42])) + ".\n")
    
    #present expected variation in returns with increased novelty
    print('If the company managed to increased novelty to 55.')
    print('The expected returns would be: ' + str(reg_res.predict([1, 54, 61, 57, 55])) + ".")
    
    print('-'*70)

    
    
    
    
print('-'*70) #print the greeting message
print('This program provides data analysis that helps inspect the effect of different business models and product strategies on firm performance.')
print('It uses the data of S&P500 companies from 3 sectors: Financials, Industrials and Information Technology.\n')

sp500 = prepare_dataset() #create the sp500 DataFrame with necessary information

print('-'*70) #present the count of companies in the sample by sector
print('Company count by sector: ')
print(sp500.groupby(by = 'Sector').size().to_string())
print('Total {:23}'.format(len(sp500)))
print('-'*70)

fig, ax = plt.subplots() #plot a histogram with returns distribution
ax.hist(sp500['Returns'], bins = 30, rwidth = 0.8, alpha = 0.8)
ax.set_xlabel('Returns', fontsize = 12, fontweight = 'bold')
ax.set_ylabel('Count', fontsize = 12)
ax.set_title('Distribution of Returns', fontsize = 14)
plt.savefig('S&P500_ReturnsDistribution.png', bbox_inches='tight') #save the histogram
plt.show()

print_descriptives(sp500) #present the descriptive statistics of the dataset

plot_returns_scores(sp500) #plot a figure where returns are on the y-axis 
                           #and differentiation, cost leadership, efficiency, and novelty - on the x-axis.    

plot_distributions(sp500) #plot histograms which show the distribution of the scores

plot_sectors_histogram(sp500) #plot three histogram where average yearly returns are on the y-axis
                              #and the different sectors are separated. 
    
regression_model(sp500) #present the regression model with expected returns

#the following inactive code was used for distinguishing top-10 companies of each model/strategy score (and returns) rating
#score = 'Returns'
#print(sp500.sort_values(by = score, ascending = True)[['Symbol', score]].head(10))

#the following code was used for inspecting correlation coefficients between different scores
#scores = ['Differentiation', 'Cost leadership', 'Efficiency', 'Novelty']
#print(sp500.corr()[scores].loc[scores])
