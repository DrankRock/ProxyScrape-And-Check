# ProxyScrape-And-Check
Multithreaded free proxy scraper and checker with configurable timeout, website, proxy list, number of threads, with a nice GUI. Proxyscrapes scrapes proxies and checks them using requests and BeautifulSoup 4.

![ProxyScrape](https://user-images.githubusercontent.com/32172257/166814443-52f1cbb2-4475-40b1-96c1-92eeda4bba67.png)

### Important Notes
Free proxies are very unstable, so maybe that the working proxies won't work if tested immediately after. This software will work with any type of proxies for the checking, but will not give you great proxies in scraping mode, as they will be from free sources.

### Install
```shell
# clone the repo
$ git clone https://github.com/DrankRock/ProxyScrape-And-Check.git
# change the working directory to ProxyScrape-And-Check
$ cd ProxyScrape-And-Check/
# download required packages
$ python3 -m pip install -r requirements.txt
```

### Usage
```shell
$ python ProxyScrape.py
```

#### Terminal/Console version
```
$ python ProxyScrape.py --help
usage: ProxyScrape.py [-h] [-i INPUT [INPUT ...]] [-l [LOGFILE]] [-nc] [-ns]
                      [-o [OUTPUT]] [-te] [-th [THREADS]] [-ti [TIMEOUT]]
                      [-w [WEBSITE]]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        file containing http/https proxies to check (one or
                        more arguments)
  -l [LOGFILE], --logfile [LOGFILE]
                        Set the output to a logfile (default = False)
  -nc, --nocheck        De-Activate proxies checking
  -ns, --noscrape       De-Activate proxies scraping
  -o [OUTPUT], --output [OUTPUT]
                        select an output file for working proxies
  -te, --terminal       launch the terminal version
  -th [THREADS], --threads [THREADS]
                        number of threads (default = 50)
  -ti [TIMEOUT], --timeout [TIMEOUT]
                        timeout (default = 10)
  -w [WEBSITE], --website [WEBSITE]
                        website used for checking (default =
                        'https://www.google.com)'

$ python ProxyScrape.py -te -th 100 -ti 5
```
Please note that there is no `--gui` option, as by default, it will launch the gui version. 

### Features
* HTTP/HTTPS Proxies
* Completely free
* ~2800 proxies scraped


### Note
Please note that the menu is currently not working. It isn't necessary for basic functionnalities, I will add themes, advanced parameters, and a help in the future.

### Websites scraped
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt  
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt  
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt  
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt  
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http%2Bhttps.txt  
https://raw.githubusercontent.com/User-R3X/proxy-list/main/online/http%2Bs.txt  
https://openproxy.space/list/http  
https://free-proxy-list.net/  

### Websites to add 
https://spys.one/en/https-ssl-proxy/  
https://proxylist.geonode.com/  
https://api.proxyscrape.com/  

For any suggestion, you can contact me on discord 
