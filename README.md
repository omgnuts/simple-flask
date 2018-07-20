# A simple-flask

### A. Requirements: Python flask is required: 
```
pip install flask
```

### B. Run:
```
python app.py
```
Go to http://localhost:5000/. Also try http://localhost:5000/classifier?value=hello 

### C. How it works.

```
.
+-- static
|   +-- css/bootstrap.min.css
|   +-- js/bootsrap.min.js
+-- templates
|   +-- index.html
+-- app.py                         ---------  (1)
+-- model.py                       ---------  (1)
```

##### (1) app.py is the entry point for the application server. 
##### (2) model.py can be the entry point for your classifier
