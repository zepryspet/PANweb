# PANweb
Inspired in my previous script (wich is inspired in the web checkpoint tool) screepa.pl that parses the netscreen firewall config https://github.com/zepryspet/screpa
This new script was created using python (learned in the hard way)
Steps to see the configuration in the webpage:
1. Keep up to date, download  and install python 3+ https://www.python.org/downloads/
2. Download the configuration file from the palo alto firewall and save it as config.xml
3. Download the python script PANweb.py into the same folder as the configuration file
4. Execute the pytho script (double click on windows)
5. The file should be opened automatically, if not search for a file name configuration.html in the same folder you can open it with your favorite browser (please don't use IE) or with excel

Know issues:
-Not able to hide columns (thinking the better way to do it as an end user)
-Missing support for tags and disabled policies
-Not multi vsys capability (I don't need it but can be added with more logic)
-Not able to see pofiles in security policies (I don't need it but can be added with more logic)
-Not able to see log action (I don't need it but can be added with more logic)
-Not able to see default rules exposed since PAN-OS 6.1 (I don't need it but can be added with more logic)
-Not able to see policy type: Universal, intrazonal, interzonal (I don't need it but can be added with more logic)
-Just able to see security policies, I'm thinking about add NAT policies and objects to the final dump file.

Notes:
-The final file uses dragtable to move the columns https://github.com/akottr/dragtable, if you don't have internet access to download the jquery repository that won't be possible.
-Tested in last chrome version and excel 2013 using PAN-OS 7.0 (it's possible to face some issue in previous versions)

