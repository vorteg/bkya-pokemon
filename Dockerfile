FROM python:3.10.5-slim

WORKDIR /pokeapi
# Install dependencies
COPY requirements.txt /tmp
RUN cd /tmp && \
    pip install --upgrade pip \
    pip install -r requirements.txt 

CMD ["bash", "./run.sh"]