Author: Joan Pelegrí Andrés

The fourier_analysis.py script accesses to e·sios time series data regarding a desired indicator
through its API. The script analyzes the data performing a Discrete Fourier Transform (DFT) with the
purpose of detecting patterns. An explanation of its main functions follows:


-> esios_API_indicators_url(indicator_ID, start_date, end_date):
        
        indicator_ID -> ID of the desired indicator.
        start_date -> Date at which the time period studied starts.
        end_date -> Date at which the time period studied ends.
        
        Returns the url string of the corresponding request according to e·sios API format. Dates 
        need to be specified as a list of strings ['YYYY', 'MM', 'DD', 'hh', 'mm', 'ss'].


-> get_data(url, token):
        
        url -> API url to which the data is requested.
        token -> Personal token needed for authentication into e·sios API.
        
        Sends the requests to the specified url, printing the request status code. In case the request
        works successfully, returns the retrieved data as a dictionary.


-> temp_series(data, time_step, value_key):

        data -> Dictionary with the data to study.
        time_step -> Time step between consecutive data samples.
        value_key -> Key with which the variable studied is regarded in the dictionary entries. 

        Returns (times, values, N), where:
        
        times -> Array with the times at which each value is sampled (starting from zero at the time
                the sampling starts).
        values -> Array with the consecutive values that the indicator has at each time step.
        N -> number of sampled points.


-> discrete_fourier_transform(TS, time_step, avg_subtract):

        TS -> (times, values, N), time series data stored in the format outputted by the temp_series 
                function.
        time_step -> Time step between consecutive data samples.
        avg_subtract -> Flag used to control whether if the average value of the indicator throughout
                the period studied is subtracted from all time series values or not before doing 
                the Discrete Fourier Transform. Only if True, the subtractions are done.
        
        Returns(amp, freq):
        
        amp -> array with the amplitudes given by the DFT.
        freq -> array with the frequencies that correspond to each amplitude.
        
        The subtraction of the average is done in order to avoid high values for the first amplitude
        (amp[0]). When subtracting the average, this value becomes zero, and the periodic analysis
        keeps being valid.
        
               
-> main(token, start_date, end_date, indicator_ID, time_step, value_key, avg_subtract, xlim_dplot):

        token -> Personal token needed for authentication into e·sios API.
        start_date -> Date at which the time period studied starts.
        end_date -> Date at which the time period studied ends.
        indicator_ID -> ID of the desired indicator.
        time_step -> Time step between consecutive data samples.
        value_key -> Key with which the variable studied is regarded in the dictionary entries.
        avg_subtract -> Flag used to control whether if the average value of the indicator throughout
                the period studied is subtracted from all time series values or not before doing 
                the Discrete Fourier Transform. Only if True, the subtractions are done.
        xlim_dplot -> Frequency range for the detailed DFT plot.
        
        Runs the method, executing all the needed functions for accessing the desired data, processing
        it, computing its DFT and plotting the results. It produces:
        
            -> An stacked plot with the time series and its DFT for all the frequencies available     
               conditioned by the time step of the input data (until the Nyquist frequency).
            -> A detailed plot for better analyzing the lower frequencies spectrum.
        
        
Brief comment about the structure of the code:

    For the sake of simplicity and because of the conciseness of this exercise, I have chosen to
    program it only using functions. However, if I had to structure the code in classes, I would do 
    four of them, devoted to the following purposes. For each of the classes, a list of the programmed
    functions that it would include follows:
    
        -> Class for communicating with the API and retrieving data:
                
                - esios_API_indicators_url(indicator_ID, start_date, end_date)
                - get_data(url, token)
                
        -> Class for data formatting:
                 
                - print_data(data)
                - temp_series(data, time_step, value_key)
        
        -> Class for processing and analysing data:
        
                - discrete_fourier_transform(TS, time_step, avg_subtract)
        
        -> Class for showing and analysing the results:
        
                - single_plot(XY, xlab, ylab, xlim = None, ylim = None)
                - stacked_plot(XY1, XY2, xlab1, ylab1, xlab2, ylab2, title1 = '', title2 = '',\
                  xlim1 = None, ylim1 = None, xlim2 = None, ylim2 = None, separation = None)
        
        
    This four classes would enable to generalize the program to solve other similar problems in which
    data is retrieved from a given API, and a particular analysis needs to be carried out.
        
        
        
        
        
        
        
        
