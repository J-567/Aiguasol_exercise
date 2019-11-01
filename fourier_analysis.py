# Author: Joan Pelegrí Andrés

import requests as rq
import json
import numpy as np
import re
import matplotlib.pyplot as plt
from scipy.fftpack import fft

### ----------------------------------------------------------------------- ###
###                                FUNCTIONS                                ###
### ----------------------------------------------------------------------- ###

### E·SIOS API DATA REQUEST ###
#
#url generator for requesting the needed data to the e·sios API
def esios_API_indicators_url(indicator_ID, start_date, end_date):
    
    #Build the url step by step, according to e·sios API format and assuming we are 
    #in time zone 02
    url = 'https://api.esios.ree.es/indicators/'
    url += indicator_ID+'?'
    url += 'start_date='+start_date[0]+'-'+start_date[1]+'-'+start_date[2]\
    +'T'+start_date[3]+'%3A'+start_date[4]+'%3A'+start_date[5]+'Z02&'
    url += 'end_date='+end_date[0]+'-'+end_date[1]+'-'+end_date[2]\
    +'T'+end_date[3]+'%3A'+end_date[4]+'%3A'+end_date[5]+'Z02'
    
    return(url)
    
#Get data from e·sios using its API
def get_data(url, token):

    head = {'Authorization': 'Token token='+str(token)}
    response = rq.get(url, headers=head)
    print('Request stauts code:', response.status_code)
    
    data = json.loads(response.text)
    
    return(data)


### DATA FORMATTING ###
#
#Print data
def print_data(data):

    print(json.dumps(data, indent=2, sort_keys=True))
    
    return
    
#Transform data into a temporal series, being time zero the one at which the time series starts
def temp_series(data, time_step, value_key):
    
    N = len(data)
    times = np.arange(0, N*time_step, time_step)
    values = np.zeros(N)
    
    i = 0
    for entry in data:

        values[i] = entry[value_key]

        i += 1
        
    return(times, values, N)


### DISCRETE FOURIER TRANSFORM ###
#
#Perform a discrete fourier transform  
def discrete_fourier_transform(TS, time_step, avg_subtract):
    
    t = np.copy(TS[0])
    x = np.copy(TS[1])
    N = TS[2]
    
    if avg_subtract == True:
        
        #Subtract mean value to the signal
        x = x-(np.sum(x)/N)
        
    amp = np.abs(fft(x))*2/N
    freq = np.arange(0,N)/(N*time_step)
    
    return(amp, freq)


### DATA PLOTTING ###
#
#Single plot
def single_plot(XY, xlab, ylab, xlim = None, ylim = None):

    plt.plot(XY[0], XY[1])
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.show()
    
    return
    
#Stacked plots
def stacked_plot(XY1, XY2, xlab1, ylab1, xlab2, ylab2, title1 = '', title2 = '',\
     xlim1 = None, ylim1 = None, xlim2 = None, ylim2 = None, separation = None):

    fig, axs = plt.subplots(2)
    plt.subplots_adjust(hspace = separation)
    axs[0].plot(XY1[0], XY1[1])
    axs[1].plot(XY2[0], XY2[1])
    
    axs[0].set_title(title1)
    axs[0].set_xlabel(xlab1)
    axs[0].set_ylabel(ylab1)
    axs[0].set_xlim(xlim1)
    axs[0].set_ylim(ylim1)
    
    axs[1].set_title(title2)
    axs[1].set_xlabel(xlab2)
    axs[1].set_ylabel(ylab2)
    axs[1].set_xlim(xlim2)
    axs[1].set_ylim(ylim2)
    
    plt.show()
    
    return


### ----------------------------------------------------------------------- ###
###                                   MAIN                                  ###
### ----------------------------------------------------------------------- ###
 
def main(token, start_date, end_date, indicator_ID, time_step, value_key, avg_subtract, xlim_dplot):
    
    #Get data
    url = esios_API_indicators_url(indicator_ID, start_date, end_date)
    data = get_data(url, token)
    #print_data(data)
    
    #Extract time series from the data
    TS = temp_series(data["indicator"]["values"], time_step, value_key)
    
    #Discrete fourier transform
    yf, xf = discrete_fourier_transform(TS, time_step, avg_subtract)

    #Plots
    #Stacked plot
    stacked_plot((TS[0],TS[1]), (xf, yf), 'Time (days)', 'Real demand(MW)',"Frequency (1/days)",\
    "Amplitude", xlim2 = [0,1/(2*time_step)], separation = 0.4, title1 = "Power demand time series",\
    title2 = "Discrete Fourier Transform")
    #Detail for lower frequencies
    single_plot((xf, yf), "Frequency (1/days)", "Amplitude", xlim = xlim_dplot)
    
    return

###############################################################################



token = 'ded05081d1a73dd50ea972b6cda5e7f6a9a91ac48cc625ec8feadebdd1815ba5'
start_date = ['2018', '09', '02', '00', '00', '00']
end_date = ['2018', '10', '06', '23', '59', '59']
indicator_ID = '1293'
time_step = 1/(6*24) #(10 minutes in DAYS)
value_key = 'value'
avg_subtract = True
xlim_dplot = [0,10]

main(token, start_date, end_date, indicator_ID, time_step, value_key, avg_subtract, [0,10])


