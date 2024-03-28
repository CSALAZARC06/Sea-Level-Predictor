import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig=sns.scatterplot(data=df, x="Year", y="CSIRO Adjusted Sea Level")

    # Create first line of best fit
    x=np.arange(df.iloc[0,0],2050+1)
    slope,intercept, rvalue, p_value, std_err=stats.linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    plt.plot(x,intercept + slope*(x),'r')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()