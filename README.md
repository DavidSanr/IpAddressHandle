# IpAddressHandle
## Algorith for handle ip address and get the most commond request 




1.  Create a custom sorting algorithm optimizer for big amount of data.

2.  RequestHandle Method has an O(1)
    TOP100 method, has O(N LOG N ) in the worst case, an avg of O(n log n).

3.  The method handles the data in a dictionary with the IP address as key, then adds to the value of this key a 1 if it is repeated as a parameter.

    The Top100 method organizes the data with the value of the key in the dictionary and obtains the first 100 values.

4.  organize all the data with the value of repeated IP instead of the IP address like a key.

5.  Generate 20 000 000 IP with a library for mocks data.

