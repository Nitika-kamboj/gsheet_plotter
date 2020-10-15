from gsheets import Sheets
import matplotlib.pyplot as plt

class GsheetPlotter:

    def __init__(self,client_secrets):
        try:
            self.sheets=Sheets.from_files(client_secrets)
            self.sheet=None
            self.worksheet=None
        except:
            print("Credential file error")
    
    def get_sheet_by_url(self,sheet_url):
        try:
            sheet=self.sheets.get(sheet_url)
            if sheet is None:
                print("Sheet with url {} does not exist.".format(sheet_url))
            else:
                print("Sheet is successfully loaded.")
                self.sheet=sheet
        except:
            print("Sheet with url {} does not exist.".format(sheet_url))
    
    def get_sheet_by_id(self,sheet_id):
        try:
            sheet=self.sheets[sheet_id]
            print("Sheet is successfully loaded.")
            self.sheet=sheet
        except:
            print("Sheet with id {} does not exist.".format(sheet_id))
    
    def get_worksheet_by_name(self,sheet_name):
        try:
            worksheet=self.sheet.find(sheet_name)
            try:
                self.worksheet =worksheet.to_frame()
            except:
                print("Worksheet with name '{}' has no data to fetch.".format(sheet_name))
        except:
            print(self.worksheet)
            print("Worksheet with name '{}' does not exist.".format(sheet_name))
    
    def get_worksheet_by_index(self,sheet_index):
        try:
            worksheet=self.sheet.sheets[sheet_index]
            try:
                self.worksheet=worksheet.to_frame()
            except:
                print("Worksheet at index {} has no data to fetch.".format(sheet_index))
        except:
            print("Worksheet at index {} does not exist.".format(sheet_index))
    
    def plot_graph(self,x_col_name,y_col_name):
        try:
            plt.plot(self.worksheet[x_col_name],self.worksheet[y_col_name])
            filename=x_col_name + '_' + y_col_name + '.png'
            plt.savefig(filename)
            print("Your graph is saved as '{}'".format(filename))
        except:
            print("Column does not exist.")

if __name__=='__main__':
    plotter=GsheetPlotter('client_secrets.json')
    url=input("Enter your url")
    plotter.get_sheet_by_url(url)
    sheet=input("Enter name")
    plotter.get_worksheet_by_name(sheet)
    plotter.plot_graph('timestamp','average_sales')