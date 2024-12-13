import tkinter as tk 
from tkinter import messagebox
from auth import signup, login
from PIL import Image, ImageTk
from dashboard import FundVaultDashboard
from auth import users 

def load_logo(root,logo_image_path):
    logo_image = Image.open(logo_image_path)
    logo_image = logo_image.resize((200, 200), Image.LANCZOS)  
    return ImageTk.PhotoImage(logo_image)

# Frame for centering elements
def create_centered_frame(window, background_color):
    frame = tk.Frame(window, bg=background_color)
    frame.pack(expand=True, fill="both")
    return frame

def hide_current_window(current_window):
    current_window.withdraw()  

# Validation function to restrict input length
def validate_input_input_length(max_length):
    def validate_input_value(P):
        if len(P) > max_length:
            return False  
        if P.isdigit() or P == "":  # Allow only digits
            return True
        return False
    return validate_input_value

def open_signup(root, hide_main_screen, show_main_screen):
    root.withdraw()  

    signup_window = tk.Toplevel(root)
    signup_window.title("FundVault - Sign Up")
    signup_window.geometry("400x700+568+50")
    signup_window.resizable(False, False)

    background_color = "#66b2b2"  

    logo_image_path = r"C:\Users\ADMIN\Desktop\FundVault\FundVault.png" 
    logo_image = load_logo(signup_window, logo_image_path)
    signup_window.logo_image = logo_image  # Attach to the window object
    
    logo_label = tk.Label(signup_window, image=logo_image, bg=background_color)
    logo_label.image = logo_image 
    logo_label.place(relx=0.5, y=40, anchor="center") 

    # Create the frame for content
    frame = create_centered_frame(signup_window, background_color)

    # Title
    title_label = tk.Label(frame, text="Sign Up", font=("Helvetica", 20, "bold"), bg=background_color, fg="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # First Name
    tk.Label(frame, text="First Name:", bg=background_color, fg="white").grid(row=1, column=0, sticky="w", padx=10)
    entry_first_name = tk.Entry(frame, width=30)
    entry_first_name.grid(row=1, column=1, padx=10, pady=5)

    # Last Name
    tk.Label(frame, text="Last Name:", bg=background_color, fg="white").grid(row=2, column=0, sticky="w", padx=10)
    entry_last_name = tk.Entry(frame, width=30)
    entry_last_name.grid(row=2, column=1, padx=10, pady=5)

    # Phone Number
    validate_phone_number = root.register(validate_input_input_length(11))  # Max length 11
    tk.Label(frame, text="Phone Number:", bg=background_color, fg="white").grid(row=3, column=0, sticky="w", padx=10)
    entry_phone_number = tk.Entry(frame, width=30, validate="key", validatecommand=(validate_phone_number, "%P"))
    entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

    # Email
    tk.Label(frame, text="Email:", bg=background_color, fg="white").grid(row=4, column=0, sticky="w", padx=10)
    entry_email = tk.Entry(frame, width=30)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    # PIN
    validate_pin = root.register(validate_input_input_length(4))  # Max length 4
    tk.Label(frame, text="PIN:", bg=background_color, fg="white").grid(row=5, column=0, sticky="w", padx=10)
    entry_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_pin.grid(row=5, column=1, padx=10, pady=5)

    # Re-enter PIN
    tk.Label(frame, text="Re-enter PIN:", bg=background_color, fg="white").grid(row=6, column=0, sticky="w", padx=10)
    entry_reenter_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_reenter_pin.grid(row=6, column=1, padx=10, pady=5)

    # Sign Up Button
    def handle_signup():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        phone_number = entry_phone_number.get()
        email = entry_email.get()
        pin = entry_pin.get()
        reenter_pin = entry_reenter_pin.get()

        if not first_name or not last_name or not phone_number or not email or not pin or not reenter_pin:
            messagebox.showwarning("Input Error", "Please fill out all fields.")
            return

        if len(phone_number) != 11 or not phone_number.isdigit():
            messagebox.showwarning("Input Error", "Phone number must be 11 digits.")
            return

        if len(pin) != 4 or not pin.isdigit():
            messagebox.showwarning("Input Error", "PIN must be 4 digits.")
            return

        if pin != reenter_pin:
            messagebox.showwarning("Input Error", "PINs do not match.")
            return
        
        # Call signup function (store in database or session)
        success, message = signup(first_name, last_name, phone_number, email, pin)

        if success:
            messagebox.showinfo("Success", message)
            signup_window.destroy()  
            root.deiconify()
        else:
            messagebox.showwarning("Error", message)

    signup_button = tk.Button(frame, text="Sign Up", command=handle_signup, width=20, bg="#004040", fg="white", activebackground="#00b3b3")
    signup_button.grid(row=7, column=1, pady=10)

    # Back Button
    def go_back():
        signup_window.destroy()  
        root.deiconify()

    back_button = tk.Button(frame, text="Back", command=go_back, width=10, bg="#007f7f", fg="white")
    back_button.grid(row=8, column=1, pady=5)

# Login window
def open_login(root, hide_main_screen, show_main_screen):
    root.withdraw()  

    login_window = tk.Toplevel(root)
    login_window.title("FundVault - Login")
    login_window.geometry("400x700+568+50") 
    login_window.resizable(False, False)

    background_color = "#66b2b2"  

    logo_image_path = r"C:\Users\ADMIN\Desktop\FundVault\FundVault.png" 
    logo_image = load_logo(login_window, logo_image_path)
    logo_label = tk.Label(login_window, image=logo_image, bg=background_color)
    logo_label.image = logo_image  
    logo_label.place(relx=0.5, y=40, anchor="center")

    frame = create_centered_frame(login_window, background_color)

    # Title
    title_label = tk.Label(frame, text="Login", font=("Helvetica", 20, "bold"), bg=background_color, fg="white")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)
    
    # Phone Number
    validate_phone_number = root.register(validate_input_input_length(11))  # Max length 11
    tk.Label(frame, text="Phone Number:", bg=background_color, fg="white").grid(row=1, column=0, sticky="w", padx=10)
    entry_phone_number = tk.Entry(frame, width=30, validate="key", validatecommand=(validate_phone_number, "%P"))
    entry_phone_number.grid(row=1, column=1, padx=10, pady=5)

    # PIN
    validate_pin = root.register(validate_input_input_length(4))  # Max length 4
    tk.Label(frame, text="PIN:", bg=background_color, fg="white").grid(row=2, column=0, sticky="w", padx=10)
    entry_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_pin.grid(row=2, column=1, padx=10, pady=5)

    # Login Button
    def handle_login():
        phone_number = entry_phone_number.get().strip()
        pin = entry_pin.get()

    # Validation for phone number and pin
        if len(phone_number) != 11 or not phone_number.isdigit():
            messagebox.showwarning("Input Error", "Phone number must be 11 digits.")
            return

        if len(pin) != 4 or not pin.isdigit():
            messagebox.showwarning("Input Error", "PIN must be 4 digits.")
            return

    # Attempt to log in
        success, message = login(phone_number, pin)

        if success:
            messagebox.showinfo("Success", message)
            login_window.destroy()
            root.withdraw()
        # Retrieve user information after successful login (from users list or session)
        
            user_info = None
            for user in users:
             if user['phone_number'] == phone_number:
                user_info = user
                break

            if user_info:
            # Extract first name, last name, and phone number from user data
                user_name = f"{user_info['first_name']} {user_info['last_name']}"
                user_number = user_info['phone_number']
            
            # Show dashboard window
                dashboard_window = tk.Toplevel(root)
                dashboard_window = FundVaultDashboard(dashboard_window, user_name, user_number)
                
            else:
             messagebox.showwarning("Error", "User information not found.")
            
        else:
            messagebox.showwarning("Login Error", message)

    login_button = tk.Button(frame, text="Login", command=handle_login, width=20, bg="#66b2b2", fg="white", activebackground="#00b3b3")
    login_button.grid(row=3, column=1, pady=10)

    # Back Button
    def go_back():
        login_window.destroy() 
        root.deiconify() 

    back_button = tk.Button(frame, text="Back", command=go_back, width=10, bg="#66b2b2", fg="white")
    back_button.grid(row=4, column=1, pady=5)


    def hide_main_screen(root):
        """Hides the main application screen."""
        root.withdraw()

    def show_main_screen(root):
        """Shows the main application screen."""
        root.deiconify()

    