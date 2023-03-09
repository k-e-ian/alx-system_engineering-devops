# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'file':
  onlyif   => 'test -e /etc/default/nginx',
  command  => 'sed -i "5s/[0-9]\+/$( ulimit -n )/" /etc/default/nginx; service nginx restart',
  provider => shell,
}
