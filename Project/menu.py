from tkinter import *
from tkinter import messagebox
from tkinter import Button


import mysql.connector
from tkinter import Tk, StringVar, ttk
#----------------------Front View------------------------------------------------------------------------------------------------------------------------------#

root=Tk()
root.title("MENU CARD")

root.geometry("1366x768+0+0")

root.iconbitmap('food.ico')
head=Frame(root, width=1350, height=100, bd=12, relief='raise')
head.pack(side=TOP)
lblhead=Label(head, font=('Pristina', 65, 'bold'), text="\t\tWelcome\t\t\t")
lblhead.grid(row=0, column=0)
bowe=Frame(root, width=1350, height=650, bd=12, relief='raise')
bowe.pack(side=BOTTOM)




lblName=Label(bowe, text=" Enter Your Name ", font=('Alegrian', 20) , width= 25,height=2)
lblName.grid(row=0,column=2)
entName=Entry(bowe,font='Alegrian',width=35)
entName.grid(row=0,column=3)
lblEm=Label(bowe, text=" Enter Your Email-ID",font=('Alegrian', 20) , width= 25,height=2 )
lblEm.grid(row=1,column=2)
entEm=Entry(bowe,font='Alegrian',width=35)
entEm.grid(row=1,column=3)
lblPn=Label(bowe,text="Enter Your Phone-NO. ",font=('Alegrian', 20) , width= 25,height=2)
lblPn.grid(row=2,column=2)
entPn=Entry(bowe,font='Alegrian',width=35)
entPn.grid(row=2,column=3)
lblTb=Label(bowe, text=" Enter Your Table No. ",font=('Alegrian', 20) , width= 25,height=2)
lblTb.grid(row=3,column=2)
entTb=Entry(bowe, font='Alegrian',width=35)
entTb.grid(row=3,column=3)


def Pn():
	try:
		Pn=entPn.get()
		Pnn=int(Pn)
		messagebox.showinfo("Success","Your Information has been Saved Successfully ")
	except ValueError:
		messagebox.showerror("Error","Re-entered your phone no. ")
		entPn.delete(0,END)
		entPn.focus()
def Tb():
	try:
		Tb=entTb.get()
		Tbn=int(Tb)
		messagebox.showinfo("Success","Your Table has been booked for you")
	except ValueError:
		messagebox.showerror("Error","Your Table is Booked or Input is taken wrong ")
		entTb.delete(0,END)
		entTb.focus()

		
def f1():
	con=None
	cursor=None
	try:
		con=mysql.connector.connect(
			host="localhost",
			user="root",
			passwd="root",
                        database="hotel")
		Name=entName.get()
		Em=entEm.get()
		Pn=int(entPn.get())
		Tb=int(entTb.get())
		cursor=con.cursor()

		cursor.execute('use hotel')
		cursor.execute("CREATE TABLE guest(Name varchar(40), Email_ID varchar(70), Phone_No bigint(10), Table_No int primary key)")
	
		sql="insert into guest values('%s', '%s', '%d','%d')"
		args=(Name,Em, Pn, Tb)
		cursor.execute(sql%args)
		con.commit()
		
	except mysql.connector.DatabaseError as e:
		con.rollback()
		messagebox.showerror("Issue ", e)
	finally:
		if cursor is not None:
			cursor.close()
		if con is not None:
			con.close()

def chk1():

       
        con=None
        cursor=None
        try:
                con=mysql.connector.connect(
                        host="localhost",
			user="root",
			passwd="root",
                        database="hotel")

                cursor=con.cursor()
                cursor.execute('use hotel')
                cursor.execute("Create Table Items( Items varchar(60), Quantity int)")

                con.commit()

        except mysql.connector.DatabaseError as e:
                con.rollback()
                messagebox.showerror("Issue ", e)
        finally:
                if cursor is not None:
                        cursor.close()
                if con is not None:
                        con.close()



Pc= Toplevel(root)
Pc.title("Menu List")
Pc.geometry("1366x768+0+0")
Pc.withdraw()
Pc.iconbitmap('food.ico')
def Pc1():
	root.withdraw()
	Pc.deiconify()

btnTb=Button(bowe, text="To check status of your table ",font=('Alegrian', 20) , width= 25, command=Tb)
btnTb.grid(columnspan=4)
btnSave=Button(bowe, text="Save ",font=('Alegrian', 20), command=Pn)
btnSave.grid(columnspan=5)
btProceed=Button(bowe, text="Proceed",font=('Alegrian', 20) , width= 25, command=lambda:[f1(),chk1(),Pc1()])
btProceed.grid(columnspan=6)
lbls1=Label(bowe,text="\n\n\n\n")
lbls1.grid(row=7)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------#


foodframe=Frame(Pc, width=1350, height=100, bd=12, relief='raise')
foodframe.pack(side=TOP)
lblTitle=Label(foodframe, font=('arail', 50, 'bold'), text="\t\tMenu Card\t\t\t\t\t\t")
lblTitle.grid(row=0, column=0)


bottomfoodframe=Frame(Pc, width=1350, height=650, bd=12, relief='raise')
bottomfoodframe.pack(side=BOTTOM)

FVstarter=Frame(bottomfoodframe, width=675, height=650, bd=12, relief='raise')
FVstarter.pack(side=LEFT)
FNstarter=Frame(bottomfoodframe, width=675, height=650, bd=12, relief='raise')
FNstarter.pack(side=LEFT)

FNstarterTOP=Frame(FNstarter, width=675, height=450, bd=12, relief='raise')
FNstarterTOP.pack(side=TOP)
FNstarterBOT=Frame(FNstarter, width=675, height=200, bd=12, relief='raise')
FNstarterBOT.pack(side=BOTTOM)


var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()
var43=IntVar()
var44=IntVar()
var45=IntVar()
var46=IntVar()
var47=IntVar()
var48=IntVar()
var49=IntVar()
var50=IntVar()
var51=IntVar()
var52=IntVar()
var53=IntVar()
var54=IntVar()
var55=IntVar()
var56=IntVar()
var57=IntVar()
var58=IntVar()
var59=IntVar()
var60=IntVar()
var61=IntVar()
var62=IntVar()
var63=IntVar()
var64=IntVar()
var65=IntVar()
var66=IntVar()
var67=IntVar()
var68=IntVar()
var69=IntVar()
var70=IntVar()
var71=IntVar()
var72=IntVar()
var73=IntVar()
var74=IntVar()
var75=IntVar()
var76=IntVar()
var77=IntVar()
var78=IntVar()
var79=IntVar()
var80=IntVar()



var1.set(0)
var2.set(0)
var3.set(0)
var4.set(0)
var5.set(0)
var6.set(0)
var7.set(0)
var8.set(0)
var9.set(0)
var10.set(0)
var11.set(0)
var12.set(0)
var13.set(0)
var14.set(0)
var15.set(0)
var16.set(0)
var17.set(0)
var18.set(0)
var19.set(0)
var20.set(0)
var21.set(0)
var22.set(0)
var23.set(0)
var24.set(0)
var25.set(0)
var26.set(0)
var27.set(0)
var28.set(0)
var29.set(0)
var30.set(0)
var31.set(0)
var32.set(0)
var33.set(0)
var34.set(0)
var35.set(0)
var36.set(0)
var37.set(0)
var38.set(0)
var39.set(0)
var40.set(0)
var41.set(0)
var42.set(0)
var43.set(0)
var44.set(0)
var45.set(0)
var46.set(0)
var47.set(0)
var48.set(0)
var49.set(0)
var50.set(0)
var51.set(0)
var52.set(0)
var53.set(0)
var54.set(0)
var55.set(0)
var56.set(0)
var57.set(0)
var58.set(0)
var59.set(0)
var60.set(0)
var61.set(0)
var62.set(0)
var63.set(0)
var64.set(0)
var65.set(0)
var66.set(0)
var67.set(0)
var68.set(0)
var69.set(0)
var70.set(0)
var71.set(0)
var72.set(0)
var73.set(0)
var74.set(0)
var75.set(0)
var76.set(0)
var77.set(0)
var78.set(0)
var79.set(0)
var80.set(0)



varPannTk=StringVar()
varPannTk.set("0")
varMancSoup=StringVar()
varMancSoup.set("0")
varVegKofta=StringVar()
varVegKofta.set("0")
varCutlet=StringVar()
varCutlet.set("0")
varManc=StringVar()
varManc.set("0")
varIdli=StringVar()
varIdli.set("0")
varDosa=StringVar()
varDosa.set("0")
varChilliPan=StringVar()
varChilliPan.set("0")
varRajmaK=StringVar()
varRajmaK.set("0")
varCheeseR=StringVar()
varCheeseR.set("0")
varAloo=StringVar()
varAloo.set("0")
varMirchi=StringVar()
varMirchi.set("0")
varDahi=StringVar()
varDahi.set("0")
varMedu=StringVar()
varMedu.set("0")

#------------------------------------#
varCMomos=StringVar()
varCMomos.set("0")
varCLolli=StringVar()
varCLolli.set("0")
varChilli=StringVar()
varChilli.set("0")
varCrispy=StringVar()
varCrispy.set("0")
varGarlic=StringVar()
varGarlic.set("0")
varCMancS=StringVar()
varCMancS.set("0")
varCAchari=StringVar()
varCAchari.set("0")
varCB=StringVar()
varCB.set("0")
varCCB=StringVar()
varCCB.set("0")
varCT=StringVar()
varCT.set("0")
varSM=StringVar()
varSM.set("0")

lblStarters=Label(FVstarter, font=('arail', 22, 'bold'), text="Starters")
lblStarters.grid(row=0,column=0)

def chkPannTk():
        if(var1.get()==1):
                entPannTk.configure(state=NORMAL)
                varPannTk.set("")
        elif(var1.get()==0):
                entPannTk.configure(state=DISABLED)
                varPannTk.set("0")

CPannTk=Checkbutton(FVstarter, text='Panner Tikka\t\t\t\tRs.70', variable=var1, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkPannTk).grid(row=1, column=0,sticky=W)

entPannTk=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varPannTk , width=6,justify='right', state=DISABLED)
entPannTk.grid(row=1,column=1)

def chkMancSoup():
        if(var2.get()==1):
                entMancSoup.configure(state=NORMAL)
                varMancSoup.set("")
        elif(var2.get()==0):
                entMancSoup.configure(state=DISABLED)
                varMancSoup.set("0")
                
CMancSoup=Checkbutton(FVstarter, text='Manchurian Soup\t\t\t\tRs.50', variable=var2, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMancSoup).grid(row=2, column=0,sticky=W)
entMancSoup=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varMancSoup , width=6,justify='right', state=DISABLED)
entMancSoup.grid(row=2,column=1)

def chkVegKofta():
        if(var3.get()==1):
                entVegKofta.configure(state=NORMAL)
                varVegKofta.set("")
        elif(var3.get()==0):
                entVegKofta.configure(state=DISABLED)
                varVegKofta.set("0")

CVegKofta=Checkbutton(FVstarter, text='Veg Kofta\t\t\t\tRs.80', variable=var3, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkVegKofta).grid(row=3, column=0,sticky=W)
entVegKofta=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varVegKofta , width=6,justify='right', state=DISABLED)
entVegKofta.grid(row=3,column=1)

def chkCutlet():
        if(var4.get()==1):
                entCutlet.configure(state=NORMAL)
                varCutlet.set("")
        elif(var4.get()==0):
                entCutlet.configure(state=DISABLED)
                varCutlet.set("0")
                
CCutlet=Checkbutton(FVstarter, text='Cutlet\t\t\t\t\tRs.75', variable=var4, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCutlet).grid(row=4, column=0,sticky=W)
entCutlet=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varCutlet , width=6,justify='right', state=DISABLED)
entCutlet.grid(row=4,column=1)

def chkManc():
        if(var5.get()==1):
                entManc.configure(state=NORMAL)
                varManc.set("")
        elif(var5.get()==0):
                entManc.configure(state=DISABLED)
                varManc.set("0")
                
CManc=Checkbutton(FVstarter, text='Veg Manchurian\t\t\t\tRs.65', variable=var5, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkManc).grid(row=5, column=0,sticky=W)
entManc=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varManc , width=6,justify='right', state=DISABLED)
entManc.grid(row=5,column=1)

def chkIdli():
        if(var6.get()==1):
                entIdli.configure(state=NORMAL)
                varIdli.set("")
        elif(var6.get()==0):
                entIdli.configure(state=DISABLED)
                varIdli.set("0")
                
CIdli=Checkbutton(FVstarter, text='Idli\t\t\t\t\tRs.40', variable=var6, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkIdli).grid(row=6, column=0,sticky=W)
entIdli=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varIdli , width=6,justify='right', state=DISABLED)
entIdli.grid(row=6,column=1)

def chkDosa():
        if(var7.get()==1):
                entDosa.configure(state=NORMAL)
                varDosa.set("")
        elif(var7.get()==0):
                entDosa.configure(state=DISABLED)
                varDosa.set("0")
                
CDosa=Checkbutton(FVstarter, text='Dosa\t\t\t\t\tRs.45', variable=var7, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDosa).grid(row=7, column=0,sticky=W)
entDosa=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varDosa , width=6,justify='right', state=DISABLED)
entDosa.grid(row=7,column=1)

def chkChilliPan():
        if(var8.get()==1):
                entChilliPan.configure(state=NORMAL)
                varChilliPan.set("")
        elif(var8.get()==0):
                entChilliPan.configure(state=DISABLED)
                varChilliPan.set("0")
                
CChilliPan=Checkbutton(FVstarter, text='Chilli Panner Dry\t\t\t\tRs.72', variable=var8, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChilliPan).grid(row=8, column=0,sticky=W)
entChilliPan=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varChilliPan , width=6,justify='right', state=DISABLED)
entChilliPan.grid(row=8,column=1)

def chkRajmaK():
        if(var9.get()==1):
                entRajmaK.configure(state=NORMAL)
                varRajmaK.set("")
        elif(var9.get()==0):
                entRajmaK.configure(state=DISABLED)
                varRajmaK.set("0")
                
CRajmaK=Checkbutton(FVstarter, text='Rajma Kebab\t\t\t\tRs.80', variable=var9, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkRajmaK).grid(row=9, column=0,sticky=W)
entRajmaK=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varRajmaK , width=6,justify='right', state=DISABLED)
entRajmaK.grid(row=9,column=1)

def chkCheeseR():
        if(var10.get()==1):
                entCheeseR.configure(state=NORMAL)
                varCheeseR.set("")
        elif(var10.get()==0):
                entCheeseR.configure(state=DISABLED)
                varCheeseR.set("0")
                
CCheeseR=Checkbutton(FVstarter, text='Cheese Roll\t\t\t\tRs.46', variable=var10, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCheeseR).grid(row=10, column=0,sticky=W)
entCheeseR=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varCheeseR , width=6,justify='right', state=DISABLED)
entCheeseR.grid(row=10,column=1)

def chkAloo():
        if(var11.get()==1):
                entAloo.configure(state=NORMAL)
                varAloo.set("")
        elif(var11.get()==0):
                entAloo.configure(state=DISABLED)
                varAloo.set("0")
CAloo=Checkbutton(FVstarter, text='Aloo Pakoda\t\t\t\tRs.48',variable=var11, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkAloo).grid(row=11, column=0,sticky=W)
entAloo=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varAloo , width=6,justify='right', state=DISABLED)
entAloo.grid(row=11,column=1)

def chkMirchi():
        if(var12.get()==1):
                entMirchi.configure(state=NORMAL)
                varMirchi.set("")
        elif(var12.get()==0):
                entMirchi.configure(state=DISABLED)
                varMirchi.set("0")
                
CMirchi=Checkbutton(FVstarter, text='Mirchi Bajji\t\t\t\tRs.35', variable=var12, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMirchi).grid(row=12, column=0,sticky=W)
entMirchi=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varMirchi , width=6,justify='right', state=DISABLED)
entMirchi.grid(row=12,column=1)

def chkDahi():
        if(var13.get()==1):
                entDahi.configure(state=NORMAL)
                varDahi.set("")
        elif(var13.get()==0):
                entDahi.configure(state=DISABLED)
                varDahi.set("0")
                
CDahi=Checkbutton(FVstarter, text='Dahi Vada\t\t\t\tRs.38', variable=var13, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDahi).grid(row=13, column=0,sticky=W)
entDahi=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varDahi , width=6,justify='right', state=DISABLED)
entDahi.grid(row=13,column=1)

def chkMedu():
        if(var14.get()==1):
                entMedu.configure(state=NORMAL)
                varMedu.set("")
        elif(var14.get()==0):
                entMedu.configure(state=DISABLED)
                varMedu.set("0")
                
CMedu=Checkbutton(FVstarter, text='Medu Vada\t\t\t\tRs.35', variable=var14, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMedu).grid(row=14, column=0,sticky=W)
entMedu=Entry(FVstarter, font=('arail', 16, 'bold') ,textvariable=varMedu , width=6,justify='right', state=DISABLED)
entMedu.grid(row=14,column=1)

lblspace=Label(FVstarter, text="\t\t\t\t\t\t\t\t\t\t\t\t")
lblspace.grid(row=15,column=0)

#---------------------------------------------------------Frame2---------------------------------------------------------------------------------------------------#

lblNStarters=Label(FNstarterTOP, font=('arail', 22, 'bold'), text="NonVeg-Starters")
lblNStarters.grid(row=0,column=0)

def chkCMomos():
        if(var15.get()==1):
                entCMomos.configure(state=NORMAL)
                varCMomos.set("")
        elif(var15.get()==0):
                entCMomos.configure(state=DISABLED)
                varCMomos.set("0")

CCMomos=Checkbutton(FNstarterTOP, text='Chicken Momos\t\t\tRs.90', variable=var15, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCMomos).grid(row=1, column=0,sticky=W)
entCMomos=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCMomos, width=6,justify='right', state=DISABLED)
entCMomos.grid(row=1,column=1)

def chkCLolli():
        if(var16.get()==1):
                entCLolli.configure(state=NORMAL)
                varCLolli.set("")
        elif(var16.get()==0):
                entCLolli.configure(state=DISABLED)
                varCLolli.set("0")
                
CCLolli=Checkbutton(FNstarterTOP, text='Chicken Lollipop\t\t\tRs.130', variable=var16, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCLolli).grid(row=2, column=0,sticky=W)
entCLolli=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCLolli, width=6,justify='right', state=DISABLED)
entCLolli.grid(row=2,column=1)

def chkChilli():
        if(var17.get()==1):
                entChilli.configure(state=NORMAL)
                varChilli.set("")
        elif(var17.get()==0):
                entChilli.configure(state=DISABLED)
                varChilli.set("0")

CChilli=Checkbutton(FNstarterTOP, text='Chicken Chilly\t\t\tRs.100', variable=var17, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChilli).grid(row=3, column=0,sticky=W)
entChilli=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varChilli, width=6,justify='right', state=DISABLED)
entChilli.grid(row=3,column=1)

def chkCrispy():
        if(var18.get()==1):
                entCrispy.configure(state=NORMAL)
                varCrispy.set("")
        elif(var18.get()==0):
                entCrispy.configure(state=DISABLED)
                varCrispy.set("0")
                
CCrispy=Checkbutton(FNstarterTOP, text='Chicken Crispy\t\t\tRs.120', variable=var18, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCrispy).grid(row=4, column=0,sticky=W)
entCrispy=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCrispy, width=6,justify='right', state=DISABLED)
entCrispy.grid(row=4,column=1)

def chkGarlic():
        if(var19.get()==1):
                entGarlic.configure(state=NORMAL)
                varGarlic.set("")
        elif(var19.get()==0):
                entGarlic.configure(state=DISABLED)
                varGarlic.set("0")
                
CGarlic=Checkbutton(FNstarterTOP, text='Chicken Garlic\t\t\tRs.123', variable=var19, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkGarlic).grid(row=5, column=0,sticky=W)
entGarlic=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varGarlic, width=6,justify='right', state=DISABLED)
entGarlic.grid(row=5,column=1)

def chkCMancS():
        if(var20.get()==1):
                entCMancS.configure(state=NORMAL)
                varCMancS.set("")
        elif(var20.get()==0):
                entCMancS.configure(state=DISABLED)
                varCMancS.set("0")
                
CCMancS=Checkbutton(FNstarterTOP, text='Chicken Manchurian Soup\t\tRs.80', variable=var20, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCMancS).grid(row=6, column=0,sticky=W)
entCMancS=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCMancS, width=6,justify='right', state=DISABLED)
entCMancS.grid(row=6,column=1)

def chkCAchari():
        if(var21.get()==1):
                entCAchari.configure(state=NORMAL)
                varCAchari.set("")
        elif(var21.get()==0):
                entCAchari.configure(state=DISABLED)
                varCAchari.set("0")
                
CCAchari=Checkbutton(FNstarterTOP, text='Chicken Achari Dry\t\tRs.100', variable=var21, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCAchari).grid(row=7, column=0,sticky=W)
entCAchari=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCAchari, width=6,justify='right', state=DISABLED)
entCAchari.grid(row=7,column=1)

def chkCB():
        if(var22.get()==1):
                entCB.configure(state=NORMAL)
                varCB.set("")
        elif(var22.get()==0):
                entCB.configure(state=DISABLED)
                varCB.set("0")
                
CCB=Checkbutton(FNstarterTOP, text='Chicken Balls\t\t\tRs.90', variable=var22, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCB).grid(row=8, column=0,sticky=W)
entCB=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCB, width=6,justify='right', state=DISABLED)
entCB.grid(row=8,column=1)

def chkCCB():
        if(var23.get()==1):
                entCCB.configure(state=NORMAL)
                varCCB.set("")
        elif(var23.get()==0):
                entCCB.configure(state=DISABLED)
                varCCB.set("0")

CCCB=Checkbutton(FNstarterTOP, text='Chicken Cheese Balls\t\tRs.88', variable=var23, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCCB).grid(row=9, column=0,sticky=W)
entCCB=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCCB, width=6,justify='right', state=DISABLED)
entCCB.grid(row=9,column=1)

def chkT():
        if(var24.get()==1):
                entCT.configure(state=NORMAL)
                varCT.set("")
        elif(var24.get()==0):
                entCT.configure(state=DISABLED)
                varCT.set("0")
                
CT=Checkbutton(FNstarterTOP, text='Chicken Tandori\t\t\tRs.140', variable=var24, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkT).grid(row=10, column=0,sticky=W)
entCT=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varCT, width=6,justify='right', state=DISABLED)
entCT.grid(row=10,column=1)

def chkSM():
        if(var25.get()==1):
                entSM.configure(state=NORMAL)
                varSM.set("")
        elif(var25.get()==0):
                entSM.configure(state=DISABLED)
                varSM.set("0")
                
CSM=Checkbutton(FNstarterTOP, text='Chicken Simply\t\t\tRs.95', variable=var25, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkSM).grid(row=11, column=0,sticky=W)
entSM=Entry(FNstarterTOP, font=('arail', 16, 'bold') ,textvariable=varSM, width=6,justify='right', state=DISABLED)
entSM.grid(row=11,column=1)


lblspace=Label(FNstarterTOP, text="\t\t\t\t\t\t\t\t\t\t\t")
lblspace.grid(row=13,column=0)




varTotal=StringVar()
varTotal.set('0')



def PannTk():
        if(var1.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Panner Tikka'
                        value2=int(varPannTk.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MancSoup():
        if(var2.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Manchurian Soup'
                        value2=int(varMancSoup.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def VegKofta():
        if(var3.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Veg Kofta'
                        value2=int(varVegKofta.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Cutlet():
        if(var4.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Cutlet'
                        value2=int(varCutlet.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Manc():
        if(var5.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Manchurian Soup'
                        value2=int(varManc.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Idli():
        if(var6.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Idli'
                        value2=int(varIdli.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Dosa():
        if(var7.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Dosa'
                        value2=int(varDosa.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChilliPan():
        if(var8.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chilli Paneer Dry'
                        value2=int(varChilliPan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def RajmaK():
        if(var9.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Rajma Kebab'
                        value2=int(varRajmaK.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CheeseR():
        if(var10.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Cheese Roll'
                        value2=int(varCheeseR.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Aloo():
        if(var11.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Aloo Pakods'
                        value2=int(varAloo.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Mirchi():
        if(var12.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Mirchi Bajji'
                        value2=int(varMirchi.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Dahi():
        if(var13.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Dahi Vada'
                        value2=int(varDahi.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Medu():
        if(var14.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Medu Vada'
                        value2=int(varMedu.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CMomos():
        if(var15.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Momos'
                        value2=int(varCMomos.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CLolli():
        if(var16.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Lollipop'
                        value2=int(varCLolli.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Chilli():
        if(var17.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Chilly'
                        value2=int(varChilli.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Crispy():
        if(var18.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Crispy'
                        value2=int(varCrispy.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Garlic():
        if(var19.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Garlic'
                        value2=int(varGarlic.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CMancS():
        if(var20.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Manchurian Soup'
                        value2=int(varCMancS.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CAchari():
        if(var21.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Achari Dry'
                        value2=int(varCAchari.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CB():
        if(var22.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Balls'
                        value2=int(varCB.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CCB():
        if(var23.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Cheese Balls'
                        value2=int(varCCB.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CT():
        if(var24.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Tandori'
                        value2=int(varCT.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def SM():
        if(var25.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Simply'
                        value2=int(varSM.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass



#-----------------------------------------Meal section-------------------------------------------------------------------------------------------------------------#
Me= Toplevel(Pc)
Me.title("Menu List")
Me.geometry("1366x768+0+0")
Me.withdraw()
Me.iconbitmap('food.ico')
def me():
	Pc.withdraw()
	Me.deiconify()

btnnext=Button(FNstarterBOT, text="Proceed towards Main Course ", width=675, font=('arail', 20, 'bold'), command=lambda:[me(),PannTk(),MancSoup(),VegKofta(),Cutlet(),Manc(),Idli(),Dosa(),ChilliPan(),RajmaK(),CheeseR(),Aloo(),Mirchi(),Dahi(),Medu(),CMomos(),CLolli(),Chilli(),Crispy(),Garlic(),CMancS(),CAchari(),CB(),CCB(),CT(),SM()])
btnnext.pack()


mealframe=Frame(Me, width=1350, height=100, bd=12, relief='raise')
mealframe.pack(side=TOP)
lblTitleM=Label(mealframe, font=('arail', 50, 'bold'), text="\t\tMain Course\t\t\t\t\t\t")
lblTitleM.grid(row=0, column=0)

bottomMCframe=Frame(Me, width=1350, height=650, bd=12, relief='raise')
bottomMCframe.pack(side=BOTTOM)

FVMC=Frame(bottomMCframe, width=675, height=650, bd=12, relief='raise')
FVMC.pack(side=LEFT)
FNonVMC=Frame(bottomMCframe, width=675, height=650, bd=12, relief='raise')
FNonVMC.pack(side=LEFT)

FVMCTOP=Frame(FVMC, width=675, height=450, bd=12, relief='raise')
FVMCTOP.pack(side=TOP)
FVMCBOTTOM=Frame(FVMC, width=675, height=200, bd=12, relief='raise')
FVMCBOTTOM.pack(side=BOTTOM)

FNonVMCTOP=Frame(FNonVMC, width=675, height=450, bd=12, relief='raise')
FNonVMCTOP.pack(side=TOP)
FNonVMCBOTTOM=Frame(FNonVMC, width=675, height=200, bd=12, relief='raise')
FNonVMCBOTTOM.pack(side=BOTTOM)

lblVMC=Label(FVMCTOP, font=('arial', 22, 'bold'), text="Veg Main Course")
lblVMC.grid(row=0,column=0)

#-----------------------------------------------------Veg Meal---------------------------------------------------------------------------------------------------#
varPanTikMas=StringVar()
varPanTikMas.set("0")
def chkPanTikMas():
        if(var26.get()==1):
                entPanTikMas.configure(state=NORMAL)
                varPanTikMas.set("")
        elif(var26.get()==0):
                entPanTikMas.configure(state=DISABLED)
                varPanTikMas.set("0")
CPanTikMas=Checkbutton(FVMCTOP, text='Panner Tikka Masala\t\tRs.120', variable=var26, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkPanTikMas).grid(row=1, column=0,sticky=W)
entPanTikMas=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varPanTikMas , width=6,justify='right', state=DISABLED)
entPanTikMas.grid(row=1,column=1)


varMutPan=StringVar()
varMutPan.set("0")
def chkMutPan():
        if(var27.get()==1):
                entMutPan.configure(state=NORMAL)
                varMutPan.set("")
        elif(var27.get()==0):
                entMutPan.configure(state=DISABLED)
                varMutPan.set("0")                
CMutPan=Checkbutton(FVMCTOP, text='Mutter Panner\t\t\tRs.120', variable=var27, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMutPan).grid(row=2, column=0,sticky=W)
entMutPan=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varMutPan , width=6,justify='right', state=DISABLED)
entMutPan.grid(row=2,column=1)


varShaPan=StringVar()
varShaPan.set("0")
def chkShaPan():
        if(var28.get()==1):
                entShaPan.configure(state=NORMAL)
                varShaPan.set("")
        elif(var28.get()==0):
                entShaPan.configure(state=DISABLED)
                varShaPan.set("0")                
CShaPan=Checkbutton(FVMCTOP, text='Shahi Paneer\t\t\tRs.125', variable=var28, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkShaPan).grid(row=3, column=0,sticky=W)
entShaPan=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varShaPan , width=6,justify='right', state=DISABLED)
entShaPan.grid(row=3,column=1)

varPalPan=StringVar()
varPalPan.set("0")
def chkPalPan():
        if(var29.get()==1):
                entPalPan.configure(state=NORMAL)
                varPalPan.set("")
        elif(var29.get()==0):
                entPalPan.configure(state=DISABLED)
                varPalPan.set("0")                
CMPalPan=Checkbutton(FVMCTOP, text='Palak Panner\t\t\tRs.140', variable=var29, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkPalPan).grid(row=4, column=0,sticky=W)
entPalPan=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varPalPan , width=6,justify='right', state=DISABLED)
entPalPan.grid(row=4,column=1)

varVegKof=StringVar()
varVegKof.set("0")
def chkVegKof():
        if(var30.get()==1):
                entVegKof.configure(state=NORMAL)
                varVegKof.set("")
        elif(var30.get()==0):
                entVegKof.configure(state=DISABLED)
                varVegKof.set("0")                
CVegKof=Checkbutton(FVMCTOP, text='Veg Kofta\t\t\tRs.130', variable=var30, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkVegKof).grid(row=5, column=0,sticky=W)
entVegKof=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varVegKof , width=6,justify='right', state=DISABLED)
entVegKof.grid(row=5,column=1)

varBhiMas=StringVar()
varBhiMas.set("0")
def chkBhiMas():
        if(var31.get()==1):
                entBhiMas.configure(state=NORMAL)
                varBhiMas.set("")
        elif(var31.get()==0):
                entBhiMas.configure(state=DISABLED)
                varBhiMas.set("0")                
CBhiMas=Checkbutton(FVMCTOP, text='Bhindi Masala\t\t\tRs.110', variable=var31, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkBhiMas).grid(row=6, column=0,sticky=W)
entBhiMas=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varBhiMas , width=6,justify='right', state=DISABLED)
entBhiMas.grid(row=6,column=1)

varDumAlo=StringVar()
varDumAlo.set("0")
def chkDumAlo():
        if(var32.get()==1):
                entDumAlo.configure(state=NORMAL)
                varDumAlo.set("")
        elif(var32.get()==0):
                entDumAlo.configure(state=DISABLED)
                varDumAlo.set("0")                
CDumAlo=Checkbutton(FVMCTOP, text='Dum Aloo\t\t\tRs.75', variable=var32, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDumAlo).grid(row=7, column=0,sticky=W)
entDumAlo=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varDumAlo , width=6,justify='right', state=DISABLED)
entDumAlo.grid(row=7,column=1)

varDalFry=StringVar()
varDalFry.set("0")
def chkDalFry():
        if(var33.get()==1):
                entDalFry.configure(state=NORMAL)
                varDalFry.set("")
        elif(var33.get()==0):
                entDalFry.configure(state=DISABLED)
                varDalFry.set("0")                
CDalFry=Checkbutton(FVMCTOP, text='Dal Fry\t\t\t\tRs.70', variable=var33, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDalFry).grid(row=8, column=0,sticky=W)
entDalFry=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varDalFry , width=6,justify='right', state=DISABLED)
entDalFry.grid(row=8,column=1)

varChaMas=StringVar()
varChaMas.set("0")
def chkChaMas():
        if(var34.get()==1):
                entChaMas.configure(state=NORMAL)
                varChaMas.set("")
        elif(var34.get()==0):
                entChaMas.configure(state=DISABLED)
                varChaMas.set("0")                
CChaMas=Checkbutton(FVMCTOP, text='Chana Masala\t\t\tRs.80', variable=var34, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChaMas).grid(row=9, column=0,sticky=W)
entChaMas=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varChaMas , width=6,justify='right', state=DISABLED)
entChaMas.grid(row=9,column=1)

varMalKof=StringVar()
varMalKof.set("0")
def chkMalKof():
        if(var35.get()==1):
                entMalKof.configure(state=NORMAL)
                varMalKof.set("")
        elif(var35.get()==0):
                entMalKof.configure(state=DISABLED)
                varMalKof.set("0")                
CMalKof=Checkbutton(FVMCTOP, text='Malai Kofta\t\t\tRs.100', variable=var35, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMalKof).grid(row=10, column=0,sticky=W)
entMalKof=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varMalKof , width=6,justify='right', state=DISABLED)
entMalKof.grid(row=10,column=1)

varFisCur=StringVar()
varFisCur.set("0")
def chkFisCur():
        if(var47.get()==1):
                entFisCur.configure(state=NORMAL)
                varFisCur.set("")
        elif(var47.get()==0):
                entFisCur.configure(state=DISABLED)
                varFisCur.set("0")                
CFisCur=Checkbutton(FVMCTOP, text='Panner Kofta\t\t\tRs.140', variable=var47, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkFisCur).grid(row=11, column=0,sticky=W)
entFisCur=Entry(FVMCTOP, font=('arial', 16, 'bold') ,textvariable=varFisCur , width=6,justify='right', state=DISABLED)
entFisCur.grid(row=11,column=1)


lblspaceVM=Label(FVMCTOP, text="\t\t\t\t\t\t\t\t\t\t\t")
lblspaceVM.grid(row=12,column=0)

def Bss():
	Me.withdraw()
	Pc.deiconify()

btnBS=Button(FVMCBOTTOM, text="Back to Starter Section ",font=('arail', 20, 'bold'), command=Bss)
btnBS.pack()


#--------------------------------------------------------------Non Veg Meal-------------------------------------------------------------------------------------#
lblNonVMC=Label(FNonVMCTOP, font=('arial', 22, 'bold'), text="Non Veg Main Course")
lblNonVMC.grid(row=0,column=0)

varCTM=StringVar()
varCTM.set("0")
def chkCTM():
        if(var36.get()==1):
                entCTM.configure(state=NORMAL)
                varCTM.set("")
        elif(var36.get()==0):
                entCTM.configure(state=DISABLED)
                varCTM.set("0")      
CCTM=Checkbutton(FNonVMCTOP, text='Chicken Tikka Masala\t\tRs.150', variable=var36, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCTM).grid(row=1, column=0,sticky=W)
entCTM=Entry(FNonVMCTOP, font=('arail', 16, 'bold') ,textvariable=varCTM , width=6,justify='right', state=DISABLED)
entCTM.grid(row=1,column=1)

varNonKof=StringVar()
varNonKof.set("0")
def chkNonKof():
        if(var37.get()==1):
                entNonKof.configure(state=NORMAL)
                varNonKof.set("")
        elif(var37.get()==0):
                entNonKof.configure(state=DISABLED)
                varNonKof.set("0")                
CNonKof=Checkbutton(FNonVMCTOP, text='Chicken Kofta Curry\t\tRs.160', variable=var37, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkNonKof).grid(row=2, column=0,sticky=W)
entNonKof=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varNonKof , width=6,justify='right', state=DISABLED)
entNonKof.grid(row=2,column=1)

varChiMM=StringVar()
varChiMM.set("0")
def chkChiMM():
        if(var38.get()==1):
                entChiMM.configure(state=NORMAL)
                varChiMM.set("")
        elif(var38.get()==0):
                entChiMM.configure(state=DISABLED)
                varChiMM.set("0")                
CChiMM=Checkbutton(FNonVMCTOP, text='Chicken Murgh Musallam\t\tRs.350', variable=var38, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChiMM).grid(row=3, column=0,sticky=W)
entChiMM=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varChiMM , width=6,justify='right', state=DISABLED)
entChiMM.grid(row=3,column=1)

varRoyC=StringVar()
varRoyC.set("0")
def chkRoyC():
        if(var39.get()==1):
                entRoyC.configure(state=NORMAL)
                varRoyC.set("")
        elif(var39.get()==0):
                entRoyC.configure(state=DISABLED)
                varRoyC.set("0")                
CRoyC=Checkbutton(FNonVMCTOP, text='Royal Chicken\t\t\tRs.250', variable=var39, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkRoyC).grid(row=4, column=0,sticky=W)
entRoyC=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varRoyC , width=6,justify='right', state=DISABLED)
entRoyC.grid(row=4,column=1)

varCAfg=StringVar()
varCAfg.set("0")
def chkCAfg():
        if(var40.get()==1):
                entCAfg.configure(state=NORMAL)
                varCAfg.set("")
        elif(var40.get()==0):
                entCAfg.configure(state=DISABLED)
                varCAfg.set("0")                
CCAfg=Checkbutton(FNonVMCTOP, text='Chicken Afghan\t\t\tRs.185', variable=var40, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCAfg).grid(row=5, column=0,sticky=W)
entCAfg=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varCAfg , width=6,justify='right', state=DISABLED)
entCAfg.grid(row=5,column=1)

varChiHan=StringVar()
varChiHan.set("0")
def chkChiHan():
        if(var41.get()==1):
                entChiHan.configure(state=NORMAL)
                varChiHan.set("")
        elif(var41.get()==0):
                entChiHan.configure(state=DISABLED)
                varChiHan.set("0")                
CChiHan=Checkbutton(FNonVMCTOP, text='Chicken Handi\t\t\tRs.190', variable=var41, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChiHan).grid(row=6, column=0,sticky=W)
entChiHan=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varChiHan , width=6,justify='right', state=DISABLED)
entChiHan.grid(row=6,column=1)

varChiHar=StringVar()
varChiHar.set("0")
def chkChiHar():
        if(var42.get()==1):
                entChiHar.configure(state=NORMAL)
                varChiHar.set("")
        elif(var42.get()==0):
                entChiHar.configure(state=DISABLED)
                varChiHar.set("0")                
CChiHar=Checkbutton(FNonVMCTOP, text='Chicken Hariyali\t\t\tRs.140', variable=var42, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChiHar).grid(row=7, column=0,sticky=W)
entChiHar=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varChiHar , width=6,justify='right', state=DISABLED)
entChiHar.grid(row=7,column=1)

varEggM=StringVar()
varEggM.set("0")
def chkEggM():
        if(var43.get()==1):
                entEggM.configure(state=NORMAL)
                varEggM.set("")
        elif(var43.get()==0):
                entEggM.configure(state=DISABLED)
                varEggM.set("0")                
CEggM=Checkbutton(FNonVMCTOP, text='Egg Masala\t\t\tRs.145', variable=var43, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkEggM).grid(row=8, column=0,sticky=W)
entEggM=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varEggM , width=6,justify='right', state=DISABLED)
entEggM.grid(row=8,column=1)

varMatChi=StringVar()
varMatChi.set("0")
def chkMatChi():
        if(var44.get()==1):
                entMatChi.configure(state=NORMAL)
                varMatChi.set("")
        elif(var44.get()==0):
                entMatChi.configure(state=DISABLED)
                varMatChi.set("0")                
CMatChi=Checkbutton(FNonVMCTOP, text='Matka Chicken\t\t\tRs.155', variable=var44, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMatChi).grid(row=9, column=0,sticky=W)
entMatChi=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varMatChi , width=6,justify='right', state=DISABLED)
entMatChi.grid(row=9,column=1)

varButChiT=StringVar()
varButChiT.set("0")
def chkButChiT():
        if(var45.get()==1):
                entButChiT.configure(state=NORMAL)
                varButChiT.set("")
        elif(var45.get()==0):
                entButChiT.configure(state=DISABLED)
                varButChiT.set("0")                
CButChiT=Checkbutton(FNonVMCTOP, text='Butter Chicken Tawa\t\tRs.135', variable=var45, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkButChiT).grid(row=10, column=0,sticky=W)
entButChiT=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varButChiT , width=6,justify='right', state=DISABLED)
entButChiT.grid(row=10,column=1)

varMutMak=StringVar()
varMutMak.set("0")
def chkMutMak():
        if(var46.get()==1):
                entMutMak.configure(state=NORMAL)
                varMutMak.set("")
        elif(var46.get()==0):
                entMutMak.configure(state=DISABLED)
                varMutMak.set("0")                
CMutMak=Checkbutton(FNonVMCTOP, text='Mutton Makhanwala\t\tRs.165', variable=var46, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMutMak).grid(row=11, column=0,sticky=W)
entMutMak=Entry(FNonVMCTOP, font=('arial', 16, 'bold') ,textvariable=varMutMak , width=6,justify='right', state=DISABLED)
entMutMak.grid(row=11,column=1)




def PanTikMas():
        if(var26.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Panner Tikka Masala'
                        value2=int(varPanTikMas.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MutPan():
        if(var27.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Mutter Panner'
                        value2=int(varMutPan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ShaPan():
        if(var28.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Shahi Panner'
                        value2=int(varShaPan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def PalPan():
        if(var29.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Palak Panner'
                        value2=int(varPalPan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def VegKof():
        if(var30.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Veg Kofta'
                        value2=int(varVegKof.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def BhiMas():
        if(var31.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Bhindi Masala'
                        value2=int(varBhiMas.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def DumAlo():
        if(var32.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Dum Aloo'
                        value2=int(varDumAlo.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def DalFry():
        if(var33.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Dal Fry'
                        value2=int(varDalFry.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChaMas():
        if(var34.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Channa Masala'
                        value2=int(varChaMas.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MalKof():
        if(var34.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Malai Kofta'
                        value2=int(varMalKof.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def FisCur():
        if(var47.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Paneer Kofta'
                        value2=int(varFisCur.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CTM():
        if(var36.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Tikka Masala'
                        value2=int(varCTM.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass


def NonKof():
        if(var37.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken KOFTA Curry'
                        value2=int(varNonKof.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChiMM():
        if(var38.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Murgh Musallam'
                        value2=int(varChiMM.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def RoyC():
        if(var39.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Royal Chicken'
                        value2=int(varRoyC.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CAfg():
        if(var40.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Afghan'
                        value2=int(varCAfg.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass


def SMChiHan():
        if(var41.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Handi'
                        value2=int(varChiHan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChiHar():
        if(var42.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chicken Hariyali'
                        value2=int(varChiHar.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass


def EggM():
        if(var43.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Egg Masala'
                        value2=int(varEggM.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MatChi():
        if(var44.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Matka Chicken'
                        value2=int(varMatChi.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ButChiT():
        if(var45.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Butter Chicken Tawa'
                        value2=int(varButChiT.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MutMak():
        if(var46.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Mutton Makhanwala'
                        value2=int(varMutMak.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass



lblspaceNonVM=Label(FNonVMCTOP, text="\t\t\t\t")
lblspaceNonVM.grid(row=13,column=1)


Ds= Toplevel(Me)
Ds.title("Tortilla & Dessert Section")
Ds.geometry("1366x768+0+0")
Ds.withdraw()
Ds.iconbitmap('food.ico')
def Ds1():
	Me.withdraw()
	Ds.deiconify()



btnPDs=Button(FNonVMCBOTTOM, text="Proceed towards Tortilla & Dessert Section", font=('arail', 20, 'bold'), command=lambda:[Ds1(),PanTikMas(),MutPan(),ShaPan(),PalPan(),VegKof(),BhiMas(),DumAlo(),DalFry(),ChaMas(),MalKof(),FisCur(),CTM(),NonKof(),ChiMM(),RoyC(),CAfg(),SMChiHan(),ChiHar(),EggM(),MatChi(),ButChiT(),MutMak()])
btnPDs.pack()

Naan=Frame(Ds, width=1350, height=100, bd=12, relief='raise')
Naan.pack(side=TOP)
lblTitle3=Label(Naan, font=('arail', 50, 'bold'), text="Tortilla & Dessert Section")
lblTitle3.grid(row=0, column=0)


bottomNaanframe=Frame(Ds, width=1350, height=650, bd=12, relief='raise')
bottomNaanframe.pack(side=BOTTOM)

FNaan=Frame(bottomNaanframe, width=450, height=650, bd=12, relief='raise')
FNaan.pack(side=LEFT)
FDesserts=Frame(bottomNaanframe, width=450, height=650, bd=12, relief='raise')
FDesserts.pack(side=LEFT)
FDrinks=Frame(bottomNaanframe, width=450, height=650, bd=12, relief='raise')
FDrinks.pack(side=LEFT)

FNaanTOP=Frame(FNaan, width=450, height=450, bd=12, relief='raise')
FNaanTOP.pack(side=TOP)
FNaanBOT=Frame(FNaan, width=450, height=200, bd=12, relief='raise')
FNaanBOT.pack(side=BOTTOM)
FDrinksTOP=Frame(FDrinks, width=450, height=450, bd=12, relief='raise')
FDrinksTOP.pack(side=TOP)
FDrinksBOT=Frame(FDrinks, width=450, height=200, bd=12, relief='raise')
FDrinksBOT.pack(side=BOTTOM)

#---------------------------------------------------------------------------------Naan-----------------------------------------------------------------------------#
lblNaan=Label(FNaanTOP, font=('arail', 22, 'bold'), text="Tortilla")
lblNaan.grid(row=0, column=0)

varRoti=StringVar()
varRoti.set("0")
def chkRoti():
        if(var48.get()==1):
                entRoti.configure(state=NORMAL)
                varRoti.set("")
        elif(var48.get()==0):
                entRoti.configure(state=DISABLED)
                varRoti.set("0")                
CRoti=Checkbutton(FNaanTOP, text='Roti\t\tRs.16',variable=var48, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkRoti).grid(row=1, column=0,sticky=W)
entRoti=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varRoti, width=6,justify='right', state=DISABLED)
entRoti.grid(row=1,column=1)

varNaann=StringVar()
varNaann.set("0")
def chkNaann():
        if(var49.get()==1):
                entNaann.configure(state=NORMAL)
                varNaann.set("")
        elif(var49.get()==0):
                entNaann.configure(state=DISABLED)
                varNaann.set("0")                
CNaann=Checkbutton(FNaanTOP, text='Naan\t\tRs.16', variable=var49, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkNaann).grid(row=2, column=0,sticky=W)
entNaann=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varNaann, width=6,justify='right', state=DISABLED)
entNaann.grid(row=2,column=1)

varBNaan=StringVar()
varBNaan.set("0")
def chkBNaan():
        if(var50.get()==1):
                entBNaan.configure(state=NORMAL)
                varBNaan.set("")
        elif(var50.get()==0):
                entBNaan.configure(state=DISABLED)
                varBNaan.set("0")                
CBNaan=Checkbutton(FNaanTOP, text='Butter Naan\tRs.20', variable=var50, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkBNaan).grid(row=3, column=0,sticky=W)
entBNaan=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varBNaan, width=6,justify='right', state=DISABLED)
entBNaan.grid(row=3,column=1)

varKulcha=StringVar()
varKulcha.set("0")
def chkKulcha():
        if(var51.get()==1):
                entKulcha.configure(state=NORMAL)
                varKulcha.set("")
        elif(var51.get()==0):
                entKulcha.configure(state=DISABLED)
                varKulcha.set("0")                
CKulcha=Checkbutton(FNaanTOP, text='Kulcha\t\tRs.23', variable=var51, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkKulcha).grid(row=4, column=0,sticky=W)
entKulcha=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varKulcha, width=6,justify='right', state=DISABLED)
entKulcha.grid(row=4,column=1)

varBKulcha=StringVar()
varBKulcha.set("0")
def chkBKulcha():
        if(var52.get()==1):
                entBKulcha.configure(state=NORMAL)
                varBKulcha.set("")
        elif(var52.get()==0):
                entBKulcha.configure(state=DISABLED)
                varBKulcha.set("0")                
CBKulcha=Checkbutton(FNaanTOP, text='Butter Kulcha\tRs.27', variable=var52, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkBKulcha).grid(row=5, column=0,sticky=W)
entBKulcha=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varBKulcha, width=6,justify='right', state=DISABLED)
entBKulcha.grid(row=5,column=1)

varParatha=StringVar()
varParatha.set("0")
def chkParatha():
        if(var53.get()==1):
                entParatha.configure(state=NORMAL)
                varParatha.set("")
        elif(var53.get()==0):
                entParatha.configure(state=DISABLED)
                varParatha.set("0")                
CParatha=Checkbutton(FNaanTOP, text='Paratha\t\tRs.20', variable=var53, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkParatha).grid(row=6, column=0,sticky=W)
entParatha=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varParatha, width=6,justify='right', state=DISABLED)
entParatha.grid(row=6,column=1)

varAlooPar=StringVar()
varAlooPar.set("0")
def chkAlooPar():
        if(var54.get()==1):
                entAlooPar.configure(state=NORMAL)
                varAlooPar.set("")
        elif(var54.get()==0):
                entAlooPar.configure(state=DISABLED)
                varAlooPar.set("0")                
CAlooPar=Checkbutton(FNaanTOP, text='Aloo Paratha\tRs.16', variable=var54, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkAlooPar).grid(row=7, column=0,sticky=W)
entAlooPar=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varAlooPar, width=6,justify='right', state=DISABLED)
entAlooPar.grid(row=7,column=1)

varStuffPar=StringVar()
varStuffPar.set("0")
def chkStuffPar():
        if(var55.get()==1):
                entStuffPar.configure(state=NORMAL)
                varStuffPar.set("")
        elif(var55.get()==0):
                entStuffPar.configure(state=DISABLED)
                varStuffPar.set("0")                
CStuffPar=Checkbutton(FNaanTOP, text='Stuffed Paratha\tRs.22', variable=var55, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkStuffPar).grid(row=8, column=0,sticky=W)
entStuffPar=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varStuffPar, width=6,justify='right', state=DISABLED)
entStuffPar.grid(row=8,column=1)

varPanPar=StringVar()
varPanPar.set("0")
def chkPanPar():
        if(var56.get()==1):
                entPanPar.configure(state=NORMAL)
                varPanPar.set("")
        elif(var56.get()==0):
                entPanPar.configure(state=DISABLED)
                varPanPar.set("0")                
CPanPar=Checkbutton(FNaanTOP, text='Paneer Paratha\tRs.29', variable=var56, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkPanPar).grid(row=9, column=0,sticky=W)
entPanPar=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varPanPar, width=6,justify='right', state=DISABLED)
entPanPar.grid(row=9,column=1)

varRotkiTok=StringVar()
varRotkiTok.set("0")
def chkRotkiTok():
        if(var57.get()==1):
                entRotkiTok.configure(state=NORMAL)
                varRotkiTok.set("")
        elif(var57.get()==0):
                entRotkiTok.configure(state=DISABLED)
                varRotkiTok.set("0")                
CRotkiTok=Checkbutton(FNaanTOP, text='Roti ki Tokri\tRs.36', variable=var57, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkRotkiTok).grid(row=10, column=0,sticky=W)
entRotkiTok=Entry(FNaanTOP, font=('arial', 16, 'bold') ,textvariable=varRotkiTok, width=6,justify='right', state=DISABLED)
entRotkiTok.grid(row=10,column=1)



lblspaceNaan=Label(FNaanTOP, text="\t")
lblspaceNaan.grid(row=11,column=1)

def Roti():
        if(var48.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Roti'
                        value2=int(varRoti.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Naann():
        if(var49.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Naan'
                        value2=int(varNaann.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass


def BNaan():
        if(var50.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Butter Naan'
                        value2=int(varBNaan.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Kulcha():
        if(var51.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Kulcha'
                        value2=int(varKulcha.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def BKulcha():
        if(var52.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Butter Kulcha'
                        value2=int(varBKulcha.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Paratha():
        if(var53.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Paratha'
                        value2=int(varParatha.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def AlooPar():
        if(var54.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Aloo Paratha'
                        value2=int(varAlooPar.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def StuffPar():
        if(var55.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Stuffed Paratha'
                        value2=int(varRotiStuffPar.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def PanPar():
        if(var56.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Paneer Paratha'
                        value2=int(varPanPar.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def RotkiTok():
        if(var57.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Roti ki Tokri'
                        value2=int(varRotkiTok.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass










#--------------------------------------------------------------------------Desserts------------------------------------------------------------------------------#

lblDesserts=Label(FDesserts, font=('arail', 22, 'bold'), text="Desserts")
lblDesserts.grid(row=0, column=0)

varChoco=StringVar()
varChoco.set("0")
def chkChoco():
        if(var58.get()==1):
                entChoco.configure(state=NORMAL)
                varChoco.set("")
        elif(var58.get()==0):
                entChoco.configure(state=DISABLED)
                varChoco.set("0")                
CChoco=Checkbutton(FDesserts, text='Choco Lava Cake\t\tRs.90', variable=var58, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChoco).grid(row=1, column=0,sticky=W)
entChoco=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varChoco, width=6,justify='right', state=DISABLED)
entChoco.grid(row=1,column=1)

varGulJam=StringVar()
varGulJam.set("0")
def chkGulJam():
        if(var59.get()==1):
                entGulJam.configure(state=NORMAL)
                varGulJam.set("")
        elif(var59.get()==0):
                entGulJam.configure(state=DISABLED)
                varGulJam.set("0")                
CGulJam=Checkbutton(FDesserts, text='Gulab Jamun\t\tRs.60', variable=var59, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkGulJam).grid(row=2, column=0,sticky=W)
entGulJam=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varGulJam, width=6,justify='right', state=DISABLED)
entGulJam.grid(row=2,column=1)

varShahTuk=StringVar()
varShahTuk.set("0")
def chkShahTuk():
        if(var60.get()==1):
                entShahTuk.configure(state=NORMAL)
                varShahTuk.set("")
        elif(var60.get()==0):
                entShahTuk.configure(state=DISABLED)
                varShahTuk.set("0")                
CShahTuk=Checkbutton(FDesserts, text= 'Shahi Tukda\t\tRs.130', variable=var60, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkShahTuk).grid(row=3, column=0,sticky=W)
entShahTuk=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varShahTuk, width=6,justify='right', state=DISABLED)
entShahTuk.grid(row=3,column=1)

varGajHal=StringVar()
varGajHal.set("0")
def chkGajHal():
        if(var61.get()==1):
                entGajHal.configure(state=NORMAL)
                varGajHal.set("")
        elif(var61.get()==0):
                entGajHal.configure(state=DISABLED)
                varGajHal.set("0")                
CGajHal=Checkbutton(FDesserts, text= 'Gajar Halwa\t\tRs.60', variable=var61, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkGajHal).grid(row=4, column=0,sticky=W)
entGajHal=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varGajHal, width=6,justify='right', state=DISABLED)
entGajHal.grid(row=4,column=1)

varChocFBro=StringVar()
varChocFBro.set("0")
def chkChocFBro():
        if(var62.get()==1):
                entChocFBro.configure(state=NORMAL)
                varChocFBro.set("")
        elif(var62.get()==0):
                entChocFBro.configure(state=DISABLED)
                varChocFBro.set("0")                
CChocFBro=Checkbutton(FDesserts, text= 'Chocolate Fudge Brownie\tRs.150', variable=var62, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChocFBro).grid(row=5, column=0,sticky=W)
entChocFBro=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varChocFBro, width=6,justify='right', state=DISABLED)
entChocFBro.grid(row=5,column=1)

varDChocMos=StringVar()
varDChocMos.set("0")
def chkDChocMos():
        if(var63.get()==1):
                entDChocMos.configure(state=NORMAL)
                varDChocMos.set("")
        elif(var63.get()==0):
                entDChocMos.configure(state=DISABLED)
                varDChocMos.set("0")                
CDChocMos=Checkbutton(FDesserts, text= 'Double Chocolate Mousse\tRs.120', variable=var63, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDChocMos).grid(row=6, column=0,sticky=W)
entDChocMos=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varDChocMos, width=6,justify='right', state=DISABLED)
entDChocMos.grid(row=6,column=1)

varCranCCak=StringVar()
varCranCCak.set("0")
def chkCranCCak():
        if(var64.get()==1):
                entCranCCak.configure(state=NORMAL)
                varCranCCak.set("")
        elif(var64.get()==0):
                entCranCCak.configure(state=DISABLED)
                varCranCCak.set("0")                
CCranCCak=Checkbutton(FDesserts, text= 'Cranberry Cheesecake\tRs.120', variable=var64, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkCranCCak).grid(row=7, column=0,sticky=W)
entCranCCak=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varCranCCak, width=6,justify='right', state=DISABLED)
entCranCCak.grid(row=7,column=1)

varVanIce=StringVar()
varVanIce.set("0")
def chkVanIce():
        if(var65.get()==1):
                entVanIce.configure(state=NORMAL)
                varVanIce.set("")
        elif(var65.get()==0):
                entVanIce.configure(state=DISABLED)
                varVanIce.set("0")                
CVanIce=Checkbutton(FDesserts, text= 'Vanilla Ice-cream\t\tRs.80', variable=var65, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkVanIce).grid(row=8, column=0,sticky=W)
entVanIce=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varVanIce, width=6,justify='right', state=DISABLED)
entVanIce.grid(row=8,column=1)

varStrawIce=StringVar()
varStrawIce.set("0")
def chkStrawIce():
        if(var66.get()==1):
                entStrawIce.configure(state=NORMAL)
                varStrawIce.set("")
        elif(var66.get()==0):
                entStrawIce.configure(state=DISABLED)
                varStrawIce.set("0")                
CStrawIce=Checkbutton(FDesserts, text= 'Strawberry Ice-cream\tRs.70', variable=var66, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkStrawIce).grid(row=9, column=0,sticky=W)
entStrawIce=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varStrawIce, width=6,justify='right', state=DISABLED)
entStrawIce.grid(row=9,column=1)

varChocIce=StringVar()
varChocIce.set("0")
def chkChocIce():
        if(var67.get()==1):
                entChocIce.configure(state=NORMAL)
                varChocIce.set("")
        elif(var67.get()==0):
                entChocIce.configure(state=DISABLED)
                varChocIce.set("0")                
CChocIce=Checkbutton(FDesserts, text= 'Chocolate Ice-cream\tRs.90', variable=var67, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkChocIce).grid(row=10, column=0,sticky=W)
entChocIce=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varChocIce, width=6,justify='right', state=DISABLED)
entChocIce.grid(row=10,column=1)

varSzBrIce=StringVar()
varSzBrIce.set("0")
def chkSzBrIce():
        if(var76.get()==1):
                entSzBrIce.configure(state=NORMAL)
                varSzBrIce.set("")
        elif(var76.get()==0):
                entSzBrIce.configure(state=DISABLED)
                varSzBrIce.set("0")                
CSzBrIce=Checkbutton(FDesserts, text= 'Sizzling Brownie\t\tRs.130', variable=var76, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkSzBrIce).grid(row=11, column=0,sticky=W)
entSzBrIce=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varSzBrIce, width=6,justify='right', state=DISABLED)
entSzBrIce.grid(row=11,column=1)

varDont=StringVar()
varDont.set("0")
def chkDont():
        if(var77.get()==1):
                entDont.configure(state=NORMAL)
                varDont.set("")
        elif(var77.get()==0):
                entDont.configure(state=DISABLED)
                varDont.set("0")                
CDont=Checkbutton(FDesserts, text= 'Donuts\t\t\tRs.90', variable=var77, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkDont).grid(row=12, column=0,sticky=W)
entDont=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varDont, width=6,justify='right', state=DISABLED)
entDont.grid(row=12,column=1)

varKlf=StringVar()
varKlf.set("0")
def chkKlf():
        if(var80.get()==1):
                entKlf.configure(state=NORMAL)
                varKlf.set("")
        elif(var80.get()==0):
                entKlf.configure(state=DISABLED)
                varKlf.set("0")                
CKlf=Checkbutton(FDesserts, text= 'Assorted Kulfi\t\tRs.60', variable=var80, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkKlf).grid(row=13, column=0,sticky=W)
entKlf=Entry(FDesserts, font=('arial', 16, 'bold') ,textvariable=varKlf, width=6,justify='right', state=DISABLED)
entKlf.grid(row=13,column=1)

lblspaceDessert=Label(FDesserts, text="\t\t")
lblspaceDessert.grid(row=14,column=1)

def Choco():
        if(var58.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Choco Lava Cake'
                        value2=int(varChoco.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def GulJam():
        if(var59.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Gulab Jamun'
                        value2=int(varGulJam.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ShahTuk():
        if(var60.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Shahi Tukda'
                        value2=int(varShahTuk.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def GajHal():
        if(var61.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Gajar Halwa'
                        value2=int(varGajHal.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChocFBro():
        if(var62.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chocolate Fudge Brownie'
                        value2=int(varChocFBro.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def DChocMos():
        if(var63.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Double Chocolate Mousse'
                        value2=int(varDChocMos.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def CranCCak():
        if(var64.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Cranberry Cheesecake'
                        value2=int(varCranCCak.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def VanIce():
        if(var65.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Vanilla Ice-Cream'
                        value2=int(varVanIce.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def StrawIce():
        if(var66.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Strawberry Ice-Cream'
                        value2=int(varStrawIce.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ChocIce():
        if(var67.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Chocolate Ice-Cream'
                        value2=int(varVanIce.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass


def SzBrIce():
        if(var76.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Sizzling Brownie with Ice-Cream'
                        value2=int(varSzBrIce.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass
        
def Dont():
        if(var77.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Donuts'
                        value2=int(varDont.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def Klf():
        if(var80.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Assorted Kulfi'
                        value2=int(varKlf.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass








#-----------------------------------------------------------------------Drinks----------------------------------------------------------------------------------#

lblDrinks=Label(FDrinksTOP, font=('arail', 22, 'bold'), text="Drinks")
lblDrinks.grid(row=0, column=0)

varPep=StringVar()
varPep.set("0")
def chkPep():
        if(var68.get()==1):
                entPep.configure(state=NORMAL)
                varPep.set("")
        elif(var68.get()==0):
                entPep.configure(state=DISABLED)
                varPep.set("0")                
CPep=Checkbutton(FDrinksTOP, text='Soft-Drinks\tRs.40', variable=var68, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkPep).grid(row=1, column=0,sticky=W)
entPep=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varPep, width=6,justify='right', state=DISABLED)
entPep.grid(row=1,column=1)

varMasSod=StringVar()
varMasSod.set("0")
def chkMasSod():
        if(var69.get()==1):
                entMasSod.configure(state=NORMAL)
                varMasSod.set("")
        elif(var69.get()==0):
                entMasSod.configure(state=DISABLED)
                varMasSod.set("0")                
CMasSod=Checkbutton(FDrinksTOP, text='Masala Soda\tRs.25', variable=var69, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMasSod).grid(row=2, column=0,sticky=W)
entMasSod=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varMasSod, width=6,justify='right', state=DISABLED)
entMasSod.grid(row=2,column=1)

varMasChs=StringVar()
varMasChs.set("0")
def chkMasChs():
        if(var70.get()==1):
                entMasChs.configure(state=NORMAL)
                varMasChs.set("")
        elif(var70.get()==0):
                entMasChs.configure(state=DISABLED)
                varMasChs.set("0")                
CMasChs=Checkbutton(FDrinksTOP, text='Masala Chaas\tRs.40', variable=var70, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkMasChs).grid(row=3, column=0,sticky=W)
entMasChs=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varMasChs, width=6,justify='right', state=DISABLED)
entMasChs.grid(row=3,column=1)

varSwtLas=StringVar()
varSwtLas.set("0")
def chkSwtLas():
        if(var71.get()==1):
                entSwtLas.configure(state=NORMAL)
                varSwtLas.set("")
        elif(var71.get()==0):
                entSwtLas.configure(state=DISABLED)
                varSwtLas.set("0")                
CSwtLas=Checkbutton(FDrinksTOP, text='Sweet Lassi\tRs.50', variable=var71, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkSwtLas).grid(row=4, column=0,sticky=W)
entSwtLas=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varSwtLas, width=6,justify='right', state=DISABLED)
entSwtLas.grid(row=4,column=1)

varIceTea=StringVar()
varIceTea.set("0")
def chkIceTea():
        if(var72.get()==1):
                entIceTea.configure(state=NORMAL)
                varIceTea.set("")
        elif(var72.get()==0):
                entIceTea.configure(state=DISABLED)
                varIceTea.set("0")                
CIceTea=Checkbutton(FDrinksTOP, text='Ice Tea\t\tRs.60', variable=var72, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkIceTea).grid(row=5, column=0,sticky=W)
entIceTea=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varIceTea, width=6,justify='right', state=DISABLED)
entIceTea.grid(row=5,column=1)

varManShk=StringVar()
varManShk.set("0")
def chkManShk():
        if(var73.get()==1):
                entManShk.configure(state=NORMAL)
                varManShk.set("")
        elif(var73.get()==0):
                entManShk.configure(state=DISABLED)
                varManShk.set("0")                
CManShk=Checkbutton(FDrinksTOP, text='Mango Milkshake\tRs.90', variable=var73, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkManShk).grid(row=6, column=0,sticky=W)
entManShk=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varManShk, width=6,justify='right', state=DISABLED)
entManShk.grid(row=6,column=1)

varOroShk=StringVar()
varOroShk.set("0")
def chkOroShk():
        if(var74.get()==1):
                entOroShk.configure(state=NORMAL)
                varOroShk.set("")
        elif(var74.get()==0):
                entOroShk.configure(state=DISABLED)
                varOroShk.set("0")                
COroShk=Checkbutton(FDrinksTOP, text='Oreo Milkshake\tRs.80', variable=var74, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkOroShk).grid(row=7, column=0,sticky=W)
entOroShk=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varOroShk, width=6,justify='right', state=DISABLED)
entOroShk.grid(row=7,column=1)

varVirMoj=StringVar()
varVirMoj.set("0")
def chkVirMoj():
        if(var75.get()==1):
                entVirMoj.configure(state=NORMAL)
                varVirMoj.set("")
        elif(var75.get()==0):
                entVirMoj.configure(state=DISABLED)
                varVirMoj.set("0")                
CVirMoj=Checkbutton(FDrinksTOP, text='Virjin Mojito\tRs.90', variable=var75, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkVirMoj).grid(row=8, column=0,sticky=W)
entVirMoj=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varVirMoj, width=6,justify='right', state=DISABLED)
entVirMoj.grid(row=8,column=1)

varWatBlst=StringVar()
varWatBlst.set("0")
def chkWatBlst():
        if(var78.get()==1):
                entWatBlst.configure(state=NORMAL)
                varWatBlst.set("")
        elif(var78.get()==0):
                entWatBlst.configure(state=DISABLED)
                varWatBlst.set("0")                
CWatBlst=Checkbutton(FDrinksTOP, text='Watermelon Blast\tRs.70', variable=var78, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkWatBlst).grid(row=9, column=0,sticky=W)
entWatBlst=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varWatBlst, width=6,justify='right', state=DISABLED)
entWatBlst.grid(row=9,column=1)

varFrsMnt=StringVar()
varFrsMnt.set("0")
def chkFrsMnt():
        if(var79.get()==1):
                entFrsMnt.configure(state=NORMAL)
                varFrsMnt.set("")
        elif(var79.get()==0):
                entFrsMnt.configure(state=DISABLED)
                varFrsMnt.set("0")                
CFrsMnt=Checkbutton(FDrinksTOP, text='Fresh Mint\tRs.50', variable=var79, onvalue=1, offvalue=0,font=('arail', 16, 'bold'),command=chkFrsMnt).grid(row=10, column=0,sticky=W)
entFrsMnt=Entry(FDrinksTOP, font=('arial', 16, 'bold') ,textvariable=varFrsMnt, width=6,justify='right', state=DISABLED)
entFrsMnt.grid(row=10,column=1)

lblspaceDrinks=Label(FDrinksTOP, text="\t\t")
lblspaceDrinks.grid(row=11,column=1)

def Pep():
        if(var68.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Soft-Drinks'
                        value2=int(varPep.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MasSod():
        if(var69.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Masala Soda'
                        value2=int(varMasSod.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def MasChs():
        if(var70.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Masala Chaas'
                        value2=int(varMasChs.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def SwtLas():
        if(var71.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Sweet Lassi'
                        value2=int(varSwtLas.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def IceTea():
        if(var72.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Ice Tea'
                        value2=int(varIceTea.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def ManShk():
        if(var73.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Mango Milkshake'
                        value2=int(varManShk.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def OroShk():
        if(var74.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Oreo Milkshake'
                        value2=int(varOroShk.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def VirMoj():
        if(var75.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Virjin Mojito'
                        value2=int(varVirMoj.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def WatBlst():
        if(var78.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Watermelon Blast'
                        value2=int(varWatBlst.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass

def FrsMnt():
        if(var79.get()==1):
       
                con=None
                cursor=None
                try:
                        con=mysql.connector.connect(
                                host="localhost",
                                user="root",
                                passwd="root",
                                database="hotel")
                        value1='Fresh Mint'
                        value2=int(varFrsMnt.get())
                        cursor=con.cursor()
                        cursor.execute('use hotel')

                        sql="insert into Items values('%s','%d')"
                        args=(value1, value2)
                        cursor.execute(sql%args)
                        con.commit()

                except mysql.connector.DatabaseError as e:
                        con.rollback()
                        messagebox.showerror("Issue ", e)
                finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close()
        else:
                pass




def Bmc():
	Ds.withdraw()
	Me.deiconify()

btnNaan=Button(FNaanBOT,text="Back to Main Course",font=('arail', 20, 'bold'), command=Bmc)
btnNaan.pack()

def cost():
        S1=float(varPannTk.get())
        S2=float(varMancSoup.get())
        S3=float(varVegKofta.get())
        S4=float(varCutlet.get())
        S5=float(varManc.get())
        S6=float(varIdli.get())
        S7=float(varDosa.get())
        S8=float(varChilliPan.get())
        S9=float(varRajmaK.get())
        S10=float(varCheeseR.get())
        S11=float(varAloo.get())
        S12=float(varMirchi.get())
        S13=float(varDahi.get())
        S14=float(varMedu.get())
        S15=float(varCMomos.get())
        S16=float(varCLolli.get())
        S17=float(varChilli.get())
        S18=float(varCrispy.get())
        S19=float(varGarlic.get())
        S20=float(vaManrCcS.get())
        S21=float(varCAchari.get())
        S22=float(varCB.get())
        S23=float(varCCB.get())
        S24=float(varCT.get())
        S25=float(varSM.get())
        S26=float(varPanTikMas.get())
        S27=float(varMutPan.get())
        S28=float(varShaPan.get())
        S29=float(varShaPan.get())
        S30=float(varVegKof.get())
        S31=float(varBhiMas.get())
        S32=float(varDumAlo.get())
        S33=float(varDalFry.get())
        S34=float(varChaMas.get())
        S35=float(varMalKof.get())
        S47=float(varFisCur.get())
        S36=float(varCTM.get())
        S37=float(varNonKof.get())
        S38=float(varChiMM.get())
        S39=float(varRoyC.get())
        S40=float(varCAfg.get())
        S41=float(varChiHan.get())
        S42=float(varChiHar.get())
        S43=float(varEggM.get())
        S44=float(varMatChi.get())
        S45=float(varButChiT.get())
        S46=float(varMutMak.get())
        S48=float(varRoti.get())
        S49=float(varNaann.get())
        S50=float(varBNaan.get())
        S51=float(varKulcha.get())
        S52=float(varBKulcha.get())
        S53=float(varParatha.get())
        S54=float(varAlooPar.get())
        S55=float(varStuffPar.get())
        S56=float(varPanPar.get())
        S57=float(varRotkiTok.get())
        S58=float(varChoco.get())
        S59=float(varGulJam.get())
        S60=float(varShahTuk.get())
        S61=float(varGajHal.get())
        S62=float(varChocFBro.get())
        S63=float(varDChocMos.get())
        S64=float(varCranCCak.get())
        S65=float(varVanIce.get())
        S66=float(varStrawIce.get())
        S67=float(varChocIce.get())
        S76=float(varSzBrIce.get())
        S77=float(varDont.get())
        S80=float(varKlf.get())
        S68=float(varPep.get())
        S69=float(varMasSod.get())
        S70=float(varMasChs.get())
        S71=float(varSwtLas.get())
        S72=float(varIceTea.get())
        S73=float(varManShk.get())
        S74=float(varOroShk.get())
        S75=float(varVirMoj.get())
        S78=float(varWatBlst.get())
        S79=float(varFrsMnt.get())




        i=(S1 * 70) + (S2 * 50) + (S3 * 80) + (S4 * 75) + (S5 * 65) + (S6 * 40) + (S7 * 45) + (S8 * 72) + (S9 * 80) + (S10 * 46) + (S11 * 48) + (S12 * 35) + (S13 * 38) + (S14 * 35) + (S15 * 90) + (S16 * 130) + (S17 * 100) + (S18 * 120) + (S19 * 123) + (S20 * 80) + (S21 * 100) + (S22 * 90) + (S23 * 88) + (S24 * 140) + (S25 * 95) + (S26 * 120) + (S27 * 120) + (S28 * 125) + (S29 * 140) + (S30 * 130) + (S31 * 110) + (S32 * 75) + (S33 * 70) + (S34 * 80) + (S35 * 100) + (S47 * 140) + (S36 * 150) + (S37 * 160) + (S38 * 350) + (S39 * 250) + (S40 * 185) + (S41 * 190) + (S42 * 140) + (S43 * 145) + (S44 * 155) + (S45 * 135) + (S46 * 165) + (S48 * 16) +(S49 * 16) + (S50 * 20) + (S51 * 23) + (S52 * 27) + (S53 * 20) + (S54 * 16) + (S55 * 22) + (S56 * 29) + (S57 * 36) + (S58 * 90) + (S59 * 60) + (S60 * 130) + (S61 * 60) + (S62 * 150) + (S63 * 120) + (S64 * 120) + (S65 * 80) + (S66 * 70) + (S67 * 90) + (S76 * 130) + (S77 * 90) + (S80 * 60) + (S68 * 40) + (S69 * 25) + (S70 * 40) + (S71 + 50) + (S72 * 60) + (S73 * 90) + (S74 * 80) + (S75 * 90) + (S78 * 70) + (S79 * 50)
        varTotal.set(i)
        varTotal=IntVar()
        tax=(i * 0.5)

finalize1= Toplevel(Ds)
finalize1.title("Finalize")
finalize1.geometry("1366x768+0+0")
finalize1.withdraw()
finalize1.iconbitmap('food.ico')



def finalize():
        Ds.withdraw()
        finalize1.deiconify()

lblFinal=Label(finalize1, font=('arail', 45, 'bold'), text="\t\tReceipt\t\t\t")
lblFinal.pack()


                
txtrpt=Text(finalize1, width=60, height=30,wrap=WORD,padx=10,pady=10,bd=5)
txtrpt.pack()

def receipt():

        S1=float(varPannTk.get())
        S2=float(varMancSoup.get())
        S3=float(varVegKofta.get())
        S4=float(varCutlet.get())
        S5=float(varManc.get())
        S6=float(varIdli.get())
        S7=float(varDosa.get())
        S8=float(varChilliPan.get())
        S9=float(varRajmaK.get())
        S10=float(varCheeseR.get())
        S11=float(varAloo.get())
        S12=float(varMirchi.get())
        S13=float(varDahi.get())
        S14=float(varMedu.get())
        S15=float(varCMomos.get())
        S16=float(varCLolli.get())
        S17=float(varChilli.get())
        S18=float(varCrispy.get())
        S19=float(varGarlic.get())
        S20=float(varCMancS.get())
        S21=float(varCAchari.get())
        S22=float(varCB.get())
        S23=float(varCCB.get())
        S24=float(varCT.get())
        S25=float(varSM.get())
        S26=float(varPanTikMas.get())
        S27=float(varMutPan.get())
        S28=float(varShaPan.get())
        S29=float(varShaPan.get())
        S30=float(varVegKof.get())
        S31=float(varBhiMas.get())
        S32=float(varDumAlo.get())
        S33=float(varDalFry.get())
        S34=float(varChaMas.get())
        S35=float(varMalKof.get())
        S47=float(varFisCur.get())
        S36=float(varCTM.get())
        S37=float(varNonKof.get())
        S38=float(varChiMM.get())
        S39=float(varRoyC.get())
        S40=float(varCAfg.get())
        S41=float(varChiHan.get())
        S42=float(varChiHar.get())
        S43=float(varEggM.get())
        S44=float(varMatChi.get())
        S45=float(varButChiT.get())
        S46=float(varMutMak.get())
        S48=float(varRoti.get())
        S49=float(varNaann.get())
        S50=float(varBNaan.get())
        S51=float(varKulcha.get())
        S52=float(varBKulcha.get())
        S53=float(varParatha.get())
        S54=float(varAlooPar.get())
        S55=float(varStuffPar.get())
        S56=float(varPanPar.get())
        S57=float(varRotkiTok.get())
        S58=float(varChoco.get())
        S59=float(varGulJam.get())
        S60=float(varShahTuk.get())
        S61=float(varGajHal.get())
        S62=float(varChocFBro.get())
        S63=float(varDChocMos.get())
        S64=float(varCranCCak.get())
        S65=float(varVanIce.get())
        S66=float(varStrawIce.get())
        S67=float(varChocIce.get())
        S76=float(varSzBrIce.get())
        S77=float(varDont.get())
        S80=float(varKlf.get())
        S68=float(varPep.get())
        S69=float(varMasSod.get())
        S70=float(varMasChs.get())
        S71=float(varSwtLas.get())
        S72=float(varIceTea.get())
        S73=float(varManShk.get())
        S74=float(varOroShk.get())
        S75=float(varVirMoj.get())
        S78=float(varWatBlst.get())
        S79=float(varFrsMnt.get())




        i=(S1 * 70) + (S2 * 50) + (S3 * 80) + (S4 * 75) + (S5 * 65) + (S6 * 40) + (S7 * 45) + (S8 * 72) + (S9 * 80) + (S10 * 46) + (S11 * 48) + (S12 * 35) + (S13 * 38) + (S14 * 35) + (S15 * 90) + (S16 * 130) + (S17 * 100) + (S18 * 120) + (S19 * 123) + (S20 * 80) + (S21 * 100) + (S22 * 90) + (S23 * 88) + (S24 * 140) + (S25 * 95) + (S26 * 120) + (S27 * 120) + (S28 * 125) + (S29 * 140) + (S30 * 130) + (S31 * 110) + (S32 * 75) + (S33 * 70) + (S34 * 80) + (S35 * 100) + (S47 * 140) + (S36 * 150) + (S37 * 160) + (S38 * 350) + (S39 * 250) + (S40 * 185) + (S41 * 190) + (S42 * 140) + (S43 * 145) + (S44 * 155) + (S45 * 135) + (S46 * 165) + (S48 * 16) +(S49 * 16) + (S50 * 20) + (S51 * 23) + (S52 * 27) + (S53 * 20) + (S54 * 16) + (S55 * 22) + (S56 * 29) + (S57 * 36) + (S58 * 90) + (S59 * 60) + (S60 * 130) + (S61 * 60) + (S62 * 150) + (S63 * 120) + (S64 * 120) + (S65 * 80) + (S66 * 70) + (S67 * 90) + (S76 * 130) + (S77 * 90) + (S80 * 60) + (S68 * 40) + (S69 * 25) + (S70 * 40) + (S71 + 50) + (S72 * 60) + (S73 * 90) + (S74 * 80) + (S75 * 90) + (S78 * 70) + (S79 * 50)
        tax=(i * 1.005)

        txtrpt.insert(END, 'Items\t\t\t\t\t'+ "Cost of Items\n\n")
        if(int(varPannTk.get())>0):
                txtrpt.insert(END, 'Paneer Tikka: \t\t\t\t\t'+ varPannTk.get()+ "\n")
        if(int(varMancSoup.get())>0):        
                txtrpt.insert(END, 'Manchurian Soup: \t\t\t\t\t'+ varMancSoup.get()+ "\n")
        if(int(varVegKofta.get())>0):
                txtrpt.insert(END, 'Veg Kofta: \t\t\t\t\t'+ varVegKofta.get()+ "\n")
        if(int(varCutlet.get())>0):
                txtrpt.insert(END, 'Cutlet: \t\t\t\t\t'+ varCutlet.get()+ "\n")
        if(int(varManc.get())>0):
                txtrpt.insert(END, 'Veg Manchurian: \t\t\t\t\t'+ varManc.get()+ "\n")
        if(int(varIdli.get())>0):
                txtrpt.insert(END, 'Idli: \t\t\t\t\t'+ varIdli.get()+ "\n")
        if(int(varDosa.get())>0):
                txtrpt.insert(END, 'Dosa: \t\t\t\t\t'+ varDosa.get()+ "\n")
        if(int(varChilliPan.get())>0):
                txtrpt.insert(END, 'Chilli Panner Dry: \t\t\t\t\t'+ varChilliPan.get()+ "\n")
        if(int(varRajmaK.get())>0):
                txtrpt.insert(END, 'Rajma Kebab: \t\t\t\t\t'+ varRajmaK.get()+ "\n")
        if(int(varCheeseR.get())>0):
                txtrpt.insert(END, 'Cheese Roll: \t\t\t\t\t'+ varCheeseR.get()+ "\n")
        if(int(varAloo.get())>0):
                txtrpt.insert(END, 'Aloo Pakoda: \t\t\t\t\t'+ varAloo.get()+ "\n")
        if(int(varMirchi.get())>0):
                txtrpt.insert(END, 'Mirchi Bajji: \t\t\t\t\t'+ varMirchi.get()+ "\n")
        if(int(varDahi.get())>0):
                txtrpt.insert(END, 'Dahi Vada: \t\t\t\t\t'+ varDahi.get()+ "\n")
        if(int(varMedu.get())>0):
                txtrpt.insert(END, 'Medu Vada: \t\t\t\t\t'+ varMedu.get()+ "\n")
        if(int(varCMomos.get())>0):
                txtrpt.insert(END, 'Chicken Momos: \t\t\t\t\t'+ varCMomos.get()+ "\n")
        if(int(varCLolli.get())>0):
                txtrpt.insert(END, 'Chicken Lollipop: \t\t\t\t\t'+ varCLolli.get()+ "\n")
        if(int(varChilli.get())>0):
                txtrpt.insert(END, 'Chicken Chilly: \t\t\t\t\t'+ varChilli.get()+ "\n")
        if(int(varCrispy.get())>0):
                txtrpt.insert(END, 'Chicken Crispy: \t\t\t\t\t'+ varCrispy.get()+ "\n")
        if(int(varGarlic.get())>0):
                txtrpt.insert(END, 'Chicken Garlic: \t\t\t\t\t'+ varGarlic.get()+ "\n")
        if(int(varCMancS.get())>0):
                txtrpt.insert(END, 'Chicken Manchurian Soup: \t\t\t\t\t'+ varCMancS.get()+ "\n")
        if(int(varCAchari.get())>0):
                txtrpt.insert(END, 'Chicken Achari Dry: \t\t\t\t\t'+ varCAchari.get()+ "\n")
        if(int(varCB.get())>0):
                txtrpt.insert(END, 'Chicken Balls: \t\t\t\t\t'+ varCB.get()+ "\n")
        if(int(varCCB.get())>0):
                txtrpt.insert(END, 'Chicken Cheese Balls: \t\t\t\t\t'+ varCCB.get()+ "\n")
        if(int(varCT.get())>0):
                txtrpt.insert(END, 'Chicken Tandori: \t\t\t\t\t'+ varCT.get()+ "\n")
        if(int(varSM.get())>0):
                txtrpt.insert(END, 'Chicken Simply: \t\t\t\t\t'+ varSM.get()+ "\n")
        if(int(varPanTikMas.get())>0):
                txtrpt.insert(END, 'Panner Tikka Masala: \t\t\t\t\t'+ varPanTikMas.get()+ "\n")
        if(int(varMutPan.get())>0):
                txtrpt.insert(END, 'Mutter Panner: \t\t\t\t\t'+ varMutPan.get()+ "\n")
        if(int(varShaPan.get())>0):
                txtrpt.insert(END, 'Shahi Paneer: \t\t\t\t\t'+ varShaPan.get()+ "\n")
        if(int(varPalPan.get())>0):
                txtrpt.insert(END, 'Palak Panner: \t\t\t\t\t'+ varPalPan.get()+ "\n")
        if(int(varVegKof.get())>0):
                txtrpt.insert(END, 'Veg Kofta: \t\t\t\t\t'+ varVegKof.get()+ "\n")
        if(int(varBhiMas.get())>0):
                txtrpt.insert(END, 'Bhindi Masala: \t\t\t\t\t'+ varBhiMas.get()+ "\n")
        if(int(varDumAlo.get())>0):
                txtrpt.insert(END, 'Dum Aloo: \t\t\t\t\t'+ varDumAlo.get()+ "\n")
        if(int(varDalFry.get())>0):
                txtrpt.insert(END, 'Dal Fry: \t\t\t\t\t'+ varDalFry.get()+ "\n")
        if(int(varChaMas.get())>0):
                txtrpt.insert(END, 'Chana Masala: \t\t\t\t\t'+ varChaMas.get()+ "\n")
        if(int(varMalKof.get())>0):
                txtrpt.insert(END, 'Malai Kofta: \t\t\t\t\t'+ varMalKof.get()+ "\n")
        if(int(varFisCur.get())>0):
                txtrpt.insert(END, 'Panner Kofta: \t\t\t\t\t'+ varFisCur.get()+ "\n")
        if(int(varCTM.get())>0):
                txtrpt.insert(END, 'Chicken Tikka Masala: \t\t\t\t\t'+ varCTM.get()+ "\n")
        if(int(varNonKof.get())>0):
                txtrpt.insert(END, 'Chicken Kofta Curry: \t\t\t\t\t'+ varNonKof.get()+ "\n")
        if(int(varChiMM.get())>0):
                txtrpt.insert(END, 'Chicken Murgh Musallam: \t\t\t\t\t'+ varChiMM.get()+ "\n")
        if(int(varRoyC.get())>0):
                txtrpt.insert(END, 'Royal Chicken: \t\t\t\t\t'+ varRoyC.get()+ "\n")
        if(int(varCAfg.get())>0):
                txtrpt.insert(END, 'Chicken Afghan: \t\t\t\t\t'+ varCAfg.get()+ "\n")
        if(int(varChiHan.get())>0):
                txtrpt.insert(END, 'Chicken Handi: \t\t\t\t\t'+ varChiHan.get()+ "\n")
        if(int(varChiHar.get())>0):
                txtrpt.insert(END, 'Chicken Hariyali: \t\t\t\t\t'+ varChiHar.get()+ "\n")
        if(int(varEggM.get())>0):
                txtrpt.insert(END, 'Egg Masala: \t\t\t\t\t'+ varEggM.get()+ "\n")
        if(int(varMatChi.get())>0):
                txtrpt.insert(END, 'Matka Chicken: \t\t\t\t\t'+ varMatChi.get()+ "\n")
        if(int(varButChiT.get())>0):
                txtrpt.insert(END, 'Butter Chicken Tawa: \t\t\t\t\t'+ varButChiT.get()+ "\n")
        if(int(varMutMak.get())>0):
                txtrpt.insert(END, 'Mutton Makhanwala: \t\t\t\t\t'+ varMutMak.get()+ "\n")
        if(int(varRoti.get())>0):
                txtrpt.insert(END, 'Roti: \t\t\t\t\t'+ varRoti.get()+ "\n")
        if(int(varNaann.get())>0):
                txtrpt.insert(END, 'Naan: \t\t\t\t\t'+ varNaann.get()+ "\n")
        if(int(varBNaan.get())>0):
                txtrpt.insert(END, 'Butter Naan: \t\t\t\t\t'+ varBNaan.get()+ "\n")
        if(int(varKulcha.get())>0):
                txtrpt.insert(END, 'Kulcha: \t\t\t\t\t'+ varKulcha.get()+ "\n")
        if(int(varBKulcha.get())>0):
                txtrpt.insert(END, 'Butter Kulcha: \t\t\t\t\t'+ varBKulcha.get()+ "\n")
        if(int(varParatha.get())>0):
                txtrpt.insert(END, 'Paratha: \t\t\t\t\t'+ varParatha.get()+ "\n")
        if(int(varAlooPar.get())>0):
                txtrpt.insert(END, 'Aloo Paratha: \t\t\t\t\t'+ varAlooPar.get()+ "\n")
        if(int(varStuffPar.get())>0):
                txtrpt.insert(END, 'Stuffed Paratha: \t\t\t\t\t'+ varStuffPar.get()+ "\n")
        if(int(varPanPar.get())>0):
                txtrpt.insert(END, 'Paneer Paratha: \t\t\t\t\t'+ varPanPar.get()+ "\n")
        if(int(varRotkiTok.get())>0):
                txtrpt.insert(END, 'Roti ki Tokri: \t\t\t\t\t'+ varRotkiTok.get()+ "\n")
        if(int(varChoco.get())>0):
                txtrpt.insert(END, 'Choco Lava Cake: \t\t\t\t\t'+ varChoco.get()+ "\n")
        if(int(varGulJam.get())>0):
                txtrpt.insert(END, 'Gulab Jamun: \t\t\t\t\t'+ varGulJam.get()+ "\n")
        if(int(varShahTuk.get())>0):
                txtrpt.insert(END, 'Shahi Tukda: \t\t\t\t\t'+ varShahTuk.get()+ "\n")
        if(int(varGajHal.get())>0):
                txtrpt.insert(END, 'Gajar Halwa: \t\t\t\t\t'+ varGajHal.get()+ "\n")
        if(int(varChocFBro.get())>0):
                txtrpt.insert(END, 'Chocolate Fudge Brownie: \t\t\t\t\t'+ varChocFBro.get()+ "\n")
        if(int(varDChocMos.get())>0):
                txtrpt.insert(END, 'Double Chocolate Mousse: \t\t\t\t\t'+ varDChocMos.get()+ "\n")
        if(int(varCranCCak.get())>0):
                txtrpt.insert(END, 'Cranberry Cheesecake: \t\t\t\t\t'+ varCranCCak.get()+ "\n")
        if(int(varVanIce.get())>0):
                txtrpt.insert(END, 'Vanilla Ice-cream: \t\t\t\t\t'+ varVanIce.get()+ "\n")
        if(int(varStrawIce.get())>0):
                txtrpt.insert(END, 'Strawberry Ice-cream: \t\t\t\t\t'+ varStrawIce.get()+ "\n")
        if(int(varChocIce.get())>0):
                txtrpt.insert(END, 'Chocolate Ice-cream: \t\t\t\t\t'+ varChocIce.get()+ "\n")
        if(int(varSzBrIce.get())>0):
                txtrpt.insert(END, 'Sizzling Brownie: \t\t\t\t\t'+ varSzBrIce.get()+ "\n")
        if(int(varDont.get())>0):
                txtrpt.insert(END, 'Donuts: \t\t\t\t\t'+ varDont.get()+ "\n")
        if(int(varKlf.get())>0):
                txtrpt.insert(END, 'Assorted Kulfi: \t\t\t\t\t'+ varKlf.get()+ "\n")
        if(int(varPep.get())>0):
                txtrpt.insert(END, 'Soft-Drinks: \t\t\t\t\t'+ varPep.get()+ "\n")
        if(int(varMasSod.get())>0):
                txtrpt.insert(END, 'Masala Soda: \t\t\t\t\t'+ varMasSod.get()+ "\n")
        if(int(varMasChs.get())>0):
                txtrpt.insert(END, 'Masala Chaas: \t\t\t\t\t'+ varMasChs.get()+ "\n")
        if(int(varSwtLas.get())>0):
                txtrpt.insert(END, 'Sweet Lassi: \t\t\t\t\t'+ varSwtLas.get()+ "\n")
        if(int(varIceTea.get())>0):
                txtrpt.insert(END, 'Ice Tea: \t\t\t\t\t'+ varIceTea.get()+ "\n")
        if(int(varManShk.get())>0):
                txtrpt.insert(END, 'Mango Milkshake: \t\t\t\t\t'+ varManShk.get()+ "\n")
        if(int(varOroShk.get())>0):
                txtrpt.insert(END, 'Oreo Milkshake: \t\t\t\t\t'+ varOroShk.get()+ "\n")
        if(int(varVirMoj.get())>0):
                txtrpt.insert(END, 'Virjin Mojito: \t\t\t\t\t'+ varVirMoj.get()+ "\n")
        if(int(varWatBlst.get())>0):
                txtrpt.insert(END, 'Watermelon Blast: \t\t\t\t\t'+ varWatBlst.get()+ "\n")
        if(int(varFrsMnt.get())>0):
                txtrpt.insert(END, 'Fresh Mint: \t\t\t\t\t'+ varFrsMnt.get()+ "\n\n")
        txtrpt.insert(END, 'Total Cost: \t\t\t\t\t' +str(i)+ "\n")
        txtrpt.insert(END, 'Total Cost including GST \t\t\t\t\t' +str(tax)+ "\n\n")
        
        txtrpt.insert(END, 'This is an Online Generated Invoice and it does not need any signature' +"\n")
        txtrpt.configure(state='disabled')
        

      


btnDrinks=Button(FDrinksBOT,text="Finalize Your Order",font=('arail', 20, 'bold'),command=lambda:[finalize(),Roti(),Naann(),BNaan(),Kulcha(),BKulcha(),Paratha(),AlooPar(),StuffPar(),PanPar(),RotkiTok(),Choco(),GulJam(),ShahTuk(),GajHal(),ChocFBro(),DChocMos(),CranCCak(),VanIce(),StrawIce(),ChocIce(),SzBrIce(),Dont(),Klf(),Pep(),MasSod(),MasChs(),SwtLas(),IceTea(),ManShk(),OroShk(),VirMoj(),WatBlst(),FrsMnt()])
btnDrinks.pack()


btnrpt=Button(finalize1, text="Generate Bill",font=('arail', 20, 'bold'),command=receipt)
btnrpt.pack()
root.mainloop()
