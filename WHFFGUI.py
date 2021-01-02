from tkinter import *
from tkinter import ttk
import pickle
from tkinter import filedialog
import pdfrw
import os
from reportlab.pdfgen import canvas
import datetime

window = Tk()
window.title('Waterhouse Form Filler')
window.geometry("1550x850")
window.minsize(width=1550, height=850)
window.maxsize(width=1550, height=850)


tabControl = ttk.Notebook(window) 

ApplicantInfo = ttk.Frame(tabControl)
Acc125 = ttk.Frame(tabControl)
Acc126 = ttk.Frame(tabControl)


  
tabControl.add(ApplicantInfo, text ='Applicant')
tabControl.add(Acc125, text ='Accord 125')
tabControl.add(Acc126, text ='Accord 126')
tabControl.pack(expand = 1, fill ="both", padx = 30, pady = 30) 

  
#---------------------------------------------------------------------------------
#-----------------------INFO------------------------------------------------------
#---------------------------------------------------------------------------------

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


#---------------------------------------------------------------------------------
#-----------------------ACCORD 126------------------------------------------------
#---------------------------------------------------------------------------------


ttk.Label(Acc126, text ="General Aggregate").grid(column = 0, row = 0, padx = 30, pady = 10)
A126GenAgg = ttk.Frame(Acc126)
A126GenAgg.grid(column = 1, row = 0, padx = 30, pady = 10, sticky = W, rowspan=2)
A126GenAggList = {"50,000" : "1", 
          		"100,000" : "2", 
          		"300,000" : "3", 
          		"500,000" : "4", 
          		"1,000,000" : "5",
          		"2,000,000" : "6"} 

v1 = StringVar(A126GenAgg, "6")
for (text, value) in A126GenAggList.items():
	Radiobutton(A126GenAgg, text = text, variable = v1, value = value).grid(column = 1, sticky=W)
A126GenAgg = v1

tabControl4 = ttk.Notebook(Acc126)
Class11 = ttk.Frame(tabControl4, width=400, height=800)
Class12 = ttk.Frame(tabControl4, width=400, height=800)
Class13 = ttk.Frame(tabControl4, width=400, height=800)
Class14 = ttk.Frame(tabControl4, width=400, height=800)

tabControl4.add(Class11, text ='Hazard 1')
tabControl4.add(Class12, text ='Hazard 2')
tabControl4.add(Class13, text ='Hazard 3')
tabControl4.add(Class14, text ='Hazard 4')

tabControl4.grid(column = 0, row = 6, padx = 30, pady = 30, columnspan=2)

def ClassCodeSec(Class1):

	ttk.Label(Class1, text ="Location #").grid(column = 0, row = 0, padx = 5, pady = 5) 
	Class1Location = ttk.Entry(Class1)
	Class1Location.grid(column = 1, row = 0, padx = 5, pady = 5) 
	ttk.Label(Class1, text ="Hazard #").grid(column = 0, row = 1, padx = 5, pady = 5) 
	Class1Hazard = ttk.Entry(Class1)
	Class1Hazard.grid(column = 1, row = 1, padx = 5, pady = 5) 
	ttk.Label(Class1, text ="Classification").grid(column = 0, row = 2, padx = 5, pady = 5) 
	Class1Classification = ttk.Entry(Class1)
	Class1Classification.grid(column = 1, row = 2, padx = 5, pady = 5) 
	ttk.Label(Class1, text ="Class code").grid(column = 0, row =3, padx = 5, pady = 5) 
	Class1CCode = ttk.Entry(Class1)
	Class1CCode.grid(column = 1, row = 3, padx = 5, pady = 5) 
	ttk.Label(Class1, text ="Premium Basis").grid(column = 0, row = 4, padx = 5, pady = 5) 
	Class1Basis = ttk.Entry(Class1)
	Class1Basis.grid(column = 1, row = 4, padx = 5, pady = 5) 
	ttk.Label(Class1, text ="Exposure").grid(column = 0, row = 5, padx = 5, pady = 5) 
	Class1Exposure = ttk.Entry(Class1)
	Class1Exposure.grid(column = 1, row = 5, padx = 5, pady = 5) 

	

	return Class1Location, Class1Hazard, Class1Classification, Class1CCode, Class1Basis, Class1Exposure

	

Class1Location1, Class1Hazard1, Class1Classification1, Class1CCode1, Class1Basis1, Class1Exposure1 = ClassCodeSec(Class11)
Class1Location2, Class1Hazard2, Class1Classification2, Class1CCode2, Class1Basis2, Class1Exposure2 = ClassCodeSec(Class12)
Class1Location3, Class1Hazard3, Class1Classification3, Class1CCode3, Class1Basis3, Class1Exposure3 = ClassCodeSec(Class13)
Class1Location4, Class1Hazard4, Class1Classification4, Class1CCode4, Class1Basis4, Class1Exposure4 = ClassCodeSec(Class14)


tabControl3 = ttk.Notebook(Acc126)
Contractors = ttk.Frame(tabControl3, width=400, height=400)
Products = ttk.Frame(tabControl3, width=400, height=400)
ClaimsMade = ttk.Frame(tabControl3, width=400, height=400)
General = ttk.Frame(tabControl3, width=400, height=400)


tabControl3.add(Contractors, text ='Contractors')
tabControl3.add(Products, text ='Products')
tabControl3.add(ClaimsMade, text ='Claims Made')
tabControl3.add(General, text ='General')



tabControl3.grid(column = 2, row = 0, pady = 0, padx = 30, rowspan = 7)

Questions = ttk.Frame(Contractors)
Questions.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions, text ="This is question number 1?").grid(column = 0, row = 0, pady = 5) 
a126q1 =['Yes', 'No']
a126q1Clk = StringVar()
a126q1Clk.set(a126q1[1])
a126q1Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q1Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 2?").grid(column = 0, row = 1, pady = 5) 
a126q2 =['Yes', 'No']
a126q2Clk = StringVar()
a126q2Clk.set(a126q1[1])
a126q2Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q2Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 3?").grid(column = 0, row = 2, pady = 5) 
a126q3 =['Yes', 'No']
a126q3Clk = StringVar()
a126q3Clk.set(a126q1[1])
a126q3Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q3Mn.grid(column = 1, row = 2, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 4?").grid(column = 0, row = 3, pady = 5) 
a126q4 =['Yes', 'No']
a126q4Clk = StringVar()
a126q4Clk.set(a126q1[1])
a126q4Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q4Mn.grid(column = 1, row = 3, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 5?").grid(column = 0, row = 4, pady = 5) 
a126q5 =['Yes', 'No']
a126q5Clk = StringVar()
a126q5Clk.set(a126q1[1])
a126q5Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q5Mn.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 6?").grid(column = 0, row = 5, pady = 5) 
a126q6 =['Yes', 'No']
a126q6Clk = StringVar()
a126q6Clk.set(a126q1[1])
a126q6Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q6Mn.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 7?").grid(column = 0, row = 6, pady = 5) 
a126q7 =['Yes', 'No']
a126q7Clk = StringVar()
a126q7Clk.set(a126q1[1])
a126q7Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q7Mn.grid(column = 1, row = 6, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="This is question number 8?").grid(column = 0, row = 7, pady = 5) 
a126q8 =['Yes', 'No']
a126q8Clk = StringVar()
a126q8Clk.set(a126q1[1])
a126q8Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q8Mn.grid(column = 1, row = 7, padx = 5, pady = 5, sticky=W)


#---------------------------------------------------------------------------------
#-----------------------ACCORD 125------------------------------------------------
#---------------------------------------------------------------------------------


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
	Loc1St = ttk.Entry(Loc1)
	Loc1St.grid(column = 1, row = 0, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="City").grid(column = 0, row = 1, padx = 5, pady = 5) 
	Loc1City = ttk.Entry(Loc1)
	Loc1City.grid(column = 1, row = 1, padx = 5, pady = 5) 

	ttk.Label(Loc1, text ="# Full T Emp").grid(column = 2, row = 0, padx = 5, pady = 5) 
	Loc1FullTEmp = ttk.Entry(Loc1, width = 5)
	Loc1FullTEmp.grid(column = 3, row = 0, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="# Part T Emp").grid(column = 2, row = 1, padx = 5, pady = 5) 
	Loc1PartTEmp = ttk.Entry(Loc1, width = 5)
	Loc1PartTEmp.grid(column = 3, row = 1, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Revenue").grid(column = 2, row = 2, padx = 5, pady = 5) 
	Loc1Rev = ttk.Entry(Loc1, width = 10)
	Loc1Rev.grid(column = 3, row = 2, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Occupied Area").grid(column = 2, row = 3, padx = 5, pady = 5) 
	Loc1OccArea = ttk.Entry(Loc1, width = 10)
	Loc1OccArea.grid(column = 3, row = 3, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Public Area").grid(column = 2, row = 4, padx = 5, pady = 5) 
	Loc1PubArea = ttk.Entry(Loc1, width = 10)
	Loc1PubArea.grid(column = 3, row = 4, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Total Area").grid(column = 2, row = 5, padx = 5, pady = 5) 
	Loc1TotArea = ttk.Entry(Loc1, width = 10)
	Loc1TotArea.grid(column = 3, row = 5, padx = 5, pady = 5) 

	ttk.Label(Loc1, text ="State").grid(column = 0, row = 2, padx = 5, pady = 5) 
	Loc1State = ttk.Entry(Loc1)
	Loc1State.grid(column = 1, row = 2, padx = 5, pady = 5) 
	ttk.Label(Loc1, text ="Zip").grid(column = 0, row = 3, padx = 5, pady = 5) 
	Loc1Zip = ttk.Entry(Loc1)
	Loc1Zip.grid(column = 1, row = 3, padx = 5, pady = 5) 
	
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

	return Loc1St, Loc1City, Loc1FullTEmp, Loc1PartTEmp, Loc1Rev, Loc1OccArea, Loc1PubArea, Loc1TotArea, Loc1State, Loc1Zip, clicked, clicked1, clicked2

	

Loc1St1, Loc1City1, Loc1FullTEmp1, Loc1PartTEmp1, Loc1Rev1, Loc1OccArea1, Loc1PubArea1, Loc1TotArea1, Loc1State1, Loc1Zip1, incitymenu1, tenantOwnerMenu1, leasedMenu1 = locations(Loc11)
Loc1St2, Loc1City2, Loc1FullTEmp2, Loc1PartTEmp2, Loc1Rev2, Loc1OccArea2, Loc1PubArea2, Loc1TotArea2, Loc1State2, Loc1Zip2, incitymenu2, tenantOwnerMenu2, leasedMenu2 = locations(Loc12)
Loc1St3, Loc1City3, Loc1FullTEmp3, Loc1PartTEmp3, Loc1Rev3, Loc1OccArea3, Loc1PubArea3, Loc1TotArea3, Loc1State3, Loc1Zip3, incitymenu3, tenantOwnerMenu3, leasedMenu3 = locations(Loc13)
Loc1St4, Loc1City4, Loc1FullTEmp4, Loc1PartTEmp4, Loc1Rev4, Loc1OccArea4, Loc1PubArea4, Loc1TotArea4, Loc1State4, Loc1Zip4, incitymenu4, tenantOwnerMenu4, leasedMenu4 = locations(Loc14)




natureOfBiz = ttk.Frame(Acc125)
ttk.Label(natureOfBiz, text ="Nature of Bussiness").grid(column = 0, row = 0, padx = 5, pady = 5) 
A125nature = ttk.Entry(natureOfBiz, width = 50)
A125nature.grid(column = 1, row = 0, pady = 5, padx = 5)
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
	carrierName = ttk.Entry(carrier)
	carrierName.grid(column = 1, row = 0, padx = 5, pady = 5) 
	ttk.Label(carrier, text ="Effective Date").grid(column = 0, row = 1, padx = 5, pady = 5) 
	carrierEff = ttk.Entry(carrier)
	carrierEff.grid(column = 1, row = 1, padx = 5, pady = 5) 
	ttk.Label(carrier, text ="Expiration Date").grid(column = 0, row = 2, padx = 5, pady = 5) 
	carrierExp = ttk.Entry(carrier)
	carrierExp.grid(column = 1, row = 2, padx = 5, pady = 5) 

	ttk.Label(carrier, text ="Type of Organization").grid(column = 0, row = 3, padx = 30, pady = 10)
	busType = ttk.Frame(carrier)
	busType.grid(column = 1, row = 3, padx = 30, pady = 10, sticky=W)
	#busTypeList = {"GENERAL LIABILITY" : "1", 
	#          		"AUTOMOBILE" : "2", 
	#          		"PROPERTY" : "3", 
	#          		"OTHER" : "4"} 
	#for (text, value) in busTypeList.items():
	#	Checkbutton(busType, text = text).grid(column = 1, sticky=W)

	A125CheckGLV = IntVar()
	A125CheckGLB = Checkbutton(busType, text = 'GENERAL LIABILITY', variable = A125CheckGLV)
	A125CheckGLB.grid(column = 1, sticky=W)
	A125CheckAutoV = IntVar()
	A125CheckAutoB = Checkbutton(busType, text = 'AUTOMOBILE', variable = A125CheckAutoV)
	A125CheckAutoB.grid(column = 1, sticky=W)
	A125CheckPropertyV = IntVar()
	A125CheckPropertyB = Checkbutton(busType, text = 'PROPERTY', variable = A125CheckPropertyV)
	A125CheckPropertyB.grid(column = 1, sticky=W)
	A125CheckOtherV = IntVar()
	A125CheckOtherB = Checkbutton(busType, text = 'OTHER', variable = A125CheckOtherV)
	A125CheckOtherB.grid(column = 1,  sticky=W)

	return carrierName, carrierEff, carrierExp, A125CheckGLV, A125CheckAutoV, A125CheckPropertyV, A125CheckOtherV




carrierName1, carrierEff1, carrierExp1, A125CheckGL1, A125CheckAuto1, A125CheckProperty1, A125CheckOther1 = carriers(Carrier1)
carrierName2, carrierEff2, carrierExp2, A125CheckGL2, A125CheckAuto2, A125CheckProperty2, A125CheckOther2 = carriers(Carrier2)
carrierName3, carrierEff3, carrierExp3, A125CheckGL3, A125CheckAuto3, A125CheckProperty3, A125CheckOther3 = carriers(Carrier3)
carrierName4, carrierEff4, carrierExp4, A125CheckGL4, A125CheckAuto4, A125CheckProperty4, A125CheckOther4 = carriers(Carrier4)

losses = ttk.Frame(Acc125)
ttk.Label(losses, text ="LOSSES").grid(column = 0, row = 0, pady = 5) 
ttk.Label(losses, text ="Number").grid(column = 0, row = 1, pady = 5) 
ttk.Label(losses, text ="Date of loss").grid(column = 1, row = 1, pady = 5)
ttk.Label(losses, text ="Type of loss").grid(column = 2, row = 1, pady = 5)
ttk.Label(losses, text ="Amount paid").grid(column = 3, row = 1, pady = 5)
A125LossNum1 = ttk.Entry(losses, width = 10)
A125LossNum1.grid(column = 0, row = 2, pady = 5)
A125LossDate1 = ttk.Entry(losses, width = 15)
A125LossDate1.grid(column = 1, row = 2, pady = 5)
A125TypeType1 = ttk.Entry(losses, width = 35)
A125TypeType1.grid(column = 2, row = 2, pady = 5)
A125LossPaid1 = ttk.Entry(losses, width = 15)
A125LossPaid1.grid(column = 3, row = 2, pady = 5)
A125LossNum2 = ttk.Entry(losses, width = 10)
A125LossNum2.grid(column = 0, row = 3, pady = 5)
A125LossDate2 = ttk.Entry(losses, width = 15)
A125LossDate2.grid(column = 1, row = 3, pady = 5)
A125TypeType2 = ttk.Entry(losses, width = 35)
A125TypeType2.grid(column = 2, row = 3, pady = 5)
A125LossPaid2 = ttk.Entry(losses, width = 15)
A125LossPaid2.grid(column = 3, row = 3, pady = 5)
losses.grid(column = 2, row = 2, padx = 30, pady = 30)




#---------------------------------------------------------------------------------
#-----------------------BUTTONS---------------------------------------------------
#---------------------------------------------------------------------------------



#-----------------------SAVE---------------------------------------------------------


def saveEntries():
	entriesDic = {}

	appNameG = appName.get()
	appAddressG = appAddress.get()
	appCityG = appCity.get()
	appStateG = appState.get()
	appZipG = appZip.get()
	appPhoneG = appPhone.get()
	appSecPhG = appSecPh.get()
	appEmailG = appEmail.get()
	
	a125EffG = a125Eff.get()
	sectionsG = sections.curselection()
	a125TypeG = a125Type.get()

	
	Loc1St1G = Loc1St1.get()
	Loc1City1G = Loc1City1.get()
	Loc1FullTEmp1G = Loc1FullTEmp1.get()
	Loc1PartTEmp1G = Loc1PartTEmp1.get()
	Loc1Rev1G = Loc1Rev1.get()
	Loc1OccArea1G = Loc1OccArea1.get()
	Loc1PubArea1G = Loc1PubArea1.get()
	Loc1TotArea1G = Loc1TotArea1.get()
	Loc1State1G = Loc1State1.get()
	Loc1Zip1G = Loc1Zip1.get()
	incitymenu1G = incitymenu1.get()
	tenantOwnerMenu1G = tenantOwnerMenu1.get()
	leasedMenu1G = leasedMenu1.get()

	Loc1St2G = Loc1St2.get()
	Loc1City2G = Loc1City2.get()
	Loc1FullTEmp2G = Loc1FullTEmp2.get()
	Loc1PartTEmp2G = Loc1PartTEmp2.get()
	Loc1Rev2G = Loc1Rev2.get()
	Loc1OccArea2G = Loc1OccArea2.get()
	Loc1PubArea2G = Loc1PubArea2.get()
	Loc1TotArea2G = Loc1TotArea2.get()
	Loc1State2G = Loc1State2.get()
	Loc1Zip2G = Loc1Zip2.get()
	incitymenu2G = incitymenu2.get()
	tenantOwnerMenu2G = tenantOwnerMenu2.get()
	leasedMenu2G = leasedMenu2.get()

	Loc1St3G = Loc1St3.get()
	Loc1City3G = Loc1City3.get()
	Loc1FullTEmp3G = Loc1FullTEmp3.get()
	Loc1PartTEmp3G = Loc1PartTEmp3.get()
	Loc1Rev3G = Loc1Rev3.get()
	Loc1OccArea3G = Loc1OccArea3.get()
	Loc1PubArea3G = Loc1PubArea3.get()
	Loc1TotArea3G = Loc1TotArea3.get()
	Loc1State3G = Loc1State3.get()
	Loc1Zip3G = Loc1Zip3.get()
	incitymenu3G = incitymenu3.get()
	tenantOwnerMenu3G = tenantOwnerMenu3.get()
	leasedMenu3G = leasedMenu3.get()

	Loc1St4G = Loc1St4.get()
	Loc1City4G = Loc1City4.get()
	Loc1FullTEmp4G = Loc1FullTEmp4.get()
	Loc1PartTEmp4G = Loc1PartTEmp4.get()
	Loc1Rev4G = Loc1Rev4.get()
	Loc1OccArea4G = Loc1OccArea4.get()
	Loc1PubArea4G = Loc1PubArea4.get()
	Loc1TotArea4G = Loc1TotArea4.get()
	Loc1State4G = Loc1State4.get()
	Loc1Zip4G = Loc1Zip4.get()
	incitymenu4G = incitymenu4.get()
	tenantOwnerMenu4G = tenantOwnerMenu4.get()
	leasedMenu4G = leasedMenu4.get()

	carrierName1G = carrierName1.get()
	carrierEff1G = carrierEff1.get()
	carrierExp1G = carrierExp1.get()
	A125CheckGL1G = A125CheckGL1.get()
	A125CheckAuto1G = A125CheckAuto1.get()
	A125CheckProperty1G = A125CheckProperty1.get()
	A125CheckOther1G = A125CheckOther1.get()

	carrierName2G = carrierName2.get()
	carrierEff2G = carrierEff2.get()
	carrierExp2G = carrierExp2.get()
	A125CheckGL2G = A125CheckGL2.get()
	A125CheckAuto2G = A125CheckAuto2.get()
	A125CheckProperty2G = A125CheckProperty2.get()
	A125CheckOther2G = A125CheckOther2.get()

	carrierName3G = carrierName3.get()
	carrierEff3G = carrierEff3.get()
	carrierExp3G = carrierExp3.get()
	A125CheckGL3G = A125CheckGL3.get()
	A125CheckAuto3G = A125CheckAuto3.get()
	A125CheckProperty3G = A125CheckProperty3.get()
	A125CheckOther3G = A125CheckOther3.get()

	carrierName4G = carrierName4.get()
	carrierEff4G = carrierEff4.get()
	carrierExp4G = carrierExp4.get()
	A125CheckGL4G = A125CheckGL4.get()
	A125CheckAuto4G = A125CheckAuto4.get()
	A125CheckProperty4G = A125CheckProperty4.get()
	A125CheckOther4G = A125CheckOther4.get()

	A125LossNum1G = A125LossNum1.get()
	A125LossDate1G = A125LossDate1.get()
	A125TypeType1G = A125TypeType1.get()
	A125LossPaid1G = A125LossPaid1.get()
	A125LossNum2G = A125LossNum2.get()
	A125LossDate2G = A125LossDate2.get()
	A125TypeType2G = A125TypeType2.get()
	A125LossPaid2G = A125LossPaid2.get()

	A125natureG = A125nature.get()
	

	for variable in ['appNameG', 'appAddressG', 'appCityG', 'appStateG', 'appZipG', 'appPhoneG', 
	'appSecPhG', 'appEmailG', 'a125EffG', 'sectionsG', 'a125TypeG',
	'Loc1St1G', 'Loc1City1G', 'Loc1FullTEmp1G', 'Loc1PartTEmp1G', 'Loc1Rev1G', 'Loc1OccArea1G', 'Loc1PubArea1G', 'Loc1TotArea1G', 'Loc1State1G', 'Loc1Zip1G', 'incitymenu1G', 'tenantOwnerMenu1G', 'leasedMenu1G',
	'Loc1St2G', 'Loc1City2G', 'Loc1FullTEmp2G', 'Loc1PartTEmp2G', 'Loc1Rev2G', 'Loc1OccArea2G', 'Loc1PubArea2G', 'Loc1TotArea2G', 'Loc1State2G', 'Loc1Zip2G', 'incitymenu2G', 'tenantOwnerMenu2G', 'leasedMenu2G',
	'Loc1St3G', 'Loc1City3G', 'Loc1FullTEmp3G', 'Loc1PartTEmp3G', 'Loc1Rev3G', 'Loc1OccArea3G', 'Loc1PubArea3G', 'Loc1TotArea3G', 'Loc1State3G', 'Loc1Zip3G', 'incitymenu3G', 'tenantOwnerMenu3G', 'leasedMenu3G',
	'Loc1St4G', 'Loc1City4G', 'Loc1FullTEmp4G', 'Loc1PartTEmp4G', 'Loc1Rev4G', 'Loc1OccArea4G', 'Loc1PubArea4G', 'Loc1TotArea4G', 'Loc1State4G', 'Loc1Zip4G', 'incitymenu4G', 'tenantOwnerMenu4G', 'leasedMenu4G',
	'carrierName1G', 'carrierEff1G', 'carrierExp1G', 'A125CheckGL1G', 'A125CheckAuto1G', 'A125CheckProperty1G', 'A125CheckOther1G',
	'carrierName2G', 'carrierEff2G', 'carrierExp2G', 'A125CheckGL2G', 'A125CheckAuto2G', 'A125CheckProperty2G', 'A125CheckOther2G',
	'carrierName3G', 'carrierEff3G', 'carrierExp3G', 'A125CheckGL3G', 'A125CheckAuto3G', 'A125CheckProperty3G', 'A125CheckOther3G',
	'carrierName4G', 'carrierEff4G', 'carrierExp4G', 'A125CheckGL4G', 'A125CheckAuto4G', 'A125CheckProperty4G', 'A125CheckOther4G',
	'A125LossNum1G', 'A125LossDate1G', 'A125TypeType1G', 'A125LossPaid1G', 'A125LossNum2G', 'A125LossDate2G', 'A125TypeType2G', 'A125LossPaid2G',
	'A125natureG']:
		entriesDic[variable] = eval(variable)


	saveFileName = 'Clients/' + appNameG + '.dat'
	with open(saveFileName, 'wb') as file:
		pickle.dump(entriesDic, file)


#-----------------------LOAD---------------------------------------------------------

def loadEntries():
	saveFileName = filedialog.askopenfilename(initialdir='Clients', title='Open File', filetypes=(('DAT Files', '*.dat'),('All Files', '*.*')))
	with open(saveFileName, 'rb') as file:
		entriesDic = pickle.load(file)

	appName.delete(0, 'end')
	appName.insert(0, entriesDic['appNameG'])
	appAddress.delete(0, 'end')
	appAddress.insert(0, entriesDic['appAddressG'])
	appCity.delete(0, 'end')
	appCity.insert(0, entriesDic['appCityG'])
	appState.delete(0, 'end')
	appState.insert(0, entriesDic['appStateG'])
	appZip.delete(0, 'end')
	appZip.insert(0, entriesDic['appZipG'])
	appPhone.delete(0, 'end')
	appPhone.insert(0, entriesDic['appPhoneG'])
	appSecPh.delete(0, 'end')
	appSecPh.insert(0, entriesDic['appSecPhG'])
	appEmail.delete(0, 'end')
	appEmail.insert(0, entriesDic['appEmailG'])
	a125Eff.delete(0, 'end')
	a125Eff.insert(0, entriesDic['a125EffG'])
	sections.selection_clear(0, 19)
	for variable in entriesDic['sectionsG']:
		sections.selection_set(variable)
	a125Type.set(entriesDic['a125TypeG'])
	Loc1St1.delete(0, 'end')
	Loc1St1.insert(0, entriesDic['Loc1St1G'])
	Loc1City1.delete(0, 'end')
	Loc1City1.insert(0, entriesDic['Loc1City1G'])
	Loc1FullTEmp1.delete(0, 'end')
	Loc1FullTEmp1.insert(0, entriesDic['Loc1FullTEmp1G'])
	Loc1PartTEmp1.delete(0, 'end')
	Loc1PartTEmp1.insert(0, entriesDic['Loc1PartTEmp1G'])
	Loc1Rev1.delete(0, 'end')
	Loc1Rev1.insert(0, entriesDic['Loc1Rev1G'])
	Loc1OccArea1.delete(0, 'end')
	Loc1OccArea1.insert(0, entriesDic['Loc1OccArea1G'])
	Loc1PubArea1.delete(0, 'end')
	Loc1PubArea1.insert(0, entriesDic['Loc1PubArea1G'])
	Loc1TotArea1.delete(0, 'end')
	Loc1TotArea1.insert(0, entriesDic['Loc1TotArea1G'])
	Loc1State1.delete(0, 'end')
	Loc1State1.insert(0, entriesDic['Loc1State1G'])
	Loc1Zip1.delete(0, 'end')
	Loc1Zip1.insert(0, entriesDic['Loc1Zip1G'])
	incitymenu1.set(entriesDic['incitymenu1G'])
	tenantOwnerMenu1.set(entriesDic['tenantOwnerMenu1G'])
	leasedMenu1.set(entriesDic['leasedMenu1G'])

	Loc1St2.delete(0, 'end')
	Loc1St2.insert(0, entriesDic['Loc1St2G'])
	Loc1City2.delete(0, 'end')
	Loc1City2.insert(0, entriesDic['Loc1City2G'])
	Loc1FullTEmp2.delete(0, 'end')
	Loc1FullTEmp2.insert(0, entriesDic['Loc1FullTEmp2G'])
	Loc1PartTEmp2.delete(0, 'end')
	Loc1PartTEmp2.insert(0, entriesDic['Loc1PartTEmp2G'])
	Loc1Rev2.delete(0, 'end')
	Loc1Rev2.insert(0, entriesDic['Loc1Rev2G'])
	Loc1OccArea2.delete(0, 'end')
	Loc1OccArea2.insert(0, entriesDic['Loc1OccArea2G'])
	Loc1PubArea2.delete(0, 'end')
	Loc1PubArea2.insert(0, entriesDic['Loc1PubArea2G'])
	Loc1TotArea2.delete(0, 'end')
	Loc1TotArea2.insert(0, entriesDic['Loc1TotArea2G'])
	Loc1State2.delete(0, 'end')
	Loc1State2.insert(0, entriesDic['Loc1State2G'])
	Loc1Zip2.delete(0, 'end')
	Loc1Zip2.insert(0, entriesDic['Loc1Zip2G'])
	incitymenu2.set(entriesDic['incitymenu2G'])
	tenantOwnerMenu2.set(entriesDic['tenantOwnerMenu2G'])
	leasedMenu2.set(entriesDic['leasedMenu2G'])

	Loc1St3.delete(0, 'end')
	Loc1St3.insert(0, entriesDic['Loc1St3G'])
	Loc1City3.delete(0, 'end')
	Loc1City3.insert(0, entriesDic['Loc1City3G'])
	Loc1FullTEmp3.delete(0, 'end')
	Loc1FullTEmp3.insert(0, entriesDic['Loc1FullTEmp3G'])
	Loc1PartTEmp3.delete(0, 'end')
	Loc1PartTEmp3.insert(0, entriesDic['Loc1PartTEmp3G'])
	Loc1Rev3.delete(0, 'end')
	Loc1Rev3.insert(0, entriesDic['Loc1Rev3G'])
	Loc1OccArea3.delete(0, 'end')
	Loc1OccArea3.insert(0, entriesDic['Loc1OccArea3G'])
	Loc1PubArea3.delete(0, 'end')
	Loc1PubArea3.insert(0, entriesDic['Loc1PubArea3G'])
	Loc1TotArea3.delete(0, 'end')
	Loc1TotArea3.insert(0, entriesDic['Loc1TotArea3G'])
	Loc1State3.delete(0, 'end')
	Loc1State3.insert(0, entriesDic['Loc1State3G'])
	Loc1Zip3.delete(0, 'end')
	Loc1Zip3.insert(0, entriesDic['Loc1Zip3G'])
	incitymenu3.set(entriesDic['incitymenu3G'])
	tenantOwnerMenu3.set(entriesDic['tenantOwnerMenu3G'])
	leasedMenu3.set(entriesDic['leasedMenu3G'])

	Loc1St4.delete(0, 'end')
	Loc1St4.insert(0, entriesDic['Loc1St4G'])
	Loc1City4.delete(0, 'end')
	Loc1City4.insert(0, entriesDic['Loc1City4G'])
	Loc1FullTEmp4.delete(0, 'end')
	Loc1FullTEmp4.insert(0, entriesDic['Loc1FullTEmp4G'])
	Loc1PartTEmp4.delete(0, 'end')
	Loc1PartTEmp4.insert(0, entriesDic['Loc1PartTEmp4G'])
	Loc1Rev4.delete(0, 'end')
	Loc1Rev4.insert(0, entriesDic['Loc1Rev4G'])
	Loc1OccArea4.delete(0, 'end')
	Loc1OccArea4.insert(0, entriesDic['Loc1OccArea4G'])
	Loc1PubArea4.delete(0, 'end')
	Loc1PubArea4.insert(0, entriesDic['Loc1PubArea4G'])
	Loc1TotArea4.delete(0, 'end')
	Loc1TotArea4.insert(0, entriesDic['Loc1TotArea4G'])
	Loc1State4.delete(0, 'end')
	Loc1State4.insert(0, entriesDic['Loc1State4G'])
	Loc1Zip4.delete(0, 'end')
	Loc1Zip4.insert(0, entriesDic['Loc1Zip4G'])
	incitymenu4.set(entriesDic['incitymenu4G'])
	tenantOwnerMenu4.set(entriesDic['tenantOwnerMenu4G'])
	leasedMenu4.set(entriesDic['leasedMenu4G'])

	carrierName1.delete(0, 'end')
	carrierName1.insert(0, entriesDic['carrierName1G'])
	carrierEff1.delete(0, 'end')
	carrierEff1.insert(0, entriesDic['carrierEff1G'])
	carrierExp1.delete(0, 'end')
	carrierExp1.insert(0, entriesDic['carrierExp1G'])
	A125CheckGL1.set(entriesDic['A125CheckGL1G'])
	A125CheckAuto1.set(entriesDic['A125CheckAuto1G'])
	A125CheckProperty1.set(entriesDic['A125CheckProperty1G'])
	A125CheckOther1.set(entriesDic['A125CheckOther1G'])

	carrierName2.delete(0, 'end')
	carrierName2.insert(0, entriesDic['carrierName2G'])
	carrierEff2.delete(0, 'end')
	carrierEff2.insert(0, entriesDic['carrierEff2G'])
	carrierExp2.delete(0, 'end')
	carrierExp2.insert(0, entriesDic['carrierExp2G'])
	A125CheckGL2.set(entriesDic['A125CheckGL2G'])
	A125CheckAuto2.set(entriesDic['A125CheckAuto2G'])
	A125CheckProperty2.set(entriesDic['A125CheckProperty2G'])
	A125CheckOther2.set(entriesDic['A125CheckOther2G'])

	carrierName3.delete(0, 'end')
	carrierName3.insert(0, entriesDic['carrierName3G'])
	carrierEff3.delete(0, 'end')
	carrierEff3.insert(0, entriesDic['carrierEff3G'])
	carrierExp3.delete(0, 'end')
	carrierExp3.insert(0, entriesDic['carrierExp3G'])
	A125CheckGL3.set(entriesDic['A125CheckGL3G'])
	A125CheckAuto3.set(entriesDic['A125CheckAuto3G'])
	A125CheckProperty3.set(entriesDic['A125CheckProperty3G'])
	A125CheckOther3.set(entriesDic['A125CheckOther3G'])

	carrierName4.delete(0, 'end')
	carrierName4.insert(0, entriesDic['carrierName4G'])
	carrierEff4.delete(0, 'end')
	carrierEff4.insert(0, entriesDic['carrierEff4G'])
	carrierExp4.delete(0, 'end')
	carrierExp4.insert(0, entriesDic['carrierExp4G'])
	A125CheckGL4.set(entriesDic['A125CheckGL4G'])
	A125CheckAuto4.set(entriesDic['A125CheckAuto4G'])
	A125CheckProperty4.set(entriesDic['A125CheckProperty4G'])
	A125CheckOther4.set(entriesDic['A125CheckOther4G'])

	A125LossNum1.delete(0, 'end')
	A125LossNum1.insert(0, entriesDic['A125LossNum1G'])
	A125LossDate1.delete(0, 'end')
	A125LossDate1.insert(0, entriesDic['A125LossDate1G'])
	A125TypeType1.delete(0, 'end')
	A125TypeType1.insert(0, entriesDic['A125TypeType1G'])
	A125LossPaid1.delete(0, 'end')
	A125LossPaid1.insert(0, entriesDic['A125LossPaid1G'])
	A125LossNum2.delete(0, 'end')
	A125LossNum2.insert(0, entriesDic['A125LossNum2G'])
	A125LossDate2.delete(0, 'end')
	A125LossDate2.insert(0, entriesDic['A125LossDate2G'])
	A125TypeType2.delete(0, 'end')
	A125TypeType2.insert(0, entriesDic['A125TypeType2G'])
	A125LossPaid2.delete(0, 'end')
	A125LossPaid2.insert(0, entriesDic['A125LossPaid2G'])

	A125nature.delete(0, 'end')
	A125nature.insert(0, entriesDic['A125natureG'])



#-----------------------GENERATE-----------------------------------------------------

def generateForms():

	def create_overlay():
		appNameG = appName.get()
		appAddressG = appAddress.get()
		appCityG = appCity.get()
		appStateG = appState.get()
		appZipG = appZip.get()
		appPhoneG = appPhone.get()
		appSecPhG = appSecPh.get()
		appEmailG = appEmail.get()
		
		a125EffG = a125Eff.get()
		sectionsG = sections.curselection()
		a125TypeG = a125Type.get()

		
		Loc1St1G = Loc1St1.get()
		Loc1City1G = Loc1City1.get()
		Loc1FullTEmp1G = Loc1FullTEmp1.get()
		Loc1PartTEmp1G = Loc1PartTEmp1.get()
		Loc1Rev1G = Loc1Rev1.get()
		Loc1OccArea1G = Loc1OccArea1.get()
		Loc1PubArea1G = Loc1PubArea1.get()
		Loc1TotArea1G = Loc1TotArea1.get()
		Loc1State1G = Loc1State1.get()
		Loc1Zip1G = Loc1Zip1.get()
		incitymenu1G = incitymenu1.get()
		tenantOwnerMenu1G = tenantOwnerMenu1.get()
		leasedMenu1G = leasedMenu1.get()

		Loc1St2G = Loc1St2.get()
		Loc1City2G = Loc1City2.get()
		Loc1FullTEmp2G = Loc1FullTEmp2.get()
		Loc1PartTEmp2G = Loc1PartTEmp2.get()
		Loc1Rev2G = Loc1Rev2.get()
		Loc1OccArea2G = Loc1OccArea2.get()
		Loc1PubArea2G = Loc1PubArea2.get()
		Loc1TotArea2G = Loc1TotArea2.get()
		Loc1State2G = Loc1State2.get()
		Loc1Zip2G = Loc1Zip2.get()
		incitymenu2G = incitymenu2.get()
		tenantOwnerMenu2G = tenantOwnerMenu2.get()
		leasedMenu2G = leasedMenu2.get()

		Loc1St3G = Loc1St3.get()
		Loc1City3G = Loc1City3.get()
		Loc1FullTEmp3G = Loc1FullTEmp3.get()
		Loc1PartTEmp3G = Loc1PartTEmp3.get()
		Loc1Rev3G = Loc1Rev3.get()
		Loc1OccArea3G = Loc1OccArea3.get()
		Loc1PubArea3G = Loc1PubArea3.get()
		Loc1TotArea3G = Loc1TotArea3.get()
		Loc1State3G = Loc1State3.get()
		Loc1Zip3G = Loc1Zip3.get()
		incitymenu3G = incitymenu3.get()
		tenantOwnerMenu3G = tenantOwnerMenu3.get()
		leasedMenu3G = leasedMenu3.get()

		Loc1St4G = Loc1St4.get()
		Loc1City4G = Loc1City4.get()
		Loc1FullTEmp4G = Loc1FullTEmp4.get()
		Loc1PartTEmp4G = Loc1PartTEmp4.get()
		Loc1Rev4G = Loc1Rev4.get()
		Loc1OccArea4G = Loc1OccArea4.get()
		Loc1PubArea4G = Loc1PubArea4.get()
		Loc1TotArea4G = Loc1TotArea4.get()
		Loc1State4G = Loc1State4.get()
		Loc1Zip4G = Loc1Zip4.get()
		incitymenu4G = incitymenu4.get()
		tenantOwnerMenu4G = tenantOwnerMenu4.get()
		leasedMenu4G = leasedMenu4.get()

		carrierName1G = carrierName1.get()
		carrierEff1G = carrierEff1.get()
		carrierExp1G = carrierExp1.get()
		A125CheckGL1G = A125CheckGL1.get()
		A125CheckAuto1G = A125CheckAuto1.get()
		A125CheckProperty1G = A125CheckProperty1.get()
		A125CheckOther1G = A125CheckOther1.get()

		carrierName2G = carrierName2.get()
		carrierEff2G = carrierEff2.get()
		carrierExp2G = carrierExp2.get()
		A125CheckGL2G = A125CheckGL2.get()
		A125CheckAuto2G = A125CheckAuto2.get()
		A125CheckProperty2G = A125CheckProperty2.get()
		A125CheckOther2G = A125CheckOther2.get()

		carrierName3G = carrierName3.get()
		carrierEff3G = carrierEff3.get()
		carrierExp3G = carrierExp3.get()
		A125CheckGL3G = A125CheckGL3.get()
		A125CheckAuto3G = A125CheckAuto3.get()
		A125CheckProperty3G = A125CheckProperty3.get()
		A125CheckOther3G = A125CheckOther3.get()

		carrierName4G = carrierName4.get()
		carrierEff4G = carrierEff4.get()
		carrierExp4G = carrierExp4.get()
		A125CheckGL4G = A125CheckGL4.get()
		A125CheckAuto4G = A125CheckAuto4.get()
		A125CheckProperty4G = A125CheckProperty4.get()
		A125CheckOther4G = A125CheckOther4.get()

		A125LossNum1G = A125LossNum1.get()
		A125LossDate1G = A125LossDate1.get()
		A125TypeType1G = A125TypeType1.get()
		A125LossPaid1G = A125LossPaid1.get()
		A125LossNum2G = A125LossNum2.get()
		A125LossDate2G = A125LossDate2.get()
		A125TypeType2G = A125TypeType2.get()
		A125LossPaid2G = A125LossPaid2.get()

		A125natureG = A125nature.get()

		c = canvas.Canvas('Forms/simple_form_overlay.pdf')

		c.setFont("Helvetica", 8)


		c.drawString(22, 278, appNameG)
		c.drawString(22, 269, appAddressG)
		c.drawString(22, 258, appCityG)
		c.drawString(100, 258, appStateG)
		c.drawString(120, 258, appZipG)
		c.drawString(313, 684, appPhoneG)
		c.drawString(313, 684, appSecPhG)
		c.drawString(313, 684, appEmailG)
		
		c.drawString(313, 684, a125EffG)
		#c.drawString(313, 684, sectionsG)
		c.drawString(313, 684, a125TypeG)
		
		c.drawString(313, 684, Loc1St1G)
		c.drawString(313, 684, Loc1City1G)
		c.drawString(313, 684, Loc1FullTEmp1G)
		c.drawString(313, 684, Loc1PartTEmp1G)
		c.drawString(313, 684, Loc1Rev1G)
		c.drawString(313, 684, Loc1OccArea1G)
		c.drawString(313, 684, Loc1PubArea1G)
		c.drawString(313, 684, Loc1TotArea1G)
		c.drawString(313, 684, Loc1State1G)
		c.drawString(313, 684, Loc1Zip1G)
		c.drawString(313, 684, incitymenu1G)
		c.drawString(313, 684, tenantOwnerMenu1G)
		c.drawString(313, 684, leasedMenu1G)

		c.drawString(313, 684, Loc1St2G)
		c.drawString(313, 684, Loc1City2G)
		c.drawString(313, 684, Loc1FullTEmp2G)
		c.drawString(313, 684, Loc1PartTEmp2G)
		c.drawString(313, 684, Loc1Rev2G)
		c.drawString(313, 684, Loc1OccArea2G)
		c.drawString(313, 684, Loc1PubArea2G)
		c.drawString(313, 684, Loc1TotArea2G)
		c.drawString(313, 684, Loc1State2G)
		c.drawString(313, 684, Loc1Zip2G)
		c.drawString(313, 684, incitymenu2G)
		c.drawString(313, 684, tenantOwnerMenu2G)
		c.drawString(313, 684, leasedMenu2G)

		c.drawString(313, 684, Loc1St3G)
		c.drawString(313, 684, Loc1City3G)
		c.drawString(313, 684, Loc1FullTEmp3G)
		c.drawString(313, 684, Loc1PartTEmp3G)
		c.drawString(313, 684, Loc1Rev3G)
		c.drawString(313, 684, Loc1OccArea3G)
		c.drawString(313, 684, Loc1PubArea3G)
		c.drawString(313, 684, Loc1TotArea3G)
		c.drawString(313, 684, Loc1State3G)
		c.drawString(313, 684, Loc1Zip3G)
		c.drawString(313, 684, incitymenu3G)
		c.drawString(313, 684, tenantOwnerMenu3G)
		c.drawString(313, 684, leasedMenu3G)

		c.drawString(313, 684, Loc1St4G)
		c.drawString(313, 684, Loc1City4G)
		c.drawString(313, 684, Loc1FullTEmp4G)
		c.drawString(313, 684, Loc1PartTEmp4G)
		c.drawString(313, 684, Loc1Rev4G)
		c.drawString(313, 684, Loc1OccArea4G)
		c.drawString(313, 684, Loc1PubArea4G)
		c.drawString(313, 684, Loc1TotArea4G)
		c.drawString(313, 684, Loc1State4G)
		c.drawString(313, 684, Loc1Zip4G)
		c.drawString(313, 684, incitymenu4G)
		c.drawString(313, 684, tenantOwnerMenu4G)
		c.drawString(313, 684, leasedMenu4G)

		c.drawString(313, 684, carrierName1G)
		c.drawString(313, 684, carrierEff1G)
		c.drawString(313, 684, carrierExp1G)
		#c.drawString(313, 684, A125CheckGL1G)
		#c.drawString(313, 684, A125CheckAuto1G)
		#c.drawString(313, 684, A125CheckProperty1G)
		#c.drawString(313, 684, A125CheckOther1G)

		c.drawString(313, 684, carrierName2G)
		c.drawString(313, 684, carrierEff2G)
		c.drawString(313, 684, carrierExp2G)
		#c.drawString(313, 684, A125CheckGL2G)
		#c.drawString(313, 684, A125CheckAuto2G)
		#c.drawString(313, 684, A125CheckProperty2G)
		#c.drawString(313, 684, A125CheckOther2G)

		c.drawString(313, 684, carrierName3G)
		c.drawString(313, 684, carrierEff3G)
		c.drawString(313, 684, carrierExp3G)
		#c.drawString(313, 684, A125CheckGL3G)
		#c.drawString(313, 684, A125CheckAuto3G)
		#c.drawString(313, 684, A125CheckProperty3G)
		#c.drawString(313, 684, A125CheckOther3G)

		c.drawString(313, 684, carrierName4G)
		c.drawString(313, 684, carrierEff4G)
		c.drawString(313, 684, carrierExp4G)
		#c.drawString(313, 684, A125CheckGL4G)
		#c.drawString(313, 684, A125CheckAuto4G)
		#c.drawString(313, 684, A125CheckProperty4G)
		#c.drawString(313, 684, A125CheckOther4G)

		c.drawString(313, 684, A125LossNum1G)
		c.drawString(313, 684, A125LossDate1G)
		c.drawString(313, 684, A125TypeType1G)
		c.drawString(313, 684, A125LossPaid1G)
		#c.drawString(313, 684, A125LossNum2G)
		#c.drawString(313, 684, A125LossDate2G)
		#c.drawString(313, 684, A125TypeType2G)
		#c.drawString(313, 684, A125LossPaid2G)

		c.drawString(313, 684, A125natureG)

		c.save()

	def merge_pdfs(form_pdf, overlay_pdf, output):
	    """
	    Merge the specified fillable form PDF with the 
	    overlay PDF and save the output
	    """
	    form = pdfrw.PdfReader(form_pdf)
	    olay = pdfrw.PdfReader(overlay_pdf)
	    
	    for form_page, overlay_page in zip(form.pages, olay.pages):
	        merge_obj = pdfrw.PageMerge()
	        overlay = merge_obj.add(overlay_page)[0]
	        pdfrw.PageMerge(form_page).add(overlay).render()
	        
	    writer = pdfrw.PdfWriter()
	    writer.write(output, form)
	    
	    
	if __name__ == '__main__':
	    create_overlay()
	    merge_pdfs('Forms/acord-125p.pdf', 
	               'Forms/simple_form_overlay.pdf', 
	               'merged_form.pdf')

	os.remove('Forms/simple_form_overlay.pdf')


buttons = ttk.Frame(window)

save = Button(buttons, text = 'Save', width=10, command = saveEntries).grid(column = 0, row = 0)
load = Button(buttons, text = 'Load', width=10, command = loadEntries).grid(column = 1, row = 0)
generate = Button(buttons, text = 'Generate', width=10, command = generateForms).grid(column = 2, row = 0)

buttons.pack(expand = 1, fill ="both", padx = 30, pady = 5)

#-------------------------------------------------------------------------------------

window.mainloop() 