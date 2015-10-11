#!/usr/bin/python


#using element tree to parse the xml configuration
import xml.etree.ElementTree as ET
import os

#Creating a blank html file, erase previous if exist
webconfig = open("configuration.html", "w")

#Creatin the HTML file head, including the CSS style and the script to create draggable columns
webconfig.write('<!DOCTYPE html>\n')
webconfig.write('<html>\n')
webconfig.write('<head>\n')
webconfig.write('<title>PAN-OS configuration</title>\n')
webconfig.write('<link rel="stylesheet" type="text/css" href="http://rawgithub.com/akottr/dragtable/master/dragtable.css">\n')
webconfig.write('<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n')
webconfig.write('<script src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js"></script>\n')
webconfig.write('<script src="http://rawgithub.com/akottr/dragtable/master/jquery.dragtable.js"></script>\n')
webconfig.write('<script>\n')
webconfig.write('$(document).ready(function() {\n')  
webconfig.write("$('#security').dragtable();\n")   
webconfig.write('});\n')
webconfig.write('</script>\n')
webconfig.write('<style>\n')
webconfig.write('table, td, th {')
webconfig.write('\tborder: 1px solid green;')
webconfig.write('\tfont-size: 1em;\n')
webconfig.write('\tborder: 1px solid #98bf21;\n')
webconfig.write('\tpadding: 3px 7px 2px 7px;\n')
webconfig.write('\tborder-collapse: collapse;\n')
webconfig.write("\ttext-align: left;\n}\n")
webconfig.write('\tth {\n')
webconfig.write('\tpadding-top: 5px;\n')
webconfig.write('\tpadding-bottom: 4px;\n')
webconfig.write("\tbackground-color: #A7C942;\n")
webconfig.write("\tcolor: #ffffff;\n}\n")
webconfig.write('tr.odd td {\n')
webconfig.write("\tcolor: #000000;\n")
webconfig.write("\tbackground-color: #EAF2D3;\n}\n")
webconfig.write('ul.a {\n')
webconfig.write('\tlist-style-type: none;\n')
webconfig.write('\tlist-style-type: none;\n')
webconfig.write('\tpadding: 0px;\n')
webconfig.write('\tmargin: 0px;\n}\n')
webconfig.write('</style>\n')
webconfig.write('</head>\n')
webconfig.write('<body>\n')

#Security policy table start
webconfig.write ("<table id='security'>\n")
#Html table titles
webconfig.write (' <thead>\n')
webconfig.write (' <tr>\n')
webconfig.write ('\t<th>Policy name</th>\n')
webconfig.write ('\t<th>Source Zone</th>\n')
webconfig.write ('\t<th>Source</th>\n')
webconfig.write ('\t<th>Source User</th>\n')
webconfig.write ('\t<th>HIP Profiles</th>\n')
webconfig.write ('\t<th>Destination Zone</th>\n')
webconfig.write ('\t<th>Destination</th>\n')
webconfig.write ('\t<th>Service</th>\n')
webconfig.write ('\t<th>Application</th>\n')
webconfig.write ('\t<th>URL Category</th>\n')
webconfig.write ('\t<th>Action</th>\n')
webconfig.write (' </tr>\n')
webconfig.write (' </thead>\n\n')
webconfig.write (' <tbody>\n')
#Importing the configuration with element tree
tree = ET.ElementTree(file='config.xml')

#HTML table used while writing the HTML file
startcell='\t<td><ul class="a">\n'
endcell='\t\t</ul>\n\t</td>\n'
startlist='\t\t<li>'
endlist='</li>\n'

#parsing the configuration and creating HTML security policy table
toogle= False
for elem in tree.iterfind('devices/entry/vsys/entry/rulebase/security/rules/entry'):
    toogle= not toogle
    if toogle:
        cssTr="even"
    else:
        cssTr='odd'
    webconfig.write (" <tr class='"+cssTr+"'>\n\t<td>"+elem.attrib['name']+'</td>\n')  #printing policy name
    webconfig.write (startcell)                       #Printing source zone
    for szone in elem.iterfind('from/member'):                       
        webconfig.write (startlist+szone.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #Printing source(s)
    for source in elem.iterfind('source/member'):                       
        webconfig.write (startlist+source.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #Printing source user(s)
    for suser in elem.iterfind('source-user/member'):                       
        webconfig.write (startlist+suser.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #Printing HIP profile(s)
    for HIP in elem.iterfind('hip-profiles/member'):                       
        webconfig.write (startlist+HIP.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                      #printing destination zone
    for dzone in elem.iterfind('to/member'):                          
        webconfig.write (startlist+dzone.text+endlist)
    webconfig.write (startcell)                       #Printing destination(s)
    for destination in elem.iterfind('destination/member'):                       
        webconfig.write (startlist+destination.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #Printing service(s)
    for service in elem.iterfind('service/member'):                       
        webconfig.write (startlist+service.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #Printing application(s)
    for application in elem.iterfind('application/member'):                       
        webconfig.write (startlist+application.text+endlist)
    webconfig.write (endcell)
    webconfig.write (startcell)                       #URL categories(s)
    for category in elem.iterfind('category/member'):                       
        webconfig.write (startlist+category.text+endlist)
    webconfig.write (endcell)
    action = elem.find('action')                                      #Printing action
    webconfig.write ('\t\t<td>'+action.text+'</td>\n')
    webconfig.write ('\t</td>\n  </tr>\n')
#HTML end of security policy table
webconfig.write (' </tbody>\n')
webconfig.write ('</table>\n')
webconfig.write('</body>')
webconfig.close()

os.system("start "+'configuration.html')
