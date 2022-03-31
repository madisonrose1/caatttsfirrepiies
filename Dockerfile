FROM sandy1709/catuserbot:slim-buster

COPY . .

# Install requirements
RUN python3 -m ensurepip --default-pip &&\
    python3 -m pip install --upgrade pip wheel setuptools &&\
    python3 -m pip install -r requirements.txt

CMD ["bash","start"]
