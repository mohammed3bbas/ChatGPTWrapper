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
- Clone repository

```
git clone https://github.com/mohammed3bbas/ChatGPTWrapper.git
```
- Create a `.env` file in the project root directory, containing your OpenAI secret key in the following format:

```
OPENAI_API_KEY='YOUR_SECRET_OPENAI_KEY'
```
## For windows

- Install the project dependencies and run the server. By default, the server runs on port 5000, but you can specify a different port if needed: 


```
.\run_app.cmd (PORT_NUMBER)
```
Example 
```
./run_app.cmd 8080
```
or run on default port (5000)
```
./run_app.cmd
```



  
