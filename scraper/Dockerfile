FROM python:3.9.13-slim

RUN apt-get update; apt-get clean
RUN apt-get install -y wget
RUN apt-get install -y gnupg

RUN useradd apps
RUN mkdir -p /home/apps && chown apps:apps /home/apps

# Adding trusting keys to apt for repositories
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# Adding Google Chrome to the repositories
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
RUN apt-get install -y google-chrome-stable

# Installing Unzip
RUN apt-get install -yqq unzip

RUN wget -O /tmp/chromedriver-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/117.0.5938.149/linux64/chromedriver-linux64.zip

RUN unzip /tmp/chromedriver-linux64.zip -d /usr/local/bin/

# RUN dbus-uuidgen > /var/lib/dbus/machine-id
# RUN mkdir -p /var/run/dbus
# RUN dbus-daemon --config-file=/usr/share/dbus-1/system.conf --print-address


WORKDIR /app

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

# Pretty sure this is wrong.  I normally start this with flask --debug run.  gunicorn app:app is what starts it on render I think.
CMD ["flask", "run"]
EXPOSE 5000

