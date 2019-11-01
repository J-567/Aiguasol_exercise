import fourier_analysis as fa

token = 'YOUR_TOKEN'
start_date = ['2018', '09', '02', '00', '00', '00']
end_date = ['2018', '10', '06', '23', '59', '59']
indicator_ID = '1293'
time_step = 1/(6*24) #(10 minutes in DAYS)
value_key = 'value'
avg_subtract = True
xlim_dplot = [0,10]

fa.main(token, start_date, end_date, indicator_ID, time_step, value_key, avg_subtract, [0,10])
