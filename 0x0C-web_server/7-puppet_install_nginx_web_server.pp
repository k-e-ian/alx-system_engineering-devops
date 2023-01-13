# Nginx server installation
# redirection must be '301 Moved Permanently'
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page) 
# using curl, it must return a page that contains the string Hello World!
exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/google.com\ permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
