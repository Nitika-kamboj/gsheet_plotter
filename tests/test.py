from gsheet_plotter import GSheetPlotter #import the library

CREDS= 'client_secret.json' #json credential file path
SHEET_ID= '1SrZfvr2ee54r7HR1jGtAE9zHIj_Y-UzK9ok8bdwkpqc' #Sheet id found in the Google sheet URL
TAB_NAME='Sheet1' #worksheet name

mysheet= GSheetPlotter(creds=CREDS,sheet_id=SHEET_ID,tab_name=TAB_NAME) #instantiate the class

mysheet.fetch_data(col_list=[0,1]) #fetch the data by passing column list
print(mysheet.data) #Data is stored as a dataframe in data attribute

mysheet.plot_graph(x_col_name='timestamp',y_col_name='average_sales') #Plot and export the graph

mysheet.fetch_and_plot_graph(col_list=[0,1]) #fetch the data and plot the graph in one go