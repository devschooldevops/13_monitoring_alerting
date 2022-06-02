FROM python:3
ADD products/ products
WORKDIR /products
RUN pip3 install -r requirements.txt
# Used to make sure that the flask app is reachable from every network interface from the container
CMD flask run --host 0.0.0.0