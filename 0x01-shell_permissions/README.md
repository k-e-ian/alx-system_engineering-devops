su betty - switch user to betty
whoami - prints effective username of current user
groups - prints all the groups the current user is part of
chown betty hello - change ownership of file hello to betty
touch hello - create empty file hello
chmod u+x hello - change hello to an executable file
chmod gu+x,o-r hello - changes maultiple permisions
chmod --reference=olleh hello - mirror permissions of hello referenced to olleh
chown vincent:staff * - change owner and group fro every file and subdirectories in the current working directory
chown -h for symbolic links
chown --from=guillaume betty hello - if only owned by guillaume
chmod ugo+x */ for only directories
mkdir -m make directories with permissions
chown :school hello change owner group of file hello
telnet towel.blinkenlights.nl to watch Star wars episode iv in your terminal 
