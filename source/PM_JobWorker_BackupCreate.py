'''
Created on 2013/1/30

@author: chiounan
'''
from xml.dom.minidom import parse
from jobCmdSpecModules import *

JobWorkerCmdSpecXML = '../xmlfiles/PM_JobWorker_BackupCreate.xml'
xmlFile = openXmlFile(JobWorkerCmdSpecXML)
xmlRoot = parse(xmlFile)
closeXmlFile(xmlFile)

jobAttributes = parseJob(xmlRoot)
#print ('jobAttributes: %s' % jobAttributes)

commandAttributes = parseCommnad(xmlRoot)
#print ('commandAttributes: %s' % commandAttributes)

optionAttributes = parseOption(xmlRoot)
#print ('optionAttributes: %s' % optionAttributes)

serversAttributes = parseServers(xmlRoot)
#print ('serversAttributes: %s' % serversAttributes)

'''
clients = xmlRoot.getElementsByTagName('client')
print ('Number of clients: %s' % clients.length)
if clients.length > 0:
    clientDict = {} 
    for client in clients:
        clientId = clients.getAttribute('id')
        clientsAttributes = parseClients(clients)
        print (clientsAttributes)
        clientDict[clientId] = clientsAttributes
else:
    print ('There is no client in %s' % JobWorkerCmdSpecXML)        
'''

clientsAttributes = parseClients(xmlRoot)
#print ('clientsAttributes: %s' % clientsAttributes)

# Client summary
#print ('Number of clients: %s' % len(clientsAttributes))
for i in range(len(clientsAttributes)):
#    print ('\n%sth client:' % (i + 1))
#    print (clientsAttributes[i])
    client_id = clientsAttributes[i]['id']
#    print ('client id: %s' % client_id)
    client_name = clientsAttributes[i]['client_name']
#    print ('client name: %s' % client_name)
    cleint_IP = clientsAttributes[i]['client_IP']
    client_isAllDisk = clientsAttributes[i]['isAllDisk']
    client_isGroupAll = clientsAttributes[i]['isGroupAll']
    client_sourcedisk = clientsAttributes[i]['sourcedisk']
#    print ('Number of sourcedisks of client: %s' % len(client_sourcedisk))
#    print ('sourcedisk: %s' % client_sourcedisk)
    for j in range(len(client_sourcedisk)):
#        print (client_sourcedisk[j])
        sourcedisk_id = client_sourcedisk[j]['id']
#        print ('sourcedisk id: %s' % sourcedisk_id)
        sourcedisk_exclusion = client_sourcedisk[j].get('exclusionPartId')  # Use 'get' method to prevent TypeError, the exclusionPartId may not exist.
#        print ('sourcedisk_exclusion: %s' % sourcedisk_exclusion)
        if (sourcedisk_exclusion != None):
            for k in range(len(sourcedisk_exclusion)):
                exclusion_partid = sourcedisk_exclusion[k]
#                print ('exlcusion partId: %s' % exclusion_partid)
    
client_id = parseXAttributes(xmlRoot, 'client', 'id')
client_name = parseXAttributes(xmlRoot, 'client', 'name')
server_id = parseXAttributes(xmlRoot, 'server', 'id')
# All sourcedisk id, not know which sourcedisk id belongs to which client (id) 
sourcedisk_id = parseXAttributes(xmlRoot, 'sourcedisk', 'id')

