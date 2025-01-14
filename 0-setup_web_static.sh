#!/usr/bin/env bash
# The Bash script that sets up your web servers for the deployment of 'web_static'.

echo -e "\e[1;35m START CONFIGURATION\e[0m\n"

sudo apt-get -y update
sudo apt-get -y install nginx
echo -e "\e[1;35m Nginx Installed\e[0m\n"

sudo ufw allow 'Nginx HTTP'
echo -e "\e[1;35m Allow incoming traffic on the default HTTP port\e[0m\n"

sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo -e "\e[1;35m Directories created\e[0m\n"
echo "<h1>Welcome to hajaralx.tech site</h1>" > /data/web_static/releases/test/index.html
echo -e "\e[1;35m Simple content page added\e[0m\n"
# The current
if [ -d /data/web_static/current ];
then
	echo "Remove the existing /data/web_static/current"
	sudo rm -rf /data/web_static/current;
fi;
echo -e "\e[1;35m The existing of /data/web_static/current dir checked\e[0m\n"

# The data web
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
echo -e "\e[1;35m Symbolic link created\e[0m\n"
sudo chown -hR ubuntu:ubuntu /data
echo -e "\e[1;35m User & Group setted\e[0m\n"
sudo sed -i '47i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'
echo -e "\e[1;35m Serve /data/web_static/current/ to hbnb_static\e[0m\n"
sudo service nginx restart
echo -e "\e[1;35m Nginx service restarted\e[0m\n"

echo -e "\e[1;35m END CONFIGURATION\e[0m\n"
