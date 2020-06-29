# Easy network packet capture

## Linux  
output the raw trace to a file in a Wireshark compatible format  
start:
```
tcpdump -i eth0 -w trace.cap
```


filter | description | example
-------|-------------|--------
host | IP/host as source/destination address | host 172.16.0.1
src | |  src 192.168.0.5
dst | | dst 192.168.0.1
net | network range (in CIDR notation) | net 172.168.0.0/24
port |tcp/udp port) | port 53
portrange | tcp/udp portrange | portrange 0-1023
proto | ether, ip/ip6, tcp/udp | proto udp


<br>

output to terminal example:  
```
tcpdump -i eth0 -q -n '(host 10.0.0.1) and (udp port 53) or (tcp port 80)'
```

options:  
-n -> don't resolve hostnames  
-q -> reduced output  



<br>
<br>
<br>



## Windows  
start:
```
netsh trace start capture=yes IPv4.Address=x.x.x.x
```
stop:
```
netsh trace stop
```
The trace will be saved as a .etl file.
It can be opened with the "Microsoft Message Analyzer" and then converted to the Wireshark compatible .cap format.

Microsoft Message Analyzer is discontinued but available through archive.org  
Download:  
http://web.archive.org/web/20190420141924/https://download.microsoft.com/download/2/8/3/283DE38A-5164-49DB-9883-9D1CC432174D/MessageAnalyzer64.msi
