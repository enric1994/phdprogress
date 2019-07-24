FROM python:3-alpine
MAINTAINER Enric Moreu <enric.moreu.filella@gmail.com>

ADD progress.py /src/progress.py
RUN pip install tqdm

ENTRYPOINT ["python3","-u","/src/progress.py"]

