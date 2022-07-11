from tkinter import *
import mysql.connector
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno


def ferramenta_consultar():
    global dados_tabela
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_ferramentas.place(x=32,y=20,height=224,width=485)
    scrollbar_ferramentas.place(x=23,y=252,width=500)
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
    try:
        if con.is_connected():
            tree_ferramentas.delete(*tree_ferramentas.get_children())
            cursor = con.cursor()
            comando_sql = "SELECT * FROM cadastro_ferramentas WHERE id_ferramenta=%s"
            entry_int = (str(entry_id_consulta.get()))
            dados = [(entry_int)]
            cursor.execute(comando_sql,dados)
            dados_tabela = cursor.fetchall()
            tree_ferramentas.insert(parent='', index=0, values=dados_tabela[0])
            
    except ValueError:
        pass
    except IndexError:
        messagebox.showerror('','ID NÃO ENCONTRADO')
def todas_ferramenta_consulta():
    global dados_tabela,tree_tecnicos
    tree_tecnicos.place(x=3000,y=3000,height=227,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_ferramentas.place(x=32,y=20,height=227,width=485)
    scrollbar_ferramentas.place(x=23,y=252,width=500)
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
 
    if con.is_connected():
        tree_ferramentas.delete(*tree_ferramentas.get_children())
        cursor = con.cursor()
        comando_sql = "SELECT * FROM cadastro_ferramentas;"
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for i in range(0,len(dados_tabela)):
            tree_ferramentas.insert(parent='', index=i, values=dados_tabela[i])
def deletar_id_ferramenta():
    answer = askyesno(title='Confirmação',
                    message='Deseja deletar o ID inserido?')
    try:
        if answer:
            con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
            if con.is_connected():
                tree_ferramentas.delete(*tree_ferramentas.get_children())
                cursor = con.cursor()
                comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                comando_sql_deletar = "DELETE FROM cadastro_ferramentas WHERE id_ferramenta=%s;"
                entry_int = (str(entry_id_consulta.get()))
                dados = [(entry_int)]
                cursor.execute(comando_sql)
                cursor.execute(comando_sql_deletar,dados)
                con.commit()
            
        else:
            pass
    except:
        messagebox.showerror('','Erro ao deletar o técnico')
def inserir_ferramenta():
    global inserir_ferramenta_janela,entry_desc,entry_fabricante,entry_voltagem,entry_partnumber,entry_tamanho,entry_unmedida,entry_tipo,entry_material,entry_reserva,frame1,frame2,frame3,img_videojfx
    
    
    inserir_ferramenta_janela = Toplevel()
    inserir_ferramenta_janela.title(' ')
    inserir_ferramenta_janela.geometry('615x363')
    inserir_ferramenta_janela.resizable(width=FALSE,height=FALSE)

    frame1 = Frame(inserir_ferramenta_janela,width=200,height=400)
    frame2 = Frame(inserir_ferramenta_janela,width=200,height=400)
    frame3 = Frame(inserir_ferramenta_janela,width=215,height=400)
    frame1.place(x=0,y=0)
    frame2.place(x=200,y=0)
    frame3.place(x=400,y=0)

    # FRAME 1 

    label_desc = Label(frame1,text='Desc. Ferramenta',font=('Athiti','13'),fg='#363636')
    label_desc.place(x=15,y=50)

    entry_desc = Text(frame1,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_desc.place(x = 18, y = 80,width = 180,height = 85)


    label_fabricante = Label(frame1,text='Fabricante *',font=('Athiti','13'),fg='#363636')
    label_fabricante.place(x=15,y=175)

    entry_fabricante = Entry(frame1,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_fabricante.place(x=18,y=205,width = 180)


    label_voltagem = Label(frame1,text='Voltagem de Uso *',font=('Athiti','13'),fg='#363636')
    label_voltagem.place(x=15,y=240)

    entry_voltagem = Entry(frame1,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_voltagem.place(x=18,y=270,width = 180)

    botao_sair_ferramenta = Button(frame1,text='Sair',command=sair_inserir_ferramenta,relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_sair_ferramenta.place(x=18,y=325,width=90)

    # FRAME 2 

    label_ferramentas_cadastra = Label(frame2,text='FERRAMENTAS',font=('Athiti SemiBold','19'),fg='#363636')
    label_ferramentas_cadastra.place(x=15,y=5)

    label_partnumber = Label(frame2,text='Part Number *',font=('Athiti','13'),fg='#363636')
    label_partnumber.place(x=15,y=50)

    entry_partnumber = Entry(frame2,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_partnumber.place(x=18,y=80,width = 180)


    label_tamanho = Label(frame2,text='Tamanho *',font=('Athiti','13'),fg='#363636')
    label_tamanho.place(x=15,y=115)

    entry_tamanho = Entry(frame2,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_tamanho.place(x=18,y=145,width = 180)


    label_unmedida = Label(frame2,text='Un. de medida *',font=('Athiti','13'),fg='#363636')
    label_unmedida.place(x=15,y=175)

    entry_unmedida = Entry(frame2,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_unmedida.place(x=18,y=205,width = 180)


    label_tipo = Label(frame2,text='Tipo*',font=('Athiti','13'),fg='#363636')
    label_tipo.place(x=15,y=240)

    entry_tipo = Entry(frame2,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_tipo.place(x=18,y=270,width = 180)

    # FRAME 3

    label_material = Label(frame3,text='Material *',font=('Athiti','13'),fg='#363636')
    label_material.place(x=15,y=50)

    entry_material = Entry(frame3,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_material.place(x=18,y=80,width = 180)


    label_reserva = Label(frame3,text='Reserva Máx * (hrs)',font=('Athiti','13'),fg='#363636')
    label_reserva.place(x=15,y=115)

    entry_reserva = Entry(frame3,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_reserva.place(x=18,y=145,width = 180)

    img_videojfx = PhotoImage(file='VIDEOJFX.png')
    videojfx_ferramentas = Label(frame3,image=img_videojfx)
    videojfx_ferramentas.place(x=0,y=168)

    botao_cadastrar_ferramenta = Button(frame3,command=cadastrar_ferramenta,text='Cadastrar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_cadastrar_ferramenta.place(x=108,y=325,width=90)    
def sair_inserir_ferramenta():
    inserir_ferramenta_janela.withdraw()

def cadastrar_ferramenta():
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
    try:
        converte_int = int(entry_reserva.get())
    
        if len(entry_reserva.get())==0 or converte_int==0 or entry_reserva.get().isalpha():
            messagebox.showerror('','TEMPO MÁX. DE RESERVA INVÁLIDO')
            
        elif len(entry_desc.get('1.0', 'end'))!=0 and len(entry_fabricante.get())!=0 and len(entry_voltagem.get())!=0 and len(entry_partnumber.get())!=0 and len(entry_tamanho.get())!=0 and len(entry_unmedida.get())!=0 and len(entry_tipo.get())!=0 and len(entry_material.get())!=0 and len(entry_reserva.get())!=0:
            try:
                if con.is_connected():
                    cursor = con.cursor()
                    comando_sql = "INSERT INTO cadastro_ferramentas (`desc_ferramenta`,`fabricante_ferramenta`,`voltagem_ferramenta`,`part_number_ferramenta`,`tamanho_ferramenta`,`un_medida_ferramenta`,`tipo_ferramenta`,`material_ferramenta`,`max_reserva_ferramenta`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    label_textbox = entry_desc.get('1.0', 'end')
                    dados =(label_textbox,str(entry_fabricante.get()),str(entry_voltagem.get()),str(entry_partnumber.get()),str(entry_tamanho.get()),str(entry_unmedida.get()),str(entry_tipo.get()),str(entry_material.get()),entry_reserva.get())
                    cursor.execute(comando_sql,dados)
                    con.commit()
                    messagebox.showinfo('','FERRAMENTA CADASTRADA')
            except:
                messagebox.showerror('','CADASTRO INVÁLIDO')
        else:
            messagebox.showerror('','CADASTRO INVÁLIDO')
    except ValueError:
        messagebox.showerror('','TEMPO MÁX. DE RESERVA INVÁLIDO')

def tecnicos_consultar():
    global dados_tabela,tree_tecnicos
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_ferramentas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=32,y=20,height=224,width=485)
    scrollbar_tecnicos.place(x=23,y=252,width=500)
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
    try:
        if entry_cpf_consulta.get() == '':
            messagebox.showerror('','CPF NÃO ENCONTRADO') 
        else:
            if con.is_connected():
                tree_tecnicos.delete(*tree_tecnicos.get_children())
                cursor = con.cursor()
                entry_int = (str(entry_cpf_consulta.get()))
                dados = [(entry_int)]
                comando_sql = ("SELECT * FROM tecnicos_responsaveis WHERE cpf_tecnicos LIKE '%"+(entry_int)+"%'")
                cursor.execute(comando_sql)
                dados_tabela = cursor.fetchall()
                tree_tecnicos.insert(parent='', index=0, values=dados_tabela[0])
            
    except ValueError:
        pass
    except IndexError:
        messagebox.showerror('','CPF NÃO ENCONTRADO')
def todos_tecnicos_consulta():
    global dados_tabela,tree_tecnicos
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_ferramentas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=32,y=20,height=224,width=485)
    scrollbar_tecnicos.place(x=23,y=252,width=500)
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
 
    if con.is_connected():
        tree_tecnicos.delete(*tree_tecnicos.get_children())
        cursor = con.cursor()
        comando_sql = "SELECT * FROM tecnicos_responsaveis;"
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for i in range(0,len(dados_tabela)):
            tree_tecnicos.insert(parent='', index=i, values=dados_tabela[i])
def deletar_cpf_tecnico():
    answer_tecnico = askyesno(title='Confirmação',
                    message='Deseja deletar o CPF inserido?')
    try:
        if answer_tecnico:
            con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
            if con.is_connected():
                tree_tecnicos.delete(*tree_tecnicos.get_children())
                cursor = con.cursor()
                comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                comando_sql_deletar = "DELETE FROM tecnicos_responsaveis WHERE cpf_tecnicos=%s;"
                entry_int = (str(entry_cpf_consulta.get()))
                dados = [(entry_int)]
                cursor.execute(comando_sql)
                cursor.execute(comando_sql_deletar,dados)
                con.commit()
            
        else:
            pass
    except:
        messagebox.showerror('','Erro ao deletar o técnico')
def inserir_tecnico():
    global cadastrar_tecnicos_janela,frame1_tecnico_cadastrar,frame2_tecnico_cadastrar,entry_cpf_cadastrar,entry_nome,entry_telefone,caixa_combo_turnos,entry_equipe
    
    cadastrar_tecnicos_janela = Toplevel()
    cadastrar_tecnicos_janela.title(' ')
    cadastrar_tecnicos_janela.geometry('442x300')
    cadastrar_tecnicos_janela.resizable(width=FALSE,height=FALSE)

    frame1_tecnico_cadastrar = Frame(cadastrar_tecnicos_janela,width=225,height=400)
    frame2_tecnico_cadastrar = Frame(cadastrar_tecnicos_janela,width=217,height=400)
    frame1_tecnico_cadastrar.place(x=0,y=50)
    frame2_tecnico_cadastrar.place(x=225,y=50)

    label_tecnicos_cadastrar = Label(cadastrar_tecnicos_janela,text='TÉCNICOS',font=('Athiti SemiBold','19'),fg='#363636')
    label_tecnicos_cadastrar.pack(side=TOP)

    # FRAME 1

    label_cpf_cadastrar = Label(frame1_tecnico_cadastrar,text='CPF *',font=('Athiti','13'),fg='#363636')
    label_cpf_cadastrar.place(x=15,y=10)

    entry_cpf_cadastrar = Entry(frame1_tecnico_cadastrar,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_cpf_cadastrar.place(x=18,y=40,width = 180)


    label_nome = Label(frame1_tecnico_cadastrar,text='Nome Completo *',font=('Athiti','13'),fg='#363636')
    label_nome.place(x=15,y=75)

    entry_nome = Entry(frame1_tecnico_cadastrar,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_nome.place(x=18,y=105,width = 180)


    label_telefone = Label(frame1_tecnico_cadastrar,text='Telefone *',font=('Athiti','13'),fg='#363636')
    label_telefone.place(x=15,y=135)

    entry_telefone = Entry(frame1_tecnico_cadastrar,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_telefone.place(x=18,y=165,width = 180)

    botao_sair_tecnico = Button(frame1_tecnico_cadastrar,command=sair_inserir_tecnico,text='Sair',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_sair_tecnico.place(x=18,y=208,width=90)

    # FRAME 2

    label_turno = Label(frame2_tecnico_cadastrar,text='Turno *',font=('Athiti','13'),fg='#363636')
    label_turno.place(x=15,y=10)

    escolher_turnos = StringVar()
    caixa_combo_turnos = ttk.Combobox(frame2_tecnico_cadastrar,textvariable=escolher_turnos)
    caixa_combo_turnos['values']= ["Manhã","Tarde","Noite"]
    caixa_combo_turnos.place(x=18,y=39,width = 180)

    label_equipe = Label(frame2_tecnico_cadastrar,text='Equipe *',font=('Athiti','13'),fg='#363636')
    label_equipe.place(x=15,y=75)

    entry_equipe = Entry(frame2_tecnico_cadastrar,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_equipe.place(x=18,y=105,width = 180)

    botao_cadastrar_tecnico = Button(frame2_tecnico_cadastrar,command=cadastrar_tecnicos,text='Cadastrar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_cadastrar_tecnico.place(x=108,y=208,width=90)
def sair_inserir_tecnico():
    cadastrar_tecnicos_janela.withdraw()

def valida_cpf():
    cpf = [int(char) for char in entry_cpf_cadastrar.get() if char.isdigit()]


    if len(cpf) != 11:
        return False

    if cpf == cpf[::-1]:
        return False


    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True
def cadastrar_tecnicos():
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
    
    if len(entry_telefone.get())!=11 and len(entry_telefone.get())!=0 or entry_telefone.get().isalpha():
        messagebox.showerror('','TELEFONE INVÁLIDO')
        
    if len(entry_equipe.get())>30:
        messagebox.showerror('','NOME DA EQUIPE MUITO GRANDE')
    
    elif len(entry_cpf_cadastrar.get())==0 or len(entry_telefone.get())==0 or len(entry_nome.get())==0 or len(entry_equipe.get())==0 or len(caixa_combo_turnos.get())==0:
        messagebox.showerror('','CADASTRO INVÁLIDO')
        
    elif entry_telefone.get().isdigit() and len(entry_telefone.get())==11 and len(entry_cpf_cadastrar.get())!=0 and len(entry_telefone.get())!=0 and len(entry_nome.get())!=0 and len(entry_equipe.get())!=0:
        try:
            if con.is_connected():
                cursor = con.cursor()
                comando_sql = "INSERT INTO tecnicos_responsaveis (`cpf_tecnicos`,`nome_completo_tecnicos`,`telefone_tecnicos`,`turno_tecnicos`,`equipe_tecnicos`) VALUES(%s,%s,%s,%s,%s);"
                cpf_validar = entry_cpf_cadastrar.get()
                if valida_cpf()==True:
                
                    dados =(str(cpf_validar),str(entry_nome.get()),str(entry_telefone.get()),str(caixa_combo_turnos.get()),str(entry_equipe.get()))
                    cursor.execute(comando_sql,dados)
                    con.commit()
                    messagebox.showinfo('','TÉCNICO CADASTRADO')
                    entry_cpf_cadastrar.delete(0,'end')
                    entry_telefone.delete(0,'end')
                    entry_nome.delete(0,'end')
                    entry_equipe.delete(0,'end')
                    caixa_combo_turnos.delete(0,'end')
                elif valida_cpf()==False:
                    messagebox.showerror('','INSIRA UM CPF VÁLIDO')
                
    
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror('','CPF JÁ CADASTRADO')
        except mysql.connector.errors.DataError:
            messagebox.showerror('','CPF INVÁLIDO')
            
    else:
        messagebox.showerror('','TELEFONE INVÁLIDO') 


def LoginBDD():
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='Mokuton:Hashirama')
    try:
        if con.is_connected():
            cursor = con.cursor()
            comando_sql = "SELECT user_admins,senha_admins FROM admins WHERE user_admins=%s AND senha_admins=%s;"
            dados = (str(input_user.get()),str(input_senha.get()))
            cursor.execute(comando_sql,dados)
            sql_login = cursor.fetchall()
            
            if sql_login[0][0]==input_user.get() and sql_login[0][1]==input_senha.get():
                messagebox.showinfo('','LOGADO COM SUCESSO!')
                tela_principal()
    except IndexError:
        messagebox.showerror('','USUÁRIO OU SENHA INVÁLIDOS')

def tela_principal():
    global janela,tabelas,colunas_ferramentas,tree_ferramentas,scrollbar_ferramentas,colunas_tecnicos,tree_tecnicos,scrollbar_tecnicos,frame_tecnicos,entry_cpf_consulta,frame_ferramentas,entry_id_consulta
    
    janela_login.withdraw()
    janela = Toplevel()
    janela.title(' ')
    janela.geometry('600x590')
    janela.resizable(width=FALSE,height=FALSE)

    # FRAME DE TABELAS
    
    tabelas = LabelFrame(janela,text='Tabelas',border=1,borderwidth=1,relief='solid',font=('Alien League Bold',12),fg='black')
    tabelas.place(x=22,y=15,width=550,height=295)

    style_ferramentas = ttk.Style()
    style_ferramentas.theme_use("vista")

    # TABELA DE FERRAMENTAS
    
    colunas_ferramentas = ('ID','desc_ferramenta','fabricante','voltagem','part_number','tamanho_ferramenta','un_medida','tipo','material','reserva_max')
    tree_ferramentas = ttk.Treeview(tabelas,columns=colunas_ferramentas,show='headings')


    tree_ferramentas.column("ID", width=40,anchor=CENTER, minwidth=40, stretch=NO)
    tree_ferramentas.column("tipo", width=60,anchor=CENTER, minwidth=60, stretch=NO)
    tree_ferramentas.column("fabricante", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("material", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("tamanho_ferramenta", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("desc_ferramenta", width=100,anchor=CENTER, minwidth=100, stretch=NO)
    tree_ferramentas.column("reserva_max", width=90,anchor=CENTER, minwidth=90, stretch=NO)
    tree_ferramentas.column("voltagem", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("part_number",anchor=CENTER, width=90, minwidth=90, stretch=NO)
    tree_ferramentas.column("un_medida", width=100,anchor=CENTER, minwidth=100, stretch=NO)


    tree_ferramentas.heading('ID', text='ID')
    tree_ferramentas.heading('tamanho_ferramenta', text='Tamanho')
    tree_ferramentas.heading('material', text='Material')
    tree_ferramentas.heading('tipo', text='Tipo')
    tree_ferramentas.heading('fabricante', text='Fabricante')
    tree_ferramentas.heading('desc_ferramenta', text='Descrição')
    tree_ferramentas.heading('reserva_max', text='Reserva máx.')
    tree_ferramentas.heading('voltagem', text='Voltagem')
    tree_ferramentas.heading('part_number', text='Part Number')
    tree_ferramentas.heading('un_medida', text='Un. de Medida')
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)

    scrollbar_ferramentas = ttk.Scrollbar(tabelas,orient='horizontal', command=tree_ferramentas.xview)


    tree_ferramentas.configure(xscrollcommand=scrollbar_ferramentas.set)
    scrollbar_ferramentas.place(x=23,y=252,width=500)


    # TABELA DE TÉCNICOS

    colunas_tecnicos = ('cpf','nome_completo','telefone','turno','equipe')
    tree_tecnicos = ttk.Treeview(tabelas,columns=colunas_tecnicos,show='headings')

    tree_tecnicos.column("cpf", width=80,anchor=CENTER, minwidth=80, stretch=NO)
    tree_tecnicos.column("nome_completo", width=173,anchor=CENTER, minwidth=173, stretch=NO)
    tree_tecnicos.column("telefone", width=80,anchor=CENTER, minwidth=80, stretch=NO)
    tree_tecnicos.column("turno", width=65,anchor=CENTER, minwidth=65, stretch=NO)
    tree_tecnicos.column("equipe",anchor=CENTER, width=85, minwidth=85, stretch=NO)

    tree_tecnicos.heading("cpf", text='CPF')
    tree_tecnicos.heading("nome_completo", text='Nome')
    tree_tecnicos.heading("telefone", text='Telefone')
    tree_tecnicos.heading("turno", text='Turno')
    tree_tecnicos.heading("equipe", text='Equipe')
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)

    scrollbar_tecnicos = ttk.Scrollbar(tabelas,orient='horizontal', command=tree_tecnicos.xview)


    tree_tecnicos.configure(xscrollcommand=scrollbar_tecnicos.set)
    scrollbar_tecnicos.place(x=23,y=252,width=500)


    # FRAME DOS TÉCNICOS

    frame_tecnicos = LabelFrame(janela,text='Técnicos',border=2,borderwidth=1,relief='solid',font=('Alien League Bold',12),fg='black')
    frame_tecnicos.place(x=22,y=340,width=260,height=200)

    cpf_label_deleta = Label(frame_tecnicos,text='CPF',font=('Athiti','13'),fg='#363636')
    cpf_label_deleta.pack(fill='x',side=TOP)

    entry_cpf_consulta = Entry(frame_tecnicos,font=('Arial',12),relief='solid')
    entry_cpf_consulta.place(x = 31, y = 35,width=195)

    botao_consultar_tecnicos = Button(frame_tecnicos,command=tecnicos_consultar,text='Consultar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_consultar_tecnicos.place(x=136,y=68,width=90)

    botao_mostrartodos_tecnicos = Button(frame_tecnicos,command=todos_tecnicos_consulta,text='Mostrar Todos',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_mostrartodos_tecnicos.place(x=32,y=68,width=90)

    botao_inserir_tecnicos = Button(frame_tecnicos,command=inserir_tecnico,text='Inserir',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_inserir_tecnicos.place(x=84,y=146,width=90)

    botao_deletar_tecnicos = Button(frame_tecnicos,command=deletar_cpf_tecnico,text='Deletar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_deletar_tecnicos.place(x=84,y=110,width=90)


    # FRAME FERRAMENTAS

    frame_ferramentas = LabelFrame(janela,text='Ferramentas',border=1,borderwidth=1,relief='solid',font=('Alien League Bold',12),fg='black')
    frame_ferramentas.place(x=312,y=340,width=260,height=200)

    id_label_deleta = Label(frame_ferramentas,text='ID',font=('Athiti','13'),fg='#363636')
    id_label_deleta.pack(fill='x',side=TOP)

    entry_id_consulta = Entry(frame_ferramentas,font=('Arial',12),relief='solid')
    entry_id_consulta.place(x = 31, y = 35,width=195)

    botao_consultar_ferramentas = Button(frame_ferramentas,command=ferramenta_consultar,text='Consultar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_consultar_ferramentas.place(x=136,y=68,width=90)

    botao_mostrartodos_ferramentas = Button(frame_ferramentas,command=todas_ferramenta_consulta,text='Mostrar Todos',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_mostrartodos_ferramentas.place(x=32,y=68,width=90)

    botao_inserir_ferramentas = Button(frame_ferramentas,command=inserir_ferramenta,text='Inserir',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_inserir_ferramentas.place(x=84,y=146,width=90)

    botao_deletar_ferramentas = Button(frame_ferramentas,command=deletar_id_ferramenta,text='Deletar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_deletar_ferramentas.place(x=84,y=110,width=90)


    botao_voltar_principal = Button(janela,text='Voltar',command=voltar_pra_principal,relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_voltar_principal.place(x=22,y=555,width=90)
def voltar_pra_principal():
    janela.withdraw()
    janela_login.deiconify()

janela_login = Tk()
janela_login.title(' ')
janela_login.geometry('400x370+700+390')
janela_login.configure(background='white')
janela_login.resizable(width=FALSE,height=FALSE)

estilo_da_fonte_titulo = tkfont.Font(family='Bahnschrift', size=23)

estilo_da_fonte_logado = tkfont.Font(family='Bahnschrift',size=16)

estilo_da_fonte_widgets = tkfont.Font(family='Arial Rounded MT Bold', size=12)

# TELA PRINCIPAL

img_videojfx = PhotoImage(file='VIDEOJFX.png')
videojfx_ferramentas = Label(janela_login,image=img_videojfx,bg='white')
videojfx_ferramentas.pack(side=TOP)


label_usuario = Label(janela_login,fg='black', text='Usuário', font=estilo_da_fonte_widgets,background='white')
label_usuario.place(x=46,y=130)

input_user = Entry(janela_login, width=25, justify='left',font=('',14), highlightthickness=1, relief='solid')
input_user.place(x=50,y=160,width=300)


label_senha = Label(janela_login,fg='black', text='Palavra passe', font=estilo_da_fonte_widgets,background='white')
label_senha.place(x=46,y=220)

input_senha = Entry(janela_login, width=25, justify='left',font=('',14),highlightthickness=1, relief='solid',show='*',fg='black',background='white')
input_senha.place(x=50,y=250,width=300)

botao_entrar = Button(janela_login,command=LoginBDD, text='Entrar',relief='flat',bg='black',fg='white',width=13,font=estilo_da_fonte_widgets)
botao_entrar.place(x=130,y=310)

janela_login.mainloop()