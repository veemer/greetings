##

PROJECT_NAME=androidgreetings

## install software

sudo apt-get update

sudo apt-get install git -y

sudo apt-get install python-dev -y
sudo apt-get install python-pip -y

#sudo apt-get install libxml2-dev -y
#sudo apt-get install libxslt1-dev -y
#sudo apt-get install libcurl4-openssl-dev -y

sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password 1'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 1'
sudo apt-get -y install mysql-server
sudo apt-get install libmysqlclient-dev -y

#create database

sudo mysql -uroot -p1 -e 'create database vagrant character set utf8'

# create production_settings.py

cat > /vagrant/$PROJECT_NAME/production_settings.py <<EOF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'vagrant',
        'USER': 'root',
        'PASSWORD': 1
    }
}
EOF


# set up django project

cd /vagrant 
sudo pip install -r req.txt
./manage.py syncdb --noinput
./manage.py migrate

#create django superuser

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | ./manage.py shell
