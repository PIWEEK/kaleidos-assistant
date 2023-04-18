### How to start

Install a new virtual environment for Python
```shell
python3.10 -m venv .venv
```

Load the .venv
```shell
. .venv/bin/activate
```

Install the requirements
```shell
pip install -r requirements.txt
```

Create an `.env` file with your valid [OPEN_API_KEY](https://platform.openai.com/account/api-keys)
```
OPENAI_API_KEY=sk-JizVlXDGbYULx...
```

### Making questions

Define your domain and URL to read and process as an input in `webqa.py`

```python
# Define root domain to crawl
domain = "libro-blanco.kaleidos.net"
full_url = "https://libro-blanco.kaleidos.net/"
```

Enter the python CLI, import the function asking ChatGPC (1), define your question (2), and finally ask for a response (3): 

`$ python`
```python
>>> from main import answer  # (1)
>>> QUESTION = "Qué flexibilidades hay"  # (2)
>>> answer(QUESTION)  # (3)
```

Complete example:


```python
$ python
Python 3.10.2 (main, Nov 15 2022, 09:21:37) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import answer
https://libro-blanco.kaleidos.net/
>>> QUESTION = "Qué flexibilidades hay"
>>> answer(QUESTION)
En Kaleidos hay flexibilidades para trabajar en remoto, para decidir el horario, para tomarse un par de horas cualquier día por alguna incidencia, para asistir a eventos, para formación, y para solicitar una reducción de jornada.
```

### Tokens limit

The model being used ('text-davinci-003') support a maximum context length of 4097 tokens. 

You could use the answer's parameters (`max_len`/`max_tokens`) to suit this limit.


### References
- https://platform.openai.com/docs/tutorials/web-qa-embeddings
- https://github.com/openai/openai-cookbook/tree/main/apps/web-crawl-q-and-a
