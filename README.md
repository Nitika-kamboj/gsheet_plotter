<h1 style="text-align:center;">GSheet Plotter</h1>

An interface to plot graphs using data from your Google Spreadsheets.

Features:

- Fetch spreadsheet from ID
- Plot 2D graphs using any two columns
- Export graphs in .png

---

# Installation:
## Install GSheet Plotter
```sh
pip install gsheet_plotter
```
# Usage:
# Initialize the library and select the desired Google sheet
  - Instantiate the class by passing Google Service Account json file,Sheet Id found in the Google Sheet URL and the work sheet name.

![plot_data](images/initialize.png)

# Other Features

- Go through your data
![fetch_data](images/fetch_data.png)

## Download a credentials file(.json) to allow access to GSheet Plotter to access your spreadsheets.
- Go to (https://console.developers.google.com/)[Google Developer Console] and login with your Google account.
- In the left pane click on ```Credentials```

![Step1](images/Step1.png)

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









