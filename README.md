# Project Description

This project is a simple chatbot API built on flask using OpenAI GPT-3.5 turbo LLM. it provides two APIs to interact with the chatbot
- GET ('/') : it sends a welcome message from chatbot 
- POST ('/chat') : it allwows the users to make conversition with the chatbot and receive chatbot response as a json by the model.  
---
# Prerequisites
- Python > 3.6
  if could be installed from https://www.python.org/downloads/    
  You can check you python verison using this command:
  ```
  python --version
  ```
- all other dependencies mentioned in the `requirements.txt` file
---
# Setup and run  

## Setup 
- Clone repository.

```
git clone https://github.com/mohammed3bbas/ChatGPTWrapper.git
```
- Change to project root directory.
```
cd .\ChatGPTWrapper\
```
- Create a `.env` file in the project root directory, containing your OpenAI secret key in the following format:

```
OPENAI_API_KEY='YOUR_SECRET_OPENAI_KEY'
```
- create virtual enviroment (if you are Windows user you can skip this and follow instruction [here](#for-windows-users) .
```
python -m venv .venv
```
- activate your virtual enviroment.
```
.venv\Scripts\activate
```
- install all dependancies .
```
pip install -r requirements.txt
```
## Run server
- go to app directory.
```
cd .\app\
```
- run flask server (by default port 5000)
```
run flask 
```
if you want to run in different port use this: 
```
run flask  -p [PORT_NUMBER]
```

### For Windows Users

- Create virtual enviroment, install project dependencies and run the server by using this cmd script.

```
.\run_app.cmd [PORT_NUMBER]
```
By default, the server runs on port 5000, but you can specify a different port if needed:     
Example :
```
./run_app.cmd 8080
```
or run on default port (5000)
```
./run_app.cmd
```

## Run unit tests

- this project is covered by unit tests using Pytest, to run unit tests
```
pytest .\tests
```

---




  
