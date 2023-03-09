# Enable the user holberton to login and open files without error.

# Increase hard file limit for Holberton user.
exec { 'Increase hard limit':
    command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile unlimited/g" /etc/security/limits.conf',
    provider => 'shell'
}

# Increase soft file limit for Holberton user.
exec { 'Increase soft limit':
    command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 3000/g" /etc/security/limits.conf',
    provider => 'shell'
}
