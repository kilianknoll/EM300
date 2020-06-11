#
# Copyright: Kilian Knoll, 15.12.2018
# Utility to parse EnergyManager EM300LR using the JSON API
#
#
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
#  Please note that any incorrect or careless usage of this module as well as errors in the implementation can damage your Energy Manager!
#  Therefore, the author does not provide any guarantee or warranty concerning to correctness, functionality or performance and does not accept any liability for damage caused by this module, examples or mentioned information.
#  Thus, use it at your own risk!
#
#
#  Purpose: 
#  Returns:
#     Returnvalue: 0    (Everything all right)
#     Returnvalue: -1   (Crap happened)
#     em300data:        (Empty list in case Returnvalue =-1)
#     em300data:        (Full list of key-value pairs in case Returnvalue = 0)
#
# Tested with:
#           python 3.5, 3,7
#           B-control Energy Manager EM300, Firmware Version 2.04
# Based on: https://www.tq-automation.com/Service-Support/Downloads/Downloads-Energiemanagement
# Using the JSON Documentation: https://www.tq-automation.com/content/download/10996/file/TQ%20Energy%20Manager%20-%20JSON-API.0104.pdf
#

# Please change the following values to reflect your environment:
Em_IP_Adress = "192.168.178.27"
EM_Serialumber= "YourEM300Serialnumber"						#Serial Number can be found accessing the Energy Manager´s Web Page under  Settings - Serial number
EM_Password= "Yoursecretpwd"								#This is the password you have specified on the Energy Manager´s Web Page (without quotes)
# End Configurable Parameters 
#
import requests
import time 
import json
import time
import datetime
import logging
#from loggerdate import loggerdate
from pprint import pprint

myparams= {'login': EM_Serialumber, 'password': EM_Password, 'save_login': '1'}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; "
}
mySession = requests.Session()


def changeobiskeys(myjsoninput):
    myjsoninput["Active power_incoming"] =  myjsoninput.pop("1-0:1.4.0*255")
    myjsoninput["Active energy_incoming"] =  myjsoninput.pop("1-0:1.8.0*255")
    myjsoninput["Apparent power-"] =  myjsoninput.pop("1-0:10.4.0*255")
    myjsoninput["Apparent energy-"] =  myjsoninput.pop("1-0:10.8.0*255")
    myjsoninput["Power factor"] =  myjsoninput.pop("1-0:13.4.0*255")
    myjsoninput["Supply frequency"] =  myjsoninput.pop("1-0:14.4.0*255")
    myjsoninput["Active power- "] =  myjsoninput.pop("1-0:2.4.0*255")
    myjsoninput["Active energy-"] =  myjsoninput.pop("1-0:2.8.0*255")
    myjsoninput["Active power_incoming L1"] =  myjsoninput.pop("1-0:21.4.0*255")
    myjsoninput["Active energy_incoming L1"] =  myjsoninput.pop("1-0:21.8.0*255")
    myjsoninput["Active power- L1"] =  myjsoninput.pop("1-0:22.4.0*255")
    myjsoninput["Active energy- L1"] =  myjsoninput.pop("1-0:22.8.0*255")
    myjsoninput["Reactive power_incoming L1"] =  myjsoninput.pop("1-0:23.4.0*255")
    myjsoninput["Reactive energy_incoming L1"] =  myjsoninput.pop("1-0:23.8.0*255")
    myjsoninput["Reactive power- L1"] =  myjsoninput.pop("1-0:24.4.0*255")
    myjsoninput["Reactive energy- L1"] =  myjsoninput.pop("1-0:24.8.0*255")
    myjsoninput["Apparent power_incoming L1"] =  myjsoninput.pop("1-0:29.4.0*255")
    myjsoninput["Apparent energy_incoming L1"] =  myjsoninput.pop("1-0:29.8.0*255")
    myjsoninput["Reactive power_incoming"] =  myjsoninput.pop("1-0:3.4.0*255")
    myjsoninput["Reactive energy_incoming"] =  myjsoninput.pop("1-0:3.8.0*255")
    myjsoninput["Apparent power- L1"] =  myjsoninput.pop("1-0:30.4.0*255")
    myjsoninput["Apparent energy- L1"] =  myjsoninput.pop("1-0:30.8.0*255")
    myjsoninput["Current L1"] =  myjsoninput.pop("1-0:31.4.0*255")
    myjsoninput["Voltage L1"] =  myjsoninput.pop("1-0:32.4.0*255")
    myjsoninput["Power factor L1"] =  myjsoninput.pop("1-0:33.4.0*255")
    myjsoninput["Reactive power-"] =  myjsoninput.pop("1-0:4.4.0*255")
    myjsoninput["Reactive energy-"] =  myjsoninput.pop("1-0:4.8.0*255")
    myjsoninput["Active power_incoming L2"] =  myjsoninput.pop("1-0:41.4.0*255")
    myjsoninput["Active energy_incoming L2"] =  myjsoninput.pop("1-0:41.8.0*255")
    myjsoninput["Active power- L2"] =  myjsoninput.pop("1-0:42.4.0*255")
    myjsoninput["Active energy- L2"] =  myjsoninput.pop("1-0:42.8.0*255")
    myjsoninput["Reactive power_incoming L2"] =  myjsoninput.pop("1-0:43.4.0*255")
    myjsoninput["Reactive energy_incoming L2"] =  myjsoninput.pop("1-0:43.8.0*255")
    myjsoninput["Reactive power- L2"] =  myjsoninput.pop("1-0:44.4.0*255")
    myjsoninput["Reactive energy- L2"] =  myjsoninput.pop("1-0:44.8.0*255")
    myjsoninput["Apparent power_incoming L2"] =  myjsoninput.pop("1-0:49.4.0*255")
    myjsoninput["Apparent energy_incoming L2"] =  myjsoninput.pop("1-0:49.8.0*255")
    myjsoninput["Apparent power- L2"] =  myjsoninput.pop("1-0:50.4.0*255")
    myjsoninput["Apparent energy- L2"] =  myjsoninput.pop("1-0:50.8.0*255")
    myjsoninput["Current L2"] =  myjsoninput.pop("1-0:51.4.0*255")
    myjsoninput["Voltage L2"] =  myjsoninput.pop("1-0:52.4.0*255")
    myjsoninput["Power factor L2"] =  myjsoninput.pop("1-0:53.4.0*255")
    myjsoninput["Active power_incoming L3"] =  myjsoninput.pop("1-0:61.4.0*255")
    myjsoninput["Active energy_incoming L3"] =  myjsoninput.pop("1-0:61.8.0*255")
    myjsoninput["Active power- L3"] =  myjsoninput.pop("1-0:62.4.0*255")
    myjsoninput["Active energy- L3"] =  myjsoninput.pop("1-0:62.8.0*255")
    myjsoninput["Reactive power_incoming L3"] =  myjsoninput.pop("1-0:63.4.0*255")
    myjsoninput["Reactive energy_incoming L3"] =  myjsoninput.pop("1-0:63.8.0*255")
    myjsoninput["Reactive power- L3"] =  myjsoninput.pop("1-0:64.4.0*255")
    myjsoninput["Reactive energy- L3"] =  myjsoninput.pop("1-0:64.8.0*255")
    myjsoninput["Apparent power_incoming L3"] =  myjsoninput.pop("1-0:69.4.0*255")
    myjsoninput["Apparent energy_incoming L3"] =  myjsoninput.pop("1-0:69.8.0*255")
    myjsoninput["Apparent power- L3"] =  myjsoninput.pop("1-0:70.4.0*255")
    myjsoninput["Apparent energy- L3"] =  myjsoninput.pop("1-0:70.8.0*255")
    myjsoninput["Current L3"] =  myjsoninput.pop("1-0:71.4.0*255")
    myjsoninput["Voltage L3"] =  myjsoninput.pop("1-0:72.4.0*255")
    myjsoninput["Power factor L3"] =  myjsoninput.pop("1-0:73.4.0*255")
    myjsoninput["Apparent power_incoming"] =  myjsoninput.pop("1-0:9.4.0*255")
    myjsoninput["Apparent energy_incoming"] =  myjsoninput.pop("1-0:9.8.0*255")
    #serial
    #status
    return myjsoninput

def readenergymanager():
    try:
        #------------------------------------------------------------
        #Start Connection to Energymanager 
            
        #------------------------------------------------------------
        # Initial handshake
        print ("starting initial handshake - start step 1 ...")
        r1 = mySession.get('http://'+ Em_IP_Adress + '/start.php',  headers=headers)
        if (r1.status_code == requests.codes.ok):
            pass
        else:
            Error_Connecting = r1.status_code
            print ("Unable to connect :", Error_Connecting)
    except Exception as Error_ConnecttoEnergymanager:
        print ("Error accessing Energy Manager step1 :", Error_ConnecttoEnergymanager)		
        time.sleep(0.25)
        #------------------------------------------------------------
        # Authenticate with credentials
    try:    
        print ("trying to authenticate -start step 2 ...")
        r2 = mySession.post('http://'+ Em_IP_Adress + '/start.php',myparams,  headers=headers)
        if (r2.status_code == requests.codes.ok):
            pass
        else:
            Error_Connecting = r2.status_code
            print ("Unable to Authenticate :", Error_Connecting)   
    except Exception as Error_ConnecttoEnergymanager:
        print ("Error accessing Energy Manager step2 :", Error_ConnecttoEnergymanager)	        
        #------------------------------------------------------------
        # Get Data from EnergyManager
    try:
        print ("trying to get data - start step 3 ...")
        r3 = mySession.get('http://'+ Em_IP_Adress +'/mum-webservice/data.php',  headers=headers)
        if (r3.status_code == requests.codes.ok):
            pass
        else:
            Error_Connecting = r3.status_code
            print ("Unable to Get data :", Error_Connecting)             
        em300data=json.loads(r3.text)
        Error_Connecting = 0

    except Exception as Error_ConnecttoEnergymanager:
        print ("Error accessing Energy Manager step3 :", Error_ConnecttoEnergymanager)
        #logging.error("%s %s %s", loggerdate(), ",readenergymanager: Ran into exception querying the energymanager : ", Error_ConnecttoEnergymanager)
        Error_Connecting=Error_ConnecttoEnergymanager

        #
        # End Connection to EnergyManager
        #_______________________________________________________________
    # 
    #--------------------------------------------------------------
    # Processing data
    Returnvalue = -1
    if (Error_Connecting == 0):
        if (len(em300data) >1):                         # We have something in the list
            if (em300data["status"] == 0):                  # We got valid data from Energymanager
                ("before calling changeobiskeys")
                em300data =changeobiskeys(em300data)
                Returnvalue =0
    else:                                               # We ran into trouble and allocate an empty list
        em300data={}
        print ("Issue getting data from EnergyManager ", Error_Connecting)
        
    return (Returnvalue, em300data)    
    


if __name__ == "__main__":  
    print ("Start querying Energy Manager....")
    try:
        Myreturnvalue, Mydata = readenergymanager();
        if (Myreturnvalue == 0):
            print ("Returnvalue -should be zero if successful : ", Myreturnvalue)
            print ("----------------Start Values from Energy Manager ----------------")
            pprint (Mydata)
            print ("----------------End - Values from Energy Manager ----------------")	
            print ("Two Specific values from array....")
            print ("Energy to Grid   (Obis code: 1-0:2.8.0)", Mydata['Active energy-'])
            print ("Energy from Grid (Obis code: 1-0:1.8.0)", Mydata['Active energy_incoming'])
        else:
            print ("I was unable to query the Energy Manager")
    except Exception as ex:
        print ("Issues querying EnergyManager :", ex)

                        