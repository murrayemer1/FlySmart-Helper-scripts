import os
import datetime
#from zipfile import Zipfile as z

from xml.dom.minidom import parse
import xml.dom.minidom as xml
'''
for file in os.listdir("S:/Flight Operations/Flight Ops Engineering/Flysmart Admin/Airport Databases"):
    if file.endswith(".zip"):
        AODBs.append(file)

filepath = r"S:/Flight Operations/Flight Ops Engineering/Flysmart Admin/Airport Databases/report-TO-210226.zip"
with z(filepath,r)as zip:
    zip.printdir()
    zip.extractall()
'''

xmlfile = input('enter file to test..')
xmlfile = xmlfile+".xml"
DOMTree = xml.parse(xmlfile)
collection = DOMTree.documentElement

tail = collection.firstChild.nextSibling.getAttribute('tailNumber')

Input = collection.getElementsByTagName('input')
weight = Input[0].getAttribute('tow')
qnh = Input[0].getAttribute('qnh')
qnh = float(qnh[1::].strip('; hp]'))
oat = Input[0].getAttribute('oat')

runway = Input[0].firstChild.nextSibling.getElementsByTagName('runway')       
slope = runway[0].getAttribute('slope')
elevation = runway[0].getAttribute('elevation')
elevation = float(elevation[1::].strip('; feet]'))+(1013.25-qnh)*30

runwayState = collection.getElementsByTagName("runwayState")
drywet = runwayState[0].getAttribute('label')

AirCon = collection.getElementsByTagName("airConditioning")
AC = AirCon[0].getAttribute('name')

conf = Input[0].getElementsByTagName('configuration')[0].getAttribute('name')
eng = Input[0].getElementsByTagName('engineOption')[0].getAttribute('name')

results = collection.getElementsByTagName("LIST_T_OUT")

x = results[0].firstChild.nodeValue
x = x.split('SECSEG( 3)')
secseg3 = x[0][-11::].strip()

x = x[0].split('CLIMIT(24)')
ASD = x[0][-12::].strip()

x = x[0].split('CLIMIT( 7)')
v1 = x[0][-11::].strip()

x = x[0].split('CLIMIT( 6)')
vR = x[0][-11::].strip()

x = x[0].split('CLIMIT( 5)')
v2 = x[0][-11::].strip()

print('pep inputs are: \nAircraft: '+tail+'\nslope: '+slope+'\nConfiguration: '+conf+'\nEngine option: '+eng+'\nair Conditioning: '+AC+'\nRunway Options: '+drywet+'\n\nv1: '+v1+'\nv2: '+v2+'\nTemp: '+oat+'\nWind: \nPressure Altitude: '+str(elevation)+'\nWeight '+weight+'\n')

pep = input('enter PEP results...').split(',')

#PEP_FMCalc = open('FMresult.txt')
#pep = PEP_FMCalc.readlines()
#pep = pep[2].split(',')

secseg32 =pep[20].strip()
ASD2 = pep[5].strip()
v12 = pep[9].strip()
vR2 = pep[11].strip()
v22 = pep[16].strip()

print('     FS      PEP     %diff')
print('v1  '+v1+'  '+v12+'  '+str((float(v12)-float(v1))*100/float(v1)))
print('vR  '+vR+'  '+vR2+'  '+str((float(vR2)-float(vR))*100/float(vR)))
print('v2  '+v2+'  '+v22+'  '+str((float(v22)-float(v2))*100/float(v2)))
print('ASD '+ASD+' '+ASD2+' '+str((float(ASD2)-float(ASD))*100/float(ASD)))
print('SS3 '+secseg3+'    '+secseg32+'    '+str((float(secseg32)-float(secseg3))*100/float(secseg3)))


Newtestfile = open(xmlfile.strip('.xml')+' test '+datetime.datetime.now().strftime("%c")[0:10]+'.txt', 'w')
Newtestfile.write('    FS    PEP\nv1  '+v1+' '+v12)
Newtestfile.write('\nvR  '+vR+' '+vR2)
Newtestfile.write('\nv2  '+v2+' '+v22)
Newtestfile.write('\nASD '+ASD+' '+ASD2)
Newtestfile.write('\nSS3 '+secseg3+'   '+secseg32)
Newtestfile.close()

input('press any key when done')
'''
###open file, process file, and save to new file###
f = open("S:/Flight Operations/Flight Ops Engineering/Flysmart Admin/Airport Databases/"+file, 'rt')
x = f.readlines()			#each line of text file becomes item in list x
f.close()

'''
