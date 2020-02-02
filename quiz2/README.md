How to use this project
===

# Planning
1. The length of a shortened path should start from 2 letters and be unique.
    I will pick 8 latters from [base 64 charaters](https://base64.guru/learn/base64-characters) except 1(numbers) ,I(upper-case I) ,l(lower-case L) and begin with 2 letters.
The uniqueness will be set on database with Primary Key, or UNIQUE constraint.
1. The website should be able to redirect the user to the original url.
    I will build one endpoint which input is short term url and output is html format with status code as 200, javascript code(original url is inclued).
1. Stakeholder wants to do some data exploration among the shortened urls.
I will collect data on the page just returned to the client. The steps like 1. client have a short url and it make a request to us to get original url. 2. we will check wheather short url is valid and find where is the original url and return a html page. 3. when client gets the html page, browser will be loading the code(html, css, js), sendind data to us, removing history, and redirect(window.location.href by js) to original url.
1. technology and architecture
I will use the postgresql as our database, redis as cache service, and rabbitmq as message queue, because it is easier in one docker file for presentation. In real world, I will choose kafka as my message queue service.

# Required
* python
* [pyenv](https://github.com/pyenv/pyenv#installation)

# Set up
```bash
pipenv install --dev
```

# Run
```bash
python run.py
```

# Test
```bash
pytest
```

# Document
