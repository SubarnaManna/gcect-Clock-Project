import  tkinter  as  tk
import customtkinter as ctk
from  tkinter  import  ttk
import json

# class OneExamLayout(ctk.CTkFrame):
    # def __init__(self, master: any, width: int = 200, height: int = 200, corner_radius: Optional[Union[int, str]] = None, border_width: Optional[Union[int, str]] = None, bg_color: Union[str, Tuple[str, str]] = "transparent", fg_color: Optional[Union[str, Tuple[str, str]]] = None, border_color: Optional[Union[str, Tuple[str, str]]] = None, background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        # super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

with open('Tests/Databases/app_Static_info.json','r') as f:
    Dataset = json.load(f)
    f.close()
panel_Text=Dataset['Control Pannel']
Font = ('calibri',16,'bold')



class OneExamLayout(ctk.CTkFrame):
    def  __init__(self,  container):
        super().__init__(container)

        options  =  {'padx':  5,  'pady':  5}
        AmPm1 = tk.IntVar()
        AmPm2 = tk.IntVar()
        AmPm3 = tk.IntVar()

        ExamHour01 = tk.StringVar()
        ExamHour02 = tk.StringVar()
        ExamHour03 = tk.StringVar()

        ExamMinute01 = tk.StringVar()
        ExamMinute02 = tk.StringVar()
        ExamMinute03 = tk.StringVar()

        Duration_01 = tk.StringVar()
        Duration_02 = tk.StringVar()
        Duration_03 = tk.StringVar()
#   Exam Information Set for => One Exam Day
        self.ExamTimeFrame = ctk.CTkFrame(container)
        self.ExamTimeFrame.pack(anchor='n')

        self.ExamTime = ctk.CTkLabel(self.ExamTimeFrame, text = panel_Text['row1col0'], font=Font)
        self.ExamTime.grid(row=0,column=0,padx=(15,25))

        self.ExamHour = ctk.CTkOptionMenu(self.ExamTimeFrame, width=80, values = panel_Text['Hours'])
        self.ExamHour.grid(row=0,column=1,pady=(5,5))

        self.timeSeparator = ctk.CTkLabel(self.ExamTimeFrame,text=" : ").grid(row=0,column=2)

        self.ExamMinute = ctk.CTkOptionMenu(self.ExamTimeFrame, width = 80, values = panel_Text['minutes'])
        self.ExamMinute.grid(row=0,column=3,padx=(0,20))

        self.AmRadio = ctk.CTkRadioButton(self.ExamTimeFrame,width = 80, variable = AmPm1, value = 1, text = 'AM', font = Font)
        self.AmRadio.grid(row=0,column= 4)

        self.PmRadio = ctk.CTkRadioButton(self.ExamTimeFrame, width = 80, variable = AmPm1, value = 2, text = 'PM', font = Font)
        self.PmRadio.grid(row=0,column= 5)

        self.ExamDurationFrame = ctk.CTkFrame(container,width=500)
        self.ExamDurationFrame.pack(anchor='n',fill="x",padx=(10,10),pady=(10,10))
        self.ExamDurationFrame.columnconfigure((0,1),weight=1)

        self.ExamDurationLabel = ctk.CTkLabel(self.ExamDurationFrame, text = panel_Text['row2col0'], font = Font)
        self.ExamDurationLabel.grid(row=0,column=0,padx=(10,10),pady=(10,10),sticky='e')
        
        self.ExamDurationInput = ctk.CTkOptionMenu(self.ExamDurationFrame, width=150, variable = Duration_01 ,values = panel_Text['Duration_Set'] )
        self.ExamDurationInput.grid(row=0 , column=1 ,sticky='w')
