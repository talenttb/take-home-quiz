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


# Set up
### Required
* docker

#### steps
```bash
cp .env.example .env
```
```bash
cat VERSION
#edit .env
#replace config (include PRJ_VERSION with VERSION)
```
```bash
docker-compose build
docker-compose up

### without docker
python run.py server
```

### Optional
* python
* [pyenv](https://github.com/pyenv/pyenv#installation)


```bash
pipenv install --dev
```

# Test
```bash
pytest
```

# Document
## create short url
```bash
curl --request POST \
  --url http://127.0.0.1:5000/urls \
  --header 'content-type: application/json' \
  --data '{"original":"http://test.com"}'

###
{
  "expired_at": "Fri, 03 Jul 2020 07:22:00 GMT",
  "original_url": "http://test.com",
  "short_url": "hddKfMAN"
}
```

## convert short url to original url
```bash
curl --request GET \
  --url http://127.0.0.1:5000/{short url}

###
<html>

<head>
    <title>Redirecting...</title>
	...
	<script>
        var data = {"identity": "426eb752-5afc-5cdb-9dae-8a81712869e2", "log_url": "http://127.0.0.1:5000/logs/TMjybPTK/426eb752-5afc-5cdb-9dae-8a81712869e2", "ori_url": "http://google.com", "short_url": "TMjybPTK"};
        console.table(data);

		......
		window.location = data.ori_url;

    </script>
</html>
```

## collect request logs
```bash
curl --request POST \
  --url http://127.0.0.1:5000/logs/{u}/{identity} \
  --header 'content-type: application/json' \
  --data '{"data":{.........}}'

###
status: 200
{}
```


## db
```sql
-- Drop table

-- DROP TABLE public.url_mapping;

CREATE TABLE public.url_mapping (
	short_url varchar(8) NOT NULL,
	original_url text NOT NULL,
	created_at timestamptz NOT NULL,
	expired_at timestamptz NOT NULL,
	CONSTRAINT url_mapping_pk PRIMARY KEY (short_url)
);

-- Drop table

-- DROP TABLE public.req_logs;

CREATE TABLE public.req_logs (
	"identity" uuid NOT NULL,
	user_data json NOT NULL,
	created_at timestamptz NOT NULL,
	short_url varchar(8) NULL,
	CONSTRAINT req_logs_un UNIQUE (identity, short_url)
);
```

# Cheatsheet

## docker
```bash
docker build -t quiz2-img:$(cat VERSION) .
```
```bash
docker run -it --rm -p 5000:5000 quiz2-img
```
```bash
docker-compose build
```

### if mac os get clang error:
```bash
export LDFLAGS="-L/usr/local/opt/openssl/lib"
export CPPFLAGS="-I/usr/local/opt/openssl/include"
```