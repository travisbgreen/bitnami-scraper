# bitnami-scraper
Generates a list of urls to download Bitnami's very cool VMs

## usage
```
$ ~/scripts/bitnami-scraper/bitnami_scrape.py
Found 134 matches.
list complete, now run the following command:
wget -nc --continue -i tmpfile
```

## why?
To create & update an archive of server releases for future CVE research. 

Example:
```
<...>
917M	bitnami-sonarqube-10.1.0-r0-debian-11-amd64.ova
1.2G	bitnami-sonarqube-10.4.1-r0-debian-12-amd64.ova
1.3G	bitnami-sonarqube-8.7.0.41497-0-linux-debian-10-x86_64.ova
972M	bitnami-sonarqube-8.9.6-3-r01-linux-debian-10-x86_64-nami.ova
968M	bitnami-sonarqube-8.9.8-0-linux-debian-10-x86_64-nami.ova
980M	bitnami-sonarqube-9.2.4-6-r01-linux-debian-10-x86_64-nami.ova
991M	bitnami-sonarqube-9.4.0-2-linux-debian-10-x86_64-nami.ova
846M	bitnami-sonarqube-9.9.1-r1-debian-11-amd64.ova
913M	bitnami-sonarqube-9.9.4-r0-debian-12-amd64.ova
924M	bitnami-spree-4.1.12-2-linux-debian-10-x86_64.ova
938M	bitnami-spree-4.2.5-4-linux-debian-10-x86_64.ova
937M	bitnami-spree-4.2.5-6-linux-debian-10-x86_64.ova
558M	bitnami-subversion-1.14.1-1-linux-debian-10-x86_64.ova
477M	bitnami-subversion-1.14.1-27-r76-linux-debian-10-x86_64-nami.ova
473M	bitnami-subversion-1.14.2-0-linux-debian-10-x86_64-nami.ova
319M	bitnami-subversion-1.14.2-r40-debian-11-amd64.ova
461M	bitnami-subversion-1.14.3-r0-debian-12-amd64.ova
<...>
```
