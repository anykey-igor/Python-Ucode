import tkinter as tk
from tkinter import ttk
import yaml
import main.request_to
import main.parser
from tkinter import messagebox
from tkinter import *

# -- Key: method -- Value: GET
# -- Key: history -- Value: None
# -- Key: auth -- Value: None
# -- Key: log -- Value: DEBUG
# -- Key: endpoint -- Value: https://google.com.ua
# -- Key: params -- Value: None
# -- Key: headers -- Value: ['User-Agent=Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)']
# -- Key: body -- Value: None
# -- Key: tree -- Value: False
# -- Key: raw -- Value: False
# -- Key: pretty -- Value: False
# -- Key: yaml -- Value: False

# method = GET
# gui = False
# history = None
# auth = ('{@username}', '{@user_pass}')
# log = INFO
# endpoint = {@request_url}
# params = {'{@par1}': '{@request_rap1}'}
# headers = {'{@user_agent}': '{@user_agent_parametr}'}
# body = None
# tree = False
# raw = False
# pretty = False
# yaml = False

#if __name__ == '__main__':

# username = tk.StringVar()
# password = tk.StringVar()
# current_method = tk.StringVar()
# current_view = tk.IntVar()
# current_log = tk.IntVar()
# request = tk.StringVar()

"Получаем переменные из файла"
def get_variables():
    with open("variables.yaml", 'r') as f:
        try:
            return yaml.safe_load(f)
        except:
            return {}

"Cоздаем словарь для запроса"



def mainwindow(my_args):


    def make_request():
        send_list =[]
        send_list.append(username_entry.get())
        send_list.append(password_entry.get())
        complite = main.parser.extract_variable('variable.yaml', **my_args)
        main.request_to.web_surfer(complite)
        #print(complite)
        # print(tuple(send_list))
        # print(request_entry.get())


    req = my_args.get('endpoint')
    auth = my_args['auth']
    username = auth[0]
    password = auth[1]
    # print(username)
    # print(password)
    # print(auth)
    # print(request)
    current_method = my_args.get('method')

    #print(my_args)


    "Главное окно GUI"
    window = tk.Tk()
    window.title("ENDGAME Python REST API client - Dark Side")
    # window.geometry('650x600')
    # window.resizable(width=False, height=True)
    # for i in range(3):
    #     window.columnconfigure(i, weight=1, minsize=75)
    #     window.rowconfigure(i, weight=1, minsize=50)

    # Глобальные переменные
    username = tk.StringVar()
    username.set(my_args.get('auth')[0])
    password = tk.StringVar()
    password.set(my_args.get('auth')[1])
    current_method = tk.StringVar()
    current_method.set(my_args.get('method'))
    current_view = tk.IntVar()
    # current_view.set(my_args.get('tree'))
    current_log = tk.IntVar()
    request = tk.StringVar()
    request.set(my_args.get('endpoint'))

    #Ключи=значения из парсера в словари, перезаписываеться после SEND"
    parametrs = {}
    body = {}
    headers = {}
    #set_dicts()
    # FONTS
    font10 = ("Arial Rounded MT Bold", 10)
    font12 = ("Arial Rounded MT Bold", 12)
    font14 = ("Arial Rounded MT Bold", 14)
    font16 = ("Arial Rounded MT Bold", 16)
    # Выпадающие меню
    main_frame = tk.Frame(window, bg="#000", bd=10)
    mainmenu = tk.Menu(window)
    window.config(menu=mainmenu)
    # меню логера
    log_menu = tk.Menu(mainmenu, tearoff=0)
    log_menu.add_command(label="DEBUG") #command=set_log_debug)
    log_menu.add_command(label="INFO") #command=set_log_info)
    log_menu.add_command(label="WARNING") #command=set_log_warn)
    mainmenu.add_cascade(label="Severity level", menu=log_menu)
    # меню переменных
    var_menu = tk.Menu(mainmenu, tearoff=0)
    var_menu.add_command(label="Variables") #command=show_variables)
    mainmenu.add_cascade(label="Variables", menu=var_menu)
    # меню истории
    hist_menu = tk.Menu(mainmenu, tearoff=0)
    hist_menu.add_command(label="History") #command=show_history)
    mainmenu.add_cascade(label="History",menu=hist_menu)
    # меню помощи
    help_menu = tk.Menu(mainmenu, tearoff=0)
    help_menu.add_command(label="Help") #command=show_help)
    help_menu.add_separator()
    help_menu.add_command(label="About") #command=show_about)
    mainmenu.add_cascade(label="Help", menu=help_menu)
    # ОКНО ЗАПРОСА
    request_frame = tk.LabelFrame(main_frame, bg="Black", bd=5, text="Choose method and send your request",
                              font=font12, fg="White", labelanchor=tk.N)
    request_subframe = tk.Frame(request_frame, bg="Black", bd=3)
    combostyle = ttk.Style()
    combostyle.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                          {'configure':
                                               {'selectforeground': 'Black',
                                                'selectbackground': '#FFD300',
                                                'fieldbackground': '#FFD300',
                                                'background': '#4671D5'
                                                }}}
                            )
    combostyle.theme_use('combostyle')
    combobox_request = ttk.Combobox(request_frame,
                                    values=[
                                "GET",
                                "POST",
                                "PUT",
                                "PATCH",
                                "DELETE"],
                                    state="readonly",
                                    font=font14,
                                    width=8, height=20,
                                    textvariable=current_method,
                                    background="#3b84d9")
    combobox_request.current(0)
    combobox_request.grid(row=0, column=0, sticky="we", padx=5, pady=5)
    request_entry = tk.Entry(request_subframe, textvariable=request, width=45)
    request_entry.grid(row=0, column=1, sticky="we", padx=5, pady=5)
    # КНОПКА SEND
    send_button = tk.Button(request_subframe,
                            text="Send",
                            background="#008500",
                            foreground="#000",
                            padx=1,
                            pady=1,
                            width=8,
                            font=font12,command=make_request)
    send_button.grid(row=0, column=2, sticky="nsew")
    request_subframe.grid(row=0, column=1, sticky="nsew")
    request_frame.grid(row=0, column=0, sticky="we", padx=5, pady=5)
    # Окно авторизации
    authent_frame = tk.LabelFrame(main_frame, bg="Black", fg="White", bd=5, text="Basic Authentication", font=font12, labelanchor=tk.N)
    name_label = tk.Label(authent_frame, text="Enter username:", font=font12, bg="Black", fg="White").grid(row=0, column=0, sticky="nsew")
    password_label = tk.Label(authent_frame, text="Enter password:", font=font12, bg="Black", fg="White").grid(row=0, column=1, sticky="nsew")
    username_entry = tk.Entry(authent_frame, textvariable=username, width=30)
    username_entry.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    password_entry = tk.Entry(authent_frame, textvariable=password, width=30)
    password_entry.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
    authent_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
    # Окно параметров
    def add_row_parametrs():
        e_key = tk.Entry(parametr_frame)
        e_key.grid(row=param_row.get(), column=0, sticky="nsew")
        e_val = tk.Entry(parametr_frame)
        e_val.grid(row=param_row.get(), column=1, sticky="nsew")
        entry_parametr.update({e_key: e_val})
        param_button.grid_remove()
        param_button.grid(row=param_row.get(), column=2, sticky="nsew")
        param_row.set(param_row.get() + 1)

    parametr_frame = tk.LabelFrame(main_frame, bd=5, text="Add parameters", font=font12, bg="Black", fg="White", labelanchor=tk.N)
    param_row = tk.IntVar(0)
    entry_parametr = {}
    for k, v in parametrs.items():
        ent_key = tk.Entry(parametr_frame, width=30)
        ent_key.insert(0, k)
        ent_key.grid(row=param_row.get(), column=0, sticky="nsew")
        ent_val = tk.Entry(parametr_frame, width=30)
        ent_val.insert(0, v)
        ent_val.grid(row=param_row.get(), column=1, sticky="nsew")
        entry_parametr.update({ent_key: ent_val})
        param_row.set(param_row.get() + 1)
    ent_key = tk.Entry(parametr_frame, width=30)
    ent_key.grid(row=param_row.get(), column=0, sticky="nsew")
    ent_val = tk.Entry(parametr_frame, width=30)
    ent_val.grid(row=param_row.get(), column=1, sticky="nsew")
    entry_parametr.update({ent_key: ent_val})
    pixelVirtual = tk.PhotoImage(width=1, height=1)
    param_button = tk.Button(parametr_frame,
                             text="+",
                             background="#FFD300",
                             foreground="#000",
                             image=pixelVirtual,
                             padx=5,
                             pady=5,
                             width=15,
                             height=2,
                             compound="c",
                             font=font12, command=add_row_parametrs)
    param_button.grid(row=param_row.get(), column=2, sticky="nsew")
    param_row.set(param_row.get() + 1)
    parametr_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    # Окно BODY
    def add_row_body():
        e_key = tk.Entry(body_frame)
        e_key.grid(row=body_row.get(), column=0, sticky="nsew")
        e_val = tk.Entry(body_frame)
        e_val.grid(row=body_row.get(), column=1, sticky="nsew")
        ent_body.update({e_key: e_val})
        body_button.grid_remove()
        body_button.grid(row=body_row.get(), column=2, sticky="nsew")
        body_row.set(body_row.get() + 1)
    body_frame = tk.LabelFrame(main_frame, bd=5, text="Add request body", font=font12, bg="Black", fg="White", labelanchor=tk.N)
    body_row = tk.IntVar(0)
    ent_body = {}
    for k, v in body.items():
        ent_key = tk.Entry(body_frame, width=30)
        ent_key.insert(0, k)
        ent_key.grid(row=body_row.get(), column=0, sticky="nsew")
        ent_val = tk.Entry(body_frame, width=30)
        ent_val.insert(0, v)
        ent_val.grid(row=body_row.get(), column=1, sticky="nsew")
        ent_body.update({ent_key: ent_val})
        body_row.set(body_row.get() + 1)
    ent_key = tk.Entry(body_frame, width=30)
    ent_key.grid(row=body_row.get(), column=0, sticky="nsew")
    ent_val = tk.Entry(body_frame, width=30)
    ent_val.grid(row=body_row.get(), column=1, sticky="nsew")
    ent_body.update({ent_key: ent_val})
    body_button = tk.Button(body_frame,
                            text="+",
                            background="#FFD300",
                            foreground="#000",
                            image=pixelVirtual,
                            padx=5,
                            pady=5,
                            width=15,
                            height=2,
                            compound="c",
                            font=font12,
                            command=add_row_body)
    body_button.grid(row=body_row.get(), column=2, sticky="nsew")
    body_row.set(param_row.get() + 1)
    body_frame.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
    #Окно HEADERS
    def add_row_header():
        e_key = tk.Entry(head_frame)
        e_key.grid(row=head_row.get(), column=0, sticky="nsew")
        e_val = tk.Entry(head_frame)
        e_val.grid(row=head_row.get(), column=1, sticky="nsew")
        ent_head.update({e_key: e_val})
        head_button.grid_remove()
        head_button.grid(row=head_row.get(), column=2, sticky="nsew")
        head_row.set(head_row.get() + 1)
    head_frame = tk.LabelFrame(main_frame, bd=5, text="Add request headers", font=font12, bg="Black", fg="White", labelanchor=tk.N)
    head_row = tk.IntVar(0)
    ent_head = {}
    for k, v in headers.items():
        ent_key = tk.Entry(head_frame, width=30, bg="Black", fg="White")
        ent_key.insert(0, k)
        ent_key.grid(row=head_row.get(), column=0, sticky="nsew")
        ent_val = tk.Entry(head_frame, width=30)
        ent_val.insert(0, v)
        ent_val.grid(row=head_row.get(), column=1, sticky="nsew")
        ent_head.update({ent_key: ent_val})
        head_row.set(head_row.get() + 1)
    ent_key = tk.Entry(head_frame, width=30)
    ent_key.grid(row=head_row.get(), column=0, sticky="nsew")
    ent_val = tk.Entry(head_frame, width=30)
    ent_val.grid(row=head_row.get(), column=1, sticky="nsew")
    ent_head.update({ent_key: ent_val})
    head_button = tk.Button(head_frame,
                            text="+",
                            background="#FFD300",
                            foreground="#000",
                            image=pixelVirtual,
                            padx=5,
                            pady=5,
                            width=15,
                            height=2,
                            compound="c",
                            font=font12,
                            command=add_row_header)
    head_button.grid(row=head_row.get(), column=2, sticky="nsew")
    head_row.set(head_row.get() + 1)
    head_frame.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
    "Окно выбора вида"
    def set_view():
        if val == 0:
            current_view = "Tree"
        elif val == 1:
            current_view = "Raw"
        elif val == 2:
            current_view = "Pretty"
        elif val == 3:
            current_view = "Yaml"
    views = [("Tree", 0), ("Raw", 1), ("Pretty", 2), ("Yaml", 3)]
    view_frame = tk.LabelFrame(main_frame, bd=5, text="Choose view mode", font=font12,bg="Black", fg="White", labelanchor=tk.N)
    column = 0
    for txt, val in views:
        tk.Radiobutton(view_frame,
                       text=txt,
                       value=val,
                       variable=current_view,
                       background="#FFD300",
                       foreground="#000",
                       padx=5,
                       pady=5,
                       width=20,
                       font=font12,
                       command=set_view) \
            .grid(row=0, column=column, sticky="nsew")
        column += 1
    view_frame.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)

    main_frame.grid(row=0, column=0, sticky="nsew")
    window.mainloop()


# if __name__ == '__main__':
#     my_args ={'method': 'GET',
#               'gui' : 'False',
#               'history':'None',
#               'auth' : ('{@username}', '{@user_pass}'),
#               'log' :'INFO',
#               'endpoint' : "{@request_url}",
#               'params' : {'{@par1}': '{@request_rap1}'},
#               'headers' : {'{@user_agent}': '{@user_agent_parametr}'},
#               'body' : 'None',
#               'tree' : 'False',
#               'raw' : 'False',
#               'pretty' : 'False',
#               'yaml' : 'False'}
#     mainwindow(my_args)
