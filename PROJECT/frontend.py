from tkinter import *
import tkinter.messagebox
import backend

class qa_sys:

    def __init__(self, root):
        self.root = root
        self.root.title("Quality Analysis and Control")
        self.root.geometry("1500x650")
        self.root.config(bg="lightgrey")

        BNO = StringVar()
        PRODNAME = StringVar()
        TYPE = StringVar()
        IMPORT_DATE = StringVar()
        SUPP = StringVar()
        selected_VALID = StringVar()
        STAB = StringVar()
        FEED = StringVar()

        # --------------------------------------FUNCTIONS-------------------------------------------------------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Quality Analysis and Control", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtBNO.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtIMPORT_DATE.delete(0, END)
            self.txtSUPP.delete(0, END)
            selected_VALID.set(VALID_options[0])  # Set the default value
            self.txtAdr.delete(0, END)
            self.txtFEED.delete(0, END)

        def addData():
            if(len(BNO.get()) != 0):
                backed.addStdRec(BNO.get(), PRODNAME.get(), TYPE.get(), IMPORT_DATE.get(), SUPP.get(),
                                 selected_VALID.get(), STAB.get(), FEED.get())
                qa_sys.delete(0, END)
                qa_sys.insert(END, (BNO.get(), PRODNAME.get(), TYPE.get(), IMPORT_DATE.get(), SUPP.get(),
                                      selected_VALID.get(), STAB.get(), FEED.get()))

        def DisplayData():
            qa_sys.delete(0, END)
            for row in backed.viewData():
                qa_sys.insert(END, row, str(""))

        def table123Rec(event):
            global sd
            searchStd = qa_sys.curselection()[0]
            sd = qa_sys.get(searchStd)

            self.txtBNO.delete(0, END)
            self.txtBNO.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtIMPORT_DATE.delete(0, END)
            self.txtIMPORT_DATE.insert(END, sd[4])
            self.txtSUPP.delete(0, END)
            self.txtSUPP.insert(END, sd[5])
            selected_VALID.set(VALID_options[0])  # Set the selected value in the dropdown
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sd[7])
            self.txtFEED.delete(0, END)
            self.txtFEED.insert(END, sd[8])

        def DeleteData():
            if(len(BNO.get()) != 0):
                backed.deleteRec(sd[0])
                clearData()
                DisplayData()

        def update():
            if (len(BNO.get()) != 0):
                backed.deleteRec(sd[0])
            if (len(BNO.get()) != 0):
                backed.addStdRec(BNO.get(), PRODNAME.get(), TYPE.get(), IMPORT_DATE.get(), SUPP.get(),
                                 selected_VALID.get(), STAB.get(), FEED.get())
                qa_sys.delete(0, END)
                qa_sys.insert(END, (BNO.get(), PRODNAME.get(), TYPE.get(), IMPORT_DATE.get(), SUPP.get(),
                                      selected_VALID.get(), STAB.get(), FEED.get()))

        # --------------------------------------Frames-----------------------------------------------------------------------__________________________________________________________
        MainFrame = Frame(self.root, bg="lightgrey")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)
        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame, font=('Arial', 48, 'bold'), text="Quality Analysis and Control", bg="Ghost White")
        self.lblTit.grid()
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg="Ghost White", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="lightgrey")
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=0, width=1500, height=600, padx=20, relief=RIDGE, bg="Ghost White",
                                   font=('Arial', 26, 'bold'), text="Material Information\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=0, width=450, height=300, padx=31, pady=3, relief=RIDGE,
                                    bg="Ghost White", font=('Arial', 27, 'bold'), text="                              Material Details\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # --------------------------------entries-------------------------------------------------------------------------------------------------
        self.lblBNO = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="BATCH NUMBER:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblBNO.grid(row=0, column=0, sticky=W)
        self.txtBNO = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=BNO, width=39)
        self.txtBNO.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="MATERIAL NAME:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=PRODNAME, width=39)
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="TYPE:", padx=2, pady=2, bg="Ghost White")
        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=TYPE, width=39)
        self.txtSna.grid(row=2, column=1)

        self.lblIMPORT_DATE = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="IMPORT DATE:", padx=2, pady=2,
                                    bg="Ghost White")
        self.lblIMPORT_DATE.grid(row=3, column=0, sticky=W)
        self.txtIMPORT_DATE = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=IMPORT_DATE, width=39)
        self.txtIMPORT_DATE.grid(row=3, column=1)

        self.lblSUPP = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="SUPPLIER:", padx=2, pady=2,
                             bg="Ghost White")
        self.lblSUPP.grid(row=4, column=0, sticky=W)
        self.txtSUPP = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=SUPP, width=39)
        self.txtSUPP.grid(row=4, column=1)

        self.lblVALID = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="TEST VALIDITY:", padx=2, pady=2, bg="Ghost White")
        self.lblVALID.grid(row=5, column=0, sticky=W)

        VALID_options = ["Yes", "No"]
        self.optionMenu = OptionMenu(DataFrameLEFT, selected_VALID, *VALID_options)
        self.optionMenu.config(font=('Arial', 15, 'bold'), width=12)
        self.optionMenu.grid(row=5, column=1, sticky=W)  # Moved to column 1 and set sticky to West (LEFT)


        self.lblAdr = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="COST:", padx=2, pady=2,
                            bg="Ghost White")
        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=STAB, width=39)
        self.txtAdr.grid(row=6, column=1)

        self.lblFEED = Label(DataFrameLEFT, font=('Arial', 20, 'bold'), text="WEIGHT(cgs):", padx=2, pady=2,
                             bg="Ghost White")
        self.lblFEED.grid(row=7, column=0, sticky=W)
        self.txtFEED = Entry(DataFrameLEFT, font=('Arial', 20, 'bold'), textvariable=FEED, width=39)
        self.txtFEED.grid(row=7, column=1)

        # --------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        qa_sys = Listbox(DataFrameRIGHT, width=50, height=16, font=('Arial', 12), yscrollcommand=scrollbar.set)
        qa_sys.bind('<<ListboxSelect>>', table123Rec)
        qa_sys.grid(row=0, column=0, padx=8)
        scrollbar.config(command=qa_sys.yview)

        # --------------------------------------buttons-----------------------------------------------------------------------------------------------------------
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,
                                command=addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,
                                     command=DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, text="Clear", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,
                                   command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=DeleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('Arial', 20, 'bold'), height=1, width=10, bd=4,
                                    command=update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text="Exit", font=('Arial', 20, 'bold'), height=1, width=10, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)

if __name__ == '__main__':
    root = Tk()
    application = qa_sys(root)
    root.mainloop()
