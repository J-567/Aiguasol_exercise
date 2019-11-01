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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
