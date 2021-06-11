import os



def nmap_scan(data,host):

    #scan tcp ports
    if 'tcp' in data:
        os.system('nmap -sT {}'.format(host))

    #scan udp ports
    elif 'udp' in data:
        os.system('nmap -sU 20 {}'.format(host))

    #scan top ports
    elif 'top port' in data:
        os.system('nmap -top-ports 20 {}'.format(host))

    #scan for detect os
    elif 'os' in data:
        os.system('nmap -sV 20 {}'.format(host))
    
#nmap_scan('scan top ports','localhost')