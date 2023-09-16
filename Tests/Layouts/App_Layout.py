
# import multiprocess as mprocess
# from multiprocess import  process ,queues as Procress ,Queues

from datetime import datetime, date, timedelta
from CTkMessagebox import CTkMessagebox as cmsg
from Application_Functions import *
from MicrocontrollerConnection import *
import multiprocessing as mprocess
import CTkMessagebox as ctkm
import customtkinter as ctk
import tkinter as tk
from tkinter.ttk import *
from PIL import ImageTk, Image
import urllib.request
from pythonping import ping
import requests
import json
import time 
import os

# ************** All Custom App Components Imports **************
# import Exam_Timer 
# import clock_controls
 

# ************** Application Theme Set **************
ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# ************** All Global Constants **************
Dataset = ''
Font = ('calibri',16,'bold')
temp_App_location = 'Tests/Layouts'
temp_database_location = 'Tests/Databases'
states=['disabled','normal']
Exam_Tab_Set = ['One Exam Day','Two Exams Day','Three Exams Day']
validation_status = 0
Uploadaple_data = {}

# ************** All Global Variables **************



# ************** Extracting the Application Information **************
with open('Tests/Databases/app_Static_info.json','r') as f:
    Dataset = json.load(f)
    f.close()
panel_Text=Dataset['Control Pannel']

# ************** Main Application Window Class **************
class App(ctk.CTk):
# class App():
    def __init__(self):
        super().__init__()

        # configure window
        self.title(Dataset['Software_Name'])
        self.geometry(f"{1280}x{720}")
        self.iconphoto(False, tk.PhotoImage(file="Tests/Layouts/Img/logo.png"))
        
        self.informationFrame = ctk.CTkFrame(self,fg_color='transparent')
        self.informationFrame.pack(anchor="n", fill ="x" ,padx=(20,20), pady=(15,8) )
        self.informationFrame.columnconfigure((0,1),weight=1)
        self.informationFrame.rowconfigure((0,1),weight=1)

        self.Title_Frame = ctk.CTkFrame(self)
        self.Title_Frame.pack(anchor="n", fill="x", padx=(20,20), pady=(15,0))
        self.Title_Frame.columnconfigure((0,1),weight=1)

        self.Title = ctk.CTkLabel(master= self.Title_Frame, text="Control Panel", font=ctk.CTkFont(size=18,family='calibri',weight='bold') )
        self.Title.grid(row=0,column=0, sticky="w",padx=(20,0),pady=(5,5))


        self.networkFrame = ctk.CTkFrame(self.Title_Frame,fg_color='transparent' ,bg_color='transparent' )
        self.networkFrame.grid(row=0,column=1,sticky="ne",padx=(0,20),pady=5)

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Img")
        self.online_Image = ctk.CTkImage(Image.open(os.path.join(image_path, "online6.png")), size=(30, 30))
        self.offline_Image = ctk.CTkImage(Image.open(os.path.join(image_path, "offline5.png")), size=(30, 30))

        self.network_states = ['Offline','Online']
        self.network_Images = [self.offline_Image,self.online_Image]

        self.networkImage = ctk.CTkLabel(self.networkFrame, text="", image=self.offline_Image,compound="left",fg_color='transparent' ,bg_color='transparent' )
        self.networkImage.grid(row=0, column=0, padx=0, pady=0)

        self.network_status = ctk.CTkLabel(self.networkFrame,text=self.network_states[0],font=ctk.CTkFont(size=18, weight='bold',family='calibri',))
        self.network_status.grid(row=0,column=1, padx=20,pady=5) 

        def Set_Network_Status():
            self.networkImage.configure(image=self.network_Images[getConnectionValue()])
            self.network_status.configure(text = self.network_states[getConnectionValue()])
            self.networkImage.after(2500,Set_Network_Status)
        Set_Network_Status()
            
        self.control_Pannel_Frame = ctk.CTkScrollableFrame(self,height=500)
        self.control_Pannel_Frame.pack(anchor="n",fill ="both" ,padx=(20,20),pady=(10,20) )
        self.control_Pannel_Frame.columnconfigure(0,weight=1)
        self.control_Pannel_Frame.columnconfigure(1,weight=2)

        # self.status_Frame = ctk.CTkFrame(self,height=20)
        # self.status_Frame.pack(anchor='s' ,fill ="x" ,padx=(20,20),pady=(10,0) )

class Application_Information() :
    def __init__(self):
        super().__init__()
        About_Txt = Dataset['About']
        self.leftFrame = ctk.CTkFrame(mainFrames.informationFrame ,width=400)
        self.leftFrame.grid(row=0,column=0,sticky='nsew',padx=(0,160))

        self.rightFrame = ctk.CTkFrame(mainFrames.informationFrame)
        self.rightFrame.grid(row=0,column=1,sticky='nsew',padx=(150,0))

# ************** Left Frame Section **************

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Img")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "gcect_logo.png")), size=(180, 180))

        self.college_logo = ctk.CTkLabel(self.leftFrame, text="", image=self.logo_image, corner_radius=30,compound="left" )
        self.college_logo.grid(row=0, column=0, padx=15, pady=20)
        
        self.college_Name_Frame = ctk.CTkFrame(self.leftFrame)
        self.college_Name_Frame.grid(row=0,column=1,sticky="n" ,pady=(20,10))
        self.College_Name = ctk.CTkLabel(self.college_Name_Frame,text=Dataset['College_Name'],font=ctk.CTkFont(size=20, weight="bold"),wraplength=350)
        self.College_Name.pack(anchor='n', padx=(10,10),pady=(10,10))

        self.college_Address_Frame = ctk.CTkFrame(self.leftFrame)
        self.college_Address_Frame.grid(row=0,column=1,sticky="s",pady=(0,20))
        self.college_Address = ctk.CTkLabel(self.college_Address_Frame,text=Dataset['College_Address'],wraplength=350,font=Font)
        self.college_Address.pack(padx=40,pady=(10,10))

# ************** Right Frame Section **************

        self. About_Frame = ctk.CTkFrame(self.rightFrame)
        self.About_Frame.grid(row=0,column=0,sticky='nw',padx=20,pady=(20,0))

        self.About_Text = ctk.CTkLabel(self.About_Frame,text=About_Txt['Topic_Heading'],font=ctk.CTkFont(size=18,family='calibri',weight='bold'))
        self.About_Text.pack(padx=20,pady=5)

        self.More_Details = ctk.CTkLabel(self.rightFrame,text='User Guide',font=ctk.CTkFont(size=16,family='calibri',weight='bold',slant='italic',underline=True))
        self.More_Details.grid(row=0,column=1, sticky='s',padx=20,pady=20)

        self.__version = ctk.CTkLabel(self.rightFrame,text=About_Txt['Current_Version'],font=ctk.CTkFont(size=20,family='calibri',weight='bold',slant='italic'))
        self.__version.grid(row=1, column=0, sticky='nw',padx=40,pady=0)

        self.__available_Txt = ctk.CTkLabel(self.rightFrame,text=About_Txt['First_Available_Date'],font=Font)
        self.__available_Txt.grid(row=2, column=0, sticky='nw',padx=40,pady=0)

        self.developer_Frame = ctk.CTkFrame(self.rightFrame)
        self.developer_Frame.grid(sticky='sw',row=3,column=0,padx=20,pady=(30,10))

        self.developer_Txt = ctk.CTkLabel(self.developer_Frame,text=About_Txt['About_Developer'],font=Font)
        self.developer_Txt.pack(padx=20,pady=10)
        def info_window():
            app=ctk.CTk()
            app.geometry , app.title =("400x500") , Dataset['Software_Name']
            # msg = '"Phone": 6289841625 , \n  "Email" : info.subarno@gmail.com '
            msg = str(Dataset['About']).replace("\\n","\n\t\t").replace("'","\"").replace(":"," :").replace("{","{\n ").replace("}}","\n \t}\n}").replace(",","\n\t\t")
            # msg = str(json(Dataset['About'],indent=4))
            ctk.CTkLabel(app , text = msg ,font=Font, justify ="left").pack(padx=20,pady=20)
            ctk.CTkButton(app, text ='OK',font=Font,command=lambda: app.destroy()).pack(padx=20,pady=10)
            app.mainloop()
        # msg = '{ Phone : 6289841625  Email : info.subarno@gmail.com Project Type : Embeded System Programming }'
        self.More_Details = ctk.CTkLabel(self.rightFrame,text='More Details',font=ctk.CTkFont(size=16,family='calibri',weight='bold',slant='italic',underline=True))
        self.More_Details.grid(row=3,column=1, sticky='s',padx=20,pady=20)
        # self.More_Details.bind(sequence="<Button-1>",command=lambda self:cmsg(title=Dataset['Software_Name'],icon='warning',message=msg))
        self.More_Details.bind(sequence="<Button-1>",command=lambda self:info_window())

# ************** Control Panel Class **************

class Control_Panel:
    def __init__(self):
        super().__init__()

        self.operationsTabSet = ctk.CTkTabview(mainFrames.control_Pannel_Frame, width = 640)
        # self.operationsTabSet.pack(anchor="nw",padx=(10,10),pady=(0,10))
        self.operationsTabSet.grid(row=0,column=0,sticky='w')

        self.operationsTabSet.add("Exam Timer")
        # self.operationsTabSet.add("Set Network and Time") # Set Network and Time  
        self.operationsTabSet.add("Check Clock Status") # Clock Current State 
 
#  ************** Exam Timer Section **************
        self.ExamDateFrame=ctk.CTkFrame(self.operationsTabSet.tab("Exam Timer"))
        self.ExamDateFrame.pack(anchor='n',fill="x",padx=(15,15))
        self.ExamDateFrame.columnconfigure((0,1),weight=1)

        self.ExamDateLabel = ctk.CTkLabel(self.ExamDateFrame,text = panel_Text['row0col0'],font=Font)
        self.ExamDateLabel.grid(row=0,column=0,padx=(10,10),sticky='e')
        
        date_list = set_Exam_Dates()
        self.ExamDateInput = ctk.CTkOptionMenu(self.ExamDateFrame, width = 120 ,values=date_list,variable=ExamDate)
        self.ExamDateInput.grid(row=0,column=1,pady=(8,8),sticky='w')
        self.ExamDateInput.set(value = date_list[0])


        self.ExamSet = ctk.CTkTabview(self.operationsTabSet.tab("Exam Timer"),width=600)
        self.ExamSet.pack(anchor='n')

        self.ExamSet.add(Exam_Tab_Set[0]) 
        self.ExamSet.add(Exam_Tab_Set[1])
        self.ExamSet.add(Exam_Tab_Set[2])

        self.saveAndUploadFrame = ctk.CTkFrame(self.operationsTabSet.tab("Exam Timer"))
        self.saveAndUploadFrame.pack(anchor='n',fill='x',padx=(15,15),pady=(15,5))
        self.saveAndUploadFrame.columnconfigure((0,1),weight=1)

        def Active_saveBtn():
            global validation_status
            print("check validation = ",self.CheckSelection.get(),validation_status)
            if self.CheckSelection.get()==0 and validation_status==1:
                lock_unlock_All(0)
                self.CheckSelection.deselect()
                self.SaveBtn.configure(state=states[0])
                self.UploadBtn.configure(state=states[0])
            else:
                checked = Validate_Data()
                self.SaveBtn.configure(state=states[checked])
                if checked == 0 : self.CheckSelection.deselect()
        
        self.CheckSelection = ctk.CTkCheckBox(self.saveAndUploadFrame, text=panel_Text['confirmation'],font=Font,command=Active_saveBtn, variable=check_Info)
        self.CheckSelection.grid(row=0,column=0,columnspan=2,pady=(15,5))

        def Save_Info():
            Save_Information()

        self.SaveBtn = ctk.CTkButton(self.saveAndUploadFrame, text='Save Information',font=Font,state=states[0],command=Save_Info)
        self.SaveBtn.grid(row=1,column=0,sticky='w',padx=(60,20),pady=(10,20))

        def UPloadData():
            cmsg(title=Dataset['Software_Name'],message=f"{ Uploadaple_data}\n This message has been Transmitted Succesfully.")
            SendSerialData(Uploadaple_data)
            pass
        
        self.UploadBtn = ctk.CTkButton(self.saveAndUploadFrame, text='UPLOAD DATA',font=Font,fg_color='green',hover_color='darkgreen',state=states[0],command=UPloadData)
        self.UploadBtn.grid(row=1,column=1,sticky='e',padx=(20,60),pady=(10,20))


# ************** Set Network and Time Section **************

        # self.timeZoneFrame = ctk.CTkFrame(self.operationsTabSet.tab("Set Network and Time"))
        # self.timeZoneFrame.pack(anchor='nw', fill='x')

        # self.TimeZoneLabel = ctk.CTkLabel(self.timeZoneFrame,text= " Set Time Zone ",font=ctk.CTkFont(size=18,weight='bold'))
        # self.TimeZoneLabel.grid(row=0,column=0,columnspan=2,padx=20,pady=20)



        # self.contenent_label = ctk.CTkLabel(self.timeZoneFrame,text="Contenent : " ,font=Font)
        # self.contenent_label.grid(row=1,column=0,padx=20,pady=10)

        # self.content_name = ctk.CTkOptionMenu(self.timeZoneFrame,variable= Contenent,values=['Asia','Europe','Africa'])
        # self.content_name.grid(row=1,column=1,padx=10,pady=10)


# ************** Check Clock Status Section **************
       
        # self.Alarm01Frame = ctk.CTkFrame(master= self.operationsTabSet.tab("Check Clock Status"))
        # self.Alarm01Frame.pack(anchor='nw',fill='x')

        # self.Alarm01Frame.columnconfigure((0,1,2,3),weight=1)

        # self.alarm01 = ctk.CTkLabel(self.Alarm01Frame,text='Set Alarm-01 : ',font=Font)
        # self.alarm01.grid(row=0,column=0,padx=20,pady=10,sticky='w')

        # self.alarm01_Date = ctksys

        self.clock_status_Frame = ctk.CTkFrame(self.operationsTabSet.tab("Check Clock Status"))
        self.clock_status_Frame.pack(anchor='n', fill='both')


        self.alarm01check =  ctk.CTkButton(self.clock_status_Frame,font=Font,text="Alarm-01 Status")
        self.alarm01check.pack(padx=20,pady=(20,10),ipadx=10)

        self.alarm02check = ctk.CTkButton(self.clock_status_Frame,font=Font,text="Alarm-02 Status")
        self.alarm02check.pack(padx=20,pady=10,ipadx=10)

        # self.Test_Sound = ctk.CTkButton(self.clock_status_Frame,font=Font,text="Sound Saystem Check")
        # self.Test_Sound.pack(padx=20,pady=10,ipadx=10)

        self.broadcast_Temp = ctk.CTkButton(self.clock_status_Frame,font=Font,text=" Current Temparature ",fg_color="orange",hover_color="orangered")
        self.broadcast_Temp.pack(padx=20,pady=10,ipadx=10)
        
        self.Date_Test = ctk.CTkButton(self.clock_status_Frame,font=Font,text=" Today's Date ")
        self.Date_Test.pack(padx=20,pady=10,ipadx=10)

        self.Exam_Data_check = ctk.CTkButton(self.clock_status_Frame,font=Font,text="is Exam Data Uploaded Just Now ? ",fg_color="green",hover_color="darkgreen")
        self.Exam_Data_check.pack(padx=20,pady=20,ipadx=10)

        self.Exam_Data_Alert = ctk.CTkLabel(self.clock_status_Frame,font=Font,text="You have only 10 minutes \n To verify After Uploading Data. ")
        self.Exam_Data_Alert.pack()
        self.verify_Exam_info = ctk.CTkButton(self.clock_status_Frame,font=Font,text="Verify Exam Information")
        self.verify_Exam_info.pack(padx=20,pady=(10,20),ipadx=10)

# ************** Clock History Section **************
        self.rightFrame = ctk.CTkFrame(mainFrames.control_Pannel_Frame)
        self.rightFrame.grid(row=0,column=1,sticky='news')

        self.rightFrame.columnconfigure(0,weight=1)
        self.rightFrame.columnconfigure(1,weight=2)
        self.rightFrame.grid_rowconfigure(0,weight=1)
        self.rightFrame.grid_rowconfigure(1,weight=0)
        self.rightFrame.grid_rowconfigure(2,weight=5)

        self.Network_Time_Button = ctk.CTkButton(self.rightFrame,text='Upload Network Time', font=Font ,state='disabled' )
        self.Network_Time_Button.grid(row=0,column=0,sticky='w',padx=20,ipadx=10,ipady=5)

        self.TimeFrame = ctk.CTkFrame(self.rightFrame)
        self.TimeFrame.grid(row=0,column=1,sticky="e",padx=(20,20))

        # TimeFrame = ctk.CTkFrame(self.rightFrame)
        # self.TimeFrame.pack(anchor="e",padx=(20,20),pady=(10,10))
        # TimeFrame.grid(row=0,column=1,sticky="e",padx=(20,20),pady=(10,10))

        self.current_Time = ctk.CTkLabel(self.TimeFrame, text='Current Date Time : 02:41 pm, Friday, 31 March 2023 (IST)', font=Font )
        self.current_Time.pack(anchor='e',padx=(20,20),pady=5)

        def Time_Runner():
            T = time.localtime()
            S = ['System','Network']
            self.Network_Time_Button.configure(state = states[getConnectionValue()])
            self.current_Time.configure(text=f"{S[getConnectionValue()]} Date Time : {zero(hour12(T.tm_hour))}:{zero(T.tm_min)}:{zero(T.tm_sec)} {ampm(T.tm_hour)}, {weekday(T.tm_wday)}, {T.tm_mday} {Month(T.tm_mon)} {T.tm_year} (IST)")
            self.current_Time.after(1000, Time_Runner)
        Time_Runner()

        self.Prev_Records_Frame = ctk.CTkFrame(self.rightFrame)
        self.Prev_Records_Frame.grid(row=1,column=0, columnspan=2, sticky='new',padx=(20,20),pady=(0,0))
        self.Prev_Records_Frame.columnconfigure((0,1),weight=1)

        self.Prev_Records_Label = ctk.CTkLabel(self.Prev_Records_Frame,text="Previous Records", font=ctk.CTkFont(size=18,weight='bold',family='calibri'))
        self.Prev_Records_Label.grid(row=0,column=0,padx=(20,20),pady=(5,5),sticky='w')

        y_List = Recorded_Years()
        self.year_list = ctk.CTkComboBox(self.Prev_Records_Frame,values=y_List,variable=record_year)
        self.year_list.grid(row=0,column=1,padx=(20,0),pady=5)
        # self.year_list.set(y_List[len(y_List)-1])
        self.year_list.set("2023")

        print(y_List)

        def OPEN_RECORDS():
            with open("Exam_Time_Info.json",'r')as f:
                data = json.load(f)
                f.close()
            Row = 1 

# ****************** Clearing Space for Exam Data's ******************
            self.Record_List_Frame.destroy()
            Generate_Record_Frame()
            year = self.year_list.get()
            if year in y_List:       
                One_Year_Records = data[f'{year}']
                def block_template(data,row,col):
                    # g = ctk.CTkFrame(self.Record_List_Area)
                    g = ctk.CTkFrame(self.Record_List_Frame,fg_color='darkcyan')
                    g.grid(row=row,column=col,sticky='ew',padx=5,pady=5)
                    ctk.CTkLabel(g,text=data,font=Font).pack(pady=5)
                for i in range(len(One_Year_Records)):
                    for j in range(0,4):
                        if j==0 or j==1:
                            rec = One_Year_Records[i][j]+"-"+year
                        else:
                            rec = One_Year_Records[i][j]
                        block_template(rec,Row,j)
                    Row += 1
            else:
                cmsg(title=Dataset['Software_Name'],message="No Record Found, For the Requested Year." ,icon='warning')
                set_Empty_Condition_Image()

        self.openRecordsBtn = ctk.CTkButton(self.Prev_Records_Frame,text='OPEN Records',font=Font,fg_color='#008080',hover_color='#00aad4',command=OPEN_RECORDS)
        self.openRecordsBtn.grid(row=0,column=2,padx=(20,20),pady=10,ipady=0,sticky='ne')

        self.Record_List_Area = ctk.CTkFrame(self.rightFrame,height=500)
        self.Record_List_Area.grid(row=2,column=0,columnspan=2,sticky='news',padx=20,pady=(10,0))

        self.Record_List_Area.columnconfigure((0,1,2,3),weight=1)
        self.Record_List_Area.rowconfigure(0,weight=1)
        self.Record_List_Area.rowconfigure(1,weight=6)

        # def Generate_Record_Area():


        Txt_set = panel_Text['Record_Headings']
        for i in range(len(Txt_set)) :
            g= ctk.CTkFrame(self.Record_List_Area)
            g.grid(row=0,column=i,sticky='ew',padx=5,pady=5)
            ctk.CTkLabel(g,text=Txt_set[i],font=Font).pack(pady=5)

        def Generate_Record_Frame():
            self.Record_List_Frame = ctk.CTkScrollableFrame(self.Record_List_Area)
            self.Record_List_Frame.grid(row=1,column=0,columnspan=4,sticky='news',padx=10,pady=(0,10))
            self.Record_List_Frame.columnconfigure((0,1,2,3),weight=1)
        Generate_Record_Frame()

        def set_Empty_Condition_Image():
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Img")
            self.Record_Image = ctk.CTkImage(Image.open(os.path.join(image_path, "records_unopened.png")), size=(200, 200))
            self.Blank_Record_Label = ctk.CTkLabel(self.Record_List_Frame,text='', image=self.Record_Image)        
            self.Blank_Record_Label.grid(row=0,column=1,columnspan=2,rowspan=2 ,sticky='news', pady=(50,0))
        set_Empty_Condition_Image()
# **************   Exam Information Layout for => One Exam **************

class OneExamLayout(ctk.CTkFrame):
    def  __init__(self,  container,timeLabel,durationLabel,Hour,Minutes,ampm_var,Duration):
        super().__init__(container)

        self.ExamTimeFrame = ctk.CTkFrame(container)
        self.ExamTimeFrame.pack(anchor='n')

        self.ExamTime = ctk.CTkLabel(self.ExamTimeFrame, text=timeLabel, font=Font)
        self.ExamTime.grid(row=0,column=0,padx=(15,25))

        self.ExamHour = ctk.CTkOptionMenu(self.ExamTimeFrame, width=80, variable = Hour, values=panel_Text['Hours'])
        self.ExamHour.grid(row=0,column=1,pady=(5,5))

        self.timeSeparator = ctk.CTkLabel(self.ExamTimeFrame,text=" : ").grid(row=0,column=2)

        self.ExamMinute = ctk.CTkOptionMenu(self.ExamTimeFrame, width = 80, variable = Minutes, values = panel_Text['minutes'])
        self.ExamMinute.grid(row=0,column=3,padx=(0,20))

        self.AmRadio = ctk.CTkRadioButton(self.ExamTimeFrame,width = 80, variable = ampm_var, value = 1, text = 'AM', font = Font)
        self.AmRadio.grid(row=0,column= 4)

        self.PmRadio = ctk.CTkRadioButton(self.ExamTimeFrame, width = 80, variable = ampm_var, value = 2, text = 'PM', font = Font)
        self.PmRadio.grid(row=0,column= 5)

        self.ExamDurationFrame = ctk.CTkFrame(container,width=500)
        self.ExamDurationFrame.pack(anchor='n',fill="x",padx=(10,10),pady=(5,10))
        self.ExamDurationFrame.columnconfigure((0,1),weight=1)

        self.ExamDurationLabel = ctk.CTkLabel(self.ExamDurationFrame, text = durationLabel, font = Font)
        self.ExamDurationLabel.grid(row=0,column=0,padx=(10,10),pady=(5,5),sticky='e')
        
        self.ExamDurationInput = ctk.CTkOptionMenu(self.ExamDurationFrame, width=150, variable = Duration ,values = panel_Text['Duration_Set'] )
        self.ExamDurationInput.grid(row=0 , column=1 ,sticky='w')


# **************** GUI Controlling Functions ****************

def Recorded_Years():
    with open ("Exam_Time_Info.json","r") as f :
        data = json.load(f)
        f.close()
    return data['Year_list'] 

    


# **************** Generating Main GUI ****************

with open("conn_data.json",'w')as f:
    json.dump({"conn_Status":"0"},f)
    f.close()


# def Network_Connection():
#     print( 'connected' if connect() else 'no internet!' )
#     # global connection 
#     if connect():
#         print("Reached inside Network_connection")
#         # mainFrames.networkImage.configure(image=mainFrames.online_Image)
#         global connection
#         connection = 1
#         # curl =  "http://worldtimeapi.org/api/ip"
#         # try:
#         #     r = requests.get(curl)
#         #     received_Data = r.json()
#         #     unixTime = received_Data['unixtime']
#         # except:
#         #     unixTime = 0 
#     else:
#         print("Reached inside else Part")
#         global connection
#         connection = 0  
#         # mainFrames.networkImage .after() .configure(image=mainFrames.offline_Image)
#     time.sleep(4)
#     Network_Connection()

def check_time_order(a,b,c):
    if c>b>a :
        return True
    else:
        return False
    

def check_time_overlap(a,ua,b,ub,c,uc):
# if ua+

    pass


def Generate_Record_List():
    pass



def remove_Data(data):
        counter, DATE = 0, datetime.now()
        for i in range(0,len(data)):
                print(i)
                print(data[counter])
            # for i in range(0, len(data)) :
            #     print(i)
                saved_date = data[counter][0].split("-")
                day,month = int(saved_date[0]) , int(saved_date[1])
                print( "data['year'] = ",(data[counter]),"day = ",day,"DATE.day = ",DATE.day,"month = ",month,"DATE.month = ",DATE.month)
                if day==int(DATE.day) and month == int(DATE.month):
            #         print(data[counter])
                    data.remove(data[counter])
                    # counter
                    print("data removed = ",counter)
                else:
                    counter +=1



if __name__ == "__main__":
    mainFrames = App()
    
    Application_Information()

    # ************** Initializing Main Time Variables **************
    
    ExamDate = ctk.StringVar()

    AmPm1 = ctk.IntVar()
    AmPm2 = ctk.IntVar()
    AmPm3 = ctk.IntVar()

    ExamHour01 = ctk.StringVar()
    ExamHour02 = ctk.StringVar()
    ExamHour03 = ctk.StringVar()

    ExamMinute01 = ctk.StringVar()
    ExamMinute02 = ctk.StringVar()
    ExamMinute03 = ctk.StringVar()

    Duration_01 = ctk.StringVar()
    Duration_02 = ctk.StringVar()
    Duration_03 = ctk.StringVar()
    
#     Alarm01_Date = ctk.StringVar()
#     Alarm01_Hour = ctk.StringVar()
#     Alarm01_Minute = ctk.StringVar()
#     Alarm01_AMPM = ctk.IntVar()

#     Alarm02_Date = ctk.StringVar()
#     Alarm02_Hour = ctk.StringVar()
#     Alarm02_Minute = ctk.StringVar()
#     Alarm02_AMPM = ctk.IntVar() 

    # Contenent = ctk.StringVar()
    # City = ctk.StringVar()

    record_year = ctk.StringVar()
    # check_Info = ctk.IntVar()
    check_Info = ctk.StringVar()

    # ************** Activating Control Pannel Section **************
    controls = Control_Panel()

    # ************** Initializing Multiple Exam Slots **************
    oneExamSet = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[0]),panel_Text['row1col0'],panel_Text['row2col0'],ExamHour01,ExamMinute01,AmPm1,Duration_01)

    TwoExamSet1 = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[1]),panel_Text['e1sa'],panel_Text['ed1'],ExamHour01,ExamMinute01,AmPm1,Duration_01)
    TwoExamSet2 = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[1]),panel_Text['e2sa'],panel_Text['ed2'], ExamHour02,ExamMinute02,AmPm2,Duration_02)
    
    ThreeExamSet1 = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[2]),panel_Text['e1sa'],panel_Text['ed1'], ExamHour01,ExamMinute01,AmPm1,Duration_01)
    ThreeExamSet2 = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[2]),panel_Text['e2sa'],panel_Text['ed2'], ExamHour02,ExamMinute02,AmPm2,Duration_02)
    ThreeExamSet3 = OneExamLayout(controls.ExamSet.tab(Exam_Tab_Set[2]),panel_Text['e3sa'],panel_Text['ed3'], ExamHour03,ExamMinute03,AmPm3,Duration_03)

    entrySets = [oneExamSet,TwoExamSet1,TwoExamSet2,ThreeExamSet1,ThreeExamSet2,ThreeExamSet3]
    for i in entrySets:
        i.ExamHour.set(value=panel_Text['Hours'][0])
        i.ExamMinute.set(value=panel_Text['minutes'][0])
        i.ExamDurationInput.set(value=panel_Text['Duration_Set'][3])
        i.AmRadio.invoke()

    def lock_unlock_All(n):
        if (n==1) :  n = 0 
        else : n = 1 
        controls.ExamDateInput.configure(state=states[n])
        controls.ExamSet.configure(state=states[n])
        for i in entrySets:
            i.ExamHour.configure(state=states[n])
            i.ExamMinute.configure(state=states[n])
            i.ExamDurationInput.configure(state=states[n])
            i.AmRadio.configure(state=states[n])
            i.PmRadio.configure(state=states[n])

    def grap_all_values():
                exams = {
            "ed":ExamDate.get(),
            "hr1":ExamHour01.get(),"min1":ExamMinute01.get(),"ap1":AmPm1.get(),"edu1":Duration_01.get(),
            "hr2":ExamHour02.get(),"min2":ExamMinute02.get(),"ap2":AmPm2.get(),"edu2":Duration_02.get(),
            "hr3":ExamHour03.get(),"min3":ExamMinute03.get(),"ap3":AmPm3.get(),"edu3":Duration_03.get()
        }
                return exams
    
    def Save_Information():
        exams = grap_all_values()
        selected_Tab = controls.ExamSet.get()
        # print(selected_Tab)
        # print('exams = ', exams,Months.index('April'))
        ymd = exams['ed'].split("-")
        year = ymd[2]
        with open("Exam_Time_Info.json","r") as f:
            data = json.load(f)
            f.close()
        

# ************** Clearing Today's Previous Data **************

        remove_Data(data[year])
# ************** Data Storage Section **************
        counter, DATE = 0, datetime.now()
        for i in range(Exam_Tab_Set.index(selected_Tab)+1,0,-1):
                d = []
                if exams[f'edu{i}'] and exams[f'hr{i}'] and exams[f'min{i}'] != '' and exams[f'ap{i}']!=0:
                    # print(f"AMPM Check :0{i} = ",exams[f'ap{i}'],int(exams[f"ap{i}"])-1)
                    d.append(f"{zero(DATE.day)}-{zero(DATE.month)}")
                    ed = exams['ed'].split("-")
                    d.append(f"{ed[0]}-{zero(Months.index(ed[1])+1)}")
                    ampm = ["AM","PM"]
                    d.append(f'{exams[f"hr{i}"]}:{exams[f"min{i}"]} {ampm[int(exams[f"ap{i}"])-1]}')
                    d.append(exams[f'edu{i}'])
                    print("before writing : ",data[year])
                    data[year].insert(0,d)

        with open("Exam_Time_Info.json","w") as f:
            json.dump(data,f)
            f.close()
                # print ("Uploadaple_data = ",Uploadaple_data)
        # print(exams)
        controls.UploadBtn.configure(state=states[1])
        controls.year_list.set(year)
        controls.openRecordsBtn.invoke()

    def Validate_Data():
        exams = grap_all_values()
# ************** Getting The UNIX VALUE(S) of the Allocated Time **************
        examUnixTimes=[]
        # examDurations=[]
        selected_Tab = controls.ExamSet.get()
        ymd = exams['ed'].split("-")
        for i in range(1,Exam_Tab_Set.index(selected_Tab)+2):
            if exams[f'edu{i}'] != '' : exams[f'edu{i}'] =  panel_Text['Seconds Set'][panel_Text['Duration_Set'].index(exams[f'edu{i}'])]
            if exams[f'hr{i}'] == '12' and exams[f'ap{i}'] == 1:exams[f'hr{i}']= '0' ; print('12',exams[f'hr{i}'])
            if exams[f'ap{i}'] == 2 and exams[f'hr{i}']!='12': exams[f'hr{i}'] = int(exams[f'hr{i}'])+12 ; print('!=12 ',exams[f'hr{i}'])
            print(exams[f'hr{i}'],exams[f'min{i}'],exams)
            if exams[f'hr{i}'] and exams[f'min{i}'] != '':
                print(exams[f'hr{i}'],exams[f'min{i}'])
                examUnixTimes.append(get_Epoch(int(ymd[2]),Months.index(ymd[1])+1,int(ymd[0]),int(exams[f'hr{i}']),int(exams[f'min{i}'])))
                # Uploadaple_data[f"unixTime{i}"] = get_Epoch(int(ymd[2]),Months.index(ymd[1])+1,int(ymd[0]),int(exams[f'hr{i}']),int(exams[f'min{i}']))
                # Uploadaple_data[f"Duration{i}"] = exams[f"edu{i}"]                
# ************** Main unix time comparison **************
        # ename=['','Exam-01','Exam-02','and Exam-03']
        def timeoverlapping ():
            cmsg(title = Dataset['Software_Name'],    message = 'Exam Times are Overlapping. ',icon='warning')
        def time_order():
            cmsg(title = Dataset['Software_Name'],    message = 'Exam Times are not in order.',icon='warning')                

        d = len(examUnixTimes)
        print(examUnixTimes)
        global validation_status 
        if d == 1 : validation_status = 1 
        if d==2:           
            if examUnixTimes[0] < examUnixTimes[1] :
                if (examUnixTimes[0]+ int(exams['edu1'])) < examUnixTimes[1] :
                    validation_status = 1
                else:
                    timeoverlapping()
                    validation_status = 0
            else:
                time_order()
                validation_status = 0
        if d==3:
            if examUnixTimes[0] < examUnixTimes[1] < examUnixTimes[2] :
                if (examUnixTimes[0] + int(exams['edu1'])) < examUnixTimes[1]  or  (examUnixTimes[1] + int(exams['edu2'])) < (examUnixTimes[2]):
                    validation_status = 1
                else:
                    timeoverlapping()
                    validation_status = 0
            else:
                time_order()
                validation_status = 0


        if validation_status == 1 :
            for i in range(0,d):
                Uploadaple_data[f'UnixTime{i+1}'], Uploadaple_data[f"Duration{i+1}"]  = examUnixTimes[i] , int(exams[f'edu{i+1}'])
        lock_unlock_All(validation_status)
        print("Uploadaple_data = ", Uploadaple_data)
        return validation_status


    def year_list_addition_function():
        Exams_Data =  get_Exam_Records()
        today = datetime.now()
        current_year = str(today.year)
        if current_year not in Exams_Data['Year_list'] :
            Exams_Data['Year_list'].append(f'{current_year}')
            Exams_Data[current_year]=[]
            with open("Exam_Time_Info.json","w")as f:
                json.dump(Exams_Data,f)
                f.close() 
    year_list_addition_function()
    
    p1 = mprocess.Process(target=NewConnect)
    p1.start()

    print("Time For generating GUI : ",time.perf_counter())
    mainFrames.mainloop()
    print("After mainloop")
    p1.kill()





# **************** Last Works *************************

# UPLOAD NETWORK TIME BUTTON
# UPLOAD DATA BUTTON
# More Details Configure

                                   

# Development Notes : 
#  bad option "-sticky": must be -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side
# _tkinter.TclError: bad fill style "xy": must be none, x, y, or both
# ipadx = > inner Padding

