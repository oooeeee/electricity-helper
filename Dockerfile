FROM node:13.7.0-alpine as node
WORKDIR /root/workdir
ADD frontend/package.json ./package.json
# install node packages
RUN npm set progress=false && npm install
# copy frontend source to container
ADD frontend .
# compiling source
RUN npm run build

FROM python:3.7.4
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . /code
# copying compiled sources to new python env
COPY --from=node /root/workdir/dist /code/frontend/dist
WORKDIR /code/backend
ENV PYTHONPATH /code:/code/
CMD python3.7 app.py
