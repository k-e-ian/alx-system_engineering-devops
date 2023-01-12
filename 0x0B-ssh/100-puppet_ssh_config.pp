# changes to the configuration file, disable authentication

exec {'echo':
  path    => 'usr/bin:/bin',
  command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentic
ation no" >> /etc/ssh/ssh_config',
  returns => [0,1],
}
