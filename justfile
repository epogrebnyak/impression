package := "ssg"

# launch streamlit app
st:
  streamlit run streamlit_app.py

# black and isort
lint:  
   black .
   isort .

# create rst source for API documentation
apidoc:
  sphinx-apidoc -o docs src/{{package}}

# build and show documentation in browser
docs:
  sphinx-build -a docs docs/site
  start docs/site/index.html