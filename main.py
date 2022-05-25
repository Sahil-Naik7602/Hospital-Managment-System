from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import numpy as np
import mysql.connector

with open('medicine_name.txt','r') as file_obj:
    medicine_name_list = np.array(file_obj.readlines())
new_medicine_name_list = [x.strip() for x in medicine_name_list]
new_medicine_name_list.sort()
medicine_name =("N/A",) + tuple(new_medicine_name_list)


class Hospital:

    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar() 
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar() 
        self.StorageAdvice =StringVar()
        self.DrivingUsingMachine=StringVar() 
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress = StringVar()
        
        lbltitle = Label(self.root,bd = 20, relief=RIDGE,text = "HOSPITAL MANAGEMENT SYSTEM",fg = 'blue',bg = 'white',font=('times new roman',50,'bold'))
        lbltitle.pack(side=TOP,fill=X)

        ############## DATA FRAME #####################
        Dataframe = Frame(self.root,bd = 20, relief= RIDGE)
        Dataframe.place(x=0,y = 130,width = 1530, height = 400)

        DataframeLeft = LabelFrame(Dataframe,bd = 10,relief = RIDGE,padx = 20,
                        font=('arial',12,'bold'),text = 'Patient Information')
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        Dataframeright = LabelFrame(Dataframe,bd = 10,relief = RIDGE,padx = 20,
                        font=('arial',12,'bold'),text = 'Prescription')
        Dataframeright.place(x=990,y=5,width=495,height = 350)

        ################## BUTTONS FRAME ###################
        Buttonframe = Frame(self.root)
        Buttonframe.place(x=0,y=530,width = 1530,height = 70)

        #################### DETAILS FRAME ##################
        Detailsframe = Frame(self.root,bd = 20,relief = RIDGE)
        Detailsframe.place(x=0,y=590,width=1530,height=240)

        ##################  DATAFRAME LEFT LABELS ############
        lblNameTablet = Label(DataframeLeft,text="Names Of Tablet",font =('arial',12,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft,state="readonly",font = ('arial',12,'normal'),
                                    width = 33,textvariable=self.Nameoftablets)
        comNameTablet['value'] = medicine_name
        comNameTablet.current(0)
        comNameTablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,font = ("arial",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.ref)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft,font = ("arial",12,"bold"),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.Dose)
        txtDose.grid(row=2,column=1)

        lblNoOfTablets = Label(DataframeLeft,font = ("arial",12,"bold"),text="No. of Tablets:",padx=2,pady=6)
        lblNoOfTablets.grid(row=3,column=0,sticky=W)
        txtNoOfTablets = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.NumberofTablets)
        txtNoOfTablets.grid(row=3,column=1)

        lblLot = Label(DataframeLeft,font = ("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.Lot)
        txtLot.grid(row=4,column=1)

        lblIssueDate = Label(DataframeLeft,font = ("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.Issuedate)
        txtIssueDate.grid(row=5,column=1)

        lblExpDate = Label(DataframeLeft,font = ("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.ExpDate)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataframeLeft,font = ("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.DailyDose)
        txtDailyDose.grid(row=7,column=1)

        lblSideAffect = Label(DataframeLeft,font = ("arial",12,"bold"),text="Side Affects:",padx=2,pady=6)
        lblSideAffect.grid(row=8,column=0,sticky=W)
        txtSideAffect = Entry(DataframeLeft,font=("arial",12,"normal"),width=35,textvariable=self.sideEffect)
        txtSideAffect.grid(row=8,column=1)

        lblFurtherInformation = Label(DataframeLeft,font = ("arial",12,"bold"),text="Further Info.:",padx=2,pady = 6)
        lblFurtherInformation.grid(row=0,column=3,sticky=W)
        txtFurtherInformation = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.FurtherInformation)
        txtFurtherInformation.grid(row=0,column=4)

        lblDrivingMachine = Label(DataframeLeft,font = ("arial",12,"bold"),text="Blood Pressure:",padx=2,pady = 6)
        lblDrivingMachine.grid(row=1,column=3,sticky=W)
        txtDrivingMachine = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.DrivingUsingMachine)
        txtDrivingMachine.grid(row=1,column=4)

        lblStorage = Label(DataframeLeft,font = ("arial",12,"bold"),text="Storage Advice:",padx=2,pady = 6)
        lblStorage.grid(row=2,column=3,sticky=W)
        txtStorage = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.StorageAdvice)
        txtStorage.grid(row=2,column=4)

        lblMedication = Label(DataframeLeft,font = ("arial",12,"bold"),text="Medication:",padx=2,pady = 6)
        lblMedication.grid(row=3,column=3,sticky=W)
        txtMedication = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.HowToUseMedication)
        txtMedication.grid(row=3,column=4)

        lblPatientId = Label(DataframeLeft,font = ("arial",12,"bold"),text="Patient Id:",padx=2,pady = 6)
        lblPatientId.grid(row=4,column=3,sticky=W)
        txtPatientId = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.PatientId)
        txtPatientId.grid(row=4,column=4)

        lblNHSNumber = Label(DataframeLeft,font = ("arial",12,"bold"),text="NHS Number:",padx=2,pady = 6)
        lblNHSNumber.grid(row=5,column=3,sticky=W)
        txtNHSNumber = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.nhsNumber)
        txtNHSNumber.grid(row=5,column=4)

        lblPatientName = Label(DataframeLeft,font = ("arial",12,"bold"),text="Patient Name:",padx=2,pady = 6)
        lblPatientName.grid(row=6,column=3,sticky=W)
        txtPatientName = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.PatientName)
        txtPatientName.grid(row=6,column=4)

        lblDateofBirth = Label(DataframeLeft,font = ("arial",12,"bold"),text="Date Of Birth:",padx=2,pady = 6)
        lblDateofBirth.grid(row=7,column=3,sticky=W)
        txtDateofBirth = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.DateOfBirth)
        txtDateofBirth.grid(row=7,column=4)

        lblPatientAddress = Label(DataframeLeft,font = ("arial",12,"bold"),text="Patient Address:",padx=2,pady = 6)
        lblPatientAddress.grid(row=8,column=3,sticky=W)
        txtPatientAddress = Entry(DataframeLeft,font=("arial",12,"normal"),width=33,textvariable=self.PatientAddress)
        txtPatientAddress.grid(row=8,column=4)


        ########### DATAFRAME RIGHT #################
        self.txtPrescription = Text(Dataframeright,font = ('arial',12,'normal'),width=49,height=16,padx=2,pady=2)
        self.txtPrescription.grid(row=0,column=0)

        ########## BUTTONS ######################
        btnPrescription = Button(Buttonframe, text="Prescription",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6,command=self.iPrescription)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
        btnPrescriptionData.config(command=self.iPrescriptionData)

        btnUpdate = Button(Buttonframe, text="Update",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6,command=self.update_data)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe, text="Delete",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6,command=self.iDelete)
        btnDelete.grid(row=0,column=3)

        btnReset = Button(Buttonframe, text="Reset",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6,command = self.clear)
        btnReset.grid(row=0,column=4)

        btnExit = Button(Buttonframe,text="Exit",bg = "blue",fg="white",font = ("arial",12,"bold"),width=25,height=2,padx=2,pady=6,command = self.iExit)
        btnExit.grid(row=0,column=5)

        ##########################TABLE###############
        #######################ScrollBar##############
        scroll_x  = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y  = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate",
                                                                "expdate","dailydose", "storage", "nhsnumber","pname","dob", "address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date") 
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage") 
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column ("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100) 
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def iPrescriptionData(self):
        '''It inserts data into SQL schema'''
        if self.Nameoftablets.get()=="N/A" or self.ref.get()=="":
            messagebox.showerror("error","All fields are required")
        else:
            conn = mysql.connector.connect(host ="localhost", username="root", password ="7602@SahiL", database="hospital")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.Nameoftablets.get(),
                                                                                                            self.ref.get(),
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberofTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.ExpDate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.StorageAdvice.get(),
                                                                                                            self.nhsNumber.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.PatientAddress.get()
                                                                                                        ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Your record has been Inserted.")

    def update_data(self):
        conn = mysql.connector.connect(host ="localhost", username="root", password ="7602@SahiL", database="hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital_data set Name_of_Tablets=%s,DOSE=%s,NumberofTablets=%s,lot=%s,IssueDate=%s,ExpDate=%s,DailyDose = %s,Storage=%s,NHSNumber=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference_No=%s",(
                                                                                                            self.Nameoftablets.get(),
                                                                                                            self.Dose.get(),
                                                                                                            self.NumberofTablets.get(),
                                                                                                            self.Lot.get(),
                                                                                                            self.Issuedate.get(),
                                                                                                            self.ExpDate.get(),
                                                                                                            self.DailyDose.get(),
                                                                                                            self.StorageAdvice.get(),
                                                                                                            self.nhsNumber.get(),
                                                                                                            self.PatientName.get(),
                                                                                                            self.DateOfBirth.get(),
                                                                                                            self.PatientAddress.get(),
                                                                                                            self.ref.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Your record has been Updated.")
        
    def fetch_data(self):
        '''It shows data in hospital_table'''
        conn = mysql.connector.connect(host ="localhost", username="root", password ="7602@SahiL", database="hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital_data")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children()) 
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        if len(self.txtPrescription.get(1.0, "end-1c"))!=0:
            self.txtPrescription.delete("1.0","end")
        self.txtPrescription.insert(END, "Name of Tablets: \t\t\t"+ self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END, "Reference No: \t\t\t"+ self.ref.get() +"\n")
        self.txtPrescription.insert(END, "Dose: \t\t\t" +self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t"+self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot: \t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END, "Issue Date: \t"+self.Issuedate.get()+"\t\t")
        self.txtPrescription.insert(END, "Exp date: \t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose: \t\t\t"+self.DailyDose.get()+"\n") 
        self.txtPrescription.insert(END, "Side Effect: \t\t\t"+self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information:\t\t\t"+self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "StorageAdvice: \t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END, "DrivingUsing Machine: \t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END, "PatientId: \t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END, "NHSNumber: \t\t\t"+self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "PatientName: \t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END, "DateOfBirth: \t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END, "PatientAddress:\t\t\t"+self.PatientAddress.get())

    def iDelete(self):
        conn=mysql.connector.connect(host='localhost', username="root", password ="7602@SahiL", database="hospital")
        my_cursor=conn.cursor()
        query="delete from hospital_data where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete", "Patient' Medication Detail has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.StorageAdvice.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        IExit=messagebox.askyesno ("Hospital managemnt system", "Confirm you want to exit")
        if IExit>0:
            root.destroy()
            return


root = Tk()
ob = Hospital(root)
root.mainloop()
