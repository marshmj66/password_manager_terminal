import time
from datetime import datetime as dt

sites_to_block = [
    'www.facebook.com',  'facebook.com',
    'www.instagram.com', 'instagram.com',
    'www.hulu.com', 'hulu.com'
]

Linux_host = '/etc/hosts'
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Linux_host
finder = [Linux_host,Window_host]
redirect = "127.0.0.1"

def block_websites(start_hour , end_hour):
    while True:
        #if True:
        if dt(dt.now().year, dt.now().month, dt.now().day,start_hour)< dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,end_hour):
            print("Do the work ....")
            try:
                with open(finder[0], 'r+') as hostfile:
                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            print(hosts)
                            hostfile.write(redirect+' '+site+'\n')
            except:
                with open(finder[1], 'r+') as hostfile:
                    hosts = hostfile.read()
                    for site in sites_to_block:
                        if site not in hosts:
                            print(hosts)
                            hostfile.write(redirect + ' ' + site + '\n')

        else:
            with open(Window_host, 'r+') as hostfile:
                hosts = hostfile.readlines()
                hostfile.seek(0)
                for host in hosts:
                    if not any(site in host for site in sites_to_block):
                        hostfile.write(host)
                hostfile.truncate()
            print('Good Time')
        time.sleep(3)
if __name__ == '__main__':
    block_websites(9, 18)