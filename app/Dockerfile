# 
FROM python:3.9

# 
WORKDIR /code
# COPY . .
# 
COPY ./requirements.txt /code/requirements.txt
COPY ./app /code/app

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# 
#
COPY ./script.sh /code/script.sh

CMD [ "/bin/sh","-c", "sh script.sh" ] 