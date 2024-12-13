import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime
from datetime import datetime, timedelta
import random

class FundVaultDashboard:
    def __init__(self, root, user_name, user_number, show_main_menu_callback):
        self.root = root
        self.root.title("FundVault Dashboard")
        self.root.geometry("400x700+568+50")  
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF4F4")  

        self.bg_image = Image.open("db_bg.jpg")  
        self.bg_image = self.bg_image.resize((400, 700))  
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  

        self.user_name = user_name
        self.user_number = user_number
        self.show_main_menu = show_main_menu_callback
        self.transactions = []
        self.balance = 50000.0  
        self.transaction_history = []
        self.emergency_fund_balance = 0.0
        self.goals = []
        self.deposit_history = []
        self.emergency_fund = 0.0  
   
        self.top_bar = tk.Frame(self.root, bg="#008080", height=50)
        self.top_bar.pack(fill="x", side="top")

        icon_title_frame = tk.LabelFrame(self.top_bar, bg="#008080", bd=0)  # Use a label frame
        icon_title_frame.pack(side="left", padx=10)
        
        self.title_label = tk.Label(icon_title_frame, text= "               " + "FundVault", font=("Arial", 15, "bold"), bg="#008080", fg="#20B2AA")
        self.title_label.pack(side="right", padx=5, pady=2)
    
        self.balance_frame = tk.Frame(self.root, bg="#CAE7E8", relief="solid", height=80, bd=2)
        self.balance_frame.pack(fill="x", padx=10, pady=10)
        self.balance_frame.pack_propagate(False)

        self.balance_frame.grid_columnconfigure(0, weight=1)
        self.balance_frame.grid_columnconfigure(1, weight=1)
        self.balance_frame.grid_columnconfigure(2, weight=0)

        balance_icon = tk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\PRAC\balance_icon.png")
        balance_icon = balance_icon.subsample(6, 6)
        self.balance_icon = tk.Label(self.balance_frame, image=balance_icon, bg="#CAE7E8")
        self.balance_icon.image = balance_icon
        self.balance_icon.grid(row=0, column=0, padx=5, pady=20, sticky="w")

        self.balance_label = tk.Label(self.balance_frame, text=f" ₱{self.balance:.2f}", font=("Arial", 22, "bold"), bg="#CAE7E8", fg="#333333", width=12)
        self.balance_label.grid(row=0, column=1, padx=5, pady=20, sticky="w")

        self.cash_in_button = tk.Button(self.balance_frame, text="Cash In +", font=("Arial", 8, "bold"), bg="#d3d3d3", fg="#808080", state=tk.DISABLED)
        self.cash_in_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.set_goal_frame = tk.Frame(self.root, bg="#CAE7E8", relief="solid",bd=2) 
        self.set_goal_frame.pack(fill="x", padx=10, pady=(10, 5))

        self.goal_frame = tk.Frame(self.root)
        self.goal_frame.pack()

        goal_icon = tk.PhotoImage(file=r"C:\Users\ADMIN\Desktop\PRAC\goal_icon.png")
        goal_icon = goal_icon.subsample(4, 4)
        self.set_goal_label = tk.Label(self.set_goal_frame, text="Set Goal", image=goal_icon, font=("Arial", 14, "bold"), bg="#CAE7E8", fg="#004c4c", compound="left")
        self.set_goal_label.image = goal_icon
        self.set_goal_label.pack(side="left", padx=(10, 5))

        self.add_goal_button = self.create_rounded_button(self.set_goal_frame, text="+", font=("Arial", 10), bg_color="#88C14F", fg_color="white", command=self.open_goal_popup)
        self.add_goal_button.pack(side="right", padx=10, pady=5)
        self.goal_display_frame = tk.Frame(self.root, bg="#CAE7E8")
        self.goal_display_frame.pack_forget()

        self.buttons_frame = tk.Frame(self.root, bg="#CAE7E8", relief="groove") 
        self.buttons_frame.pack(fill="x", side="bottom", padx=10, pady=10)

        self.add_deposit_button = self.create_rounded_button(self.buttons_frame,text="➕ Add Deposit",font=("Arial", 10),bg_color="#11A797",fg_color="white",command=self.open_deposit_popup)
        self.add_deposit_button.pack(side="left", expand=True, padx=3, pady=5)

        self.transaction_button = self.create_rounded_button(self.buttons_frame,text="🔍 Transaction",font=("Arial", 10),bg_color="#798CAD",fg_color="white",command=self.open_transaction_popup)
        self.transaction_button.pack(side="left", expand=True, padx=3, pady=5)

        self.emergency_button = self.create_rounded_button(self.buttons_frame,text="🚑 Emergency Fund",font=("Arial", 10),bg_color="#FB4D4C",fg_color="white",command=self.open_emergency_popup)
        self.emergency_button.pack(side="left", expand=True, padx=3, pady=5)

    #menu
        self.icon_image = Image.open("menu.png")
        self.icon_image = self.icon_image.resize((25, 25))
        self.icon_photo = ImageTk.PhotoImage(self.icon_image)
        self.icon_label = tk.Label(icon_title_frame, image=self.icon_photo, bg="#008080")
        self.icon_label.pack(side="left", padx=5, pady=2)
        self.icon_label.bind("<Button-1>", self.toggle_sidebar)
    #sidebar
        self.sidebar_frame = tk.Frame(self.root, width=200, bg="#008080", highlightthickness=2, highlightbackground="#008080")
        self.sidebar_frame.place(x=0, y=0, relheight=1) 
        self.sidebar_frame.place_forget() 

        self.user_info_frame = tk.Frame(self.sidebar_frame, bg="#008080", height=250)
        self.user_info_frame.pack(fill="x", pady=20, padx=20)

        self.user_label = tk.Label(self.user_info_frame, text=f"{self.user_name}", font=("Arial", 12, "bold"), bg="#008080", fg="white", justify="center")
        self.user_label.pack(expand=True)

        # Display phone number 
        self.phone_number_label = tk.Label(self.user_info_frame, text=f"{self.user_number}", font=("Arial", 10), bg="#008080", fg="white", justify="center")
        self.phone_number_label.pack(expand=True)

        self.separator_line = tk.Frame(self.user_info_frame, bg="white", height=2)  # Adjust height for thickness
        self.separator_line.pack(fill="x")
    # Bind toggle functionality to an event
        self.root.bind("<Control-s>", self.toggle_sidebar)

        back_arrow_button = tk.Button(self.sidebar_frame, text="⇚", font=("Arial", 16, "bold"), bg="#66b2b2", fg="white", bd=0, command=self.close_sidebar)
        back_arrow_button.place(relx=0.9, rely=0.5, anchor="w") 
    #send money
        self.send_money_button = tk.Button(self.sidebar_frame, text="💱 Send Cash", font=("Arial", 10, "bold"), bg="#008080", fg="white", bd=0, command=self.toggle_send_money)
        self.send_money_button.pack(fill="x", pady=5, padx=20)
    # Notifications Button
        self.notifications_button = tk.Button(self.sidebar_frame, text="🔔 Notifications", font=("Arial", 10, "bold"), bg="#008080", fg="white", bd=0, command=self.toggle_notifications)
        self.notifications_button.pack(fill="x", pady=5, padx=20)
    # Log Out Button (placed at the very bottom)
        self.logout_button = tk.Button(self.sidebar_frame, text="🚪 Log Out", font=("Arial", 10, "bold"), bg="#FB4D4C", fg="white", bd=0, command=self.logout)
        self.logout_button.pack(fill="x", pady=5, padx=20, side="bottom")
     # Show reminders when the dashboard opens
        self.show_reminder()

    def show_reminder(self):
        """Display a reminder message box when the dashboard opens."""
        reminder_message = (
            "Welcome to FundVault!\n"
            "\nReminders: \n"
            "\n1. Only two goals can be held at a time to avoid financial overload.\n"
            "2. Saving for achievable goals helps you stay on track and avoid frustrations.\n"
            "3. Avoid impulsive spending and always think about your financial future.\n"
            "\n" + " " * 17 + '"Your Financial Goals, Our Priority"'
        )
        messagebox.showinfo("Important Reminders", reminder_message)
        
    #this is for rounded button
    def create_rounded_button(self, parent, text, bg_color, fg_color, command, width=120, height=25, font=("Arial", 10, "bold")):
            """Creates a custom rounded button with customizable font."""
            canvas = tk.Canvas(parent, width=width, height=height, bg=parent['bg'], highlightthickness=0)
            canvas.pack_propagate(0)  # Prevent resizing to fit content

            radius = height // 2  # Calculate radius based on button height
            canvas.create_arc(0, 0, radius * 2, radius * 2, start=90, extent=90, fill=bg_color, outline=bg_color)
            canvas.create_arc(width - radius * 2, 0, width, radius * 2, start=0, extent=90, fill=bg_color, outline=bg_color)
            canvas.create_arc(0, height - radius * 2, radius * 2, height, start=180, extent=90, fill=bg_color, outline=bg_color)
            canvas.create_arc(width - radius * 2, height - radius * 2, width, height, start=270, extent=90, fill=bg_color, outline=bg_color)
            canvas.create_rectangle(radius, 0, width - radius, height, fill=bg_color, outline=bg_color)
            canvas.create_rectangle(0, radius, width, height - radius, fill=bg_color, outline=bg_color)
            canvas.create_text(width // 2, height // 2, text=text, fill=fg_color, font=font)

    # Bind click event
            canvas.bind("<Button-1>", lambda e: command())
            canvas.pack(side="left", padx=3, pady=5) 
            return canvas
    
    def toggle_send_money(self):
        """Show or hide send money related frames."""
        # Hide other UI elements if necessary
        self.hide_other_frames()
        self.show_send_money_balance()

    def hide_other_frames(self):
        """Hide other frames or widgets on the dashboard."""
        pass  

    def show_send_money_balance(self):
        """Show the user's balance at the top for send money."""
        self.send_money_frame = tk.Frame(self.root, bg="#CAE7E8")
        self.send_money_frame.pack(fill="x", pady=10, padx=10)

        balance_label = tk.Label(self.send_money_frame, text=f"Your Balance: ₱{self.balance:.2f}",font=("Arial", 14), bg="#CAE7E8", fg="black")
        balance_label.pack(pady=10)

        self.amount_label = tk.Label(self.send_money_frame, text="Enter Amount to Send:",font=("Arial", 12), bg="#CAE7E8", fg="black")
        self.amount_label.pack(pady=10)

        self.amount_entry = tk.Entry(self.send_money_frame, font=("Arial", 12))
        self.amount_entry.pack(pady=10)

        button_frame = tk.Frame(self.send_money_frame, bg="#CAE7E8")
        button_frame.pack(pady=10)

        back_button = tk.Button(button_frame, text="Back", font=("Arial", 12), bg="#FB4D4C", fg="white", command=self.go_back) 
        back_button.pack(side="left", padx=10)

        next_button = tk.Button(button_frame, text="Next", font=("Arial", 12), bg="#11A797", fg="white", command=self.enter_phone_number)
        next_button.pack(side="left", padx=10)

    def go_back(self):
        self.send_money_frame.destroy() 
        self.toggle_sidebar() 

    def enter_phone_number(self):
        """Prompt the user to enter the recipient's phone number."""
        try:
            self.amount_to_send = float(self.amount_entry.get().strip())  # Set as an instance variable
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")
            return
    # Check if the amount is less than or equal to the balance
        if self.amount_to_send <= 0 or self.amount_to_send > self.balance:
            messagebox.showerror("Input Error", "Amount must be less than or equal to your balance.")
            return
        self.send_money_frame.pack_forget()

        self.phone_number_frame = tk.Frame(self.root, bg="#CAE7E8")
        self.phone_number_frame.pack(fill="x", pady=10, padx=10)

        phone_label = tk.Label(self.phone_number_frame, text="Enter Recipient's Phone Number:",font=("Arial", 12), bg="#CAE7E8", fg="black")
        phone_label.pack(pady=10)

    # Phone number entry with validation for 11 digits
        self.phone_entry = tk.Entry(self.phone_number_frame, font=("Arial", 12), validate="key",validatecommand=(self.root.register(self.validate_phone_number), "%P"))
        self.phone_entry.pack(pady=10)

        confirm_button = tk.Button(self.phone_number_frame, text="Next",font=("Arial", 12), bg="#11A797", fg="white",command=self.show_confirmation)
        confirm_button.pack(pady=10)

    def generate_random_name(self):
        """Generate a random name for the recipient."""
        first_names = ['John', 'Jane', 'Alex', 'Mary', 'Chris', 'Patricia', 'Michael', 'Linda', 'David', 'Sarah']
        last_names = ['Smith', 'Johnson', 'Brown', 'Williams', 'Jones', 'Miller', 'Davis', 'Garcia', 'Martinez', 'Hernandez']
        
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        
        self.recipient_name = f"{first_name} {last_name}"
        return self.recipient_name

    def show_confirmation(self):
        """Show a confirmation dialog before proceeding with the transaction."""
        recipient_number = self.phone_entry.get().strip()

        # Ensure recipient's phone number is exactly 11 digits
        if len(recipient_number) != 11:
            messagebox.showerror("Input Error", "Phone number must be exactly 11 digits.")
            return

        # Generate random recipient name
        recipient_name = self.generate_random_name()

        # Ask for confirmation
        confirmation = messagebox.askyesno(
            "Confirm Transaction",f"Are you sure you want to send ₱{self.amount_to_send:.2f} to {recipient_name} ({recipient_number})?")

        if confirmation:
            self.confirm_send(recipient_number, recipient_name)
        else:
            self.phone_number_frame.pack_forget()
            self.enter_phone_number()  # Reopen the phone number input screen

    def confirm_send(self, recipient_number, recipient_name):
        """Confirm sending the money."""
    # Deduct the amount from the balance
        self.balance -= self.amount_to_send
        self.update_balance_display()

        self.transaction_history.append({
        "type": "send_money",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": self.amount_to_send,
        "recipient_name": recipient_name,
        "recipient_number": recipient_number
    })
        self.phone_number_frame.pack_forget()
        self.show_receipt(recipient_number, recipient_name, self.amount_to_send)

    def validate_phone_number(self, input_value):
        """Validate the phone number input to allow only numbers and limit to 11 digits."""
        # Allow only digits and ensure the length is 11
        if input_value.isdigit() and len(input_value) <= 11:
            return True
        elif input_value == "":  # Allow clearing the input field
            return True
        return False
    
    def process_send_money(self, recipient_number, amount_to_send):
        """Process the send money transaction and update the balance."""
        self.balance -= amount_to_send
        self.update_balance_display()

        self.show_receipt(recipient_number, amount_to_send)

    def update_balance_display(self):
        self.balance_label.config(text=f"Balance: ₱{self.balance:,.2f}")


    def show_receipt(self, recipient_number, recipient_name, amount_to_send):
        """Show the receipt of the send money transaction."""
        receipt_popup = tk.Toplevel(self.root)
        receipt_popup.title("Receipt")
    
    # Set the size of the popup window
        window_width = 400
        window_height = 300
    
    # Center the window on the screen
        screen_width = receipt_popup.winfo_screenwidth()
        screen_height = receipt_popup.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
    
        receipt_popup.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
        receipt_popup.configure(bg="#CAE7E8")
    
    # Frame for content with padding to ensure content isn't touching the edges
        frame = tk.Frame(receipt_popup, bg="#CAE7E8", padx=20, pady=20)  # Added padding for left and right
        frame.pack(fill="both", expand=True)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add labels with appropriate spacing
        receipt_label1 = tk.Label(frame, text="Successfully Paid To", justify="center", font=("Arial", 16, "bold"), bg="#CAE7E8", fg="black")
        receipt_label1.pack(pady=(5, 5))

        receipt_label2 = tk.Label(frame, text=recipient_name, justify="center", font=("Arial", 14, "bold"), fg="darkgreen", bg="#CAE7E8")
        receipt_label2.pack(pady=(0, 5))

        receipt_label3 = tk.Label(frame, text=f"Phone Number: {recipient_number}", justify="center", font=("Arial", 10), bg="#CAE7E8", fg="black")
        receipt_label3.pack(pady=(0, 5))

        receipt_label4 = tk.Label(frame, text=f"Amount Sent: ₱{amount_to_send:.2f}", justify="center", font=("Arial", 10), bg="#CAE7E8", fg="black")
        receipt_label4.pack(pady=(0, 10))

    # Display current date and time (no extra space before it)
        receipt_label5 = tk.Label(frame, text=f"Date & Time: {current_time}", font=("Arial", 8), bg="#CAE7E8", fg="black")
        receipt_label5.pack(pady=(0, 10))

    # Button frame to hold the buttons and center them
        button_frame = tk.Frame(frame, bg="#CAE7E8")
        button_frame.pack(pady=10)

    # Save button and Close button placed side by side
        save_button = tk.Button(button_frame, text="Save Receipt", font=("Arial", 12), bg="#798CAD", fg="white", 
                            command=lambda: self.save_receipt(recipient_number, amount_to_send, recipient_name))
        save_button.pack(side="left", padx=10)

        close_button = tk.Button(button_frame, text="Close", font=("Arial", 12), bg="#FB4D4C", fg="white", command=receipt_popup.destroy)
        close_button.pack(side="left", padx=10)

    def save_receipt(self, recipient_number, amount_to_cash_out, random_name):
        """Save the receipt details to a file and show a notification."""
        try:
        # Save the receipt details to a file using UTF-8 encoding
            with open("receipt.txt", "w", encoding="utf-8") as file:
                file.write("Successfully Paid To\n")
                file.write(f"Name: {random_name}\n")
                file.write(f"Phone Number: {recipient_number}\n")
                file.write(f"Amount Sent: ₱{amount_to_cash_out:.2f}\n")
                file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Show a success notification
            messagebox.showinfo("Receipt Saved", "The receipt has been saved.")
        except Exception as e:
        # Show an error notification in case of issues
            messagebox.showerror("Save Error", f"Failed to save receipt: {e}")


    def toggle_notifications(self):
        """Show or hide notifications frame."""
        if hasattr(self, 'notifications_frame'):
            if self.notifications_frame.winfo_ismapped():
                self.notifications_frame.pack_forget()  # Hide the notifications frame
            else:
                self.notifications_frame.pack_forget()  # Remove any existing frame before re-packing
                self.notifications_frame.pack(pady=(10, 10), padx=10, fill="x")  # Repack with smaller vertical space
        else:
            self.notifications_frame = tk.Frame(self.root, bg="#66b2b2")
            tk.Label(self.notifications_frame, text="No New Notifications", bg="#66b2b2", font=("Arial", 10)).pack(pady=5)
            self.create_back_button(self.notifications_frame)  # Place the "Back" button below
            self.notifications_frame.pack(pady=(10, 10), padx=10, fill="x")  # Set appropriate padding

    def create_back_button(self, frame_to_hide):
        """Create a Back button to hide the current frame and show the main screen."""
        back_button = tk.Button(frame_to_hide, text="Back", font=("Arial", 8), bg="#FB4D4C", fg="white", command=self.on_back_button_click)
        back_button.pack(pady=10)

    def on_back_button_click(self):
        """Hide the current frame and return to the main screen."""
        # Close any popup or hide the current frame
        if hasattr(self, 'notifications_frame') and self.notifications_frame.winfo_ismapped():
            self.notifications_frame.pack_forget()
        if hasattr(self, 'inboxes_frame') and self.inboxes_frame.winfo_ismapped():
            self.inboxes_frame.pack_forget()

    def logout(self):
        confirmed = tk.messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirmed:
            self.root.destroy()  # Close the dashboard
            self.show_main_menu()  # Trigger the callback to go back to main menu
        
    def close_sidebar(self):
        """Hide the sidebar."""
        self.sidebar_frame.place_forget()
    def populate_frame(self, frame, items):
        """Populate a frame with items."""
        for item in items:
            tk.Label(frame, text=item, font=("Arial", 10), bg="#444444", fg="white", wraplength=180, justify="left", anchor="w").pack(fill="x", pady=2)
    def toggle_sidebar(self, event=None):
        """Toggle the visibility of the sidebar."""
        if self.sidebar_frame.winfo_ismapped():
            self.sidebar_frame.place_forget()  # Hide the sidebar
        else:
            self.sidebar_frame.place(x=0, y=0, relheight=1)  #Show the sidebar
    def update_balance_display(self):
        """Update the main balance label with the current balance."""
        self.main_balance_label.config(text=f"Main Balance: ₱{self.balance:.2f}")  

    def open_emergency_popup(self):
        """Open a popup to manage the emergency fund."""
        self.emergency_popup = tk.Toplevel(self.root)
        self.emergency_popup.overrideredirect(True)
        self.emergency_popup.configure(bg="#66b2b2")
    # Set size and position
        popup_width, popup_height = 400, 400
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        x, y = (screen_width - popup_width) // 2 + 8, (screen_height - popup_height) // 2
        self.emergency_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")
    # Emergency Fund Balance Display
        self.emergency_fund_label = tk.Label(self.emergency_popup,text=f"Emergency Fund: ₱{self.emergency_fund_balance:.2f}",font=("Arial", 14, "bold"),bg="#66b2b2", fg="white")
        self.emergency_fund_label.pack(pady=20)

        tk.Button(self.emergency_popup,text="Add Funds",font=("Arial", 12),bg="#11A797", fg="white",command=self.open_add_fund_popup).pack(pady=10)
        button_frame = tk.Frame(self.emergency_popup, bg="#66b2b2")
        button_frame.pack(pady=20)

        back_button = tk.Button(button_frame,text="Back",font=("Arial", 12),bg="#FB4D4C", fg="white",command=self.close_emergency_popup)
        back_button.pack(side="left", padx=10)
        cash_out_button = tk.Button(button_frame,text="Cash Out",font=("Arial", 12),bg="#798CAD", fg="white",command=self.open_send_amount_popup)
        cash_out_button.pack(side="left", padx=10)

    def close_emergency_popup(self):
        self.emergency_popup.destroy()

    def open_add_fund_popup(self):
        self.add_fund_popup = tk.Toplevel(self.root)
        self.add_fund_popup.overrideredirect(True)
        self.add_fund_popup.configure(bg="#66b2b2")

        popup_width, popup_height = 400, 300
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()

    # Adjust the x-coordinate to shift the window to the right
        x, y = (screen_width - popup_width) // 2 + 8, (screen_height - popup_height) // 2  # 50 pixels to the right
    
        self.add_fund_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        tk.Label(self.add_fund_popup, text="Amount to Add:", font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=10)
        self.add_fund_entry = tk.Entry(self.add_fund_popup, font=("Arial", 12))
        self.add_fund_entry.pack(pady=10)

        button_frame = tk.Frame(self.add_fund_popup, bg="#66b2b2")
        button_frame.pack(side="bottom", pady=10, fill="x")  # Align at the bottom

        # Back button
        back_button = tk.Button(button_frame, text="Back", font=("Arial", 12), bg="#FB4D4C", fg="white", command=self.close_add_fund_popup)
        back_button.pack(side="left", padx=20, pady=10)  # Add padding to the right side

        add_fund_button = tk.Button(button_frame, text="Add Funds", font=("Arial", 12), bg="#11A797", fg="white", command=self.add_funds)
        add_fund_button.pack(side="left", padx=20, pady=10)  # Add padding to the left side

    # Center the buttons by using the place method
        button_frame.place(relx=0.5, rely=1, anchor="s")  # Align button_frame to the bottom center
        add_fund_button.pack(side="left")
        back_button.pack(side="left")

    def close_add_fund_popup(self):
        self.add_fund_popup.destroy()  # Close the current popup
        self.root.deiconify()  # Show the main window again
    def add_funds(self):
        """Add funds to the emergency fund and update the balance."""
        try:
            amount_to_add = float(self.add_fund_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")
            return

        if amount_to_add <= 0:
            messagebox.showerror("Input Error", "Amount must be greater than zero.")
            return

        if amount_to_add > self.balance:
            messagebox.showerror("Insufficient Balance", "You do not have enough balance to add this amount.")
            return

    # Deduct from main balance and add to emergency fund
        self.balance -= amount_to_add
        self.emergency_fund_balance += amount_to_add
        self.transaction_history.append({
        "type": "emergency_deposit",
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount_to_add,
        "details": "Added to Emergency Fund"
    })

        self.update_balance_display()
        self.emergency_fund_label.config(text=f"Emergency Fund: ₱{self.emergency_fund_balance:.2f}")

    # Clear the input field
        self.add_fund_entry.delete(0, tk.END)

    # Show success message and close the window
        messagebox.showinfo("Success", f"₱{amount_to_add:.2f} has been added to your emergency fund.")
        self.add_fund_popup.destroy()  # Close the Add Funds window

    
    def validate_phone_number(self, input_value):
        """Only allow input of 11 digits."""
        if len(input_value) <= 11 and input_value.isdigit():
            return True
        return False

    def open_send_amount_popup(self):
        """Open popup for sending amount to a recipient."""
        self.send_amount_popup = tk.Toplevel(self.root)
        self.send_amount_popup.overrideredirect(True)  # Remove the top bar
        self.send_amount_popup.configure(bg="#66b2b2")

    # Set size and position
        popup_width, popup_height = 400, 300
        screen_width, screen_height = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        x, y = (screen_width - popup_width) // 2 + 8, (screen_height - popup_height) // 2
        self.send_amount_popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        tk.Label(self.send_amount_popup, text="Amount to Send:", font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=10)
        self.send_amount_entry = tk.Entry(self.send_amount_popup, font=("Arial", 12))
        self.send_amount_entry.pack(pady=10)

    # Recipient Number
        vcmd = (self.root.register(self.validate_phone_number), "%P")  # Validate command
        tk.Label(self.send_amount_popup, text="Phone Number:", font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=10)

        self.recipient_number_entry = tk.Entry(self.send_amount_popup, font=("Arial", 12), validate="key", validatecommand=vcmd)
        self.recipient_number_entry.pack(pady=10)
    # Create a frame for the buttons to place them horizontally at the bottom and center them
        button_frame = tk.Frame(self.send_amount_popup, bg="#66b2b2")
        button_frame.pack(side="bottom", pady=10, fill="x")  # Align at the bottom

    # Cancel button
        cancel_button = tk.Button(button_frame, text="Cancel", font=("Arial", 12), bg="#FB4D4C", fg="white", command=self.close_send_amount_popup)
        cancel_button.pack(side="left", padx=20, pady=10)  # Add padding to the left side

    # Send button
        send_button = tk.Button(button_frame, text="Send", font=("Arial", 12), bg="#11A797", fg="white", command=self.confirm_send_amount)
        send_button.pack(side="left", padx=20, pady=10)  # Add padding to the right side

    # Center the buttons by using the place method
        button_frame.place(relx=0.5, rely=1, anchor="s")  # Align button_frame to the bottom center
        cancel_button.pack(side="left")
        send_button.pack(side="left")
    
    def close_send_amount_popup(self):
        """Close the send amount popup."""
        self.send_amount_popup.destroy()


    def confirm_send_amount(self):
        """Confirm the send amount and deduct from the emergency fund."""
        try:
            amount_to_send = float(self.send_amount_entry.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for the amount to send.")
            return
        recipient_number = self.recipient_number_entry.get().strip()

    # Validate recipient number. it's should be 11 digits.
        if len(recipient_number) != 11 or not recipient_number.isdigit():
            messagebox.showerror("Input Error", "Please enter a valid 11-digit phone number.")
            return
        if amount_to_send <= 0:
            messagebox.showerror("Input Error", "Amount must be greater than zero.")
            return
    # Check if the emergency fund balance is sufficient
        if amount_to_send > self.emergency_fund_balance:
            messagebox.showerror("Insufficient Funds", "You do not have enough balance in your emergency fund.")
            return
    # Get a random name for the recipient
        recipient_name = self.get_random_name()
    # Confirm the transaction
        confirmation = messagebox.askyesno("Confirm Send",f"Are you sure you want to send ₱{amount_to_send:.2f} to {recipient_name} ({recipient_number})?")
        if confirmation:
        # Deduct the amount from the emergency fund
            self.emergency_fund_balance -= amount_to_send
        # Record the transaction
            self.transaction_history.append({
            "type": "emergency_cashout",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "amount": amount_to_send,
            "recipient_name": recipient_name,
            "recipient_number": recipient_number,
            "details": "Cash-out from Emergency Fund"
        })
            self.print_receipt(recipient_name, recipient_number, amount_to_send)
        # Update UI
            if hasattr(self, 'emergency_fund_label'):  # Update only if the label exists
                self.emergency_fund_label.config(text=f"Emergency Fund: ₱{self.emergency_fund_balance:.2f}")

            self.send_amount_popup.destroy()
            self.close_emergency_popup()

            messagebox.showinfo( "Success",f"₱{amount_to_send:.2f} has been sent to {recipient_name} ({recipient_number}).")

    def get_random_name(self):
        """Generate a random recipient name."""
        names = ["John Doe", "Jane Smith", "Michael Johnson", "Emily Davis", "Daniel Lee"]
        return random.choice(names)

    def print_receipt(self, recipient_name, recipient_number, amount_to_send):
        """Show a receipt popup after sending money from the emergency fund."""
    # Ensure amount_to_send is a float
        try:
            amount_to_send = float(amount_to_send)
            print(f"Amount to Send: ₱{amount_to_send}")  # Debugging output
        except ValueError:
            messagebox.showerror("Error", "Invalid amount format.")
            return

    # Create a new popup window for the receipt
        receipt_popup = tk.Toplevel(self.root)
        receipt_popup.title("Emergency Fund Receipt")
    
    # Set the size of the popup window
        window_width = 400
        window_height = 300
    
    # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
    
        receipt_popup.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")
        receipt_popup.configure(bg="#CAE7E8")
    
    # Frame for content with padding to ensure content isn't touching the edges
        frame = tk.Frame(receipt_popup, bg="#CAE7E8", padx=20, pady=20)  # Added padding for left and right
        frame.pack(fill="both", expand=True)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add labels with appropriate spacing
        receipt_label1 = tk.Label(frame, text="Successfully Sent to", justify="center", font=("Arial", 16, "bold"), bg="#CAE7E8", fg="black")
        receipt_label1.pack(pady=(5, 5))

        receipt_label2 = tk.Label(frame, text=recipient_name, justify="center", font=("Arial", 14, "bold"), fg="darkgreen", bg="#CAE7E8")
        receipt_label2.pack(pady=(0, 5))

        receipt_label3 = tk.Label(frame, text=f"Phone Number: {recipient_number}", justify="center", font=("Arial", 10), bg="#CAE7E8", fg="black")
        receipt_label3.pack(pady=(0, 5))

        receipt_label4 = tk.Label(frame, text=f"Amount Sent: ₱{amount_to_send:.2f}", justify="center", font=("Arial", 10), bg="#CAE7E8", fg="black")
        receipt_label4.pack(pady=(0, 10))

    # Display current date and time (no extra space before it)
        receipt_label5 = tk.Label(frame, text=f"Date & Time: {current_time}", font=("Arial", 8), bg="#CAE7E8", fg="black")
        receipt_label5.pack(pady=(0, 10))

    # Button frame to hold the buttons and center them
        button_frame = tk.Frame(frame, bg="#CAE7E8")
        button_frame.pack(pady=10)

    # Save button and Close button placed side by side
        save_button = tk.Button(button_frame, text="Save Receipt", font=("Arial", 12), bg="#11A797", fg="white", 
                            command=lambda: self.save_receipt(recipient_name, recipient_number, amount_to_send))
        save_button.pack(side="left", padx=10)

        close_button = tk.Button(button_frame, text="Close", font=("Arial", 12), bg="#FB4D4C", fg="white", command=receipt_popup.destroy)
        close_button.pack(side="left", padx=10)

    def save_receipt(self, recipient_name, recipient_number, amount_to_send):
        """Save the receipt to a text file."""
    # Debugging: print the values being passed
        print(f"Saving receipt for {recipient_name} ({recipient_number}), Amount: ₱{amount_to_send:.2f}")

    # Ensure amount_to_send is a float before saving
        try:
            amount_to_send = float(amount_to_send)
            print(f"Converted Amount to Float: ₱{amount_to_send}")  # Debugging output
        except ValueError:
            messagebox.showerror("Error", "Invalid amount format.")
            return

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the receipt string
        receipt = f"--- Transaction Receipt ---\n"
        receipt += f"Recipient: {recipient_name} ({recipient_number})\n"
        receipt += f"Amount Sent: ₱{amount_to_send:.2f}\n"
        receipt += f"Date and Time: {current_time}\n"
    
    # Debugging: check receipt content
        print("Receipt Content:\n", receipt)

    # Test writing to a file, confirm that it works independently
        try:
            test_file_path = "test_receipt.txt"  # Use a relative path first
            with open(test_file_path, "a", encoding="utf-8") as test_file:
                test_file.write("Test: File is being written\n")
            print(f"Test file written at {test_file_path}.")
        except Exception as e:
            print(f"Error during test file write: {e}")
            messagebox.showerror("Error", "There was an issue with file writing. Check permissions.")
            return

    # Try to save the receipt to the file
        try:
            receipt_file_path = "emergency_transaction_receipt.txt"  # Make sure this path is correct
            with open(receipt_file_path, "a", encoding="utf-8") as file:
                file.write(receipt + "\n")
            print(f"Receipt saved successfully at {receipt_file_path}.")
        except Exception as e:
            print(f"Error saving receipt: {e}")
            messagebox.showerror("Error", f"There was an issue saving the receipt: {e}")

    messagebox.showinfo("Success", "Receipt has been saved successfully.")



    def close_emergency_popup(self):
        self.emergency_popup.destroy()

    def validate_number_format(self, number, length=11):
        """Validate number format for digits and specific length."""
        return number.isdigit() and len(number) == length

    def create_goal_frame(self, goal_info):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("darkblue.Horizontal.TProgressbar", troughcolor="#CAE7E8", background="#00008B")  

        goal_frame = tk.Frame(self.goal_display_frame, relief="solid", bg="#CAE7E8")  
        goal_frame.pack(fill="x", pady=5, padx=10)

    # Store the frame reference in goal_info for later removal
        goal_info["frame"] = goal_frame

        progress_container = tk.Frame(goal_frame, bg="#CAE7E8")
        progress_container.pack(fill="x", padx=10, pady=5)

        goal_label = tk.Label(progress_container, text=f"{goal_info['name']} - ₱{goal_info['current_amount']:.2f} / ₱{goal_info['target_amount']} ",font=("Arial", 10), bg="#CAE7E8", anchor="w")
        goal_label.pack(side="top", padx=5, pady=5)

        progress_bar = ttk.Progressbar(progress_container, orient="horizontal", length=300, mode="determinate",style="darkblue.Horizontal.TProgressbar")  # Apply the custom style
        progress_bar["value"] = goal_info["current_amount"]
        progress_bar["maximum"] = goal_info["target_amount"]
        progress_bar.pack(pady=5)

        bottom_frame = tk.Frame(progress_container, bg="#CAE7E8")
        bottom_frame.pack(fill="x", pady=5)

        target_date_label = tk.Label(bottom_frame, text=f"Target Date: {goal_info['target_date']}", font=("Arial", 8), bg="#CAE7E8", anchor="e")
        target_date_label.pack(side="left", padx=10, pady=5)

    # Button that looks locked if the goal is not yet met
        self.cash_out_button = tk.Button(bottom_frame, text="Cash Out", font=("Arial", 8), bg="#ff5722", fg="white",state=tk.DISABLED, command=lambda: self.cash_out_goal(goal_info))
        self.cash_out_button.pack(side="right", padx=10, pady=5)
        if goal_info["current_amount"] < goal_info["target_amount"]:
            self.cash_out_button.config(bg="#d3d3d3", fg="#808080")  # Grey button to look disabled
    # Store the widgets in the goal_info for future updates
        goal_info["progress_bar"] = progress_bar
        goal_info["label"] = goal_label
        goal_info["target_date_label"] = target_date_label
        goal_info["cash_out_button"] = self.cash_out_button

        self.goal_display_frame.update_idletasks()
        self.goal_display_frame.pack_propagate(True)
        self.show_goal_frame()

    def update_goal_display(self):
        """Refresh the goal display based on the current goals."""
        # Clear all existing frames
        for widget in self.goal_display_frame.winfo_children():
            widget.destroy()
    # Rebuild UI for each goal in the current list
        for goal in self.goals:
            self.create_goal_frame(goal)
            for goal in self.goals:
                if goal["current_amount"] >= goal["target_amount"]:
                    if "cash_out_button" in goal:
                        goal["cash_out_button"].config(state=tk.NORMAL, bg="#FF5722", fg="white")

    def enable_all_buttons(self):
        """Enable all cash-out buttons."""
        for goal in self.goals:
            if "frame" in goal:
                for widget in goal["frame"].winfo_children():
                    if isinstance(widget, tk.Button):
                        widget.config(state=tk.NORMAL)

    def open_goal_popup(self):
        """Open a popup to add a new goal, but only if two or fewer goals are set."""
        if len(self.goals) >= 2:
        # Show an alert or message that only two goals are allowed
            tk.messagebox.showinfo("Limit Reached", "You can only set two goals at a time.")
            return
        self.root.withdraw()
        self.goal_popup = tk.Toplevel(self.root)
        self.goal_popup.title("Set New Goal")
        self.goal_popup.geometry("400x700+568+50")
        self.goal_popup.configure(bg="#66b2b2")  

        title_label = tk.Label(self.goal_popup, text="Set a New Goal", font=("Arial", 16, "bold"), bg="#66b2b2", fg="white")
        title_label.pack(pady=20)

        tk.Label(self.goal_popup, text="Goal Name:", font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=5)
        self.goal_name_entry = tk.Entry(self.goal_popup, font=("Arial", 12))
        self.goal_name_entry.pack(pady=5)

    # Target Amount input with validation
        tk.Label(self.goal_popup, text="Target Amount:", font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=5)
        validate_command = (self.goal_popup.register(self.validate_numeric_input), "%P")
        self.target_amount_entry = tk.Entry(self.goal_popup, font=("Arial", 12), validate="key", validatecommand=validate_command)
        self.target_amount_entry.pack(pady=5)

        tk.Label(self.goal_popup,text="Target Date:",font=("Arial", 12),bg="#66b2b2",fg="white",).pack(pady=(10, 0)) 

        self.calendar = Calendar(self.goal_popup, selectmode='day',date_pattern='yyyy-mm-dd',background="#00637C", foreground="white", font=("Arial", 12),borderwidth=2,
        normalbackground="white", normalforeground="black",selectbackground="#5F9E8F", selectforeground="white",headersbackground="#66b2b2", headersforeground="white",weekendbackground="#FB4D4C",weekendforeground="white")
        self.calendar.pack(pady=5)

        button_frame = tk.Frame(self.goal_popup, bg="#66b2b2")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Save Goal", font=("Arial", 12), bg="#11A797", fg="white", command=self.save_goal).pack(side="left", padx=10)
        tk.Button(button_frame, text="Reset", font=("Arial", 12), bg="#798CAD", fg="white", command=self.reset_goal_inputs).pack(side="left", padx=10)
        tk.Button(button_frame, text="Back", font=("Arial", 12), bg="#FB4D4C", fg="white", command=self.close_goal_popup).pack(side="left", padx=10)
            
    def save_goal(self):
        """Save the new goal into the system.""" 
        goal_name = self.goal_name_entry.get()
        target_amount = self.target_amount_entry.get()
        target_date = self.calendar.get_date()
        self.root.deiconify()

        if not goal_name or not target_amount:
            messagebox.showwarning("Input Error", "Please complete all fields")
            self.root.withdraw()
            return
        try:
            target_amount = float(target_amount)
        except ValueError:
            messagebox.showerror("Input Error", "Target amount must be a number")
            return
        
        if datetime.strptime(target_date, '%Y-%m-%d') < datetime.today():
            messagebox.showerror("Input Error", "Target date cannot be in the past.")
            self.root.withdraw()
            return
        goal_info = {
            "name": goal_name,
            "target_amount": target_amount,
            "current_amount": 0,
            "target_date": target_date,
            "deposit_history": []  # Initialize deposit history for this goal
        }
        self.goals.append(goal_info)

        self.create_goal_frame(goal_info)
        self.show_goal_frame()

        # Display the goal display frame after a goal is saved
        self.goal_display_frame.grid_rowconfigure(len(self.goals)-1, weight=1)
        self.goal_popup.destroy()

    def reset_goal_inputs(self):
        """Clear all inputs in the Set New Goal popup."""
        self.goal_name_entry.delete(0, tk.END)  
        self.target_amount_entry.delete(0, tk.END)  
        self.calendar.selection_set(datetime.today()) 

    def validate_numeric_input(self, value):
        """Allow only numeric input in the entry field."""
        if value.isdigit() or value == "": 
            return True
        return False

    def close_goal_popup(self):
        """Close the goal popup and return to the main window."""
        self.goal_popup.destroy()
        self.root.deiconify()

    def show_goal_frame(self):
        self.goal_display_frame.pack(fill="x", padx=10, pady=(5, 10))

    def validate_phone_number(self, value):
        return value.isdigit() and len(value) <= 11

    def cash_out_goal(self, goal_info):
        if hasattr(self, 'cash_out_in_progress') and self.cash_out_in_progress:
            messagebox.showwarning("Cash Out In Progress", "A goal is already being cashed out. Please wait.")
            return
        self.cash_out_in_progress = True  # Set the flag to indicate cash-out in progress
        today = datetime.today()
        target_date = datetime.strptime(goal_info["target_date"], '%Y-%m-%d')
    # Check if current amount >= target amount
        if goal_info["current_amount"] >= goal_info["target_amount"]:
            if today < target_date:
                self.open_phone_number_popup(goal_info)
            else:
            # Prompt confirmation first
                confirm = messagebox.confirmation(
                "Confirm Cash Out",
                f"Are you sure you want to send ₱{goal_info['target_amount']} to {goal_info['recipient_name']}?")
                if confirm:  # If the user clicks 'Yes'
                # Proceed with generating the receipt and finalize the cash-out
                    receipt = f"""
                Receipt:
                Amount: ₱{goal_info['target_amount']}
                Recipient Name: {goal_info['recipient_name']}
                Target Date: {goal_info['target_date']}
                Status: Successful
                """
                # Show the receipt
                    messagebox.showinfo("Transaction Complete", receipt)
                
                # Finalize the cash-out (disable button, reset amount, etc.)
                    self.finalize_cash_out(goal_info)
                else:  # If user clicks 'No'
                    messagebox.showinfo("Transaction Canceled", "Cash out was not completed.")
        else:
        # Handle case where goal amount is not reached
            if today >= target_date:
                extended_date = target_date + timedelta(days=5)
                goal_info["target_date"] = extended_date.strftime('%Y-%m-%d')
                messagebox.showinfo(
                "Target Date Extended",
                f"The target amount is not yet reached. The target date has been extended to {extended_date.strftime('%Y-%m-%d')}."
            )
            else:
            # If it's not yet the target date, show a warning
                messagebox.showwarning(
                "Goal Not Reached",
                "You cannot cash out before reaching the target amount."
            )

        self.cash_out_in_progress = False  # Reset the flag after completion

    def finalize_cash_out(self, goal_info):
        """Handles the final steps for cashing out a goal."""
    # Remove the goal data from the list
        if goal_info in self.goals:
            self.goals.remove(goal_info)

    # Destroy the frame associated with the goal
        if "frame" in goal_info and goal_info["frame"].winfo_exists():
            goal_info["frame"].destroy()

    # Refresh the goal display to reflect changes
        self.update_goal_display()
        messagebox.showinfo("Cash Out Successful", f"₱{goal_info['target_amount']} has been sent successfully.")

    def open_phone_number_popup(self, goal_info):
        self.cash_out_window = tk.Toplevel(self.root)
        self.cash_out_window.title("Enter Recipient's Phone Number")
        self.cash_out_window.geometry("400x700+568+50")
        self.cash_out_window.configure(bg="#66b2b2")

        tk.Label(self.cash_out_window, text=f"₱{goal_info['target_amount']:.2f}", font=("Arial", 18, "bold"), bg="#66b2b2", fg="white").pack(pady=20)
        tk.Label(self.cash_out_window, text="Enter Recipient's Phone Number:",font=("Arial", 12), bg="#66b2b2", fg="white").pack(pady=10)
        self.recipient_phone_entry = tk.Entry(self.cash_out_window, font=("Arial", 12))

    # Validate phone number input
        validate_command = (self.cash_out_window.register(self.validate_phone_number), "%P")
        self.recipient_phone_entry.config(validate="key", validatecommand=validate_command)
        self.recipient_phone_entry.pack(pady=10)
    
        button_frame = tk.Frame(self.cash_out_window, bg="#66b2b2")
        button_frame.pack(pady=20)
        tk.Button(button_frame, text="Proceed to Cash Out", font=("Arial", 12), bg="#11A797", fg="white",command=lambda: self.process_cash_out(goal_info)).pack(side="left", padx=10)
        tk.Button(button_frame, text="Cancel", font=("Arial", 12), bg="#FB4D4C", fg="white",command=self.cash_out_window.destroy).pack(side="left", padx=10)

    def open_cash_goal_confirmation(self, goal_info):
        recipient_number = self.recipient_phone_entry.get().strip()
        if not recipient_number:
            messagebox.showerror("Input Error", "Please enter a recipient's phone number.")
            return
        if len(recipient_number) != 11:
            messagebox.showerror("Input Error", "Phone number must be exactly 11 digits.")
            return

        amount_to_cash_out = goal_info["current_amount"]

        confirmation_popup = tk.Toplevel(self.root)
        confirmation_popup.title("Confirm Cash Out")
        confirmation_popup.geometry("400x300+568+50")
        confirmation_popup.configure(bg="#66b2b2")

        recipient_name = self.generate_random_name()  # Randomly generated recipient name

        tk.Label(confirmation_popup,text=f"Are you sure you want to send ₱{amount_to_cash_out:.2f} to {recipient_name} ({recipient_number})?",font=("Arial", 14, "bold"),bg="#66b2b2",fg="white").pack(pady=20)

        button_frame = tk.Frame(confirmation_popup, bg="#66b2b2")
        button_frame.pack(pady=20)

        tk.Button(button_frame,text="Confirm",font=("Arial", 12),bg="#11A797",fg="white",command=lambda: self.process_cash_out(goal_info, recipient_name, recipient_number, amount_to_cash_out, confirmation_popup)).pack(side="left", padx=10)
        tk.Button(button_frame,text="Cancel",font=("Arial", 12),bg="#FB4D4C",fg="white",command=confirmation_popup.destroy).pack(side="left", padx=10)

    def validate_phone_number(self, input_value):
        """Ensure that only digits are allowed and the phone number is at most 11 digits."""
        if input_value.isdigit() and len(input_value) <= 11:   # Check if the input is a digit and its length is <= 11
            return True
        elif input_value == "":  # Allow for empty string (deletion)
            return True
        else:
            return False

    def process_cash_out(self, goal_info):
        """Process the cash-out after entering recipient's phone number."""
        recipient_number = self.recipient_phone_entry.get().strip()

        if not recipient_number:
            messagebox.showerror("Input Error", "Please enter a recipient's phone number.")
            return
        if len(recipient_number) != 11:  # Phone number must be 11 digits
            messagebox.showerror("Input Error", "Phone number must be exactly 11 digits.")
            return

        amount_to_cash_out = goal_info["current_amount"]
        random_name = self.generate_random_name()  # Generate a random name
    # Confirm with the user before proceeding
        confirm = messagebox.askyesno(
        "Confirm Cash Out",
        f"Are you sure you want to send ₱{amount_to_cash_out:.2f} to {random_name} ({recipient_number})?"
    )
        if not confirm:  # If the user clicks "No"
            messagebox.showinfo("Transaction Canceled", "Cash out was not completed.")
            return
        
            # Record the cash-out in transaction history
        transaction = {
        "type": "cash_out",
        "amount": amount_to_cash_out,
        "recipient_name": random_name,
        "recipient_number": recipient_number,
        "goal_name": goal_info["name"],
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
        self.transaction_history.append(transaction)
        
        self.cash_out_window.destroy()
        self.open_receipt_popup(recipient_number, amount_to_cash_out, random_name)
    # Disable the cash-out button and reset the goal amount
        goal_info["cash_out_button"]["state"] = tk.DISABLED
        goal_info["current_amount"] = 0  # Reset goal amount to 0

        self.goals.remove(goal_info)
    # Destroy the goal frame completely
        if "frame" in goal_info:
            goal_info["frame"].destroy()  # Destroy the entire frame

    # Optionally, you can update the UI or perform any other actions related to removing the goal.
        self.update_goal_display()
        self.finalize_cash_out(goal_info)

    def open_receipt_popup(self, recipient_number, amount_to_cash_out, random_name):
        """Display the receipt popup after cashing out."""
        receipt_window = tk.Toplevel(self.root)
        receipt_window.title("Receipt")
        receipt_window.geometry("300x200")
        receipt_window.resizable(False, False)
        receipt_window.configure(bg="#66b2b2") 

        window_width = 300
        window_height = 200
        screen_width = receipt_window.winfo_screenwidth()
        screen_height = receipt_window.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        receipt_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        receipt_label1 = tk.Label(receipt_window,text="Successfully Paid To",justify="center",font=("Arial", 16, "bold"),bg="#66b2b2", fg="white")
        receipt_label1.pack(pady=(20, 5)) 
        receipt_label2 = tk.Label(receipt_window,text=random_name,justify="center",font=("Arial", 14, "bold"),bg="#66b2b2", fg="darkgreen"  )
        receipt_label2.pack(pady=(0, 5))  
        receipt_label3 = tk.Label(receipt_window,text=f"Phone Number: {recipient_number}",justify="center",font=("Arial", 10),bg="#66b2b2", fg="white")
        receipt_label3.pack(pady=(0, 5))
        receipt_label4 = tk.Label(receipt_window,text=f"Amount Due: ₱{amount_to_cash_out:.2f}",justify="center",font=("Arial", 10), bg="#66b2b2", fg="white")
        receipt_label4.pack(pady=(0, 20))
        # Frame for buttons
        button_frame = tk.Frame((receipt_window), bg="#66b2b2")
        button_frame.pack(pady=(10, 0))

    # Save Button
        save_button = tk.Button(button_frame, text="Save", command=lambda: self.save_receipt(recipient_number, amount_to_cash_out, random_name), font=("Arial", 10))
        save_button.pack(side="left", padx=10)

    # Close Button
        close_button = tk.Button(button_frame, text="Close", command=receipt_window.destroy, font=("Arial", 10))
        close_button.pack(side="left", padx=10)

    def save_receipt(self, recipient_number, amount_to_cash_out, random_name):
        """Save the receipt details to a file and show a notification."""
        try:
        # Save the receipt details to a file using UTF-8 encoding
         with open("receipt.txt", "w", encoding="utf-8") as file:
            file.write("Successfully Paid To\n")
            file.write(f"Name: {random_name}\n")
            file.write(f"Phone Number: {recipient_number}\n")
            file.write(f"Amount Due: ₱{amount_to_cash_out:.2f}\n")

            messagebox.showinfo("Save Receipt", "Receipt saved successfully!")
        except Exception as e:
            messagebox.showerror("Save Receipt", f"Failed to save receipt: {e}")

        self.update_goal_display()

    def open_deposit_popup(self):
        """Open a popup to add a deposit.""" 
        if not self.goals:
            messagebox.showwarning("No Goals", "Please set a goal first.")
            self.root.deiconify()
            return
 
        self.deposit_popup = tk.Toplevel(self.root)
        self.deposit_popup.title("Add Deposit")
        self.deposit_popup.configure(bg="#66b2b2")

    # Calculate the position to center the popup on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 400  # Width of the popup window
        window_height = 250  # Height of the popup window

    # Calculate position
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.deposit_popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Add widgets to the popup
        tk.Label(self.deposit_popup, text="Select Goal:", bg="#66b2b2").pack(pady=5)
        self.goal_var = tk.StringVar(value=self.goals[0]['name'])
        self.goal_menu = ttk.Combobox(self.deposit_popup, textvariable=self.goal_var, values=[goal['name'] for goal in self.goals])
        self.goal_menu.pack(pady=5)

        tk.Label(self.deposit_popup, text="Deposit Amount:", bg="#66b2b2").pack(pady=5)
        self.deposit_amount_entry = tk.Entry(self.deposit_popup)
        self.deposit_amount_entry.pack(pady=5)

        tk.Button(self.deposit_popup, text="Add Deposit", bg= "#11A797", command=self.add_deposit).pack(pady=5)
        tk.Button(self.deposit_popup, text="Back", bg="#798CAD", command=self.close_deposit_popup).pack( pady=10)

    def close_deposit_popup(self):
        """Close the deposit popup and return to the main window."""
        self.deposit_popup.destroy()  
        self.root.deiconify()  

    def validate_numeric_input(self, input_value):
        """Ensure that only digits (and optionally a decimal point) are allowed."""
        if input_value == "": 
            return True
        elif input_value.isdigit():  # Allow digits
            return True
        elif input_value.count('.') == 1 and input_value.replace('.', '').isdigit():  # Allow one decimal point
            return True
        else:
            return False

    def add_deposit(self):
        """Add a deposit to the selected goal."""
        deposit_amount = self.deposit_amount_entry.get()

        try:
          deposit_amount = float(deposit_amount)
        except ValueError:
            messagebox.showerror("Input Error", "Deposit amount must be a number")
            return

        selected_goal_name = self.goal_var.get()
        selected_goal = next(goal for goal in self.goals if goal["name"] == selected_goal_name)

    # Check if deposit amount exceeds balance before proceeding
        if deposit_amount > self.balance:
            messagebox.showerror("Insufficient Balance", "You do not have enough balance to make this deposit.")
            return

    # Check if the deposit will exceed the target amount
        if selected_goal["current_amount"] + deposit_amount > selected_goal["target_amount"]:
            messagebox.showerror(
            "Deposit Exceeds Target",
            f"The deposit exceeds the target amount for {selected_goal_name}. You can only deposit up to ₱{selected_goal['target_amount'] - selected_goal['current_amount']:.2f} more."
        )
            return
        
        # Save deposit history with current time and date
        deposit_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format: yr-mm-dd hh:mm:ss
        selected_goal["deposit_history"].append({
            "date": deposit_time,
            "amount": deposit_amount
        })

    # Update the goal's current amount and progress bar
        selected_goal["current_amount"] += deposit_amount
        selected_goal["progress_bar"]["value"] = selected_goal["current_amount"]
        selected_goal["label"]["text"] = f"{selected_goal['name']} - ₱{selected_goal['current_amount']:.2f} /  ₱{selected_goal['target_amount']:.2f} "

    # Deduct the deposit from the user's balance after updating the goal
        self.balance -= deposit_amount
        self.update_balance_display()  # Update the balance display to reflect the deduction

    # Enable Cash Out Button once goal is reached
        if selected_goal["current_amount"] >= selected_goal["target_amount"]:
            selected_goal["cash_out_button"]["state"] = tk.NORMAL  # Enable the button
            selected_goal["cash_out_button"].config(bg="#ff5722", fg="white")  # Change color to show it's enabled
            messagebox.showinfo("Goal Reached", f"Congratulations! You can now cash out your goal '{selected_goal['name']}'.")

            # Add transaction to the history
        self.transaction_history.append({
        "type": "add_deposit",
        "goal_name": selected_goal_name,
        "amount": deposit_amount,
        "date": deposit_time
    })

        self.deposit_popup.destroy()  
        messagebox.showinfo("Success", "Deposit added successfully.")
        self.root.deiconify()  
        
    def save_deposit(self, goal_info):
        """Save the deposit amount and update the goal."""
        deposit_amount = self.deposit_amount_entry.get()

        try:
            deposit_amount = float(deposit_amount)
        except ValueError:
            messagebox.showerror("Input Error", "Deposit amount must be a number.")
            return

        if deposit_amount <= 0:
            messagebox.showerror("Input Error", "Deposit amount must be greater than zero.")
            return

        # Deduct from balance
        if deposit_amount > self.balance:
            messagebox.showerror("Insufficient Balance", "You do not have enough balance to make this deposit.")
            return

        self.balance -= deposit_amount
        self.update_balance_display()

        # Update goal's current amount
        goal_name = self.goal_dropdown.get()
        for goal in self.goals:
            if goal['name'] == goal_name:
                goal['current_amount'] += deposit_amount
                goal['deposit_history'].append(deposit_amount)

        messagebox.showinfo("Deposit Successful", f"₱{deposit_amount:.2f} has been deposited into {goal_name}.")
        self.deposit_popup.destroy()

    def update_balance_display(self):
        """Update the balance label and ensure no resizing occurs."""
        self.balance_label.config(text=f" ₱{self.balance:.2f}")
   
    def close_deposit_popup(self):
        """Close the deposit popup and return to the main window."""
        self.deposit_popup.destroy()  
        self.root.deiconify() 

    def open_transaction_popup(self):
        """Open a popup to show transaction history."""
        self.root.withdraw()  
        self.transaction_popup = tk.Toplevel(self.root)
        self.transaction_popup.title("Transaction History")
        self.transaction_popup.geometry("400x700+568+50")
        self.transaction_popup.configure(bg="#66b2b2")

        content_frame = tk.Frame(self.transaction_popup, bg="#66b2b2")
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)

        history_found = False  #check if any transaction history exists

        for transaction in self.transaction_history:
            history_found = True

            if transaction["type"] == "send_money":
                transaction_text = (
                f"You successfully sent ₱{transaction['amount']:.2f} to "
                f"{transaction['recipient_name']} ({transaction['recipient_number']})."
            )
            elif transaction["type"] == "add_deposit":
                transaction_text = (
                f"₱{transaction['amount']:.2f} was successfully deposited to the goal '{transaction['goal_name']}'."
            )
            elif transaction["type"] == "cash_out":
                transaction_text = (
                f"You successfully cashed out ₱{transaction['amount']:.2f} from your Goal "
                f"to {transaction['recipient_name']} ({transaction['recipient_number']})."
            )

            elif transaction["type"] == "emergency_deposit":
                transaction_text = (
                f"You successfully added ₱{transaction['amount']:.2f} to your Emergency Fund."
            )
            elif transaction["type"] == "emergency_cashout":
                transaction_text = (
                f"You successfully cashed out ₱{transaction['amount']:.2f} from your Emergency Fund "
                f"to {transaction['recipient_name']} ({transaction['recipient_number']})."
            )
            else:
                transaction_text = "Unknown transaction type."
        # Add the details text
            tk.Label(content_frame,text=transaction_text,bg="#66b2b2",font=("Arial", 10),anchor="w", wraplength=380).pack(fill="x", pady=(5, 0))
            tk.Label(content_frame, text=f"Date: {transaction['date']}", bg="#66b2b2", font=("Arial", 8, "italic"), fg="gray",anchor="w", justify="left",wraplength=380).pack(fill="x", pady=(0, 10))

            tk.Frame(content_frame,bg="black",height=2,width=380).pack(fill="x", pady=5)

    # If no transactions are found
        if not history_found:
            tk.Label(content_frame,text="No Transactions Yet",bg="#66b2b2",font=("Arial", 10, "italic"),fg="gray").pack(pady=20)

        back_button = tk.Button(self.transaction_popup,text="Back",font=("Arial", 12),bg="#798CAD",fg="white",command=self.close_transaction_popup)
        back_button.pack(pady=10)

    def close_transaction_popup(self):
        """Close the transaction popup and return to the main window."""
        self.transaction_popup.destroy()  
        self.root.deiconify()
