import tkinter as tk
from tkinter import messagebox, filedialog
import json
import requests
from PIL import Image, ImageTk
from APP.Data.Info import userList, UserData, msgList

# 全局变量
root = None
register_window = None
clientUsername = ''


# 登录界面
def login_screen():
    global login_window, root
    root = tk.Tk()
    root.title("登录")
    root.geometry("300x300")  # 设置窗口大小

    # 将窗口居中显示
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 用户名输入框
    username_label = tk.Label(root, text="用户名:")
    username_label.grid(row=0, column=0, padx=10, pady=10)
    global username_entry
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # 密码输入框
    password_label = tk.Label(root, text="密码:")
    password_label.grid(row=1, column=0, padx=10, pady=10)
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    # 登录按钮
    login_button = tk.Button(root, text="登录", width=12, command=login)
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # 注册按钮
    register_button = tk.Button(root, text="注册", width=12, command=register_screen)
    register_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


# 注册界面
def register_screen():
    global register_window, root
    root.withdraw()
    register_window = tk.Tk()
    register_window.title("注册")
    register_window.geometry("300x300")  # 设置窗口大小

    # 将窗口居中显示
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()
    window_width = 300
    window_height = 300
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    register_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 用户名输入框
    username_label = tk.Label(register_window, text="用户名:")
    username_label.grid(row=0, column=0, padx=10, pady=10)
    global register_username_entry
    register_username_entry = tk.Entry(register_window)
    register_username_entry.grid(row=0, column=1, padx=10, pady=10)

    # 密码输入框
    password_label = tk.Label(register_window, text="密码:")
    password_label.grid(row=1, column=0, padx=10, pady=10)
    global register_password_entry
    register_password_entry = tk.Entry(register_window, show="*")
    register_password_entry.grid(row=1, column=1, padx=10, pady=10)

    # 确认密码输入框
    confirm_password_label = tk.Label(register_window, text="确认密码:")
    confirm_password_label.grid(row=2, column=0, padx=10, pady=10)
    global confirm_password_entry
    confirm_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

    # 注册按钮
    register_button = tk.Button(register_window, text="注册", width=12, command=register)
    register_button.grid(row=3, column=0, columnspan=2, pady=10)
    register_window.protocol("WM_DELETE_WINDOW", lambda: on_register_window_close())
    register_window.mainloop()


def on_register_window_close():
    register_window.destroy()
    login_screen()


def main_screen():
    global root, chat_display, chat_input, friend_list, friend_entry
    root = tk.Tk()
    root.title("主界面")
    root.geometry("700x500")  # 设置窗口大小

    # 将窗口居中显示
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 700
    window_height = 500
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 创建主界面
    main_frame = tk.Frame(root)
    main_frame.pack(fill="both", expand=True)

    # 创建标签显示当前用户
    user_label = tk.Label(main_frame, text=f"当前用户为——— {clientUsername}", font=("Arial", 12))
    user_label.pack(side="top", pady=10)

    # 左侧聊天框
    chat_frame = tk.Frame(main_frame, width=420, height=360)
    chat_frame.pack(side="left", fill="both", expand=True)

    # 聊天显示区域
    chat_display = tk.Text(chat_frame, width=50, height=20)
    chat_display.pack(side="top", fill="both", expand=True)

    # 消息输入区域
    input_frame = tk.Frame(chat_frame, height=80)
    input_frame.pack(side="bottom", fill="x")
    chat_input = tk.Entry(input_frame, width=50)
    chat_input.pack(side="left", fill="x", expand=True)
    send_button = tk.Button(input_frame, text="发送", command=send_message)
    send_button.pack(side="left")
    send_image_button = tk.Button(input_frame, text="发送图片", command=send_image)
    send_image_button.pack(side="right")

    # 右侧添加好友区域
    friend_frame = tk.Frame(main_frame, width=180, height=360)
    friend_frame.pack(side="right", fill="both", expand=True)

    # 好友列表
    friend_list = tk.Listbox(friend_frame, width=20, height=20)
    friend_list.pack(side="top", fill="both", expand=True)

    # 添加好友输入框和按钮
    friend_entry = tk.Entry(friend_frame, width=20)
    friend_entry.pack(side="top", pady=10)
    add_friend_button = tk.Button(friend_frame, text="添加好友", command=add_friend)
    add_friend_button.pack(side="top", pady=10)

    update_friend_list()
    root.after(100, update_friend_list)  # 每5秒钟更新一次
    root.mainloop()


# 登录功能
def login():
    # 在这里添加登录验证逻辑
    username = username_entry.get()
    password = password_entry.get()
    data = json.dumps(
        {
            'username': username,
            'password': password,
        }
    )
    r = requests.post(
        f'http://127.0.0.1:8000/api/login',
        data=data
    )
    response = r.json()
    code = response['code']
    msg = response['msg']
    if code == -1:
        print(msg)
        messagebox.showerror('Error', msg)
        root.destroy()
        login_screen()
        return
    else:
        global clientUsername
        clientUsername = username
        print("当前用户为" + clientUsername)
        root.destroy()
        main_screen()


# 注册功能
def register():
    username = register_username_entry.get()
    password = register_password_entry.get()
    confirm_password = confirm_password_entry.get()
    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "填入的信息不能为空")
        return
    data = json.dumps(
        {
            'username': username,
            'password': password,
            'confirm_password': confirm_password,
        }
    )
    r = requests.post(
        'http://127.0.0.1:8000/api/register',
        data=data
    )
    response = r.json()
    code = response['code']
    msg = response['msg']
    if code == -1:
        messagebox.showerror('Error', msg)
        register_window.withdraw()
        register_screen()
        return
    print(msg)
    register_window.destroy()
    login_screen()


def add_friend():
    friend_name = friend_entry.get()
    if friend_name:
        data = json.dumps(
            {
                'username': clientUsername,
                'friend': friend_name
            }
        )
        r = requests.post(
            'http://127.0.0.1:8000/api/addFriend',
            data=data
        )
        response = r.json()
        code = response['code']
        msg = response['msg']
        if code == -1:
            messagebox.showerror('Error', msg)
            friend_entry.delete(0, tk.END)
            return
        # 将新的好友添加到好友列表
        else:
            messagebox.showerror('Success', msg)
            friend_entry.delete(0, tk.END)
            update_friend_list()


def update_friend_list():
    print(clientUsername + '客户端刷新好友信息')
    friend_list.delete(0, tk.END)
    data = json.dumps(
        {
            "username": clientUsername
        }
    )
    r = requests.post(
        'http://127.0.0.1:8000/api/updateFriend',
        data=data
    )
    friendList = r.json()
    print(friendList)
    for friend in friendList:
        print("客户端好友列表添加好友：" + friend)
        friend_list.insert(tk.END, friend)


# 主界面
def send_message():
    message = chat_input.get()
    if message:
        # 在这里添加将消息发送到聊天框的逻辑
        chat_display.insert(tk.END, f"You: {message}\n")
        chat_input.delete(0, tk.END)


def send_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.gif")])
    if file_path:
        # 在这里添加将图片发送到聊天框的逻辑
        image = Image.open(file_path)
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        chat_display.image_create(tk.END, image=photo)
        chat_display.insert(tk.END, "\n")


if __name__ == "__main__":
    login_screen()
