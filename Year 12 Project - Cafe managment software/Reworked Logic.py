#don't pollute your namespace with *
import tkinter as tk
from collections import Counter
import json
from datetime import datetime
import sys

dev_version = 0
print ('''      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  By: William van den Wall Bake
( C|/\/\/\/\/|  with a lot of help from
 '-./\/\/\/\/|  Michael Guidry on Stackoverflow
   '_________'
    '-------''')

#Window Initilisation
root = tk.Tk()
root.title('Cafe-Au-Lait Ordering')
root['bg']='#FFD966'
Innow = datetime.now()
InTime = Innow.strftime("%y%m%d%M")
StrTime = Innow.strftime("%d/%m/%Y")




#your variables had strange names and value syntax
pricelist = []
purchases = []
if dev_version == 1: header    = 'Developer Version\n'
else: header = 'Order:\n'
offset    = 0    #first line items will be printed on ~ set internally
selected  = -1   #used as a purchase index ~ -1 means nothing is selected
Takout_Cost = 0
Amount_Discount = 1
Totall = 0
invoice = int(InTime)
Customer_Name = ''

#by listing the properties of your items this way
#~you can create and manage buttons dynamically
items =[
    {'name':'Cappucino',       'cost':3.75},
    {'name':'Expresso',        'cost':3.00},
    {'name':'Double Expresso', 'cost':4.25},
    {'name':'Flat White',      'cost':3.75},
    {'name':'Latte',           'cost':3.50},
    {'name':'Iced',            'cost':2.50},
    {'name':'Cookie',          'cost':5.00},
]
#force an extra dummy row to take up all remaining space
root.grid_rowconfigure(len(items), weight=1)
#force Text display to resize with window
root.grid_columnconfigure(2, weight=1)

#only Text widgets are truly multiline
receipt_txt = tk.Text(root, width=35, bg='white', cursor='arrow', height=20)
receipt_txt.grid(row=0, column=2, rowspan=len(items)+5, sticky='nswe') #span to include dummy row

#init receipt
receipt_txt.insert('1.0', header) 
receipt_txt.insert('4.0', '\ntotal: $0.00') 
receipt_txt.tag_configure('selected', background='#FFF6AD')
receipt_txt.config(state='disabled')       #disable receipt

#work on later low priority
def Discount_Cal():
    global pricelist
    global Totall
    global Takout_Cost
    global Amount_Discount
    global dev_version

    Totall = sum(pricelist)
    if Takout_Cost == 1:
        Totall = Totall*1.05
        if dev_version ==1: print('Takeout Discount applied')
    if Amount_Discount == 1:
        if len(pricelist) > 2:    
            Totall = Totall*0.9
            if dev_version ==1: print ('Amount Discount applied')

#select a line for complete item deletion
def select(event):
    global selected
    global offset
    
    #line number that was clicked
    b = int(receipt_txt.index('@%d,%d' % (event.x, event.y)).split('.')[0])
    #the "total: $00.00" line number
    e = int(receipt_txt.index('end-1c').split('.')[0])
    #the text
    t = receipt_txt.get(f'{b}.0', f'{b}.end').strip()
    #if the line falls within the item range and has text
    if b in range(offset, e) and t:
        #reposition selected tag
        receipt_txt.tag_remove("selected", '1.0', 'end')
        receipt_txt.tag_add("selected", f'{b}.0', f'{b}.end')
    
    #used as 'purchases' index    
    selected = b - offset


#rewrite receipt and reconsider pricelist, selected and offset
def retotal():
    global pricelist
    global purchases
    global selected
    global offset
    global header
    global Takout_Cost
    global Amount_Discount
    global dev_version
    
    selected  = -1                          #unset selected
    pricelist = []                          #reset pricelist
    
    receipt_txt.config(state='normal')      #enable receipt for writing
    receipt_txt.delete('1.0', 'end')        #remove all text
    receipt_txt.insert('1.0', header)       #rewrite header
    
    #store the line that items will start on
    offset   = int(receipt_txt.index('end-1c').split('.')[0]) + 1 #because item starts with \n
    
    #rewrite all items
    for it in purchases:
        if it:
            pricelist.append(it["cost"])                 #rewrite pricelist
            strcost = f'${format(it["cost"], ".2f")}'    #create string of cost
            #write item to receipt
            receipt_txt.insert('end-1c', f'\n{it["name"]:<16} ---- {strcost:>{16-len(strcost)}}')
                                
    #rewrite "total" line
    Totall = sum(pricelist)
    if Takout_Cost == 1:
        Totall = Totall*1.05
        if dev_version ==1: print('Takeout Discount applied')
    if Amount_Discount == 1:
        if len(pricelist) > 2:    
            Totall = Totall*0.9
            if dev_version ==1: print ('Amount Discount applied')

    receipt_txt.insert('end-1c', f'\n\ntotal: ${format((Totall), ".2f")}') 
    receipt_txt.config(state='disabled')    #disable receipt

#invoice printing program, could be more optimised, but I am happy with function ATM
def Invoice():
    global pricelist
    global purchases
    global selected
    global offset
    global header
    global Takout_Cost
    global Amount_Discount
    global dev_version
    global datetime
    global invoice
    global Customer_Name
    global items

    Cust_Nam_Entry = tk.Toplevel()
    Cust_Nam_Entry.title('Enter Customer Name')

    e = tk.Label(Cust_Nam_Entry,text='Enter Customer Name')
    e.pack(side='top')

    #Custom Name for invoice
    def get_Name():
        global Name
        global Customer_Name
        Customer_Name = name.get()  
        Cust_Nam_Entry.destroy()

    b = tk.Button(Cust_Nam_Entry,text='okay',command=get_Name)
    b.pack(side='bottom')
    
    name = tk.Entry(Cust_Nam_Entry)
    name.pack()
    name.focus_set()
    root.wait_window(Cust_Nam_Entry) #Pausing main root window until Customer Name window has been destroyed

    receipt_txt.config(state='normal')      #enable receipt for writing
    receipt_txt.delete('1.0', 'end')        #remove all text
    receipt_txt.insert('1.0', '-Cafe-Au-Lait-\t  \nInvoice Number:'+str(invoice)) 
    #Putting time of order on sheet
    now = datetime.now()
    time = now.strftime("Date:%d/%m/%Y\nTime:%H:%M")
    receipt_txt.insert('end-1c', '\n'+time) 

    receipt_txt.insert('end-1c', '\nBilled to: ' + str(Customer_Name))
    current = []
    for it in purchases:
        if it:
             current.append((it['name']))
    a = dict(Counter(current))
    x = str(a)
    y = x.replace('{','')
    x = y.replace('}','')
    y = x.replace(',','\n')
    x = y.replace(':','--------------X')

    receipt_txt.insert('end-1c','\n ' + y)

    Totall = sum(pricelist)
    receipt_txt.insert('end-1c', f'\n\nTotal without discount: ${format((Totall), ".2f")}') 

    if Takout_Cost == 1:
        Totall = Totall*1.058
        if dev_version ==1: print('Takeout Discount applied')
    if Amount_Discount == 1:
        if len(pricelist) > 2:    
            Totall = Totall*0.9
            if dev_version ==1: print ('Amount Discount applied')
    Discount = sum(pricelist) - Totall

    if Discount > 0: elf = ('-') 
    else: elf = ('+')
    receipt_txt.insert('end-1c', '\nDiscount\Additonal Costs: $'+ (elf) + f'{format((Discount), ".2f")}') 

    receipt_txt.insert('end-1c', f'\n\n\t\t     Total: ${format((Totall), ".2f")}') 
    receipt_txt.config(state='disabled')


def Takout_Costr():
    global Takout_Cost
    if Takout_Cost == 0:
        Takout_Cost = 1
    else:
        Takout_Cost = 0
    retotal()

def Amount_Discontr():
    global Amount_Discount
    if Amount_Discount == 0:
        Amount_Discount = 1
    else:
        Amount_Discount = 0
    retotal()

#handles all item purchases
def add_item(item):
    global purchases
    
    purchases.append(item) #append to purchases
    retotal()              #reconsider receipt

#handles all item purchases
def add_item(item):
    global purchases
    
    purchases.append(item) #append to purchases
    retotal()              #reconsider receipt

#handles all item removals    
def remove_item(event=None, purchase_num=None):
    global purchases
    global selected

    selected = selected if not purchase_num else purchase_num
    if selected in range(0, len(purchases)):
        purchases.pop(selected) #append to purchases
        retotal()              #reconsider receipt

#unset selected    
def unselect(event=None):
    global selected
    selected = -1   

def archive():
    global invoice
    global InTime
    global text_Invoice
    export = receipt_txt.get("1.0", 'end')
    text_file = open(f'Invoice_{format((invoice), ".2f")}.txt','w+')
    text_file.write(export)
    text_file.close
    receipt_txt.config(state='normal')
    receipt_txt.insert('end-1c','\nInvoice now Avaliable in the same\nfolder as the .py in .txt')
    receipt_txt.config(state='disabled')
    

#receipt is left-clicked
receipt_txt.bind('<1>', select)
#receipt loses focus ~ unset 'selected'
receipt_txt.bind('<FocusOut>', unselect)
#delete key was pressed ~ remove   and retotal
receipt_txt.bind('<Delete>', remove_item)

#create all register buttons dynamically
for i, v in enumerate(items):
    tk.Button(root, text=v['name'], width=13, bg='#DB954A', command=lambda v=v: add_item(v)).grid(row=i, column=0, sticky='nw', pady=0)
    tk.Label(root, text=f"${format(v['cost'], '.2f')}", width=7, fg='#003BFF').grid(row=i, column=1,columnspan=1)

tk.Button(root, text='Toggle (On/off)\nTakeout cost', width=21, height=5, bg='#FFAF72',command=Takout_Costr).grid(row=i+1, column=0, columnspan=2)

tk.Button(root, text='Toggle (On/off)\nProduct Number Discount', width=21, height=5,bg='#FFAF72', command=Amount_Discontr).grid(row=i+2, column=0, columnspan=2)

tk.Button(root, text='Delete\nSelected item', height=5, width=13,bg='#FF6551', command=remove_item).grid(row=i+3,column=0)

tk.Button(root, text='Archive\n Invoice', height=5, width=7, bg='#FFC58E', command=archive).grid(row=i+3,column=1)

#Invoices
tk.Button(root, text='Print invoice', bg='#FFD966', command=Invoice,width=61,height=3).grid(row=i+4, column=0, columnspan=3)

root.mainloop()

print('exiting program...')