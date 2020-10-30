from tkinter import *
from tkinter import ttk
import pickle

window = Tk()
window.title('Waterhouse Form Filler')
window.geometry("1550x850")
window.minsize(width=1550, height=850)
window.maxsize(width=1550, height=850)


tabControl = ttk.Notebook(window) 

ApplicantInfo = ttk.Frame(tabControl)
Acc125 = ttk.Frame(tabControl)


  
tabControl.add(ApplicantInfo, text ='Applicant')
tabControl.add(Acc125, text ='Accord 125')
tabControl.pack(expand = 1, fill ="both", padx = 30, pady = 30) 

  

#-----------------------INFO------------------------------------------------------
#  -Named Insured
ttk.Label(ApplicantInfo, text ="Applicant").grid(column = 0, row = 0, padx = 30, pady = 20) 
appName = ttk.Entry(ApplicantInfo, width = 50)
appName.grid(column = 1, row = 0, padx = 30, pady = 20) 
#  -Address
ttk.Label(ApplicantInfo, text ="Address").grid(column = 0, row = 1, padx = 30, pady = 5) 
appAddress = ttk.Entry(ApplicantInfo, width = 50)
appAddress.grid(column = 1, row = 1, padx = 30, pady = 5)
#  -City
ttk.Label(ApplicantInfo, text ="City").grid(column = 0, row = 2, padx = 30, pady = 5) 
appCity = ttk.Entry(ApplicantInfo, width = 50)
appCity.grid(column = 1, row = 2, padx = 30, pady = 5)
#  -State
ttk.Label(ApplicantInfo, text ="State").grid(column = 0, row = 3, padx = 30, pady = 5) 
appState = ttk.Entry(ApplicantInfo, width = 50)
appState.grid(column = 1, row = 3, padx = 30, pady = 5)
#  -Zip Code
ttk.Label(ApplicantInfo, text ="Zip Code").grid(column = 0, row = 4, padx = 30, pady = 5)
appZip = ttk.Entry(ApplicantInfo, width = 50)
appZip.grid(column = 1, row = 4, padx = 30, pady = 5) 
#  -Contact Info
ttk.Label(ApplicantInfo, text = 'Contact Info').grid(column = 0, row = 5, padx = 30, pady = 20) 
#  -Primary Phone
ttk.Label(ApplicantInfo, text = 'Primary Phone').grid(column = 0, row = 6, padx = 30, pady = 5) 
appPhone = ttk.Entry(ApplicantInfo, width = 20)
appPhone.grid(column = 1, row = 6, padx = 30, pady = 5, sticky=W) 
#  -Secondary Phone
ttk.Label(ApplicantInfo, text = 'Secondary Phone').grid(column = 0, row = 7, padx = 30, pady = 5) 
appSecPh = ttk.Entry(ApplicantInfo, width = 20)
appSecPh.grid(column = 1, row = 7, padx = 30, pady = 5, sticky=W) 
#  -Email
ttk.Label(ApplicantInfo, text = 'Email').grid(column = 0, row = 8, padx = 30, pady = 5) 
appEmail = ttk.Entry(ApplicantInfo, width = 50)
appEmail.grid(column = 1, row = 8, padx = 30, pady = 5) 

#-----------------------ACCORD 125------------------------------------------------------

ttk.Label(Acc125, text ="Effective date").grid(column = 0, row = 0, padx = 30, pady = 10) 
a125Eff = ttk.Entry(Acc125, width = 10)
a125Eff.grid(column = 1, row = 0, padx = 30, pady = 10, sticky=W) 

ttk.Label(Acc125, text ="Sections").grid(column = 0, row = 1, padx = 30, pady = 10)
sections = Listbox(Acc125, width = 35, height = 20, selectmode=MULTIPLE )
sections.grid(column = 1, row = 1, padx = 30, pady = 10)
sectionsList = ['ACCOUNTS RECEIVABLE', 'BOILER & MACHINERY', 'BUSINESS AUTO', 'BUSINESS OWNERS', 'COMMERCIAL GENERAL LIABILITY', 'CRIME / MISCELLANEOUS CRIME', 'DEALERS', 'ELECTRONIC DATA PROC', 'EQUIPMENT FLOATER', 'GARAGE AND DEALERS', 'GLASS AND SIGN', 'INSTALLATION '' BUILDERS RISK', 'OPEN CARGO', 'PROPERTY', 'TRANPORTATION / MOTOR TRUCK CARGO', 'TRUCKERS / MOTOR CARRIER', 'UMBRELLA', 'YACHT', 'ETO', 'PROFESSIONAL LIABILITY']
for item in sectionsList:
    sections.insert(END, item)

ttk.Label(Acc125, text ="Type of Organization").grid(column = 0, row = 2, padx = 30, pady = 10)
busType = ttk.Frame(Acc125)
busType.grid(column = 1, row = 2, padx = 30, pady = 10, sticky = W, rowspan=2)
busTypeList = {"CORPORATION" : "1", 
          		"INDIVIDUAL" : "2", 
          		"JOINT VENTURE" : "3", 
          		"LLC" : "4", 
          		"NON-PROFIT" : "5",
          		"PARTNERSHIP" : "6",
          		"SUBCHAPTER" : "7",
          		"TRUST" : "8"} 
v = StringVar(busType, "1")
for (text, value) in busTypeList.items():
	Radiobutton(busType, text = text, variable = v, value = value).grid(column = 1, sticky=W)
a125Type = v

#             -------Locations----------

tabControl1 = ttk.Notebook(Acc125)
Loc11 = ttk.Frame(tabControl1, width=375, height=330)
Loc12 = ttk.Frame(tabControl1, width=375, height=330)
Loc13 = ttk.Frame(tabControl1, width=375, height=330)
Loc14 = ttk.Frame(tabControl1, width=375, height=330)

tabControl1.add(Loc11, text ='Location 1')
tabControl1.add(Loc12, text ='Location 2')
tabControl1.add(Loc13, text ='Location 3')
tabControl1.add(Loc14, text ='Location 4')

tabControl1.grid(column = 2, row = 0, padx = 30, pady = 30, rowspan=2)

def locations(Loc1):

	ttk.Label(Loc1, text ="Street").grid(column = 0, row = 0, padx = 5, pady = 5) 
	ttk.Entry(Loc1).grid(column = 1, row = 0, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="City").grid(column = 0, row = 1, padx = 5, pady = 5) 
	ttk.Entry(Loc1).grid(column = 1, row = 1, padx = 5, pady = 5) 

	ttk.Label(Loc1, text ="# Full T Emp").grid(column = 2, row = 0, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 5).grid(column = 3, row = 0, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="# Part T Emp").grid(column = 2, row = 1, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 5).grid(column = 3, row = 1, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Revenue").grid(column = 2, row = 2, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 10).grid(column = 3, row = 2, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Occupied Area").grid(column = 2, row = 3, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 10).grid(column = 3, row = 3, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Public Area").grid(column = 2, row = 4, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 10).grid(column = 3, row = 4, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Total Area").grid(column = 2, row = 5, padx = 5, pady = 5) 
	ttk.Entry(Loc1, width = 10).grid(column = 3, row = 5, padx = 5, pady = 5) 

	ttk.Label(Loc1, text ="State").grid(column = 0, row = 2, padx = 5, pady = 5) 
	ttk.Entry(Loc1).grid(column = 1, row = 2, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Zip").grid(column = 0, row = 3, padx = 5, pady = 5) 
	ttk.Entry(Loc1).grid(column = 1, row = 3, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="City Limits").grid(column = 0, row = 4, padx = 5, pady = 5) 
	incity = ['In', 'Out']
	clicked = StringVar()
	clicked.set(incity[0])
	incitymenu = OptionMenu(Loc1, clicked, *incity)
	incitymenu.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)
	ttk.Label(Loc1, text ="Interest").grid(column = 0, row = 5, padx = 5, pady = 5) 
	tenantOwner =['Owner', 'Tenant']
	clicked1 = StringVar()
	clicked1.set(tenantOwner[0])
	tenantOwnerMenu = OptionMenu(Loc1, clicked1, *tenantOwner)
	tenantOwnerMenu.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)

	ttk.Label(Loc1, text ="Area Leased to Others?").grid(column = 0, row = 6, padx = 5, pady = 5) 
	leased =['Yes', 'No']
	clicked2 = StringVar()
	clicked2.set(leased[0])
	leasedMenu = OptionMenu(Loc1, clicked2, *leased)
	leasedMenu.grid(column = 1, row = 6, padx = 5, pady = 5, sticky=W)

locations(Loc11)
locations(Loc12)
locations(Loc13)
locations(Loc14)


natureOfBiz = ttk.Frame(Acc125)
ttk.Label(natureOfBiz, text ="Nature of Bussiness").grid(column = 0, row = 0, padx = 5, pady = 5) 
ttk.Entry(natureOfBiz, width = 50).grid(column = 1, row = 0, pady = 5, padx = 5)
natureOfBiz.grid(column = 2, row = 3, padx = 30, pady = 30)



#             -------Carriers----------

tabControl2 = ttk.Notebook(Acc125)
Carrier1 = ttk.Frame(tabControl2, width=375, height=330)
Carrier2 = ttk.Frame(tabControl2, width=375, height=330)
Carrier3 = ttk.Frame(tabControl2, width=375, height=330)
Carrier4 = ttk.Frame(tabControl2, width=375, height=330)

tabControl2.add(Carrier1, text ='Carrier 1')
tabControl2.add(Carrier2, text ='Carrier 2')
tabControl2.add(Carrier3, text ='Carrier 3')
tabControl2.add(Carrier4, text ='Carrier 4')

tabControl2.grid(column = 3, row = 0, padx = 30, pady = 30, rowspan=2)

def carriers(carrier):

	ttk.Label(carrier, text ="Carrier").grid(column = 0, row = 0, padx = 5, pady = 5) 
	ttk.Entry(carrier).grid(column = 1, row = 0, padx = 5, pady = 5) 
	ttk.Label(carrier, text ="Effective Date").grid(column = 0, row = 1, padx = 5, pady = 5) 
	ttk.Entry(carrier).grid(column = 1, row = 1, padx = 5, pady = 5) 
	ttk.Label(carrier, text ="Expiration Date").grid(column = 0, row = 2, padx = 5, pady = 5) 
	ttk.Entry(carrier).grid(column = 1, row = 2, padx = 5, pady = 5) 

	ttk.Label(carrier, text ="Type of Organization").grid(column = 0, row = 3, padx = 30, pady = 10)
	busType = ttk.Frame(carrier)
	busType.grid(column = 1, row = 3, padx = 30, pady = 10, sticky=W)
	busTypeList = {"GENERAL LIABILITY" : "1", 
	          		"AUTOMOBILE" : "2", 
	          		"PROPERTY" : "3", 
	          		"OTHER" : "4"} 
	for (text, value) in busTypeList.items():
		Checkbutton(busType, text = text).grid(column = 1, sticky=W)


carriers(Carrier1)
carriers(Carrier2)
carriers(Carrier3)
carriers(Carrier4)

losses = ttk.Frame(Acc125)
ttk.Label(losses, text ="LOSSES").grid(column = 0, row = 0, pady = 5) 
ttk.Label(losses, text ="Number").grid(column = 0, row = 1, pady = 5) 
ttk.Label(losses, text ="Date of loss").grid(column = 1, row = 1, pady = 5)
ttk.Label(losses, text ="Type of loss").grid(column = 2, row = 1, pady = 5)
ttk.Label(losses, text ="Amount paid").grid(column = 3, row = 1, pady = 5)
ttk.Entry(losses, width = 10).grid(column = 0, row = 2, pady = 5)
ttk.Entry(losses, width = 15).grid(column = 1, row = 2, pady = 5)
ttk.Entry(losses, width = 35).grid(column = 2, row = 2, pady = 5)
ttk.Entry(losses, width = 15).grid(column = 3, row = 2, pady = 5)
ttk.Entry(losses, width = 10).grid(column = 0, row = 3, pady = 5)
ttk.Entry(losses, width = 15).grid(column = 1, row = 3, pady = 5)
ttk.Entry(losses, width = 35).grid(column = 2, row = 3, pady = 5)
ttk.Entry(losses, width = 15).grid(column = 3, row = 3, pady = 5)
losses.grid(column = 2, row = 2, padx = 30, pady = 30)




#-----------------------BUTTONS------------------------------------------------------

def saveEntries():
	#entries = {'Name': appName.get()
	#	'Address': appNameAddress.get()}
	appNameG = appName.get()
	saveFileName = appNameG + '.txt'
	file = open(saveFileName, "w")
	file.write(saveFileName)
	file.close()


buttons = ttk.Frame(window)

save = Button(buttons, text = 'Save', width=10, command = saveEntries).grid(column = 0, row = 0)
generate = Button(buttons, text = 'Generate', width=10).grid(column = 1, row = 0)

buttons.pack(expand = 1, fill ="both", padx = 30, pady = 5)

#-------------------------------------------------------------------------------------

window.mainloop() 