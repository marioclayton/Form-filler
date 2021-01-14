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
Acc140 = ttk.Frame(tabControl)


  
tabControl.add(ApplicantInfo, text ='Applicant')
tabControl.add(Acc125, text ='Accord 125')
tabControl.add(Acc126, text ='Accord 126')
tabControl.add(Acc140, text ='Accord 140')
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
A126GenAggV = v1

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
GeneralCont = ttk.Frame(tabControl3, width=400, height=400)


tabControl3.add(Contractors, text ='Contractors')
tabControl3.add(Products, text ='Products')
tabControl3.add(ClaimsMade, text ='Claims Made')
tabControl3.add(General, text ='General')
tabControl3.add(GeneralCont, text ='General Continued')



tabControl3.grid(column = 2, row = 0, pady = 0, padx = 30, rowspan = 7)

Questions = ttk.Frame(Contractors)
Questions.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions, text ="Does applicant draw plans, designs, or specifications for others?").grid(column = 0, row = 0, pady = 5) 
a126q1 =['Yes', 'No']
a126q1Clk = StringVar()
a126q1Clk.set(a126q1[1])
a126q1Mn = OptionMenu(Questions, a126q1Clk, *a126q1)
a126q1Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="Do any operations include blasting or utilize or store explosive material?").grid(column = 0, row = 1, pady = 5) 
a126q2 =['Yes', 'No']
a126q2Clk = StringVar()
a126q2Clk.set(a126q1[1])
a126q2Mn = OptionMenu(Questions, a126q2Clk, *a126q2)
a126q2Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="Do any operations include excavation, tunneling, underground work or earth moving?").grid(column = 0, row = 2, pady = 5) 
a126q3 =['Yes', 'No']
a126q3Clk = StringVar()
a126q3Clk.set(a126q3[1])
a126q3Mn = OptionMenu(Questions, a126q3Clk, *a126q3)
a126q3Mn.grid(column = 1, row = 2, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="Do your subcontractors carry coverages or limits less than yours?").grid(column = 0, row = 3, pady = 5) 
a126q4 =['Yes', 'No']
a126q4Clk = StringVar()
a126q4Clk.set(a126q4[1])
a126q4Mn = OptionMenu(Questions, a126q4Clk, *a126q4)
a126q4Mn.grid(column = 1, row = 3, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="Are subcontractors allowed to work without providing you with Certificates of Insurance?").grid(column = 0, row = 4, pady = 5) 
a126q5 =['Yes', 'No']
a126q5Clk = StringVar()
a126q5Clk.set(a126q5[1])
a126q5Mn = OptionMenu(Questions, a126q5Clk, *a126q5)
a126q5Mn.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions, text ="Does applicant lease equipment to others with or without operators?").grid(column = 0, row = 5, pady = 5) 
a126q6 =['Yes', 'No']
a126q6Clk = StringVar()
a126q6Clk.set(a126q6[1])
a126q6Mn = OptionMenu(Questions, a126q6Clk, *a126q6)
a126q6Mn.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)


Questions2 = ttk.Frame(Products)
Questions2.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions2, text ="Does applicant install, service or demonstrate products?").grid(column = 0, row = 0, pady = 5) 
a126q7 =['Yes', 'No']
a126q7Clk = StringVar()
a126q7Clk.set(a126q7[1])
a126q7Mn = OptionMenu(Questions2, a126q7Clk, *a126q7)
a126q7Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Foreign products sold, distributed, or used as components?").grid(column = 0, row = 1, pady = 5) 
a126q8 =['Yes', 'No']
a126q8Clk = StringVar()
a126q8Clk.set(a126q8[1])
a126q8Mn = OptionMenu(Questions2, a126q8Clk, *a126q8)
a126q8Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Research and development conducted or new products planned?").grid(column = 0, row = 2, pady = 5) 
a126q9 =['Yes', 'No']
a126q9Clk = StringVar()
a126q9Clk.set(a126q9[1])
a126q9Mn = OptionMenu(Questions2, a126q9Clk, *a126q9)
a126q9Mn.grid(column = 1, row = 2, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Guarantees, warranties, hold harmless agreements?").grid(column = 0, row = 3, pady = 5) 
a126q10 =['Yes', 'No']
a126q10Clk = StringVar()
a126q10Clk.set(a126q10[1])
a126q10Mn = OptionMenu(Questions2, a126q10Clk, *a126q10)
a126q10Mn.grid(column = 1, row = 3, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Products related to aircraft/space industry?").grid(column = 0, row = 4, pady = 5) 
a126q11 =['Yes', 'No']
a126q11Clk = StringVar()
a126q11Clk.set(a126q11[1])
a126q11Mn = OptionMenu(Questions2, a126q11Clk, *a126q11)
a126q11Mn.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Products recalled, discontinued, changed?").grid(column = 0, row = 5, pady = 5) 
a126q12 =['Yes', 'No']
a126q12Clk = StringVar()
a126q12Clk.set(a126q12[1])
a126q12Mn = OptionMenu(Questions2, a126q12Clk, *a126q12)
a126q12Mn.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Products of others sold or repackaged under applicant’s label?").grid(column = 0, row = 6, pady = 5) 
a126q13 =['Yes', 'No']
a126q13Clk = StringVar()
a126q13Clk.set(a126q13[1])
a126q13Mn = OptionMenu(Questions2, a126q13Clk, *a126q1)
a126q13Mn.grid(column = 1, row = 6, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Products under label of others?").grid(column = 0, row = 7, pady = 5) 
a126q14 =['Yes', 'No']
a126q14Clk = StringVar()
a126q14Clk.set(a126q14[1])
a126q14Mn = OptionMenu(Questions2, a126q14Clk, *a126q14)
a126q14Mn.grid(column = 1, row = 7, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Vendor’s coverage required?").grid(column = 0, row = 8, pady = 5) 
a126q15 =['Yes', 'No']
a126q15Clk = StringVar()
a126q15Clk.set(a126q15[1])
a126q15Mn = OptionMenu(Questions2, a126q15Clk, *a126q15)
a126q15Mn.grid(column = 1, row = 8, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions2, text ="Does any named insured sell to any other named insured?").grid(column = 0, row = 9, pady = 5) 
a126q16 =['Yes', 'No']
a126q16Clk = StringVar()
a126q16Clk.set(a126q16[1])
a126q16Mn = OptionMenu(Questions2, a126q16Clk, *a126q16)
a126q16Mn.grid(column = 1, row = 9, padx = 5, pady = 5, sticky=W)

Questions3 = ttk.Frame(ClaimsMade)
Questions3.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions3, text ="Does applicant install, service or demonstrate products?").grid(column = 0, row = 0, pady = 5) 
a126q17 =['Yes', 'No']
a126q17Clk = StringVar()
a126q17Clk.set(a126q17[1])
a126q17Mn = OptionMenu(Questions3, a126q17Clk, *a126q17)
a126q17Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions3, text ="Foreign products sold, distributed, or used as components?").grid(column = 0, row = 1, pady = 5) 
a126q18 =['Yes', 'No']
a126q18Clk = StringVar()
a126q18Clk.set(a126q18[1])
a126q18Mn = OptionMenu(Questions3, a126q18Clk, *a126q18)
a126q18Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

Questions4 = ttk.Frame(General)
Questions4.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions4, text ="Any medical facilities provided or medical professionals employed or contracted?").grid(column = 0, row = 0, pady = 5) 
a126q19 =['Yes', 'No']
a126q19Clk = StringVar()
a126q19Clk.set(a126q19[1])
a126q19Mn = OptionMenu(Questions4, a126q19Clk, *a126q19)
a126q19Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Any exposure to radioactive/nuclear materials?").grid(column = 0, row = 1, pady = 5) 
a126q20 =['Yes', 'No']
a126q20Clk = StringVar()
a126q20Clk.set(a126q20[1])
a126q20Mn = OptionMenu(Questions4, a126q20Clk, *a126q20)
a126q20Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Do operations involve storing, treating, discharging, applying, disposing or transporting hazardous material?").grid(column = 0, row = 2, pady = 5) 
a126q21 =['Yes', 'No']
a126q21Clk = StringVar()
a126q21Clk.set(a126q21[1])
a126q21Mn = OptionMenu(Questions4, a126q21Clk, *a126q21)
a126q21Mn.grid(column = 1, row = 2, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Any listed operations sold, acquired, or discontinued in the last five (5) years?").grid(column = 0, row = 3, pady = 5) 
a126q22 =['Yes', 'No']
a126q22Clk = StringVar()
a126q22Clk.set(a126q22[1])
a126q22Mn = OptionMenu(Questions4, a126q22Clk, *a126q22)
a126q22Mn.grid(column = 1, row = 3, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Is any machinery or equipment loaned or rented to others?").grid(column = 0, row = 4, pady = 5) 
a126q23 =['Yes', 'No']
a126q23Clk = StringVar()
a126q23Clk.set(a126q23[1])
a126q23Mn = OptionMenu(Questions4, a126q23Clk, *a126q23)
a126q23Mn.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Any watercraft, docks, floats owned, hired, or leased?").grid(column = 0, row = 5, pady = 5) 
a126q24 =['Yes', 'No']
a126q24Clk = StringVar()
a126q24Clk.set(a126q24[1])
a126q24Mn = OptionMenu(Questions4, a126q24Clk, *a126q24)
a126q24Mn.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Any parking facilities owned/ rented?").grid(column = 0, row = 6, pady = 5) 
a126q25 =['Yes', 'No']
a126q25Clk = StringVar()
a126q25Clk.set(a126q25[1])
a126q25Mn = OptionMenu(Questions4, a126q25Clk, *a126q25)
a126q25Mn.grid(column = 1, row = 6, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Is a fee charged for parking?").grid(column = 0, row = 7, pady = 5) 
a126q26 =['Yes', 'No']
a126q26Clk = StringVar()
a126q26Clk.set(a126q26[1])
a126q26Mn = OptionMenu(Questions4, a126q26Clk, *a126q26)
a126q26Mn.grid(column = 1, row = 7, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Are any recreational facilities provided?").grid(column = 0, row = 8, pady = 5) 
a126q27 =['Yes', 'No']
a126q27Clk = StringVar()
a126q27Clk.set(a126q27[1])
a126q27Mn = OptionMenu(Questions4, a126q27Clk, *a126q27)
a126q27Mn.grid(column = 1, row = 8, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Are there any lodging operations including apartments?").grid(column = 0, row = 9, pady = 5) 
a126q28 =['Yes', 'No']
a126q28Clk = StringVar()
a126q28Clk.set(a126q28[1])
a126q28Mn = OptionMenu(Questions4, a126q28Clk, *a126q28)
a126q28Mn.grid(column = 1, row = 9, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions4, text ="Is there a swimming pool on the premises?").grid(column = 0, row = 10, pady = 5) 
a126q29 =['Yes', 'No']
a126q29Clk = StringVar()
a126q29Clk.set(a126q29[1])
a126q29Mn = OptionMenu(Questions4, a126q29Clk, *a126q29)
a126q29Mn.grid(column = 1, row = 10, padx = 5, pady = 5, sticky=W)

Questions5 = ttk.Frame(GeneralCont)
Questions5.grid(column = 0, row = 0, pady = 0, padx = 30)

ttk.Label(Questions5, text ="Are social events sponsored?").grid(column = 0, row = 0, pady = 5) 
a126q30 =['Yes', 'No']
a126q30Clk = StringVar()
a126q30Clk.set(a126q30[1])
a126q30Mn = OptionMenu(Questions5, a126q30Clk, *a126q30)
a126q30Mn.grid(column = 1, row = 0, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Are athletic teams sponsored?").grid(column = 0, row = 1, pady = 5) 
a126q31 =['Yes', 'No']
a126q31Clk = StringVar()
a126q31Clk.set(a126q31[1])
a126q31Mn = OptionMenu(Questions5, a126q31Clk, *a126q31)
a126q31Mn.grid(column = 1, row = 1, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Any structural alterations contemplated?").grid(column = 0, row = 2, pady = 5) 
a126q32 =['Yes', 'No']
a126q32Clk = StringVar()
a126q32Clk.set(a126q32[1])
a126q32Mn = OptionMenu(Questions5, a126q32Clk, *a126q32)
a126q32Mn.grid(column = 1, row = 2, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Any demolition exposure contemplated?").grid(column = 0, row = 3, pady = 5) 
a126q33 =['Yes', 'No']
a126q33Clk = StringVar()
a126q33Clk.set(a126q33[1])
a126q33Mn = OptionMenu(Questions5, a126q33Clk, *a126q33)
a126q33Mn.grid(column = 1, row = 3, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Has applicant been active in or is currently active in joint ventures?").grid(column = 0, row = 4, pady = 5) 
a126q34 =['Yes', 'No']
a126q34Clk = StringVar()
a126q34Clk.set(a126q34[1])
a126q34Mn = OptionMenu(Questions5, a126q34Clk, *a126q34)
a126q34Mn.grid(column = 1, row = 4, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Do you lease employees to or from others?").grid(column = 0, row = 5, pady = 5) 
a126q35 =['Yes', 'No']
a126q35Clk = StringVar()
a126q35Clk.set(a126q35[1])
a126q35Mn = OptionMenu(Questions5, a126q35Clk, *a126q35)
a126q35Mn.grid(column = 1, row = 5, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Is there a labor interchange with any other business or subsidiaries?").grid(column = 0, row = 6, pady = 5) 
a126q36 =['Yes', 'No']
a126q36Clk = StringVar()
a126q36Clk.set(a126q36[1])
a126q36Mn = OptionMenu(Questions5, a126q36Clk, *a126q36)
a126q36Mn.grid(column = 1, row = 6, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Are daycare facilities operated or controlled?").grid(column = 0, row = 7, pady = 5) 
a126q37 =['Yes', 'No']
a126q37Clk = StringVar()
a126q37Clk.set(a126q37[1])
a126q37Mn = OptionMenu(Questions5, a126q37Clk, *a126q37)
a126q37Mn.grid(column = 1, row = 7, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Have any crimes occurred or been attempted on your premises within the last three (3) years?").grid(column = 0, row = 8, pady = 5) 
a126q38 =['Yes', 'No']
a126q38Clk = StringVar()
a126q38Clk.set(a126q38[1])
a126q38Mn = OptionMenu(Questions5, a126q38Clk, *a126q38)
a126q38Mn.grid(column = 1, row = 8, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Is there a formal, written safety and security policy in effect?").grid(column = 0, row = 9, pady = 5) 
a126q39 =['Yes', 'No']
a126q39Clk = StringVar()
a126q39Clk.set(a126q39[1])
a126q39Mn = OptionMenu(Questions5, a126q39Clk, *a126q39)
a126q39Mn.grid(column = 1, row = 9, padx = 5, pady = 5, sticky=W)

ttk.Label(Questions5, text ="Does the businesses’ promotional literature make any representations about the safety or security of the premises?").grid(column = 0, row = 10, pady = 5) 
a126q40 =['Yes', 'No']
a126q40Clk = StringVar()
a126q40Clk.set(a126q40[1])
a126q40Mn = OptionMenu(Questions5, a126q40Clk, *a126q40)
a126q40Mn.grid(column = 1, row = 10, padx = 5, pady = 5, sticky=W)



#---------------------------------------------------------------------------------
#-----------------------ACCORD 140------------------------------------------------
#---------------------------------------------------------------------------------


tabControl5 = ttk.Notebook(Acc140)
tabControl5.pack(expand = 1, fill ="both", padx = 30, pady = 30) 
a140Prem1 = ttk.Frame(tabControl5, width=400, height=400)
a140Prem2 = ttk.Frame(tabControl5, width=400, height=400)
tabControl5.add(a140Prem1, text ='Premise 1')
tabControl5.add(a140Prem2, text ='Premise 2')

def a140PremTabs(a140Prem):

	ttk.Label(a140Prem, text ="Subject of Ins").grid(column = 0, row = 0, padx = 5, pady = 5) 
	a140SubjectOfIns1 = ttk.Entry(a140Prem)
	a140SubjectOfIns1.grid(column = 0, row = 1, padx = 5, pady = 5) 
	a140SubjectOfIns2 = ttk.Entry(a140Prem)
	a140SubjectOfIns2.grid(column = 0, row = 2, padx = 5, pady = 5) 
	a140SubjectOfIns3 = ttk.Entry(a140Prem)
	a140SubjectOfIns3.grid(column = 0, row = 3, padx = 5, pady = 5) 
	a140SubjectOfIns4 = ttk.Entry(a140Prem)
	a140SubjectOfIns4.grid(column = 0, row = 4, padx = 5, pady = 5) 
	a140SubjectOfIns5 = ttk.Entry(a140Prem)
	a140SubjectOfIns5.grid(column = 0, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Amount").grid(column = 1, row = 0, padx = 5, pady = 5) 
	a140Amount1 = ttk.Entry(a140Prem)
	a140Amount1.grid(column = 1, row = 1, padx = 5, pady = 5) 
	a140Amount2 = ttk.Entry(a140Prem)
	a140Amount2.grid(column = 1, row = 2, padx = 5, pady = 5) 
	a140Amount3 = ttk.Entry(a140Prem)
	a140Amount3.grid(column = 1, row = 3, padx = 5, pady = 5) 
	a140Amount4 = ttk.Entry(a140Prem)
	a140Amount4.grid(column = 1, row = 4, padx = 5, pady = 5) 
	a140Amount5 = ttk.Entry(a140Prem)
	a140Amount5.grid(column = 1, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Coinsurance").grid(column = 2, row = 0, padx = 5, pady = 5) 
	a140Coins1 = ttk.Entry(a140Prem, width = 5)
	a140Coins1.grid(column = 2, row = 1, padx = 5, pady = 5) 
	a140Coins2 = ttk.Entry(a140Prem, width = 5)
	a140Coins2.grid(column = 2, row = 2, padx = 5, pady = 5) 
	a140Coins3 = ttk.Entry(a140Prem, width = 5)
	a140Coins3.grid(column = 2, row = 3, padx = 5, pady = 5) 
	a140Coins4 = ttk.Entry(a140Prem, width = 5)
	a140Coins4.grid(column = 2, row = 4, padx = 5, pady = 5) 
	a140Coins5 = ttk.Entry(a140Prem, width = 5)
	a140Coins5.grid(column = 2, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Valuation").grid(column = 3, row = 0, padx = 5, pady = 5) 
	a140Valuation1 = ttk.Entry(a140Prem, width = 5)
	a140Valuation1.grid(column = 3, row = 1, padx = 5, pady = 5) 
	a140Valuation2 = ttk.Entry(a140Prem, width = 5)
	a140Valuation2.grid(column = 3, row = 2, padx = 5, pady = 5) 
	a140Valuation3 = ttk.Entry(a140Prem, width = 5)
	a140Valuation3.grid(column = 3, row = 3, padx = 5, pady = 5) 
	a140Valuation4 = ttk.Entry(a140Prem, width = 5)
	a140Valuation4.grid(column = 3, row = 4, padx = 5, pady = 5) 
	a140Valuation5 = ttk.Entry(a140Prem, width = 5)
	a140Valuation5.grid(column = 3, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Causes").grid(column = 4, row = 0, padx = 5, pady = 5) 
	a140Cause1 = ttk.Entry(a140Prem)
	a140Cause1.grid(column = 4, row = 1, padx = 5, pady = 5) 
	a140Cause2 = ttk.Entry(a140Prem)
	a140Cause2.grid(column = 4, row = 2, padx = 5, pady = 5) 
	a140Cause3 = ttk.Entry(a140Prem)
	a140Cause3.grid(column = 4, row = 3, padx = 5, pady = 5) 
	a140Cause4 = ttk.Entry(a140Prem)
	a140Cause4.grid(column = 4, row = 4, padx = 5, pady = 5) 
	a140Cause5 = ttk.Entry(a140Prem)
	a140Cause5.grid(column = 4, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Infl Guard").grid(column = 5, row = 0, padx = 5, pady = 5) 
	a140INfGuard1 = ttk.Entry(a140Prem, width = 5)
	a140INfGuard1.grid(column = 5, row = 1, padx = 5, pady = 5) 
	a140INfGuard2 = ttk.Entry(a140Prem, width = 5)
	a140INfGuard2.grid(column = 5, row = 2, padx = 5, pady = 5) 
	a140INfGuard3 = ttk.Entry(a140Prem, width = 5)
	a140INfGuard3.grid(column = 5, row = 3, padx = 5, pady = 5) 
	a140INfGuard4 = ttk.Entry(a140Prem, width = 5)
	a140INfGuard4.grid(column = 5, row = 4, padx = 5, pady = 5) 
	a140INfGuard5 = ttk.Entry(a140Prem, width = 5)
	a140INfGuard5.grid(column = 5, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Deductible").grid(column = 6, row = 0, padx = 5, pady = 5) 
	a140Ded1 = ttk.Entry(a140Prem, width = 8)
	a140Ded1.grid(column = 6, row = 1, padx = 5, pady = 5) 
	a140Ded2 = ttk.Entry(a140Prem, width = 8)
	a140Ded2.grid(column = 6, row = 2, padx = 5, pady = 5) 
	a140Ded3 = ttk.Entry(a140Prem, width = 8)
	a140Ded3.grid(column = 6, row = 3, padx = 5, pady = 5) 
	a140Ded4 = ttk.Entry(a140Prem, width = 8)
	a140Ded4.grid(column = 6, row = 4, padx = 5, pady = 5) 
	a140Ded5 = ttk.Entry(a140Prem, width = 8)
	a140Ded5.grid(column = 6, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Forms and Conditions").grid(column = 7, row = 0, padx = 5, pady = 5) 
	a140Conditions1 = ttk.Entry(a140Prem)
	a140Conditions1.grid(column = 7, row = 1, padx = 5, pady = 5) 
	a140Conditions2 = ttk.Entry(a140Prem)
	a140Conditions2.grid(column = 7, row = 2, padx = 5, pady = 5) 
	a140Conditions3 = ttk.Entry(a140Prem)
	a140Conditions3.grid(column = 7, row = 3, padx = 5, pady = 5) 
	a140Conditions4 = ttk.Entry(a140Prem)
	a140Conditions4.grid(column = 7, row = 4, padx = 5, pady = 5) 
	a140Conditions5 = ttk.Entry(a140Prem)
	a140Conditions5.grid(column = 7, row = 5, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text =" ").grid(column = 0, row = 6, padx = 5, pady = 5)

	ttk.Label(a140Prem, text ="Construction Type").grid(column = 0, row = 7, padx = 5, pady = 5)
	a140Construction = ttk.Entry(a140Prem)
	a140Construction.grid(column = 1, row = 7, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Distance to hydrant").grid(column = 0, row = 8, padx = 5, pady = 5)
	a140Hydrant = ttk.Entry(a140Prem)
	a140Hydrant.grid(column = 1, row = 8, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Distance to fire station").grid(column = 0, row = 9, padx = 5, pady = 5)
	a140FireSt = ttk.Entry(a140Prem)
	a140FireSt.grid(column = 1, row = 9, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="PROT CL").grid(column = 0, row = 10, padx = 5, pady = 5)
	a140PROTCL = ttk.Entry(a140Prem)
	a140PROTCL.grid(column = 1, row = 10, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Number of stories").grid(column = 0, row = 11, padx = 5, pady = 5)
	a140Stories = ttk.Entry(a140Prem)
	a140Stories.grid(column = 1, row = 11, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Year built").grid(column = 0, row = 12, padx = 5, pady = 5)
	a140YearB = ttk.Entry(a140Prem)
	a140YearB.grid(column = 1, row = 12, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Total area").grid(column = 0, row = 13, padx = 5, pady = 5)
	a140TotalArea = ttk.Entry(a140Prem)
	a140TotalArea.grid(column = 1, row = 13, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Wiring update").grid(column = 0, row = 14, padx = 5, pady = 5)
	a140WiringUpd = ttk.Entry(a140Prem)
	a140WiringUpd.grid(column = 1, row = 14, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Plumbing update").grid(column = 0, row = 15, padx = 5, pady = 5)
	a140PlumbUpd = ttk.Entry(a140Prem)
	a140PlumbUpd.grid(column = 1, row = 15, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Roof update").grid(column = 0, row = 16, padx = 5, pady = 5)
	a140RoofUpd = ttk.Entry(a140Prem)
	a140RoofUpd.grid(column = 1, row = 16, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Heating update").grid(column = 0, row = 17, padx = 5, pady = 5)
	a140HeatUpd = ttk.Entry(a140Prem)
	a140HeatUpd.grid(column = 1, row = 17, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Roof type").grid(column = 2, row = 7, padx = 5, pady = 5)
	a140RoofType = ttk.Entry(a140Prem)
	a140RoofType.grid(column = 3, row = 7, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Other occupancies").grid(column = 2, row = 8, padx = 5, pady = 5)
	a140Occupancy = ttk.Entry(a140Prem)
	a140Occupancy.grid(column = 3, row = 8, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Burglar alarm").grid(column = 2, row = 9, padx = 5, pady = 5)
	a140Burglar = ttk.Entry(a140Prem)
	a140Burglar.grid(column = 3, row = 9, padx = 5, pady = 5) 

	ttk.Label(a140Prem, text ="Fire protection").grid(column = 2, row = 10, padx = 5, pady = 5)
	a140FireProt = ttk.Entry(a140Prem)
	a140FireProt.grid(column = 3, row = 10, padx = 5, pady = 5) 


	return a140SubjectOfIns1, a140SubjectOfIns2, a140SubjectOfIns3, a140SubjectOfIns4, a140SubjectOfIns5, a140Amount1, a140Amount2, a140Amount3, a140Amount4, a140Amount5, a140Coins1, a140Coins2, a140Coins3, a140Coins4, a140Coins5, a140Valuation1, a140Valuation2, a140Valuation3, a140Valuation4, a140Valuation5, a140Cause1, a140Cause2, a140Cause3, a140Cause4, a140Cause5, a140INfGuard1, a140INfGuard2, a140INfGuard3, a140INfGuard4, a140INfGuard5, a140Ded1, a140Ded2, a140Ded3, a140Ded4, a140Ded5, a140Conditions1, a140Conditions2, a140Conditions3, a140Conditions4, a140Conditions5, a140Construction, a140Hydrant, a140FireSt, a140PROTCL, a140Stories, a140YearB, a140TotalArea, a140WiringUpd, a140PlumbUpd, a140RoofUpd, a140HeatUpd, a140RoofType, a140Occupancy, a140Burglar, a140FireProt


	

a140SubjectOfIns11, a140SubjectOfIns21, a140SubjectOfIns31, a140SubjectOfIns41, a140SubjectOfIns51, a140Amount11, a140Amount21, a140Amount31, a140Amount41, a140Amount51, a140Coins11, a140Coins21, a140Coins31, a140Coins41, a140Coins51, a140Valuation11, a140Valuation21, a140Valuation31, a140Valuation41, a140Valuation51, a140Cause11, a140Cause21, a140Cause31, a140Cause41, a140Cause51, a140INfGuard11, a140INfGuard21, a140INfGuard31, a140INfGuard41, a140INfGuard51, a140Ded11, a140Ded21, a140Ded31, a140Ded41, a140Ded51, a140Conditions11, a140Conditions21, a140Conditions31, a140Conditions41, a140Conditions51, a140Construction1, a140Hydrant1, a140FireSt1, a140PROTCL1, a140Stories1, a140YearB1, a140TotalArea1, a140WiringUpd1, a140PlumbUpd1, a140RoofUpd1, a140HeatUpd1, a140RoofType1, a140Occupancy1, a140Burglar1, a140FireProt1 = a140PremTabs(a140Prem1)
a140SubjectOfIns12, a140SubjectOfIns22, a140SubjectOfIns32, a140SubjectOfIns42, a140SubjectOfIns52, a140Amount12, a140Amount22, a140Amount32, a140Amount42, a140Amount52, a140Coins12, a140Coins22, a140Coins32, a140Coins42, a140Coins52, a140Valuation12, a140Valuation22, a140Valuation32, a140Valuation42, a140Valuation52, a140Cause12, a140Cause22, a140Cause32, a140Cause42, a140Cause52, a140INfGuard12, a140INfGuard22, a140INfGuard32, a140INfGuard42, a140INfGuard52, a140Ded12, a140Ded22, a140Ded32, a140Ded42, a140Ded52, a140Conditions12, a140Conditions22, a140Conditions32, a140Conditions42, a140Conditions52, a140Construction2, a140Hydrant2, a140FireSt2, a140PROTCL2, a140Stories2, a140YearB2, a140TotalArea2, a140WiringUpd2, a140PlumbUpd2, a140RoofUpd2, a140HeatUpd2, a140RoofType2, a140Occupancy2, a140Burglar2, a140FireProt2 = a140PremTabs(a140Prem2)



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

	A126GenAggVG = A126GenAggV.get()

	Class1Location1G = Class1Location1.get()
	Class1Hazard1G = Class1Hazard1.get()
	Class1Classification1G = Class1Classification1.get()
	Class1CCode1G = Class1CCode1.get()
	Class1Basis1G = Class1Basis1.get()
	Class1Exposure1G = Class1Exposure1.get()
	Class1Location2G = Class1Location2.get()
	Class1Hazard2G = Class1Hazard2.get()
	Class1Classification2G = Class1Classification2.get()
	Class1CCode2G = Class1CCode2.get()
	Class1Basis2G = Class1Basis2.get()
	Class1Exposure2G = Class1Exposure2.get()
	Class1Location3G = Class1Location3.get()
	Class1Hazard3G = Class1Hazard3.get()
	Class1Classification3G = Class1Classification3.get()
	Class1CCode3G = Class1CCode3.get()
	Class1Basis3G = Class1Basis3.get()
	Class1Exposure3G = Class1Exposure3.get()
	Class1Location4G = Class1Location4.get()
	Class1Hazard4G = Class1Hazard4.get()
	Class1Classification4G = Class1Classification4.get()
	Class1CCode4G = Class1CCode4.get()
	Class1Basis4G = Class1Basis4.get()
	Class1Exposure4G = Class1Exposure4.get()

	a126q1MnG = a126q1Clk.get()
	a126q2MnG = a126q2Clk.get()
	a126q3MnG = a126q3Clk.get()
	a126q4MnG = a126q4Clk.get()
	a126q5MnG = a126q5Clk.get()
	a126q6MnG = a126q6Clk.get()
	a126q7MnG = a126q7Clk.get()
	a126q8MnG = a126q8Clk.get()
	a126q9MnG = a126q9Clk.get()
	a126q10MnG = a126q10Clk.get()
	a126q11MnG = a126q11Clk.get()
	a126q12MnG = a126q12Clk.get()
	a126q13MnG = a126q13Clk.get()
	a126q14MnG = a126q14Clk.get()
	a126q15MnG = a126q15Clk.get()
	a126q16MnG = a126q16Clk.get()
	a126q17MnG = a126q17Clk.get()
	a126q18MnG = a126q18Clk.get()
	a126q19MnG = a126q19Clk.get()
	a126q20MnG = a126q20Clk.get()
	a126q21MnG = a126q21Clk.get()
	a126q22MnG = a126q22Clk.get()
	a126q23MnG = a126q23Clk.get()
	a126q24MnG = a126q24Clk.get()
	a126q25MnG = a126q25Clk.get()
	a126q26MnG = a126q26Clk.get()
	a126q27MnG = a126q27Clk.get()
	a126q28MnG = a126q28Clk.get()
	a126q29MnG = a126q29Clk.get()
	a126q30MnG = a126q30Clk.get()
	a126q31MnG = a126q31Clk.get()
	a126q32MnG = a126q32Clk.get()
	a126q33MnG = a126q33Clk.get()
	a126q34MnG = a126q34Clk.get()
	a126q35MnG = a126q35Clk.get()
	a126q36MnG = a126q36Clk.get()
	a126q37MnG = a126q37Clk.get()
	a126q38MnG = a126q38Clk.get()
	a126q39MnG = a126q39Clk.get()
	a126q40MnG = a126q40Clk.get()

	a140SubjectOfIns11G = a140SubjectOfIns11.get()
	a140SubjectOfIns21G = a140SubjectOfIns21.get()
	a140SubjectOfIns31G = a140SubjectOfIns31.get()
	a140SubjectOfIns41G = a140SubjectOfIns41.get()
	a140SubjectOfIns51G = a140SubjectOfIns51.get()
	a140Amount11G = a140Amount11.get()
	a140Amount21G = a140Amount21.get()
	a140Amount31G = a140Amount31.get()
	a140Amount41G = a140Amount41.get()
	a140Amount51G = a140Amount51.get()
	a140Coins11G = a140Coins11.get()
	a140Coins21G = a140Coins21.get()
	a140Coins31G = a140Coins31.get()
	a140Coins41G = a140Coins41.get()
	a140Coins51G = a140Coins51.get()
	a140Valuation11G = a140Valuation11.get()
	a140Valuation21G = a140Valuation21.get()
	a140Valuation31G = a140Valuation31.get()
	a140Valuation41G = a140Valuation41.get()
	a140Valuation51G = a140Valuation51.get()
	a140Cause11G = a140Cause11.get()
	a140Cause21G = a140Cause21.get()
	a140Cause31G = a140Cause31.get()
	a140Cause41G = a140Cause41.get()
	a140Cause51G = a140Cause51.get()
	a140INfGuard11G = a140INfGuard11.get()
	a140INfGuard21G = a140INfGuard21.get()
	a140INfGuard31G = a140INfGuard31.get()
	a140INfGuard41G = a140INfGuard41.get()
	a140INfGuard51G = a140INfGuard51.get()
	a140Ded11G = a140Ded11.get()
	a140Ded21G = a140Ded21.get()
	a140Ded31G = a140Ded31.get()
	a140Ded41G = a140Ded41.get()
	a140Ded51G = a140Ded51.get()
	a140Conditions11G = a140Conditions11.get()
	a140Conditions21G = a140Conditions21.get()
	a140Conditions31G = a140Conditions31.get()
	a140Conditions41G = a140Conditions41.get()
	a140Conditions51G = a140Conditions51.get()
	a140Construction1G = a140Construction1.get()
	a140Hydrant1G = a140Hydrant1.get()
	a140FireSt1G = a140FireSt1.get()
	a140PROTCL1G = a140PROTCL1.get()
	a140Stories1G = a140Stories1.get()
	a140YearB1G = a140YearB1.get()
	a140TotalArea1G = a140TotalArea1.get()
	a140WiringUpd1G = a140WiringUpd1.get()
	a140PlumbUpd1G = a140PlumbUpd1.get()
	a140RoofUpd1G = a140RoofUpd1.get()
	a140HeatUpd1G = a140HeatUpd1.get()
	a140RoofType1G = a140RoofType1.get()
	a140Occupancy1G = a140Occupancy1.get()
	a140Burglar1G = a140Burglar1.get()
	a140FireProt1G = a140FireProt1.get()

	a140SubjectOfIns12G = a140SubjectOfIns12.get()
	a140SubjectOfIns22G = a140SubjectOfIns22.get()
	a140SubjectOfIns32G = a140SubjectOfIns32.get()
	a140SubjectOfIns42G = a140SubjectOfIns42.get()
	a140SubjectOfIns52G = a140SubjectOfIns52.get()
	a140Amount12G = a140Amount12.get()
	a140Amount22G = a140Amount22.get()
	a140Amount32G = a140Amount32.get()
	a140Amount42G = a140Amount42.get()
	a140Amount52G = a140Amount52.get()
	a140Coins12G = a140Coins12.get()
	a140Coins22G = a140Coins22.get()
	a140Coins32G = a140Coins32.get()
	a140Coins42G = a140Coins42.get()
	a140Coins52G = a140Coins52.get()
	a140Valuation12G = a140Valuation12.get()
	a140Valuation22G = a140Valuation22.get()
	a140Valuation32G = a140Valuation32.get()
	a140Valuation42G = a140Valuation42.get()
	a140Valuation52G = a140Valuation52.get()
	a140Cause12G = a140Cause12.get()
	a140Cause22G = a140Cause22.get()
	a140Cause32G = a140Cause32.get()
	a140Cause42G = a140Cause42.get()
	a140Cause52G = a140Cause52.get()
	a140INfGuard12G = a140INfGuard12.get()
	a140INfGuard22G = a140INfGuard22.get()
	a140INfGuard32G = a140INfGuard32.get()
	a140INfGuard42G = a140INfGuard42.get()
	a140INfGuard52G = a140INfGuard52.get()
	a140Ded12G = a140Ded12.get()
	a140Ded22G = a140Ded22.get()
	a140Ded32G = a140Ded32.get()
	a140Ded42G = a140Ded42.get()
	a140Ded52G = a140Ded52.get()
	a140Conditions12G = a140Conditions12.get()
	a140Conditions22G = a140Conditions22.get()
	a140Conditions32G = a140Conditions32.get()
	a140Conditions42G = a140Conditions42.get()
	a140Conditions52G = a140Conditions52.get()
	a140Construction2G = a140Construction2.get()
	a140Hydrant2G = a140Hydrant2.get()
	a140FireSt2G = a140FireSt2.get()
	a140PROTCL2G = a140PROTCL2.get()
	a140Stories2G = a140Stories2.get()
	a140YearB2G = a140YearB2.get()
	a140TotalArea2G = a140TotalArea2.get()
	a140WiringUpd2G = a140WiringUpd2.get()
	a140PlumbUpd2G = a140PlumbUpd2.get()
	a140RoofUpd2G = a140RoofUpd2.get()
	a140HeatUpd2G = a140HeatUpd2.get()
	a140RoofType2G = a140RoofType2.get()
	a140Occupancy2G = a140Occupancy2.get()
	a140Burglar2G = a140Burglar2.get()
	a140FireProt2G = a140FireProt2.get()
	

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
	'A125natureG', 'A126GenAggVG',
	'Class1Location1G', 'Class1Hazard1G', 'Class1Classification1G', 'Class1CCode1G', 'Class1Basis1G','Class1Exposure1G',
	'Class1Location2G', 'Class1Hazard2G', 'Class1Classification2G', 'Class1CCode2G', 'Class1Basis2G','Class1Exposure2G',
	'Class1Location3G', 'Class1Hazard3G', 'Class1Classification3G', 'Class1CCode3G', 'Class1Basis3G','Class1Exposure3G',
	'Class1Location4G', 'Class1Hazard4G', 'Class1Classification4G', 'Class1CCode4G', 'Class1Basis4G','Class1Exposure4G',
	'a126q1MnG', 'a126q2MnG', 'a126q3MnG', 'a126q4MnG', 'a126q5MnG', 'a126q6MnG', 'a126q7MnG', 'a126q8MnG', 'a126q9MnG', 'a126q10MnG',
	'a126q11MnG', 'a126q12MnG', 'a126q13MnG', 'a126q14MnG', 'a126q15MnG', 'a126q16MnG', 'a126q17MnG', 'a126q18MnG', 'a126q19MnG', 'a126q20MnG',
	'a126q21MnG', 'a126q22MnG', 'a126q23MnG', 'a126q24MnG', 'a126q25MnG', 'a126q26MnG', 'a126q27MnG', 'a126q28MnG', 'a126q29MnG', 'a126q30MnG',
	'a126q31MnG', 'a126q32MnG', 'a126q33MnG', 'a126q34MnG', 'a126q35MnG', 'a126q36MnG', 'a126q37MnG', 'a126q38MnG', 'a126q39MnG', 'a126q40MnG',
	'a140SubjectOfIns11G', 'a140SubjectOfIns21G', 'a140SubjectOfIns31G', 'a140SubjectOfIns41G', 'a140SubjectOfIns51G', 
	'a140Amount11G', 'a140Amount21G', 'a140Amount31G', 'a140Amount41G', 'a140Amount51G', 
	'a140Coins11G', 'a140Coins21G', 'a140Coins31G', 'a140Coins41G', 'a140Coins51G', 
	'a140Valuation11G', 'a140Valuation21G', 'a140Valuation31G', 'a140Valuation41G', 'a140Valuation51G', 
	'a140Cause11G', 'a140Cause21G', 'a140Cause31G', 'a140Cause41G', 'a140Cause51G', 
	'a140INfGuard11G', 'a140INfGuard21G', 'a140INfGuard31G', 'a140INfGuard41G', 'a140INfGuard51G', 
	'a140Ded11G', 'a140Ded21G', 'a140Ded31G', 'a140Ded41G', 'a140Ded51G', 
	'a140Conditions11G', 'a140Conditions21G', 'a140Conditions31G', 'a140Conditions41G', 'a140Conditions51G', 
	'a140Construction1G', 'a140Hydrant1G', 'a140FireSt1G', 'a140PROTCL1G', 'a140Stories1G', 'a140YearB1G', 
	'a140TotalArea1G', 'a140WiringUpd1G', 'a140PlumbUpd1G', 'a140RoofUpd1G','a140HeatUpd1G', 'a140RoofType1G', 
	'a140Occupancy1G', 'a140Burglar1G', 'a140FireProt1G', 
	'a140SubjectOfIns12G', 'a140SubjectOfIns22G', 'a140SubjectOfIns32G', 'a140SubjectOfIns42G', 'a140SubjectOfIns52G', 
	'a140Amount12G', 'a140Amount22G', 'a140Amount32G', 'a140Amount42G', 'a140Amount52G', 
	'a140Coins12G', 'a140Coins22G', 'a140Coins32G', 'a140Coins42G', 'a140Coins52G', 
	'a140Valuation12G', 'a140Valuation22G', 'a140Valuation32G','a140Valuation42G', 'a140Valuation52G', 
	'a140Cause12G', 'a140Cause22G', 'a140Cause32G', 'a140Cause42G', 'a140Cause52G', 
	'a140INfGuard12G', 'a140INfGuard22G', 'a140INfGuard32G', 'a140INfGuard42G', 'a140INfGuard52G', 
	'a140Ded12G', 'a140Ded22G', 'a140Ded32G', 'a140Ded42G', 'a140Ded52G', 
	'a140Conditions12G', 'a140Conditions22G', 'a140Conditions32G', 'a140Conditions42G', 'a140Conditions52G', 
	'a140Construction2G', 'a140Hydrant2G', 'a140FireSt2G', 'a140PROTCL2G', 'a140Stories2G', 'a140YearB2G', 
	'a140TotalArea2G', 'a140WiringUpd2G', 'a140PlumbUpd2G', 'a140RoofUpd2G', 'a140HeatUpd2G', 'a140RoofType2G', 
	'a140Occupancy2G', 'a140Burglar2G', 'a140FireProt2G']:
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


	A126GenAggV.set(entriesDic['A126GenAggVG'])


	Class1Location1.delete(0, 'end')
	Class1Location1.insert(0, entriesDic['Class1Location1G'])
	Class1Hazard1.delete(0, 'end')
	Class1Hazard1.insert(0, entriesDic['Class1Hazard1G'])
	Class1Classification1.delete(0, 'end')
	Class1Classification1.insert(0, entriesDic['Class1Classification1G'])
	Class1CCode1.delete(0, 'end')
	Class1CCode1.insert(0, entriesDic['Class1CCode1G'])
	Class1Basis1.delete(0, 'end')
	Class1Basis1.insert(0, entriesDic['Class1Basis1G'])
	Class1Exposure1.delete(0, 'end')
	Class1Exposure1.insert(0, entriesDic['Class1Exposure1G'])
	Class1Location2.delete(0, 'end')
	Class1Location2.insert(0, entriesDic['Class1Location2G'])
	Class1Hazard2.delete(0, 'end')
	Class1Hazard2.insert(0, entriesDic['Class1Hazard2G'])
	Class1Classification2.delete(0, 'end')
	Class1Classification2.insert(0, entriesDic['Class1Classification2G'])
	Class1CCode2.delete(0, 'end')
	Class1CCode2.insert(0, entriesDic['Class1CCode2G'])
	Class1Basis2.delete(0, 'end')
	Class1Basis2.insert(0, entriesDic['Class1Basis2G'])
	Class1Exposure2.delete(0, 'end')
	Class1Exposure2.insert(0, entriesDic['Class1Exposure2G'])
	Class1Location3.delete(0, 'end')
	Class1Location3.insert(0, entriesDic['Class1Location3G'])
	Class1Hazard3.delete(0, 'end')
	Class1Hazard3.insert(0, entriesDic['Class1Hazard3G'])
	Class1Classification3.delete(0, 'end')
	Class1Classification3.insert(0, entriesDic['Class1Classification3G'])
	Class1CCode3.delete(0, 'end')
	Class1CCode3.insert(0, entriesDic['Class1CCode3G'])
	Class1Basis3.delete(0, 'end')
	Class1Basis3.insert(0, entriesDic['Class1Basis3G'])
	Class1Exposure3.delete(0, 'end')
	Class1Exposure3.insert(0, entriesDic['Class1Exposure3G'])
	Class1Location4.delete(0, 'end')
	Class1Location4.insert(0, entriesDic['Class1Location4G'])
	Class1Hazard4.delete(0, 'end')
	Class1Hazard4.insert(0, entriesDic['Class1Hazard4G'])
	Class1Classification4.delete(0, 'end')
	Class1Classification4.insert(0, entriesDic['Class1Classification4G'])
	Class1CCode4.delete(0, 'end')
	Class1CCode4.insert(0, entriesDic['Class1CCode4G'])
	Class1Basis4.delete(0, 'end')
	Class1Basis4.insert(0, entriesDic['Class1Basis4G'])
	Class1Exposure4.delete(0, 'end')
	Class1Exposure4.insert(0, entriesDic['Class1Exposure4G'])

	a126q1Clk.set(entriesDic['a126q1MnG'])
	a126q2Clk.set(entriesDic['a126q2MnG'])
	a126q3Clk.set(entriesDic['a126q3MnG'])
	a126q4Clk.set(entriesDic['a126q4MnG'])
	a126q5Clk.set(entriesDic['a126q5MnG'])
	a126q6Clk.set(entriesDic['a126q6MnG'])
	a126q7Clk.set(entriesDic['a126q7MnG'])
	a126q8Clk.set(entriesDic['a126q8MnG'])
	a126q9Clk.set(entriesDic['a126q9MnG'])
	a126q10Clk.set(entriesDic['a126q10MnG'])
	a126q11Clk.set(entriesDic['a126q11MnG'])
	a126q12Clk.set(entriesDic['a126q12MnG'])
	a126q13Clk.set(entriesDic['a126q13MnG'])
	a126q14Clk.set(entriesDic['a126q14MnG'])
	a126q15Clk.set(entriesDic['a126q15MnG'])
	a126q16Clk.set(entriesDic['a126q16MnG'])
	a126q17Clk.set(entriesDic['a126q17MnG'])
	a126q18Clk.set(entriesDic['a126q18MnG'])
	a126q19Clk.set(entriesDic['a126q19MnG'])
	a126q20Clk.set(entriesDic['a126q20MnG'])
	a126q21Clk.set(entriesDic['a126q21MnG'])
	a126q22Clk.set(entriesDic['a126q22MnG'])
	a126q23Clk.set(entriesDic['a126q23MnG'])
	a126q24Clk.set(entriesDic['a126q24MnG'])
	a126q25Clk.set(entriesDic['a126q25MnG'])
	a126q26Clk.set(entriesDic['a126q26MnG'])
	a126q27Clk.set(entriesDic['a126q27MnG'])
	a126q28Clk.set(entriesDic['a126q28MnG'])
	a126q29Clk.set(entriesDic['a126q29MnG'])
	a126q30Clk.set(entriesDic['a126q30MnG'])
	a126q31Clk.set(entriesDic['a126q31MnG'])
	a126q32Clk.set(entriesDic['a126q32MnG'])
	a126q33Clk.set(entriesDic['a126q33MnG'])
	a126q34Clk.set(entriesDic['a126q34MnG'])
	a126q35Clk.set(entriesDic['a126q35MnG'])
	a126q36Clk.set(entriesDic['a126q36MnG'])
	a126q37Clk.set(entriesDic['a126q37MnG'])
	a126q38Clk.set(entriesDic['a126q38MnG'])
	a126q39Clk.set(entriesDic['a126q39MnG'])
	a126q40Clk.set(entriesDic['a126q40MnG'])

	a140SubjectOfIns11.delete(0, 'end')
	a140SubjectOfIns11.insert(0, entriesDic['a140SubjectOfIns11G'])
	a140SubjectOfIns21.delete(0, 'end')
	a140SubjectOfIns21.insert(0, entriesDic['a140SubjectOfIns21G'])
	a140SubjectOfIns31.delete(0, 'end')
	a140SubjectOfIns31.insert(0, entriesDic['a140SubjectOfIns31G'])
	a140SubjectOfIns41.delete(0, 'end')
	a140SubjectOfIns41.insert(0, entriesDic['a140SubjectOfIns41G'])
	a140SubjectOfIns51.delete(0, 'end')
	a140SubjectOfIns51.insert(0, entriesDic['a140SubjectOfIns51G'])
	a140Amount11.delete(0, 'end')
	a140Amount11.insert(0, entriesDic['a140Amount11G'])
	a140Amount21.delete(0, 'end')
	a140Amount21.insert(0, entriesDic['a140Amount21G'])
	a140Amount31.delete(0, 'end')
	a140Amount31.insert(0, entriesDic['a140Amount31G'])
	a140Amount41.delete(0, 'end')
	a140Amount41.insert(0, entriesDic['a140Amount41G'])
	a140Amount51.delete(0, 'end')
	a140Amount51.insert(0, entriesDic['a140Amount51G'])
	a140Coins11.delete(0, 'end')
	a140Coins11.insert(0, entriesDic['a140Coins11G'])
	a140Coins21.delete(0, 'end')
	a140Coins21.insert(0, entriesDic['a140Coins21G'])
	a140Coins31.delete(0, 'end')
	a140Coins31.insert(0, entriesDic['a140Coins31G'])
	a140Coins41.delete(0, 'end')
	a140Coins41.insert(0, entriesDic['a140Coins41G'])
	a140Coins51.delete(0, 'end')
	a140Coins51.insert(0, entriesDic['a140Coins51G'])
	a140Valuation11.delete(0, 'end')
	a140Valuation11.insert(0, entriesDic['a140Valuation11G'])
	a140Valuation21.delete(0, 'end')
	a140Valuation21.insert(0, entriesDic['a140Valuation21G'])
	a140Valuation31.delete(0, 'end')
	a140Valuation31.insert(0, entriesDic['a140Valuation31G'])
	a140Valuation41.delete(0, 'end')
	a140Valuation41.insert(0, entriesDic['a140Valuation41G'])
	a140Valuation51.delete(0, 'end')
	a140Valuation51.insert(0, entriesDic['a140Valuation51G'])
	a140Cause11.delete(0, 'end')
	a140Cause11.insert(0, entriesDic['a140Cause11G'])
	a140Cause21.delete(0, 'end')
	a140Cause21.insert(0, entriesDic['a140Cause21G'])
	a140Cause31.delete(0, 'end')
	a140Cause31.insert(0, entriesDic['a140Cause31G'])
	a140Cause41.delete(0, 'end')
	a140Cause41.insert(0, entriesDic['a140Cause41G'])
	a140Cause51.delete(0, 'end')
	a140Cause51.insert(0, entriesDic['a140Cause51G'])
	a140INfGuard11.delete(0, 'end')
	a140INfGuard11.insert(0, entriesDic['a140INfGuard11G'])
	a140INfGuard21.delete(0, 'end')
	a140INfGuard21.insert(0, entriesDic['a140INfGuard21G'])
	a140INfGuard31.delete(0, 'end')
	a140INfGuard31.insert(0, entriesDic['a140INfGuard31G'])
	a140INfGuard41.delete(0, 'end')
	a140INfGuard41.insert(0, entriesDic['a140INfGuard41G'])
	a140INfGuard51.delete(0, 'end')
	a140INfGuard51.insert(0, entriesDic['a140INfGuard51G'])
	a140Ded11.delete(0, 'end')
	a140Ded11.insert(0, entriesDic['a140Ded11G'])
	a140Ded21.delete(0, 'end')
	a140Ded21.insert(0, entriesDic['a140Ded21G'])
	a140Ded31.delete(0, 'end')
	a140Ded31.insert(0, entriesDic['a140Ded31G'])
	a140Ded41.delete(0, 'end')
	a140Ded41.insert(0, entriesDic['a140Ded41G'])
	a140Ded51.delete(0, 'end')
	a140Ded51.insert(0, entriesDic['a140Ded51G'])
	a140Conditions11.delete(0, 'end')
	a140Conditions11.insert(0, entriesDic['a140Conditions11G'])
	a140Conditions21.delete(0, 'end')
	a140Conditions21.insert(0, entriesDic['a140Conditions21G'])
	a140Conditions31.delete(0, 'end')
	a140Conditions31.insert(0, entriesDic['a140Conditions31G'])
	a140Conditions41.delete(0, 'end')
	a140Conditions41.insert(0, entriesDic['a140Conditions41G'])
	a140Conditions51.delete(0, 'end')
	a140Conditions51.insert(0, entriesDic['a140Conditions51G'])
	a140Construction1.delete(0, 'end')
	a140Construction1.insert(0, entriesDic['a140Construction1G'])
	a140Hydrant1.delete(0, 'end')
	a140Hydrant1.insert(0, entriesDic['a140Hydrant1G'])
	a140FireSt1.delete(0, 'end')
	a140FireSt1.insert(0, entriesDic['a140FireSt1G'])
	a140PROTCL1.delete(0, 'end')
	a140PROTCL1.insert(0, entriesDic['a140PROTCL1G'])
	a140Stories1.delete(0, 'end')
	a140Stories1.insert(0, entriesDic['a140Stories1G'])
	a140YearB1.delete(0, 'end')
	a140YearB1.insert(0, entriesDic['a140YearB1G'])
	a140TotalArea1.delete(0, 'end')
	a140TotalArea1.insert(0, entriesDic['a140TotalArea1G'])
	a140WiringUpd1.delete(0, 'end')
	a140WiringUpd1.insert(0, entriesDic['a140WiringUpd1G'])
	a140PlumbUpd1.delete(0, 'end')
	a140PlumbUpd1.insert(0, entriesDic['a140PlumbUpd1G'])
	a140RoofUpd1.delete(0, 'end')
	a140RoofUpd1.insert(0, entriesDic['a140RoofUpd1G'])
	a140HeatUpd1.delete(0, 'end')
	a140HeatUpd1.insert(0, entriesDic['a140HeatUpd1G'])
	a140RoofType1.delete(0, 'end')
	a140RoofType1.insert(0, entriesDic['a140RoofType1G'])
	a140Occupancy1.delete(0, 'end')
	a140Occupancy1.insert(0, entriesDic['a140Occupancy1G'])
	a140Burglar1.delete(0, 'end')
	a140Burglar1.insert(0, entriesDic['a140Burglar1G'])
	a140FireProt1.delete(0, 'end')
	a140FireProt1.insert(0, entriesDic['a140FireProt1G'])

	a140SubjectOfIns12.delete(0, 'end')
	a140SubjectOfIns12.insert(0, entriesDic['a140SubjectOfIns12G'])
	a140SubjectOfIns22.delete(0, 'end')
	a140SubjectOfIns22.insert(0, entriesDic['a140SubjectOfIns22G'])
	a140SubjectOfIns32.delete(0, 'end')
	a140SubjectOfIns32.insert(0, entriesDic['a140SubjectOfIns32G'])
	a140SubjectOfIns42.delete(0, 'end')
	a140SubjectOfIns42.insert(0, entriesDic['a140SubjectOfIns42G'])
	a140SubjectOfIns52.delete(0, 'end')
	a140SubjectOfIns52.insert(0, entriesDic['a140SubjectOfIns52G'])
	a140Amount12.delete(0, 'end')
	a140Amount12.insert(0, entriesDic['a140Amount12G'])
	a140Amount22.delete(0, 'end')
	a140Amount22.insert(0, entriesDic['a140Amount22G'])
	a140Amount32.delete(0, 'end')
	a140Amount32.insert(0, entriesDic['a140Amount32G'])
	a140Amount42.delete(0, 'end')
	a140Amount42.insert(0, entriesDic['a140Amount42G'])
	a140Amount52.delete(0, 'end')
	a140Amount52.insert(0, entriesDic['a140Amount52G'])
	a140Coins12.delete(0, 'end')
	a140Coins12.insert(0, entriesDic['a140Coins12G'])
	a140Coins22.delete(0, 'end')
	a140Coins22.insert(0, entriesDic['a140Coins22G'])
	a140Coins32.delete(0, 'end')
	a140Coins32.insert(0, entriesDic['a140Coins32G'])
	a140Coins42.delete(0, 'end')
	a140Coins42.insert(0, entriesDic['a140Coins42G'])
	a140Coins52.delete(0, 'end')
	a140Coins52.insert(0, entriesDic['a140Coins52G'])
	a140Valuation12.delete(0, 'end')
	a140Valuation12.insert(0, entriesDic['a140Valuation12G'])
	a140Valuation22.delete(0, 'end')
	a140Valuation22.insert(0, entriesDic['a140Valuation22G'])
	a140Valuation32.delete(0, 'end')
	a140Valuation32.insert(0, entriesDic['a140Valuation32G'])
	a140Valuation42.delete(0, 'end')
	a140Valuation42.insert(0, entriesDic['a140Valuation42G'])
	a140Valuation52.delete(0, 'end')
	a140Valuation52.insert(0, entriesDic['a140Valuation52G'])
	a140Cause12.delete(0, 'end')
	a140Cause12.insert(0, entriesDic['a140Cause12G'])
	a140Cause22.delete(0, 'end')
	a140Cause22.insert(0, entriesDic['a140Cause22G'])
	a140Cause32.delete(0, 'end')
	a140Cause32.insert(0, entriesDic['a140Cause32G'])
	a140Cause42.delete(0, 'end')
	a140Cause42.insert(0, entriesDic['a140Cause42G'])
	a140Cause52.delete(0, 'end')
	a140Cause52.insert(0, entriesDic['a140Cause52G'])
	a140INfGuard12.delete(0, 'end')
	a140INfGuard12.insert(0, entriesDic['a140INfGuard12G'])
	a140INfGuard22.delete(0, 'end')
	a140INfGuard22.insert(0, entriesDic['a140INfGuard22G'])
	a140INfGuard32.delete(0, 'end')
	a140INfGuard32.insert(0, entriesDic['a140INfGuard32G'])
	a140INfGuard42.delete(0, 'end')
	a140INfGuard42.insert(0, entriesDic['a140INfGuard42G'])
	a140INfGuard52.delete(0, 'end')
	a140INfGuard52.insert(0, entriesDic['a140INfGuard52G'])
	a140Ded12.delete(0, 'end')
	a140Ded12.insert(0, entriesDic['a140Ded12G'])
	a140Ded22.delete(0, 'end')
	a140Ded22.insert(0, entriesDic['a140Ded22G'])
	a140Ded32.delete(0, 'end')
	a140Ded32.insert(0, entriesDic['a140Ded32G'])
	a140Ded42.delete(0, 'end')
	a140Ded42.insert(0, entriesDic['a140Ded42G'])
	a140Ded52.delete(0, 'end')
	a140Ded52.insert(0, entriesDic['a140Ded52G'])
	a140Conditions12.delete(0, 'end')
	a140Conditions12.insert(0, entriesDic['a140Conditions12G'])
	a140Conditions22.delete(0, 'end')
	a140Conditions22.insert(0, entriesDic['a140Conditions22G'])
	a140Conditions32.delete(0, 'end')
	a140Conditions32.insert(0, entriesDic['a140Conditions32G'])
	a140Conditions42.delete(0, 'end')
	a140Conditions42.insert(0, entriesDic['a140Conditions42G'])
	a140Conditions52.delete(0, 'end')
	a140Conditions52.insert(0, entriesDic['a140Conditions52G'])
	a140Construction2.delete(0, 'end')
	a140Construction2.insert(0, entriesDic['a140Construction2G'])
	a140Hydrant2.delete(0, 'end')
	a140Hydrant2.insert(0, entriesDic['a140Hydrant2G'])
	a140FireSt2.delete(0, 'end')
	a140FireSt2.insert(0, entriesDic['a140FireSt2G'])
	a140PROTCL2.delete(0, 'end')
	a140PROTCL2.insert(0, entriesDic['a140PROTCL2G'])
	a140Stories2.delete(0, 'end')
	a140Stories2.insert(0, entriesDic['a140Stories2G'])
	a140YearB2.delete(0, 'end')
	a140YearB2.insert(0, entriesDic['a140YearB2G'])
	a140TotalArea2.delete(0, 'end')
	a140TotalArea2.insert(0, entriesDic['a140TotalArea2G'])
	a140WiringUpd2.delete(0, 'end')
	a140WiringUpd2.insert(0, entriesDic['a140WiringUpd2G'])
	a140PlumbUpd2.delete(0, 'end')
	a140PlumbUpd2.insert(0, entriesDic['a140PlumbUpd2G'])
	a140RoofUpd2.delete(0, 'end')
	a140RoofUpd2.insert(0, entriesDic['a140RoofUpd2G'])
	a140HeatUpd2.delete(0, 'end')
	a140HeatUpd2.insert(0, entriesDic['a140HeatUpd2G'])
	a140RoofType2.delete(0, 'end')
	a140RoofType2.insert(0, entriesDic['a140RoofType2G'])
	a140Occupancy2.delete(0, 'end')
	a140Occupancy2.insert(0, entriesDic['a140Occupancy2G'])
	a140Burglar2.delete(0, 'end')
	a140Burglar2.insert(0, entriesDic['a140Burglar2G'])
	a140FireProt2.delete(0, 'end')
	a140FireProt2.insert(0, entriesDic['a140FireProt2G'])




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


		#mycanvas.showPage()

		c.drawString(22, 278, appNameG)
		c.drawString(22, 269, appAddressG)
		c.drawString(22, 258, appCityG)
		c.drawString(100, 258, appStateG)
		c.drawString(120, 258, appZipG)
		c.drawString(23, 316, a125EffG)
		#c.drawString(313, 684, sectionsG)
		if a125TypeG == '1': c.drawString(20, 232, 'X')
		if a125TypeG == '2': c.drawString(20, 219, 'X')
		if a125TypeG == '3': c.drawString(96, 232, 'X')
		if a125TypeG == '4': c.drawString(96, 219, 'X')
		if a125TypeG == '5': c.drawString(226, 232, 'X')
		if a125TypeG == '6': c.drawString(226, 219, 'X')
		if a125TypeG == '7': c.drawString(323, 232, 'X')
		if a125TypeG == '8': c.drawString(323, 219, 'X')

		c.showPage()
		c.setFont("Helvetica", 8)

		c.drawString(28, 706, appPhoneG)
		c.drawString(107, 692, appEmailG)
		
		c.drawString(52, 648, Loc1St1G)
		c.drawString(70, 632, Loc1City1G)
		c.drawString(384, 648, Loc1FullTEmp1G)
		c.drawString(384, 622, Loc1PartTEmp1G)
		c.drawString(520, 656, Loc1Rev1G)
		c.drawString(520, 644, Loc1OccArea1G)
		c.drawString(520, 632, Loc1PubArea1G)
		c.drawString(520, 620, Loc1TotArea1G)
		c.drawString(225, 632, Loc1State1G)
		c.drawString(225, 620, Loc1Zip1G)
		if incitymenu1G == 'In': c.drawString(265, 645, 'X')
		if incitymenu1G == 'Out': c.drawString(265, 632, 'X')
		if tenantOwnerMenu1G == 'Owner' : c.drawString(313, 645, 'X')
		if tenantOwnerMenu1G == 'Tenant' : c.drawString(313, 632, 'X')
		if leasedMenu1G == 'Yes' : c.drawString(579, 608, 'Y')
		if leasedMenu1G == 'No' : c.drawString(579, 608, 'N')

		c.drawString(52, 588, Loc1St2G)
		c.drawString(70, 572, Loc1City2G)
		c.drawString(384, 588, Loc1FullTEmp2G)
		c.drawString(384, 562, Loc1PartTEmp2G)
		c.drawString(520, 596, Loc1Rev2G)
		c.drawString(520, 584, Loc1OccArea2G)
		c.drawString(520, 572, Loc1PubArea2G)
		c.drawString(520, 560, Loc1TotArea2G)
		c.drawString(225, 572, Loc1State2G)
		c.drawString(225, 560, Loc1Zip2G)
		if incitymenu2G == 'In': c.drawString(265, 585, 'X')
		if incitymenu2G == 'Out': c.drawString(265, 572, 'X')
		if tenantOwnerMenu2G == 'Owner' : c.drawString(313, 585, 'X')
		if tenantOwnerMenu2G == 'Tenant' : c.drawString(313, 572, 'X')
		if leasedMenu1G == 'Yes' : c.drawString(579, 548, 'Y')
		if leasedMenu1G == 'No' : c.drawString(579, 548, 'N')

		c.drawString(52, 528, Loc1St3G)
		c.drawString(70, 512, Loc1City3G)
		c.drawString(384, 528, Loc1FullTEmp3G)
		c.drawString(384, 502, Loc1PartTEmp3G)
		c.drawString(520, 536, Loc1Rev3G)
		c.drawString(520, 524, Loc1OccArea3G)
		c.drawString(520, 512, Loc1PubArea3G)
		c.drawString(520, 500, Loc1TotArea3G)
		c.drawString(225, 512, Loc1State3G)
		c.drawString(225, 500, Loc1Zip3G)
		if incitymenu3G == 'In': c.drawString(265, 525, 'X')
		if incitymenu3G == 'Out': c.drawString(265, 512, 'X')
		if tenantOwnerMenu3G == 'Owner' : c.drawString(313, 525, 'X')
		if tenantOwnerMenu3G == 'Tenant' : c.drawString(313, 512, 'X')
		if leasedMenu3G == 'Yes' : c.drawString(579, 488, 'Y')
		if leasedMenu3G == 'No' : c.drawString(579, 488, 'N')

		c.drawString(52, 468, Loc1St4G)
		c.drawString(70, 452, Loc1City4G)
		c.drawString(384, 468, Loc1FullTEmp4G)
		c.drawString(384, 442, Loc1PartTEmp4G)
		c.drawString(520, 476, Loc1Rev4G)
		c.drawString(520, 464, Loc1OccArea4G)
		c.drawString(520, 452, Loc1PubArea4G)
		c.drawString(520, 440, Loc1TotArea4G)
		c.drawString(225, 452, Loc1State4G)
		c.drawString(225, 440, Loc1Zip4G)
		if incitymenu4G == 'In': c.drawString(265, 465, 'X')
		if incitymenu4G == 'Out': c.drawString(265, 452, 'X')
		if tenantOwnerMenu4G == 'Owner' : c.drawString(313, 465, 'X')
		if tenantOwnerMenu4G == 'Tenant' : c.drawString(313, 452, 'X')
		if leasedMenu4G == 'Yes' : c.drawString(579, 428, 'Y')
		if leasedMenu4G == 'No' : c.drawString(579, 428, 'N')

		c.drawString(30, 360, 'A125nature')

		c.showPage()
		c.showPage()
		c.setFont("Helvetica", 8)

		c.drawString(23, 434, A125LossDate1G)
		c.drawString(133, 434, A125TypeType1G)
		c.drawString(382, 434, A125LossPaid1G)
		c.drawString(23, 422, A125LossDate2G)
		c.drawString(133, 422, A125TypeType2G)
		c.drawString(382, 422, A125LossPaid2G)
		



		if A125CheckGL1G == 1:
			c.drawString(126, 730, carrierName1G)
			c.drawString(126, 693, carrierEff1G)
			c.drawString(126, 682, carrierExp1G)
		if A125CheckAuto1G == 1:
			c.drawString(244, 730, carrierName1G)
			c.drawString(244, 693, carrierEff1G)
			c.drawString(244, 682, carrierExp1G)
		if A125CheckProperty1G == 1:
			c.drawString(363, 730, carrierName1G)
			c.drawString(363, 693, carrierEff1G)
			c.drawString(363, 682, carrierExp1G)
		if A125CheckOther1G == 1:
			c.drawString(482, 730, carrierName1G)
			c.drawString(482, 693, carrierEff1G)
			c.drawString(482, 682, carrierExp1G)

		if A125CheckGL2G == 1:
			c.drawString(126, 669, carrierName2G)
			c.drawString(126, 633, carrierEff2G)
			c.drawString(126, 622, carrierExp2G)
		if A125CheckAuto2G == 1:
			c.drawString(244, 669, carrierName2G)
			c.drawString(244, 633, carrierEff2G)
			c.drawString(244, 622, carrierExp2G)
		if A125CheckProperty2G == 1:
			c.drawString(363, 669, carrierName2G)
			c.drawString(363, 633, carrierEff2G)
			c.drawString(363, 622, carrierExp2G)
		if A125CheckOther2G == 1:
			c.drawString(482, 669, carrierName2G)
			c.drawString(482, 633, carrierEff2G)
			c.drawString(482, 622, carrierExp2G)

		if A125CheckGL2G == 1:
			c.drawString(126, 609, carrierName2G)
			c.drawString(126, 572, carrierEff2G)
			c.drawString(126, 561, carrierExp2G)
		if A125CheckAuto2G == 1:
			c.drawString(244, 609, carrierName2G)
			c.drawString(244, 572, carrierEff2G)
			c.drawString(244, 561, carrierExp2G)
		if A125CheckProperty2G == 1:
			c.drawString(363, 609, carrierName2G)
			c.drawString(363, 572, carrierEff2G)
			c.drawString(363, 561, carrierExp2G)
		if A125CheckOther2G == 1:
			c.drawString(482, 609, carrierName2G)
			c.drawString(482, 572, carrierEff2G)
			c.drawString(482, 561, carrierExp2G)

		if A125CheckGL2G == 1:
			c.drawString(126, 549, carrierName2G)
			c.drawString(126, 512, carrierEff2G)
			c.drawString(126, 500, carrierExp2G)
		if A125CheckAuto2G == 1:
			c.drawString(244, 549, carrierName2G)
			c.drawString(244, 512, carrierEff2G)
			c.drawString(244, 561, carrierExp2G)
		if A125CheckProperty2G == 1:
			c.drawString(363, 549, carrierName2G)
			c.drawString(363, 512, carrierEff2G)
			c.drawString(363, 500, carrierExp2G)
		if A125CheckOther2G == 1:
			c.drawString(482, 549, carrierName2G)
			c.drawString(482, 572, carrierEff2G)
			c.drawString(482, 500, carrierExp2G)



		

		


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