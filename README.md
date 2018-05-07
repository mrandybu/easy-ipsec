# easy-ipsec
easy-ipsec is designed to quickly deploy a tunnel type of site-to-site. 
easy-ipsec automatically raises the tunnel between two remote networks, users can only exchange keys.
Generation of keys, installation of dependencies and configuration of the firewall occur automatically after the script is run.

How does it work
------------------
1. Clone the repository anywhere
2. For auto-installing use 'sudo ./setup'
3. Run the easy-ipsec (sudo easy-ipsec)

**ipsec parameters**

required parameters

    launch type
    --init - at the first start or reconfiguration. the option clears, 
    if any, the old attachment files and initializes the new ones.
    --reboot - reboots the current configuration. Required if the configuration was broken.

    authentication type
    --cer - certificate
    --psk - pre-shared key

    first and second networks
    At start it is required to specify on what network the script is launched. 
    --mun --san respectively. It is necessary for the correct definition of subnets.

    the gateway address of the remote network.

optional parameters

    --debug - includes output of information on all stages of ipsec execution.
    --chekoff - disables most of the checks. Required if an error occurred. 
    
When the configuration was successful, you can manage the ipsec connection use 'sudo service easy-ipsec PARAM'

If you doubt the compatibility with your distribution or if there was an error while configuring connections, 
you can try to start the configuration with the parameter '--chekoff'. But you must first 
set all the dependencies yourself.
At this moment easy-ipsec supports only ipv4 and connections type of site-to-site 
but this will be fixed in the near future ;)

3. After the ipsec is executed in the current directory, a file of the format .p12 appears. 
It contains the encrypted certificate and the key to it. It must be passed to the other 
end of the future tunnel and runed the auth-apply which has two parameters type of authentication used and file .p12.

4. At the second end, you must do the same.

5. After that you can raise tunnel, stop tunnel, restart tunnel using etcnet-ipsec.
