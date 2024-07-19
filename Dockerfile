FROM ubuntu

# Install all generic software
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install -y apache2
RUN apt install -y apache2-utils
RUN apt install -y libapache2-mod-wsgi-py3

# Install all python packages
COPY requirements.txt .
RUN pip3 install --break-system-packages -r requirements.txt

# Copy the Django project
COPY pigs /var/cv

# Prepare Apache
ADD apache.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod wsgi

# Expose the port and start Apache
EXPOSE 80

CMD ["bash", "/var/cv/start"]