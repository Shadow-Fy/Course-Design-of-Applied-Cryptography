import base64
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import json
import requests
from PIL import Image, ImageTk
from APP.Data.Info import userList, UserData
from APP.Tool import ImageByte, SM4, SM3
from APP.Tool.ImageByte import byte2image
import time

# 全局变量
root = None
register_window = None
clientUsername = ''
clientUserData = None


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
    global root, chat_display, chat_input, friend_list, friend_entry, friend_option_menu, selected_friend, selected_friend_label
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

    # 好友选择下拉框
    selected_friend = tk.StringVar()
    friend_option_menu = ttk.OptionMenu(input_frame, selected_friend, '', *[])
    friend_option_menu.pack(side="left", padx=5)

    # 创建标签显示选择的好友
    selected_friend_label = tk.Label(input_frame, text='', font=("Arial", 10), width=10)
    selected_friend_label.pack(side="left", padx=5)

    chat_input = tk.Entry(input_frame, width=50)
    chat_input.pack(side="left", fill="x", expand=True)

    send_button = tk.Button(input_frame, text="发送", command=send_message)
    send_button.pack(side="left", padx=5)

    send_image_button = tk.Button(input_frame, text="发送图片", command=send_image)
    send_image_button.pack(side="right", padx=5)

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
    update_UserData_msg()
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
        f'http://192.168.137.1:8000/api/login',
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
        update_userData()
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
        'http://192.168.137.1:8000/api/register',
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
            'http://192.168.137.1:8000/api/addFriend',
            data=data
        )
        response = r.json()
        code = response['code']
        msg = response['msg']
        privateKey = response['privateKey']
        if code == -1:
            messagebox.showerror('Error', msg)
            friend_entry.delete(0, tk.END)
            return
        # 将新的好友添加到好友列表
        else:
            messagebox.showerror('Success', msg)
            byte_value = privateKey.to_bytes(length=4, byteorder='big', signed=False)
            chat_display.insert(tk.END, f"和好友{friend_name}的共享密钥为：{SM3.sm3_hash(byte_value)}\n")
            friend_entry.delete(0, tk.END)
            update_friend_list()
            update_userData()


def update_friend_list():
    print(clientUsername + '客户端刷新好友信息')
    friend_list.delete(0, tk.END)
    data = json.dumps(
        {
            "username": clientUsername
        }
    )
    r = requests.post(
        'http://192.168.137.1:8000/api/updateFriend',
        data=data
    )
    friendList = r.json()
    print(friendList)
    for friend in friendList:
        print("客户端好友列表添加好友：" + friend)
        friend_list.insert(tk.END, friend)

    # 更新好友选择下拉框
    menu = friend_option_menu['menu']
    menu.delete(0, 'end')
    for friend in friendList:
        menu.add_command(label=friend, command=tk._setit(selected_friend, friend))
    # 设置选项菜单的值为当前选择的对象
    if selected_friend.get() not in friendList:
        selected_friend.set("")  # 如果当前选择的对象不在新的好友列表中，清空选择

    # 如果当前选择的对象不在新的好友列表中，将其设置为第一个好友
    if selected_friend.get() not in friendList and friendList:
        selected_friend.set(friendList[0])
    else:
        selected_friend.set(selected_friend.get())  # 如果当前选择的对象在新的好友列表中，设置为当前选择的对象
    root.after(1000, update_friend_list)


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
        byte_data = ImageByte.image2byte(image)
        recv = selected_friend.get()

        private_key = None
        if 'userKeyList' in clientUserData:
            for key_info in clientUserData['userKeyList']:
                if key_info.get('friendUser') == recv:
                    private_key = key_info.get('private_key')
                    break
        start_time = time.time()
        en_msg = SM4.sm4_encode(private_key, byte_data)
        end_time = time.time()
        chat_display.insert(tk.END, f'图片加密用时：{end_time - start_time:.6f}\n')
        data = json.dumps(
            {
                'sendname': clientUsername,
                'recvname': recv,
                'msg': en_msg,
                'sm3_msg': SM3.sm3_hash(byte_data),
                'send_time': time.time(),
            }
        )
        r = requests.post(
            'http://192.168.137.1:8000/api/sendMsg',
            data=data
        )
        send_message = f"{clientUsername}成功发送图片给{recv}"
        chat_display.insert(tk.END, send_message + "\n")
        chat_display.see(tk.END)


# 更新当前用户的数据
def update_userData():
    global clientUserData
    data = json.dumps(
        {
            'username': clientUsername,
        }
    )
    r = requests.post(
        'http://192.168.137.1:8000/api/updateUserData',
        data=data
    )
    clientUserData = r.json()


# 更新用户消息列表
def update_UserData_msg():
    msg_list = clientUserData.get('msgList', [])
    update_userData()
    send = ''
    if msg_list:
        for item in msg_list:
            en_msg = item.get('msg', '')
            send = item.get('sendUser', '')
            sm3_msg = item.get('sm3_msg', '')
            send_time = item.get('send_time', '')
            private_key = None
            if 'userKeyList' in clientUserData:
                for key_info in clientUserData['userKeyList']:
                    if key_info.get('friendUser') == send:
                        private_key = key_info.get('private_key')
                        break

            def ask_accept_image():
                # 截断长消息并添加换行符
                get_time = time.time()
                chat_display.insert(tk.END, f'图片传输用时：{get_time - send_time:.6f}\n')
                truncated_msg = (en_msg[:50] + '...') if len(en_msg) > 50 else en_msg
                display_msg = f"你收到了来自 {send} 的一张图片，是否解密接收？\n密文是:\n{truncated_msg}"
                accept_image = messagebox.askyesno("接收图片", display_msg)
                # 接受图片数据
                if accept_image:
                    start_time = time.time()
                    de_msg = SM4.sm4_decode(private_key, en_msg)
                    end_time = time.time()
                    de_msg = bytes(de_msg, 'utf-8')
                    byte_str = de_msg[2:-1]
                    byte_data = byte_str.decode('unicode_escape').encode('latin1')
                    new_sm3_msg = SM3.sm3_hash(byte_data)
                    chat_display.insert(tk.END, f"加密前图片sm3数据为:{sm3_msg}\n解密后图片sm3数据为:{new_sm3_msg} \n")
                    if new_sm3_msg == sm3_msg:
                        chat_display.insert(tk.END, f" 经过验证后消息完整度为：{new_sm3_msg == sm3_msg} \n")
                        image2 = ImageByte.byte2image(byte_data)
                        image2.show()
                        chat_display.insert(tk.END, f"来自 {send} 图片已解密并显示\n")
                        chat_display.insert(tk.END, f"图片解密用时：{end_time - start_time:.6f}\n")
                    else:
                        chat_display.insert(tk.END, f" 经过sm3验证后消息完整度：{new_sm3_msg == sm3_msg} \n")
                # 拒绝解密接受
                else:
                    chat_display.insert(tk.END, f"来自 {send} 图片已拒绝解密接受\n")

            chat_display.after(0, ask_accept_image)

        data = json.dumps(
            {
                'username': clientUsername,
                'sendUser': send,
            }
        )
        r = requests.post(
            'http://192.168.137.1:8000/api/msg_clean',
            data=data
        )
        update_userData()
    root.after(1000, update_UserData_msg)


if __name__ == "__main__":
    login_screen()
