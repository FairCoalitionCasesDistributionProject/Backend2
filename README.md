# About
Backend of our [project](https://github.com/FairCoalitionCasesDistributionProject), made using [Django Rest Framework](https://www.django-rest-framework.org). Used to evaluate a fair division using [Fairpy](https://github.com/erelsgl/fairpy) implementations as well as to save/restore user sessions using [Firebase](https://firebase.google.com/) database.<br />
Deployed with [Heroku](https://www.heroku.com/). <br />


## Running and Installing Guide
* Clone Repository <br /> 
``` git clone https://github.com/FairCoalitionCasesDistributionProject/Backend.git```


* Virtual Enviorment Setup<br />
It is strongly recommended to use python virtual enviorment. [For more information.](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
  * Installation <br />
``` pip install --user virtualenv```

  * Creation <br />
``` python -m venv env ```

  * Activation <br />
``` .\env\Scripts\activate ```


* Dependencies installation
``` pip install -r requirements.txt```

### Running Local Server
Run at the main directory:<br />
``` python manage.py runserver ```<br />

Can be viewed at the url:<br /> 
http://127.0.0.1:8000/api/ <br />
<br />
At the form send a json using the format: <br />
``` {"key": "1.1", "items": 3, "mandates": [1, 1], "preferences": [[1, 1, 1], [1, 1, 1]]} ```

### Running Unit Tests at /api/tests.py
At the main directory run:<br />
``` python manage.py test ```








