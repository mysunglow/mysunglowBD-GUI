from tkinter import *
from ordersManager import *
from XMLGenerator import *
import os
import ftplib
from pathlib import Path
from logger import *
import schedule
import time
import sys

convLogger = Logger()
# Make Sure you save after modifying
# Run GUI True if you want to manually handle issues
# runGui = True
# Gui False for Automatic Downloads
runGui = False


class Converter:

    def __init__(self, master):
        self.ediGenerated = False
        self.master = master
        master.title("Blind Data JSON-XML Mapper")
        self.fullPath = ''
        self.fileName = ''
        # Variables
        self.oManager = OrdersManager()
        self.status = self.oManager.callServer()
        self.xmlGenerator = XMLGenerator()
        self.activeFile = None
        self.serviceCount = self.oManager.getSimpleService()

        # LAYOUT``
        rows = 0
        while rows < 6:
            master.rowconfigure(rows, weight=1)
            master.columnconfigure(rows, weight=1)
            rows += 1

        # Header
        self.header = Label(master, text="BD JSON-XML Mapper")
        self.header.grid(row=0, column=0, columnspan=4, sticky=(N, S, E, W))

        # Left List Box
        self.orderList = Listbox(master, selectmode='multiple')
        self.orderList.grid(row=1, column=0, rowspan=5,
                            columnspan=4, padx=10, pady=10, sticky=(N, S, E, W))

        # self.scrollY = Scrollbar(self.orderList, orient="vertical")
        # self.scrollY.config(command=self.orderList.yview)
        # self.scrollY.pack(side="right", fill="y")

        # self.scrollX = Scrollbar(self.orderList, orient="horizontal")
        # self.scrollX.config(command=self.orderList.xview)
        # self.scrollX.pack(side="bottom", fill="x")

        # Right Button Box
        self.getList = Button(master, text='Load Orders', command=lambda: self.generateList(
            self.oManager, self.orderList))
        self.getList.grid(row=1, column=4, padx=10,
                          pady=10, sticky=(N, S, E, W))

        self.selectAll = Button(master, text='Select All',
                                command=lambda: self.selectAllItems())
        self.selectAll.grid(row=2, column=4, padx=10,
                            pady=10, sticky=(N, S, E, W))

        self.makeEDI = Button(master, text='Generate EDI',
                              command=lambda: self.ediGenerator(self.oManager))
        self.makeEDI.grid(row=3, column=4, padx=10,
                          pady=10, sticky=(N, S, E, W))

        self.upload = Button(master, text='Upload File',
                             state=DISABLED, command=lambda: self.handleFTP())
        self.upload.grid(row=4, column=4, padx=10,
                         pady=10, sticky=(N, S, E, W))

        self.submit = Button(master, text='Mark as Submitted',
                             command=lambda: self.callSubmit())
        self.submit.grid(row=5, column=4, padx=10,
                         pady=10, sticky=(N, S, E, W))

        # Bottom Section
        self.errorLabel = Label(master, text="Errors: None")
        self.errorLabel.grid(row=6, column=1, sticky=(N, S, E, W))

        self.statusLabel = Label(master, text="Status: ")
        self.statusResult = Label(master, text=self.status)

        self.statusLabel.grid(row=6, column=2, sticky=(N, S, E, W))
        self.statusResult.grid(row=6, column=3, sticky=(N, S, E, W))

        self.serviceLabel = Label(master, text=f"Service: {self.serviceCount}")
        self.serviceLabel.grid(row=6, column=4, sticky=(N, S, E, W))

        if(self.serviceCount > 0):
            self.serviceLabel['foreground'] = 'red'
            self.serviceLabel['font'] = 'bold'
        else:
            self.serviceLabel['foreground'] = 'black'

        # Row/Column Weight Adjustment

    def generateList(self, ordersManager, orderList):
        self.submittedOrders = ordersManager.getOrders()
        orderList.delete(0, 'end')
        if (len(self.submittedOrders) > 0):
            for i in range(len(self.submittedOrders)):
                orderItem = self.submittedOrders[i].get(
                    'orderTag') + ", " + self.submittedOrders[i].get('PO') + ", " + self.submittedOrders[i].get('email')
                orderList.insert(END, orderItem)
        else:
            orderItem = 'No Orders Found'
            orderList.insert(END, orderItem)

        self.errorLabel['text'] = f'Loaded: {len(self.submittedOrders)}'
        orderList.config(width=0)

    def selectAllItems(self):
        self.orderList.select_set(0, END)

    def getSelectedPO(self):
        POList = []
        if(self.submittedOrders != []):
            for index in self.orderList.curselection():
                POList.append(self.submittedOrders[index].get('PO'))
                # pass
        return POList

    def ediGenerator(self, ordersManager):
        poList = self.getSelectedPO()
        myArray = ordersManager.getProducts(poList)

        # Start Logging
        dt = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        convLogger.log(
            "------------------------------------------------------")
        convLogger.log(dt)

        ediList = self.xmlGenerator.makeOrder(myArray, self.submittedOrders)

        # Get checkNumber if int returned (could do if edilist[0] != '<transfer>' if desired, but would probably prefer to do the number check?)
        if(isinstance(ediList[0], int)):
            check = int(ediList[0])
        else:
            check = 0

        if(check < 0):
            self.errorLabel['text'] = ediList[1]
            # No Orders Selected
            convLogger.log(ediList[1])
            # print(ediList[1])
        else:
            self.errorLabel['text'] = 'EDI Generating..'
            convLogger.log("Generating EDI...")

            self.writeToFile(ediList)
            convLogger.log("List Generated!")

    def writeToFile(self, stringList):
        dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        month = datetime.datetime.now().strftime("%B")
        year = datetime.datetime.now().strftime("%Y")

        dir = os.getcwd()
        dir = os.path.join(dir, 'output')
        if not os.path.exists(dir):
            os.mkdir(dir)

        dir = os.getcwd()
        dir = os.path.join(dir, 'output', year)
        if not os.path.exists(dir):
            os.mkdir(dir)

        dir = os.getcwd()
        dir = os.path.join(dir, 'output', year, month)
        if not os.path.exists(dir):
            os.mkdir(dir)

        self.fileName = f"EDI-{dt}"
        self.fullPath = f"{dir}\\{self.fileName}.xml"
        f = open(f"{dir}/{self.fileName}.xml", "w")
        # Adding apos to see if it works?
        strConcat = " ".join(stringList).replace(
            '&', '&amp;').replace('apos', '&apos;')
        f.write(strConcat)
        f.close()
        self.errorLabel['text'] = 'EDI Generated'
        self.upload['state'] = 'normal'
        convLogger.log("EDI Generated!")
        self.ediGenerated = True

        # print(f"Written to {self.fileName}")
        # print(self.fullPath)

    def callSubmit(self):
        ordersUpdated = self.oManager.submitOrder(self.getSelectedPO())
        if(ordersUpdated > 0):
            self.errorLabel['foreground'] = 'black'
            self.generateList(self.oManager, self.orderList)
        elif(ordersUpdated == 0):
            self.errorLabel['text'] = f'No Orders Submitted'
            convLogger.log("No Orders Submitted")
            self.errorLabel['foreground'] = 'red'
        else:
            self.errorLabel['text'] = f'Error: Unable to Submit'
            convLogger.log("Error: Unable to Submit")
            self.errorLabel['foreground'] = 'red'

    def handleFTP(self):
        session = ftplib.FTP('sunglow.blindata.online', 'sunglow', '3JpsGsa5')
        try:
            session.cwd('private')
            print(session.pwd())

            file = open(self.fullPath, 'rb')
            # print(file.read())
            # file_path = Path(self.fullPath)
            # print(file_path)
            # send the file
            session.storbinary(f'STOR {self.fileName}.xml', file)
            file.close()                                    # close file and FTP

            self.upload['state'] = 'disabled'
            self.errorLabel['text'] = 'EDI Uploaded Succesfully'
            self.errorLabel['foreground'] = 'black'
            convLogger.log("EDI Uploaded Succesfully")

        except:
            self.errorLabel['text'] = 'No EDI File Found'
            self.errorLabel['foreground'] = 'red'
            convLogger.log("No EDI File Found")

            print("No File Found")
        # print(session.pwd())
        # print(session.dir())
        finally:
            print(session.dir())
            session.quit()
        # print(currentFilePath)

    def autoRun(self):
        self.generateList(self.oManager, self.orderList)
        self.selectAllItems()
        self.ediGenerator(self.oManager)

        if(self.ediGenerated == True):
            self.handleFTP()
            self.callSubmit()
            self.ediGenerated = False
            self.fullPath = ''
        else:
            if(self.submittedOrders == []):
                convLogger.log("No Orders to Download")
            else:
                convLogger.log("Failed to Complete Automatically")
            convLogger.log(
                "------------------------------------------------------")
            convLogger.log("")

    def quit(self):
        schedule.clear()
        # sys.exit()


root = Tk()
my_gui = Converter(root)

# my_gui.autoRun()

# def test():
#     print("Hi Rei")

# This one enables GUI
if(runGui):
    root.mainloop()
else:
    print("Starting in BG")
    # schedule.every(2).seconds.do(test)
    # schedule.every(5).seconds.do(my_gui.autoRun)
    schedule.every().monday.at("06:55").do(my_gui.autoRun)
    schedule.every().monday.at("07:55").do(my_gui.autoRun)
    schedule.every().monday.at("08:55").do(my_gui.autoRun)
    schedule.every().monday.at("09:55").do(my_gui.autoRun)
    schedule.every().monday.at("10:55").do(my_gui.autoRun)
    schedule.every().monday.at("11:55").do(my_gui.autoRun)
    schedule.every().monday.at("12:55").do(my_gui.autoRun)
    schedule.every().monday.at("13:55").do(my_gui.autoRun)
    schedule.every().monday.at("14:55").do(my_gui.autoRun)
    schedule.every().monday.at("15:55").do(my_gui.autoRun)
    schedule.every().monday.at("16:55").do(my_gui.autoRun)
    schedule.every().monday.at("17:55").do(my_gui.autoRun)

    schedule.every().tuesday.at("06:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("07:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("08:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("09:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("10:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("11:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("12:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("13:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("14:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("15:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("16:55").do(my_gui.autoRun)
    schedule.every().tuesday.at("17:55").do(my_gui.autoRun)

    schedule.every().wednesday.at("06:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("07:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("08:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("09:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("10:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("11:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("12:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("13:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("14:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("15:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("16:55").do(my_gui.autoRun)
    schedule.every().wednesday.at("17:55").do(my_gui.autoRun)

    schedule.every().thursday.at("06:55").do(my_gui.autoRun)
    schedule.every().thursday.at("07:55").do(my_gui.autoRun)
    schedule.every().thursday.at("08:55").do(my_gui.autoRun)
    schedule.every().thursday.at("09:55").do(my_gui.autoRun)
    schedule.every().thursday.at("10:55").do(my_gui.autoRun)
    schedule.every().thursday.at("11:55").do(my_gui.autoRun)
    schedule.every().thursday.at("12:55").do(my_gui.autoRun)
    schedule.every().thursday.at("13:55").do(my_gui.autoRun)
    schedule.every().thursday.at("14:55").do(my_gui.autoRun)
    schedule.every().thursday.at("15:55").do(my_gui.autoRun)
    schedule.every().thursday.at("16:55").do(my_gui.autoRun)
    schedule.every().thursday.at("17:55").do(my_gui.autoRun)

    schedule.every().friday.at("06:55").do(my_gui.autoRun)
    schedule.every().friday.at("07:55").do(my_gui.autoRun)
    schedule.every().friday.at("08:55").do(my_gui.autoRun)
    schedule.every().friday.at("09:55").do(my_gui.autoRun)
    schedule.every().friday.at("10:55").do(my_gui.autoRun)
    schedule.every().friday.at("11:55").do(my_gui.autoRun)
    schedule.every().friday.at("12:55").do(my_gui.autoRun)
    schedule.every().friday.at("13:55").do(my_gui.autoRun)
    schedule.every().friday.at("14:55").do(my_gui.autoRun)
    schedule.every().friday.at("15:55").do(my_gui.autoRun)
    schedule.every().friday.at("16:55").do(my_gui.autoRun)
    schedule.every().friday.at("17:55").do(my_gui.autoRun)

    # schedule.every().friday.at("18:00").do(my_gui.quit)

    # new Timings
    schedule.every().saturday.at("08:55").do(my_gui.autoRun)
    schedule.every().saturday.at("12:55").do(my_gui.autoRun)
    schedule.every().saturday.at("15:55").do(my_gui.autoRun)
    schedule.every().saturday.at("17:55").do(my_gui.autoRun)

    schedule.every().sunday.at("08:55").do(my_gui.autoRun)
    schedule.every().sunday.at("12:55").do(my_gui.autoRun)
    schedule.every().sunday.at("15:55").do(my_gui.autoRun)
    schedule.every().sunday.at("17:55").do(my_gui.autoRun)

    while True:
        n = schedule.idle_seconds()
        schedule.run_pending()
        if n is None:
            # no more jobs
            break
        elif n > 0:
            # sleep exactly the right amount of time
            time.sleep(n)
