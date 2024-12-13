import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from dashboard import FundVaultDashboard
from database import register_user, check_login
    
def load_logo_safe(root, logo_image_path):
    try:
        logo_image = Image.open(logo_image_path)
        logo_image = logo_image.resize((200, 200), Image.LANCZOS)
        return ImageTk.PhotoImage(logo_image)
    except FileNotFoundError:
        messagebox.showerror("Error", "Logo image not found. Please check the file path.")
        return None

def create_centered_frame(window, background_color):
    frame = tk.Frame(window, bg=background_color)
    frame.pack(expand=True, fill="both")
    return frame

def create_footer(root):
    footer = tk.Frame(root, bg="#004040", height=30)
    footer.pack(side="bottom", fill="x")
    footer_label = tk.Label(footer, text="Your Secure Vault", bg="#004040", fg="#66b2b2", font=("Helvetica", 10))
    footer_label.pack(pady=5)

def validate_input_input_length(max_length):
    def validate_input_value(P):
        if len(P) > max_length:
            return False
        if P.isdigit() or P == "":
            return True
        return False
    return validate_input_value

def open_signup(root):
    root.withdraw()
    signup_window = tk.Toplevel(root)
    signup_window.title("FundVault - Sign Up")
    signup_window.geometry("400x700+568+50")
    signup_window.resizable(False, False)
    background_color = "#66b2b2"
    signup_window.configure(bg=background_color)


    logo_image_path = r"C:\Users\ADMIN\Desktop\FundVault\FundVault.png"
    logo_image = load_logo_safe(signup_window, logo_image_path)
    if logo_image:
        logo_label = tk.Label(signup_window, image=logo_image, bg=background_color)
        logo_label.image = logo_image
        logo_label.pack(pady=(20, 10))  # Add padding for better spacing

    frame = tk.Frame(signup_window, bg=background_color)
    frame.pack(expand=True, fill="both")

    # Add form elements here (same as before)
    tk.Label(frame, text="First Name:", bg=background_color, fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_first_name = tk.Entry(frame, width=30)
    entry_first_name.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Last Name:", bg=background_color, fg="white").grid(row=2, column=0, sticky="w", padx=10)
    entry_last_name = tk.Entry(frame, width=30)
    entry_last_name.grid(row=2, column=1, padx=10, pady=5)

    validate_phone_number = root.register(validate_input_input_length(11))
    tk.Label(frame, text="Phone Number:", bg=background_color, fg="white").grid(row=3, column=0, sticky="w", padx=10)
    entry_phone_number = tk.Entry(frame, width=30, validate="key", validatecommand=(validate_phone_number, "%P"))
    entry_phone_number.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(frame, text="Email:", bg=background_color, fg="white").grid(row=4, column=0, sticky="w", padx=10)
    entry_email = tk.Entry(frame, width=30)
    entry_email.grid(row=4, column=1, padx=10, pady=5)

    validate_pin = root.register(validate_input_input_length(4))
    tk.Label(frame, text="PIN:", bg=background_color, fg="white").grid(row=5, column=0, sticky="w", padx=10)
    entry_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_pin.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(frame, text="Re-enter PIN:", bg=background_color, fg="white").grid(row=6, column=0, sticky="w", padx=10)
    entry_reenter_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_reenter_pin.grid(row=6, column=1, padx=10, pady=5)

    def handle_signup():
        first_name = entry_first_name.get()
        last_name = entry_last_name.get()
        phone_number = entry_phone_number.get()
        email = entry_email.get()
        pin = entry_pin.get()
        reenter_pin = entry_reenter_pin.get()

        if not all([first_name, last_name, phone_number, email, pin, reenter_pin]):
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

        success, message = register_user(first_name, last_name, phone_number, email, pin)
        if success:
            messagebox.showinfo("Success", message)
            signup_window.destroy()
            root.deiconify()
        else:
            messagebox.showwarning("Error", message)
    tk.Button(frame, text="Sign Up", command=handle_signup, width=20, bg="#1b8c8c", fg="white").grid(row=7, column=1, pady=10)

    def go_back():
        signup_window.destroy()
        root.deiconify()
    tk.Button(frame, text="Back", command=go_back, width=10, bg="#007f7f", fg="white").grid(row=8, column=1, pady=5)

def open_login(root):
    root.withdraw()
    login_window = tk.Toplevel(root)
    login_window.title("FundVault - Login")
    login_window.geometry("400x700+568+50")
    login_window.resizable(False, False)
    background_color = "#66b2b2"
    login_window.configure(bg=background_color)

    logo_image_path = r"C:\Users\ADMIN\Desktop\FundVault\FundVault.png"
    logo_image = load_logo_safe(login_window, logo_image_path)
    if logo_image:
        logo_label = tk.Label(login_window, image=logo_image, bg=background_color)
        logo_label.image = logo_image
        logo_label.pack(pady=(20, 10))  # Add padding for better spacing

    frame = tk.Frame(login_window, bg=background_color)
    frame.pack(expand=True, fill="both")

    # Phone number field with validation
    validate_phone_number = root.register(validate_input_input_length(11))
    tk.Label(frame, text="Phone Number:", bg=background_color, fg="white").grid(row=0, column=0, sticky="w", padx=10, pady=5)
    entry_phone_number = tk.Entry(frame, width=30, validate="key", validatecommand=(validate_phone_number, "%P"))
    entry_phone_number.grid(row=0, column=1, padx=10, pady=5)

    # PIN field with validation
    validate_pin = root.register(validate_input_input_length(4))
    tk.Label(frame, text="PIN:", bg=background_color, fg="white").grid(row=2, column=0, sticky="w", padx=10)
    entry_pin = tk.Entry(frame, show="*", width=30, validate="key", validatecommand=(validate_pin, "%P"))
    entry_pin.grid(row=2, column=1, padx=10, pady=5)

    def handle_login():
        phone_number = entry_phone_number.get().strip()
        pin = entry_pin.get()

        if len(phone_number) != 11 or not phone_number.isdigit():
            messagebox.showwarning("Input Error", "Phone number must be 11 digits.")
            return

        if len(pin) != 4 or not pin.isdigit():
            messagebox.showwarning("Input Error", "PIN must be 4 digits.")
            return

        success, result = check_login(phone_number, pin)
        if success:
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy()
            dashboard_window = tk.Toplevel(root)
            FundVaultDashboard(dashboard_window, f"{result['first_name']} {result['last_name']}", result['phone_number'], show_main_menu_callback=go_back)
        else:
            messagebox.showwarning("Login Error", result)

    tk.Button(frame, text="Login", command=handle_login, width=20, bg="#1b8c8c", fg="white").grid(row=3, column=1, pady=10)

    def go_back():
        login_window.destroy()
        root.deiconify()

    tk.Button(frame, text="Back", command=go_back, width=10, bg="#007f7f", fg="white").grid(row=4, column=1, pady=5)


def load_logo_safe(root, logo_image_path):
    try:
        logo_image = Image.open(logo_image_path)
        logo_image = logo_image.resize((200, 200), Image.LANCZOS)
        return ImageTk.PhotoImage(logo_image)
    except FileNotFoundError:
        messagebox.showerror("Error", f"Logo file not found: {logo_image_path}")
        return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load logo: {str(e)}")
        return None

def show_main_menu():
    main_menu = tk.Frame(root, bg="#66b2b2")
    main_menu.pack(expand=True, fill="both")

    tk.Label(main_menu, text="FundVault", font=("Helvetica", 24, "bold"), bg="#66b2b2", fg="#004040").pack(pady=(50, 10))

    logo_image_path = r"C:\Users\ADMIN\Desktop\FundVault\FundVault.png"
    logo_image = load_logo_safe(root, logo_image_path)
    if logo_image:
        logo_label = tk.Label(main_menu, image=logo_image, bg="#66b2b2")
        logo_label.image = logo_image 
        logo_label.pack(pady=20) 

    tk.Button(main_menu, text="Sign Up", width=20, bg="#1b8c8c", fg="white", command=lambda: open_signup(root)).pack(pady=10)
    tk.Button(main_menu, text="Login", width=20, bg="#1b8c8c", fg="white", command=lambda: open_login(root)).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("FundVault")
    root.geometry("400x700+568+50")
    root.resizable(False, False)

    create_footer(root)  # Add footer
    show_main_menu()
    root.mainloop()
