'''
This program creates an edited version of the latest AODB in this folder. Edits are as follows:
1. for standard Engine fail procedures, prints the following text in the EFP box on TO page: 'TAKEOFF BASED ON CLIMBING ON EXTENDED RUNWAY CENTERLINE'
2. for non standard EFPs, copies TO EFP to landing page
3. for TMPs, if a TMP includes runway shortening, shortens the LDA by same amount (as LDA always looks at full length runway)

'''
import os

###Choose latest file in folder###
AODBs = []
date = []

for file in os.listdir("S:/Flight Operations/Flight Ops Engineering/Flysmart Admin/Airport Databases/Airport Database Editor"):
    if file.startswith("Airbus_extract_NO_STD_EFP-AIRCON.AIRBUS_A330"):
        AODBs.append(file)

for AODB in AODBs:
    info = AODB.split('.')
    info2 = info[2].split('_')
    date.append(info2[0]+info2[1]) #isolate the date from the filename and make list of all dates


file = AODBs[date.index(max(date))] #get max of dates. corresponding AODB is latest file.
print(file)                         #print file that will be used to console (check)


###open file, process file###
f = open("S:/Flight Operations/Flight Ops Engineering/Flysmart Admin/Airport Databases/airport Database Editor/"+file, 'rt')
x = f.readlines()		#each line of text file becomes item in list x
f.close()

LDA = []
runway = []
airfeild = []

#x = x[1:10]                    #for testing
for n, i in enumerate(x):	#cycle through each line of text (items in list x)
 if '=' in i:                   #if this line has an = sign in it
  b = i.split('=')	        #splits current line of file into what comes before and after the =
  if 'IATA' in b[0]:
   current_airfeild = b[1].strip(';\n')
  if 'TOComments' in b[0]:      #if what comes before the '=' sign contains the text 'TOComments:' (might also contain white spaces)
   if b[1] == ';\n':            #if TOComments is blank, put standard wording
    b[1] = 'TAKEOFF BASED ON CLIMBING ON EXTENDED RUNWAY CENTERLINE;\n'
    x[n] = "=".join(b)
   else:                        #if TOComments is not blank, copy it to landing
    c = x[n+1].split('=')	#asign contents of NEXT line of text to new variable, c, and split it into what comes before and after the '=' sign. C is now a list two items long containing the text before and after the '=' sign in the line after the line we're on
    c[1]=b[1]		        #change value of second item of c to be the same as second half of current line
    x[n+1] = "=".join(c)	#change value of next line in list x to the updated contents of c, separated by '=' 

 if 'Ident' and 'TMP' in i:     #looking for all temp runway data
  b = i.split('=')              #once we find one, separate the runway identifier from the rest of the line
  airfeild.append(current_airfeild)
  f = b[1].split('TMP')
  runway.append(f[0])           #add the runway (without TMP) to a list. These are the runways we need to update the landing distance of.
  c = x[n+2].split('=')         #extract the landing distance we will need to update the runway
  LDA.append(c[1])              #add to list. This can keep its ';\n' chars because we can just replace them too

for n, i in enumerate(runway):  #when we have our full list of runways that have TMPs associated with them, go through this list
 for o, j in enumerate(x):      #for every runway with a TMP, search the file from that runway
  if 'IATA' in j:
   a = j.split('=')
   current_airfeild = a[1].strip(';\n')
  if 'Ident' in j:
   d = j.strip(';\n').split('=')
   if d[1] == i and current_airfeild == airfeild[n]:    #once we found that runway, update the landing distance (two lines later in main file)
     e = x[o+2].split('=')
     if e[1] > LDA[n]:
      e[1]=LDA[n]
      x[o+2]="=".join(e)

###write the updated runway data to a new file###
NewAirportDatabasefile = open('AirportDatabase_Edited_A'+file.strip('Airbus_extract_NO_STD_EFP-AIRCON.AIRBUS_')+'.txt', 'w')
for item in x:
 NewAirportDatabasefile.write("%s" % item)

NewAirportDatabasefile.close()
