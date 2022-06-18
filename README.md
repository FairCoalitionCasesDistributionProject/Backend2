# Running and installing
## Clone the repository
``` git clone https://github.com/FairCoalitionCasesDistributionProject/Backend.git```

## Setting a virtual enviorment
It is strongly recommanded to use python virtual enviorment.<br />
### Install
``` pip install --user virtualenv```

### Create
``` python -m venv env ```

### Activate
``` .\env\Scripts\activate ```

[More information](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

## Installing dependencies
``` pip install -r requirements.txt```

## Running local server
At the main directory run:<br />
``` python manage.py runserver ```<br />

Which can be viewed at the url:<br /> http://127.0.0.1:8000/api/ <br />
<br />
Send a json using the format: <br />
``` {"key": "1.1.1.1.1.1.1", "items": 2, "mandates": [1, 1], "preferences": [[1, 1], [1, 1]]} ```

## To run unit tests at /api/tests.py
At the main directory run:<br />
``` python manage.py test ```
