# A simple-flask

### A. Requirements: Python flask is required.
```
pip install flask
pip install flask-cors
```

### B. Run:
```
python app.py
```
Go to http://localhost:5000/. 

Also try the following: 
- http://localhost:5000/classifier?value=hello 
- http://localhost:5000/ajax 

### C. How it works.

```
.
+-- static
|   +-- css/bootstrap.min.css
|   +-- js/bootsrap.min.js
+-- templates
|   +-- index.html
|   +-- ajax.html                  ---------  (3)
+-- app.py                         ---------  (1)
+-- model.py                       ---------  (2)
```

##### (1) app.py is the entry point for the application server. 
##### (2) model.py can be the entry point for your classifier
##### (3) ajax.html is an example to run an ajax call on document load.
