# HuaweiMeter
Command-line program to show current data usage from the Huawei Mobile WiFi router's API. 


## Gotchas
The software will read data-cap from the API, and will only really work on GB usage, but can easily be adapted to count MB instead. Code is hacked together on vacation, expect stuff to break.


## Initiation:
You can provide an integer as argument to specify the update interval. Data will be fetched from the API of the router, so only local connections will be made, and thus not incur traffic on your mobile connection.

	main.py 10

This will set an update interval of 10 seconds. The default IP for the router API is set to 192.168.0.1, the default IP of the Huawei mobile routers. If you have changed this, you need to provide the IP to the GigReader object.

## Example Output:

[██████████████████████████████████████████------------------] 6.99 GB / 10.0 GB