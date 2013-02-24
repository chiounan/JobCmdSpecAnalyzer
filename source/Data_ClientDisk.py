'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *

Data_ClientDiskXML = '../xmlfiles/Data_ClientDisk.xml'
xmlFile = openXmlFile(Data_ClientDiskXML) 
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot) 
#print ('jobAttributes: %s' % jobAttributes)

commandAttributes = parseCommnad(xmlRoot)
#print ('commandAttributes: %s' % commandAttributes)

clientAttributes = parseClient(xmlRoot)
#print ('clientAttributes: %s' % clientAttributes)

client = xmlRoot.getElementsByTagName('client')[0]
clientId = client.getAttribute('id')
#print ('JobAgt ClientId: %s' % clientId)

# get disks attributes
disksAttributes = parseDisksAttributes(xmlRoot)
for i in range(len(disksAttributes)):
#    print ('disk[%d]: %s' % (i, disksAttributes[i]))
    # disk id, if disk role = original
    diskIdOriginal = []
    if(disksAttributes[i].get('role') == 'original'):
        diskIdOriginal.append(disksAttributes[i].get('id'))
#        print (diskIdOriginal)
    # disk id, if disk role = backup
    diskIdBackup = []
    if(disksAttributes[i].get('role') == 'backup'):
        diskIdBackup.append(disksAttributes[i].get('id'))
#        print (diskIdBackup)

# get volume attributes
volumesAttributes = parseVolumesAttributes(xmlRoot)
#print ('volumesAttributes[]: %s' % volumesAttributes)
volumeSerial = []
for i in range(len(volumesAttributes)):
#    print ('voluem[%d]: %s' % (i, volumesAttributes[i]))
    volumeSerial.append(volumesAttributes[i].get('serialNum'))
#    print (volumeSerial)

disksAttributes = parseDataClientDiskAttributes(xmlRoot)
#print (disksAttributes)

os_ipAddress = parseXAttributes(xmlRoot, 'os', 'ipAddress')

disk_id = parseXAttributes(xmlRoot, 'disk', 'id')
client_id = parseXAttributes(xmlRoot, 'client', 'id')