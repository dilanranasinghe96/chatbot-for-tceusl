# import tkinter as tk
# from tkinter import Scrollbar, Text, Button, PhotoImage
# from chatbot import chatbot_response

# # Function to send user message and get bot response
# def send():
#     user_message = EntryBox.get("1.0", 'end-1c').strip()
#     EntryBox.delete("0.0", tk.END)
#     if user_message != '':
#         ChatLog.config(state=tk.NORMAL)
#         ChatLog.insert(tk.END, "You: " + user_message + '\n\n')
#         ChatLog.config(foreground="#1a1a1a", font=("Verdana", 12))

#         bot_response = chatbot_response(user_message)
#         ChatLog.insert(tk.END, "Bot: " + bot_response + '\n\n')
#         ChatLog.config(state=tk.DISABLED)
#         ChatLog.yview(tk.END)

# # Main window setup
# base = tk.Tk()
# base.title("Enrollment Inquiry Chatbot")
# base.geometry("500x600")
# base.resizable(width=False, height=False)
# base.configure(bg="#e6e6e6")

# # Adding a header
# header_frame = tk.Frame(base, bd=0, bg="#0073e6", height=60)
# header_frame.pack(fill="x", pady=(0, 10))
# header_label = tk.Label(header_frame, text="Trincomalee Campus Inquiry Chatbot", font=("Arial", 16, "bold"), bg="#0073e6", fg="white")
# header_label.pack(pady=10)

# # Adding a chatbot logo (optional)
# # logo = PhotoImage(file="path/to/logo.png")  # Uncomment and add your logo path here
# # logo_label = tk.Label(header_frame, image=logo, bg="#0073e6")
# # logo_label.pack(side="left", padx=20)

# # Chat log
# ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial", wrap="word", padx=10, pady=10)
# ChatLog.config(state=tk.DISABLED)

# # Scrollbar
# scrollbar = Scrollbar(base, command=ChatLog.yview)
# ChatLog['yscrollcommand'] = scrollbar.set

# # Send button
# SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5, bd=0, bg="#0073e6", activebackground="#005bb5", fg='#ffffff', command=send)

# # Entry box for user input
# EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial", padx=10, pady=10)

# # Positioning components on screen
# scrollbar.place(x=476, y=70, height=386)
# ChatLog.place(x=6, y=70, height=386, width=470)
# EntryBox.place(x=6, y=470, height=90, width=370)
# SendButton.place(x=380, y=470, height=90)

# # Running the GUI
# base.mainloop()



import tkinter as tk
from tkinter import ttk, messagebox

class EnrollmentInquiryChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Enrollment Inquiry Chatbot")
        
        # Language selection
        self.language_label = tk.Label(root, text="Please select your language:")
        self.language_label.pack(pady=10)

        self.languages = ["English", "Sinhala", "Tamil"]
        self.language_var = tk.StringVar(value=self.languages[0])
        self.language_menu = ttk.Combobox(root, textvariable=self.language_var, values=self.languages)
        self.language_menu.pack(pady=10)

        self.continue_button = tk.Button(root, text="Continue", command=self.select_campus)
        self.continue_button.pack(pady=10)

    def select_campus(self):
        # Hide language selection
        self.language_label.pack_forget()
        self.language_menu.pack_forget()
        self.continue_button.pack_forget()

        # Campus selection
        self.campus_label = tk.Label(self.root, text="Do you belong to Trincomalee Campus?")
        self.campus_label.pack(pady=10)

        self.yes_button = tk.Button(self.root, text="Yes", command=self.select_faculty)
        self.yes_button.pack(pady=10)
        
        self.no_button = tk.Button(self.root, text="No", command=self.not_trincomalee)
        self.no_button.pack(pady=10)

    def not_trincomalee(self):
        messagebox.showinfo("Info", "Please check the information for your campus.")
        self.root.quit()

    def select_faculty(self):
        # Hide campus selection
        self.campus_label.pack_forget()
        self.yes_button.pack_forget()
        self.no_button.pack_forget()

        # Faculty selection
        self.faculty_label = tk.Label(self.root, text="Please select your faculty:")
        self.faculty_label.pack(pady=10)

        self.faculties = ["Applied Science", "Communication and Business Studies", "Siddha Medicine"]
        self.faculty_var = tk.StringVar(value=self.faculties[0])
        self.faculty_menu = ttk.Combobox(root, textvariable=self.faculty_var, values=self.faculties)
        self.faculty_menu.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.select_department)
        self.next_button.pack(pady=10)

    def select_department(self):
        # Hide faculty selection
        self.faculty_label.pack_forget()
        self.faculty_menu.pack_forget()
        self.next_button.pack_forget()

        # Department selection
        self.department_label = tk.Label(self.root, text="Please select your department:")
        self.department_label.pack(pady=10)

        self.departments = {
            "Applied Science": ["Computer Science", "Physical Science"],
            "Communication and Business Studies": ["Languages and Communication Studies", "Business and Management Studies"],
            "Siddha Medicine": []
        }

        selected_faculty = self.faculty_var.get()
        self.department_var = tk.StringVar(value="")
        self.department_menu = ttk.Combobox(root, textvariable=self.department_var, values=self.departments[selected_faculty])
        self.department_menu.pack(pady=10)

        self.next_button = tk.Button(root, text="Next", command=self.select_inquiry_area)
        self.next_button.pack(pady=10)

    def select_inquiry_area(self):
        # Hide department selection
        self.department_label.pack_forget()
        self.department_menu.pack_forget()
        self.next_button.pack_forget()

        # Inquiry area selection
        self.inquiry_label = tk.Label(self.root, text="Please select the area you need help with:")
        self.inquiry_label.pack(pady=10)

        self.inquiry_areas = [
            "Hostel facilities", "Student ID", "Library registration", "Mahapola, bursary",
            "General Admission", "Sports", "Campus location (Bus routes, train)", "Canteen (foods)",
            "About lecturers, staff", "Faculties in campus", "Health Services (Medical Centre)",
            "IT Services (Wi-Fi, Computer Labs)", "Activities and Clubs in campus", "Campus map"
        ]

        self.inquiry_var = tk.StringVar(value=self.inquiry_areas[0])
        self.inquiry_menu = ttk.Combobox(root, textvariable=self.inquiry_var, values=self.inquiry_areas)
        self.inquiry_menu.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", command=self.show_summary)
        self.submit_button.pack(pady=10)

    def show_summary(self):
        # Collect user selections
        language = self.language_var.get()
        faculty = self.faculty_var.get()
        department = self.department_var.get() if self.department_var.get() else "None"
        inquiry_area = self.inquiry_var.get()

        # Show summary
        summary = f"Language: {language}\nFaculty: {faculty}\nDepartment: {department}\nInquiry Area: {inquiry_area}"
        messagebox.showinfo("Summary", summary)

        # You can add more detailed responses based on the inquiry area if needed

        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = EnrollmentInquiryChatbot(root)
    root.mainloop()
