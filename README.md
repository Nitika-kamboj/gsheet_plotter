<h1 style="text-align:center;">GSheet Plotter</h1>

An interface to plot graphs using data from your Google Spreadsheets.

Features:

- Fetch spreadsheet from ID
- Plot 2D graphs using any two columns
- Export graphs in .png

---

# Quick Links to get up and running
- [Installation](#Installation)
- [Usage](#Usage)
- [Available Methods](#Available-methods)


# Installation:
## Install GSheet Plotter
```sh
pip install gsheet_plotter
```
---
## Download a credentials file(.json) to allow access to GSheet Plotter to access your spreadsheets.
- Go to (https://console.developers.google.com)[Google Developer Console] and login with your Google account.
- In the left pane click on ```Credentials```

![Step1](https://iili.io/3nHAZX.png)

- Click on ```Create Credentials```

![Step2](images/Step2.png)

- In the dropdown, choose ```Service Account```

![Step3](images/Step3.png)

- Fill in the details, and click on ```Create```

![Step4](images/Step4.png)

- Click on ```Done```

- Go back to your dashboard and you'll see new credentials added with the information you entered.

- Click on the <strong>Edit</strong> icon

![Step5](images/Step5.png)

- Goto <strong>Keys</strong> on ```Add Key```.

- Download the <strong>JSON</strong> file and move to the working directory.

---
# Usage:

  - Instantiate the class by passing Google Service Account json file,Sheet Id found in the Google Sheet URL and the work sheet name

![plot_data](images/initialize.png)

  - Fetch data from the sheet to a pandas dataframe. The dataframe is saved in the ```data``` attribute.
  
![plot_data](images/fetch_data.png)

  - Plot the graph by using two column names
 
![plot_data](images/plot_data.png)

  - Additional method- Fetch the data and plot the graph in one go by passing the column list 
 
![plot_data](images/fetch_and_plot.png)

---
# Available methods 

![plot_data](images/method_details.png)











