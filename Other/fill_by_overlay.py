# fill_by_overlay.py
import pdfrw
import os
from reportlab.pdfgen import canvas
import datetime

print('Welcome Waterhouse and Associates!')
print(' ')


def create_overlay():
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """

    effdate = input('Effective date: ')
    insured = input('Named insured: ')
    date = datetime.datetime.now()

    sub1 = input('Subject of insurance: ')
    amount1 = input('Amount: ')
    coin1 = input('Coinsurance: ')
    val1 = input('Valuation: ')
    cause1 = input('Cause of loss: ')
    infl1 = input('Inflation guard: ')
    ded1 = input('Deductible: ')
    condi1 = input('Fomrs and conditions to apply: ')
    ansub1 = input("Do you want to add a new subject of insurance? (y for yes)")
    if ansub1 == 'y':
        sub2 = input('Subject of insurance: ')
        amount2 = input('Amount: ')
        coin2 = input('Coinsurance: ')
        val2 = input('Valuation: ')
        cause2 = input('Cause of loss: ')
        infl2 = input('Inflation guard: ')
        ded2 = input('Deductible: ')
        condi2 = input('Fomrs and conditions to apply: ')
        ansub2 = input("Do you want to add a new subject of insurance? (y for yes)")
        if ansub2 == 'y':
            sub3 = input('Subject of insurance: ')
            amount3 = input('Amount: ')
            coin3 = input('Coinsurance: ')
            val3 = input('Valuation: ')
            cause3 = input('Cause of loss: ')
            infl3 = input('Inflation guard: ')
            ded3 = input('Deductible: ')
            condi3 = input('Fomrs and conditions to apply: ')
        else:
            sub3 = ' '
            amount3 = ' '
            coin3 = ' '
            val3 = ' '
            cause3 = ' '
            infl3 = ' '
            ded3 = ' '
            condi3 = ' '
    else:
        sub2 = ' '
        amount2 = ' '
        coin2 = ' '
        val2 = ' '
        cause2 = ' '
        infl2 = ' '
        ded2 = ' '
        condi2 = ' '
        sub3 = ' '
        amount3 = ' '
        coin3 = ' '
        val3 = ' '
        cause3 = ' '
        infl3 = ' '
        ded3 = ' '
        condi3 = ' '

    cnstr = input('Construction type: ')
    hdr = input('Distance to hydrant: ')
    fire = input('Distance to fire station: ')
    prot = input('PROT CL: ')
    stories = input('Number of stories: ')
    yrBuilt = input('Year built: ')
    area = input('Total area: ')

    wyr = input('Wiring update: ')
    pyr = input('Plumbing update: ')
    ryr = input('Roof update: ')
    hyr = input('Heating update: ')

    roofTy = input('Roof type: ')
    otherOcc = input('Other occupancies: ')

    burgAl = input('Burglar alarm: ')
    fireProt = input('Fire protection: ')





    c = canvas.Canvas('Forms/simple_form_overlay.pdf')

    c.drawString(25, 708, 'Waterhouse and Associates, Inc') 
    c.drawString(253, 684, effdate)
    c.drawString(313, 684, insured)
    c.drawString(513, 732, date.strftime("%x")) 


    c.drawString(25, 580, sub1)
    c.drawString(140, 580, amount1)
    c.drawString(213, 580, coin1)
    c.drawString(240, 580, val1)
    c.drawString(265, 580, cause1)
    c.drawString(330, 580, infl1)
    c.drawString(365, 580, ded1)
    c.drawString(456, 580, condi1)

    c.drawString(25, 556, sub2)
    c.drawString(140, 556, amount2)
    c.drawString(213, 556, coin2)
    c.drawString(240, 556, val2)
    c.drawString(265, 556, cause2)
    c.drawString(330, 556, infl2)
    c.drawString(365, 556, ded2)
    c.drawString(456, 556, condi2)

    c.drawString(25, 532, sub3)
    c.drawString(140, 532, amount3)
    c.drawString(213, 532, coin3)
    c.drawString(240, 532, val3)
    c.drawString(265, 532, cause3)
    c.drawString(330, 532, infl3)
    c.drawString(365, 532, ded3)
    c.drawString(456, 532, condi3)

    c.drawString(25, 317, cnstr)
    c.drawString(150, 317, hdr)
    c.drawString(193, 317, fire)
    c.drawString(384, 317, prot)
    c.drawString(420, 317, stories)
    c.drawString(492, 317, yrBuilt)
    c.drawString(532, 317, area)

    c.drawString(21, 292, 'x')
    c.drawString(80, 292, wyr)
    c.drawString(106, 292, 'x')
    c.drawString(168, 292, pyr)
    c.drawString(21, 279, 'x')
    c.drawString(80, 279, wyr)
    c.drawString(106, 279, 'x')
    c.drawString(168, 279, hyr)

    c.drawString(286, 292, roofTy)
    c.drawString(363, 292, otherOcc)

    c.drawString(21, 185, burgAl)
    c.drawString(21, 138, fireProt)
    
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
    merge_pdfs('Forms/acord-140p.pdf', 
               'Forms/simple_form_overlay.pdf', 
               'merged_form.pdf')

os.remove('Forms/simple_form_overlay.pdf')