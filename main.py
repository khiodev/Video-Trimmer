import customtkinter
from tkinter import * 
from tkinter import messagebox 
import customtkinter as ctk
from moviepy.editor import *


#clip1 = clip.subclip((0,4),(0,12))
#clip1.write_videofile('edited_clip.mp4',codec="libx264")

root = ctk.CTk()
root.geometry("400x750")
root.title("Video Trimmer")
root.minsize(400,750)
root.configure(fg_color="#181818")

global video_file
video_file = ''

def validate_number(input):
    if input.isdigit():
        return True
    elif input == "" or input == "-":
        return True
    else:
        return False

def select_video_path():
    global clip
    global video_file
    video_file = ctk.filedialog.askopenfilename(title="Select A Video",filetypes=(("Mp4 File", "*.mp4"),("All Files","*.*")))
    clip = VideoFileClip(video_file)
    merged_text = "Input: " + video_file
    input_label.configure(text=merged_text)

def select_video_output_path():
    global video_file
    global clip
    if video_file == '':
        messagebox.showerror("Error", "Please Select A Video") 
        return
        
    if beginning_cut_entry.get() == "" or end_cut_entry.get() == "" or beginning_cut_sec_entry.get() == "" or end_cut_sec_entry.get() == "":
        messagebox.showerror("Error", "Please Make Sure Start Of The Cut Or End Of The Cut Is Not Empty.") 
        return
    save_directory = ctk.filedialog.asksaveasfilename(title="Save Directory",defaultextension=".mp4",filetypes=[("Mp4 Files","*.mp4"),("All Files","*.*")])

    if save_directory != '':
        merged_text = "Output: " + save_directory
        output_label.configure(text=merged_text)
        messagebox.showinfo("Status", "Your video is being trimmed, once the video is done trimming we will notify you.")

        converted_b_min = int(beginning_cut_entry.get()) 
        converted_b_sec = int(beginning_cut_sec_entry.get())
        converted_e_min = int(end_cut_entry.get())
        converted_e_sec = int(end_cut_sec_entry.get())


        clip_trimmed = clip.subclip((converted_b_min,converted_b_sec),(converted_e_min,converted_e_sec))
        clip_trimmed.write_videofile(save_directory,codec="libx264")

        messagebox.showinfo("Status", "Your video has been trimmed!")
    else:
        messagebox.showerror("Error", "Please Select A Vaild Save Directory") 


validate_command = root.register(validate_number)

title_label = ctk.CTkLabel(root,text="Video Timmer",font=ctk.CTkFont("Bahnschrift",30,weight="bold"))
title_label.pack(pady=(15,15))

input_label = ctk.CTkLabel(root,text="Input: ",font=ctk.CTkFont("Bahnschrift",20,weight="bold"),wraplength=350)
input_label.pack(pady=(15,15))

select_file_button = ctk.CTkButton(root,text="Browse A Video",width=180,height=40,fg_color="#0f0f0f",font=ctk.CTkFont("Bahnschrift",size=20,weight="bold"),hover_color="#2f2f2f",command=select_video_path)
select_file_button.pack(pady=(15,15))

beginning_cut_label = ctk.CTkLabel(root,text="Start Of The Cut",font=ctk.CTkFont("Bahnschrift",18,weight="bold"))
beginning_cut_label.pack(pady=(15,0))

beginning_cut_min_label = ctk.CTkLabel(root,text="Minutes",font=ctk.CTkFont("Bahnschrift",15,weight="bold"))
beginning_cut_min_label.pack(pady=(0,0))

beginning_cut_entry = ctk.CTkEntry(root,placeholder_text="Minutes",width=150,height=25,font=ctk.CTkFont("Bahnschrift",weight="bold",slant='italic'), validate="key", validatecommand=(validate_command, '%P'))
beginning_cut_entry.pack(pady=(0,5))

beginning_cut_sec_label = ctk.CTkLabel(root,text="Seconds",font=ctk.CTkFont("Bahnschrift",15,weight="bold"))
beginning_cut_sec_label.pack(pady=(0,0))

beginning_cut_sec_entry = ctk.CTkEntry(root,placeholder_text="Seconds",width=150,height=25,font=ctk.CTkFont("Bahnschrift",weight="bold",slant='italic'), validate="key", validatecommand=(validate_command, '%P'))
beginning_cut_sec_entry.pack(pady=(0,10))

end_cut_label = ctk.CTkLabel(root,text="End Of The Cut",font=ctk.CTkFont("Bahnschrift",18,weight="bold"))
end_cut_label.pack(pady=(0,0))

end_cut_min_label = ctk.CTkLabel(root,text="Minutes",font=ctk.CTkFont("Bahnschrift",15,weight="bold"))
end_cut_min_label.pack(pady=(0,0))

end_cut_entry = ctk.CTkEntry(root,placeholder_text="Minutes",width=150,height=25,font=ctk.CTkFont("Bahnschrift",weight="bold",slant='italic'), validate="key", validatecommand=(validate_command, '%P'))
end_cut_entry.pack(pady=(0,5))

end_cut_sec_label = ctk.CTkLabel(root,text="Seconds",font=ctk.CTkFont("Bahnschrift",15,weight="bold"))
end_cut_sec_label.pack(pady=(0,0))

end_cut_sec_entry = ctk.CTkEntry(root,placeholder_text="Seconds",width=150,height=25,font=ctk.CTkFont("Bahnschrift",weight="bold",slant='italic'), validate="key", validatecommand=(validate_command, '%P'))
end_cut_sec_entry.pack(pady=(0,15))

trim_button = ctk.CTkButton(root,text="Trim Video",width=150,height=40,fg_color="#0f0f0f",font=ctk.CTkFont("Bahnschrift",size=20,weight="bold"),hover_color="#2f2f2f",command=select_video_output_path)
trim_button.pack(pady=(15,15))

output_label = ctk.CTkLabel(root,text="Output: ",font=ctk.CTkFont("Bahnschrift",20,weight="bold"),wraplength=350)
output_label.pack(pady=(0,15))

root.mainloop()
