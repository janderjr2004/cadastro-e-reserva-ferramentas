from tkinter import *
import mysql.connector
import tkinter.font as tkfont
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import askyesno
import smtplib
import email.message
import unidecode
from datetime import datetime,date,timedelta
# FERRAMENTAS CONFIGURAÇÕES 

def ferramenta_consultar():
    global dados_tabela
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_reservas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_reservas.place(x=3000,y=3000,width=500)
    
    tree_ferramentas.place(x=32,y=20,height=224,width=485)
    scrollbar_ferramentas.place(x=23,y=252,width=500)
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
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
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_reservas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_reservas.place(x=3000,y=3000,width=500)
    
    tree_ferramentas.place(x=32,y=20,height=224,width=485)
    scrollbar_ferramentas.place(x=23,y=252,width=500)
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
 
    if con.is_connected():
        tree_ferramentas.delete(*tree_ferramentas.get_children())
        cursor = con.cursor()
        comando_sql = "SELECT * FROM cadastro_ferramentas;"
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for i in range(0,len(dados_tabela)):
            tree_ferramentas.insert(parent='', index=i, values=dados_tabela[i])
def deletar_id_ferramenta():
    curItem = tree_ferramentas.focus()
    valor = tree_ferramentas.item(curItem)
    lista_valores = valor['values']
    
    if lista_valores=='':
        answer = askyesno(title='Confirmação',
                    message=(f'Deseja deletar a ferramenta de ID {entry_id_consulta.get()}?'))
        try:
            if answer:
                con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
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
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror('','Ferramenta vinculado a uma reserva')
        except:
            messagebox.showerror('','Erro ao deletar a ferramenta')
            
    elif lista_valores!='':
        answer = askyesno(title='Confirmação',
                    message=(f'Deseja deletar a ferramenta de ID {lista_valores[0]}?'))
        try:
            if answer:
                con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
                if con.is_connected():
                    tree_ferramentas.delete(*tree_ferramentas.get_children())
                    cursor = con.cursor()
                    comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                    comando_sql_deletar = "DELETE FROM cadastro_ferramentas WHERE id_ferramenta=%s;"
                    entry_int = (str(lista_valores[0]))
                    dados = [(entry_int)]
                    cursor.execute(comando_sql)
                    cursor.execute(comando_sql_deletar,dados)
                    con.commit()
                    
            else:
                pass
        except mysql.connector.errors.IntegrityError:
            messagebox.showerror('','Ferramenta vinculado a uma reserva')
        except:
            messagebox.showerror('','Erro ao deletar a ferramenta') 
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
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
    try:
        converte_int = int(entry_reserva.get())
    
        if len(entry_reserva.get())==0 or converte_int==0 or entry_reserva.get().isalpha() or int(entry_reserva.get())%24!=0:
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

# TÉCNICOS CONFIGURAÇÕES

def tecnicos_consultar():
    global dados_tabela,tree_tecnicos
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_ferramentas.place(x=3000,y=3000,width=500)
    
    tree_reservas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_reservas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=32,y=20,height=224,width=485)
    scrollbar_tecnicos.place(x=23,y=252,width=500)

    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
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
    
    tree_reservas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_reservas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=32,y=20,height=224,width=485)
    scrollbar_tecnicos.place(x=23,y=252,width=500)
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
 
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
            con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
            if con.is_connected():
                tree_tecnicos.delete(*tree_tecnicos.get_children())
                cursor = con.cursor()
                comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                comando_sql_deletar = "DELETE FROM tecnicos_responsaveis WHERE cpf_tecnicos=%s;"
                comando_sql_deletar_user = "DELETE FROM users WHERE cpf_user_tecnico=%s"
                entry_int = (str(entry_cpf_consulta.get()))
                dados = [(entry_int)]
                cursor.execute(comando_sql)
                cursor.execute(comando_sql_deletar,dados)
                cursor.execute(comando_sql_deletar_user,dados)
                con.commit()
    except mysql.connector.errors.IntegrityError:
        messagebox.showerror('','Técnico vinculado a uma reserva')
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
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
    
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
                    gerar_user()
                    comando_sql_gerar = "INSERT INTO users(cpf_user_tecnico,nome_sobrenome) VALUES (%s,%s);"
                    dados_user = (cpf_validar,str(nome_bdd))
                    cursor.execute(comando_sql_gerar,dados_user)
                    con.commit()
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
def gerar_user():
    global nome_bdd
    nome = str(entry_nome.get())

    nome2 = nome.split()
    primeiro = unidecode.unidecode(nome2[0])
    ultimo = unidecode.unidecode(nome2[-1])
    nome_bdd = (f'{primeiro.lower()}{ultimo.lower()}')

# RESERVA DE FERRAMENTAS CONFIGURAÇÕES

def janela_reserva():
    global caixa_combo_dias_retirada,caixa_combo_meses_retirada,caixa_combo_anos_retirada,caixa_combo_dias_devolucao,caixa_combo_meses_devolucao,caixa_combo_anos_devolucao,entry_id_ferramenta_reservar,entry_cpf_tecnico_reservar,entry_nome_tecnico_reservar,entry_retirada_horario_reservar,entry_devolucao_horario_reservar,reservar_ferramentas
    
    reservar_ferramentas = Toplevel()
    reservar_ferramentas.title(' ')
    reservar_ferramentas.geometry('442x300')
    reservar_ferramentas.resizable(width=FALSE,height=FALSE)

    frame1_reservas = Frame(reservar_ferramentas,width=225,height=400)
    frame2_reservas = Frame(reservar_ferramentas,width=217,height=400)
    frame1_reservas.place(x=0,y=50)
    frame2_reservas.place(x=225,y=50)

    label_reservas = Label(reservar_ferramentas,text='RESERVAR',font=('Athiti SemiBold','19'),fg='#363636')
    label_reservas.pack(side=TOP)

    # FRAME 1

    label_id_ferramenta_reservar = Label(frame1_reservas,text='ID da Ferramenta *',font=('Athiti','13'),fg='#363636')
    label_id_ferramenta_reservar.place(x=15,y=10)

    entry_id_ferramenta_reservar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_id_ferramenta_reservar.place(x=18,y=40,width = 180)


    label_cpf_tecnico_reservar = Label(frame1_reservas,text='CPF do Técnico *',font=('Athiti','13'),fg='#363636')
    label_cpf_tecnico_reservar.place(x=15,y=75)

    entry_cpf_tecnico_reservar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_cpf_tecnico_reservar.bind('<FocusOut>',inserir_nome_do_tecnico)
    entry_cpf_tecnico_reservar.place(x=18,y=105,width = 180)


    label_nome_tecnico_reservar = Label(frame1_reservas,text='Nome do Técnico *',font=('Athiti','13'),fg='#363636')
    label_nome_tecnico_reservar.place(x=15,y=135)

    entry_nome_tecnico_reservar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_nome_tecnico_reservar.place(x=18,y=165,width = 180)

    botao_sair_reservar = Button(frame1_reservas,command=sair_da_reserva_janela,text='Sair',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_sair_reservar.place(x=18,y=208,width=90)

    # FRAME 2

    label_retirada = Label(frame2_reservas,text='Data da Retirada *',font=('Athiti','13'),fg='#363636')
    label_retirada.place(x=15,y=10)

    label_devolucao = Label(frame2_reservas,text='Data da Devolução *',font=('Athiti','13'),fg='#363636')
    label_devolucao.place(x=15,y=100)


    botao_reservar_ferramenta = Button(frame2_reservas,command=valida_reserva_ferramenta,text='Reservar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_reservar_ferramenta.place(x=108,y=208,width=90)


    escolher_dia_retirada = StringVar()
    caixa_combo_dias_retirada = ttk.Combobox(frame2_reservas,textvariable=escolher_dia_retirada)
    caixa_combo_dias_retirada['values']= ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    caixa_combo_dias_retirada.place(x=18,y=39,width = 45,height=28)

    escolher_meses_retirada = StringVar()
    caixa_combo_meses_retirada = ttk.Combobox(frame2_reservas,textvariable=escolher_meses_retirada)
    caixa_combo_meses_retirada['values']= ['01','02','03','04','05','06','07','08','09','10','11','12']
    caixa_combo_meses_retirada.place(x=85,y=39,width = 45,height=28)

    escolher_anos_retirada = StringVar()
    caixa_combo_anos_retirada = ttk.Combobox(frame2_reservas,textvariable=escolher_anos_retirada)
    caixa_combo_anos_retirada['values']= ["2021","2022","2023"]
    caixa_combo_anos_retirada.place(x=152,y=39,width = 50,height=28)
    
    
    
    escolher_dia_devolucao = StringVar()
    caixa_combo_dias_devolucao = ttk.Combobox(frame2_reservas,textvariable=escolher_dia_devolucao)
    caixa_combo_dias_devolucao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    caixa_combo_dias_devolucao.place(x=18,y=129,width = 45,height=28)

    escolher_meses_devolucao = StringVar()
    caixa_combo_meses_devolucao = ttk.Combobox(frame2_reservas,textvariable=escolher_meses_devolucao)
    caixa_combo_meses_devolucao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12']
    caixa_combo_meses_devolucao.place(x=85,y=129,width = 45,height=28)

    escolher_anos_devolucao = StringVar()
    caixa_combo_anos_devolucao = ttk.Combobox(frame2_reservas,textvariable=escolher_anos_devolucao)
    caixa_combo_anos_devolucao['values']= ["2021","2022","2023"]
    caixa_combo_anos_devolucao.place(x=152,y=129,width = 50,height=28)
    
    label_retirada_horario_reservar = Label(frame2_reservas,text='Horário:',font=('Athiti','13'),fg='#363636')
    label_retirada_horario_reservar.place(x=15,y=67)

    entry_retirada_horario_reservar = Entry(frame2_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_retirada_horario_reservar.place(x=85,y=75,width = 45)
    
    
    
    label_devolucao_horario_reservar = Label(frame2_reservas,text='Horário:',font=('Athiti','13'),fg='#363636')
    label_devolucao_horario_reservar.place(x=15,y=157)

    entry_devolucao_horario_reservar = Entry(frame2_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_devolucao_horario_reservar.place(x=85,y=165,width = 45)
def valida_reserva_ferramenta():
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
    if con.is_connected():
        cursor = con.cursor()
        comando_sql = "SELECT max_reserva_ferramenta FROM cadastro_ferramentas WHERE id_ferramenta=%s;"
        dado_converter = int(entry_id_ferramenta_reservar.get())
        dados = [dado_converter]
        cursor.execute(comando_sql,dados)
        dados_tabela = cursor.fetchall()
        tempo_max_reserva = int(dados_tabela[0][0])
    
    data1 = str(caixa_combo_dias_retirada.get()+'/'+caixa_combo_meses_retirada.get()+'/'+caixa_combo_anos_retirada.get()+' '+entry_retirada_horario_reservar.get()+':00:00')

    data_retirada = datetime.strptime(data1, "%d/%m/%Y %H:%M:%S")
    print(data_retirada)


    time_1 = timedelta(days=0, hours=0)
    time_2 = timedelta(hours=tempo_max_reserva)
    data_devolucao_max = time_1+time_2
    data_max = data_devolucao_max + data_retirada
    print(data_max)


    data2 = str(caixa_combo_dias_devolucao.get()+'/'+caixa_combo_meses_devolucao.get()+'/'+caixa_combo_anos_devolucao.get()+' '+entry_devolucao_horario_reservar.get()+':00:00')
    data_devolucao = datetime.strptime(data2, "%d/%m/%Y %H:%M:%S")
    print(data_devolucao)
    
    if data_devolucao<=data_max and data_devolucao>data_retirada:
        if con.is_connected():
            cursor = con.cursor()
            comando_sql = "INSERT INTO reserva_ferramenta(id_ferramenta,cpf_tecnico_responsavel,nome_tecnico_responsavel,data_hor_retirada,data_hor_devolucao) VALUES(%s,%s,%s,%s,%s);"
            data_retirada = str(caixa_combo_anos_retirada.get()+'-'+caixa_combo_meses_retirada.get()+'-'+caixa_combo_dias_retirada.get()+' '+entry_retirada_horario_reservar.get()+':00:00')
            data_devolucao = str(caixa_combo_anos_devolucao.get()+'-'+caixa_combo_meses_devolucao.get()+'-'+caixa_combo_dias_devolucao.get()+' '+entry_devolucao_horario_reservar.get()+':00:00')
            dados =(entry_id_ferramenta_reservar.get(),str(entry_cpf_tecnico_reservar.get()),str(entry_nome_tecnico_reservar.get()),data_retirada,data_devolucao)
            cursor.execute(comando_sql,dados)
            con.commit()
            messagebox.showinfo('','RESERVA CONCLUÍDA')
    else:
        messagebox.showerror('','RESERVA INVÁLIDA')
    
    inserir_nome_do_tecnico()
def inserir_nome_do_tecnico(event):
    global nome_tecnico
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
    if con.is_connected():
        cursor = con.cursor()
        comando_sql = "SELECT nome_completo_tecnicos FROM tecnicos_responsaveis WHERE cpf_tecnicos=%s;"
        dado_converter = str(entry_cpf_tecnico_reservar.get())
        dados = [dado_converter]
        cursor.execute(comando_sql,dados)
        dados_tabela = cursor.fetchall()
        nome_tecnico = str(dados_tabela[0][0])
        print(nome_tecnico)
    
    entry_nome_tecnico_reservar['state'] = 'normal'
    entry_nome_tecnico_reservar.delete(0,'end')
    entry_nome_tecnico_reservar.insert(0,nome_tecnico)
    entry_nome_tecnico_reservar['state'] = 'disabled'
def sair_da_reserva_janela():
    reservar_ferramentas.withdraw()
def consultar_reservas():
    global dados_tabela,tree_tecnicos,tree_ferramentas,tree_reservas
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_ferramentas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_reservas.place(x=32,y=20,height=224,width=485)
    scrollbar_reservas.place(x=23,y=252,width=500)
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
 
    if con.is_connected():
        tree_reservas.delete(*tree_reservas.get_children())
        cursor = con.cursor()
        comando_sql = (r"SELECT id_ferramenta,cpf_tecnico_responsavel,nome_tecnico_responsavel, DATE_FORMAT(data_hor_retirada,'%d/%m/%Y %H:%i:%s') as data_hor_retirada,DATE_FORMAT(data_hor_devolucao, '%d/%m/%Y %H:%i:%s') as data_hor_devolucao FROM reserva_ferramenta;")
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for i in range(0,len(dados_tabela)):
            tree_reservas.insert(parent='', index=i, values=dados_tabela[i])
def deletar_reserva():
    answer = askyesno(title='Confirmação',
                    message='Deseja excluir a reserva?')
    curItem = tree_reservas.focus()
    valor = tree_reservas.item(curItem)
    lista_valores = valor['values']
    
    if lista_valores=='':
        try:
            if answer:
                con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
                if con.is_connected():
                    tree_reservas.delete(*tree_reservas.get_children())
                    cursor = con.cursor()
                    comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                    comando_sql_deletar = "DELETE FROM reserva_ferramenta WHERE id_ferramenta=%s;"
                    entry_int = (str(entry_id_consulta_reserva.get()))
                    dados = [(entry_int)]
                    cursor.execute(comando_sql)
                    cursor.execute(comando_sql_deletar,dados)
                    con.commit()
                    
            else:
                pass
        except:
            messagebox.showerror('','Erro ao excluir a reserva')
    
    elif lista_valores!='':
        try:
            if answer:
                con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
                if con.is_connected():
                    tree_reservas.delete(*tree_reservas.get_children())
                    cursor = con.cursor()
                    comando_sql = "SET SQL_SAFE_UPDATES = 0;"
                    comando_sql_deletar = "DELETE FROM reserva_ferramenta WHERE id_ferramenta=%s;"
                    entry_int = (str(lista_valores[0]))
                    dados = [(entry_int)]
                    cursor.execute(comando_sql)
                    cursor.execute(comando_sql_deletar,dados)
                    con.commit()
                    
            else:
                pass
        except:
            messagebox.showerror('','Erro ao excluir a reserva')
def deletar_reserva_automatico():
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
    data_agora = datetime.now()
    dia_atual = data_agora.day
    hora_atual = data_agora.hour
    mes_atual = data_agora.month
    ano_atual = data_agora.year
    strdata = str(f'{dia_atual}/{mes_atual}/{ano_atual} {hora_atual}:00:00')
    strdata_date = datetime.strptime(strdata, "%d/%m/%Y %H:%M:%S")
    print(strdata_date, type(strdata_date))
    if con.is_connected():
        comando_sql = "SELECT id_ferramenta,data_hor_devolucao FROM reserva_ferramenta"
        cursor = con.cursor()
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        lista_ids = []
        reserva_certa = 0
        for i in range(len(dados_tabela)):
            
            
            dia_reserva = dados_tabela[i][1].day
            hora_reserva = dados_tabela[i][1].hour
            mes_reserva = dados_tabela[i][1].month
            ano_reserva = dados_tabela[i][1].year
            id_ferramenta = dados_tabela[i][0]
            strdata_devolucao = str(f'{dia_reserva}/{mes_reserva}/{ano_reserva} {hora_reserva}:00:00')
            strdata_devolucao_date = datetime.strptime(strdata_devolucao, "%d/%m/%Y %H:%M:%S")
            if strdata_date>=strdata_devolucao_date:
                reserva_certa = 1
                lista_ids.append(id_ferramenta)
            else:
                pass
    if reserva_certa==1:
        messagebox.showinfo('',(f'Os seguinte(s) ID(s) estão com a reserva em atraso: {lista_ids}'))
    else:
        pass  
def consultar_reserva_id_cpf():
    global dados_tabela,tree_tecnicos,tree_ferramentas,tree_reservas
    tree_ferramentas.place(x=3000,y=3000,height=224,width=485)
    scrollbar_ferramentas.place(x=3000,y=3000,width=500)
    
    tree_tecnicos.place(x=3000,y=3000,height=224,width=485)
    scrollbar_tecnicos.place(x=3000,y=3000,width=500)
    
    tree_reservas.place(x=32,y=20,height=224,width=485)
    scrollbar_reservas.place(x=23,y=252,width=500)
    
    con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
 
    if con.is_connected():
        tree_reservas.delete(*tree_reservas.get_children())
        cursor = con.cursor()
        comando_sql1 = (r"SELECT id_ferramenta,cpf_tecnico_responsavel,nome_tecnico_responsavel, DATE_FORMAT(data_hor_retirada,'%d/%m/%Y %H:%i:%s') as data_hor_retirada,DATE_FORMAT(data_hor_devolucao, '%d/%m/%Y %H:%i:%s') as data_hor_devolucao FROM reserva_ferramenta "+(f"WHERE id_ferramenta={(str(entry_id_consulta_reserva.get()))} OR cpf_tecnico_responsavel={(str(entry_id_consulta_reserva.get()))};"))
        cursor.execute(comando_sql1)
        dados_tabela = cursor.fetchall()
        tree_reservas.insert(parent='', index=0, values=dados_tabela[0])



def LoginBDD():
    if input_user.get()=='root' and input_acesso123.get()=='admin':
        tela_principal_admins()
    
    else:
        con = mysql.connector.connect(host='localhost',database='estacio_projeto',user='root',password='acesso123')
        try:
            if con.is_connected():
                cursor = con.cursor()
                comando_sql = "SELECT * FROM users WHERE cpf_user_tecnico=%s AND nome_sobrenome=%s;"
                dados = (str(input_acesso123.get()),str(input_user.get()))
                cursor.execute(comando_sql,dados)
                sql_login = cursor.fetchall()
                
                if sql_login[0][0]==input_acesso123.get() and sql_login[0][1]==input_user.get():
                    messagebox.showinfo('','LOGADO COM SUCESSO!')
                    tela_principal_colaboradores()
        except IndexError:
            messagebox.showerror('','USUÁRIO OU acesso123 INVÁLIDOS')

def tela_principal_admins():
    global janela,tabelas,colunas_reservas,tree_reservas,scrollbar_reservas,colunas_ferramentas,tree_ferramentas,scrollbar_ferramentas,colunas_tecnicos,tree_tecnicos,scrollbar_tecnicos,frame_tecnicos,entry_cpf_consulta,frame_ferramentas,entry_id_consulta_reserva,entry_id_consulta
    
    janela_login.withdraw()
    janela = Toplevel()
    janela.geometry('600x800')
    janela.resizable(width=FALSE, height=FALSE)

    # FRAME DE TABELAS

    tabelas = LabelFrame(janela, text='Tabelas', border=1, borderwidth=1,relief='solid', font=('Alien League Bold', 12), fg='black')
    tabelas.place(x=22, y=15, width=550, height=295)

    style_ferramentas = ttk.Style()
    style_ferramentas.theme_use("vista")

    # TABELA DE FERRAMENTAS

    colunas_ferramentas = ('ID', 'desc_ferramenta', 'fabricante', 'voltagem', 'part_number','tamanho_ferramenta', 'un_medida', 'tipo', 'material', 'reserva_max')
    tree_ferramentas = ttk.Treeview(tabelas, columns=colunas_ferramentas, show='headings')

    tree_ferramentas.column("ID", width=40, anchor=CENTER, minwidth=40, stretch=NO)
    tree_ferramentas.column("tipo", width=60, anchor=CENTER, minwidth=60, stretch=NO)
    tree_ferramentas.column("fabricante", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("material", width=85,anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("tamanho_ferramenta", width=85, anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("desc_ferramenta", width=100, anchor=CENTER, minwidth=100, stretch=NO)
    tree_ferramentas.column("reserva_max", width=90, anchor=CENTER, minwidth=90, stretch=NO)
    tree_ferramentas.column("voltagem", width=85, anchor=CENTER, minwidth=85, stretch=NO)
    tree_ferramentas.column("part_number", anchor=CENTER, width=90, minwidth=90, stretch=NO)
    tree_ferramentas.column("un_medida", width=100, anchor=CENTER, minwidth=100, stretch=NO)

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
    tree_ferramentas.place(x=3000, y=3000, height=224, width=485)

    scrollbar_ferramentas = ttk.Scrollbar(tabelas, orient='horizontal', command=tree_ferramentas.xview)

    tree_ferramentas.configure(xscrollcommand=scrollbar_ferramentas.set)
    scrollbar_ferramentas.place(x=23, y=252, width=500)

    # TABELA DE TÉCNICOS

    colunas_tecnicos = ('cpf', 'nome_completo', 'telefone', 'turno', 'equipe')
    tree_tecnicos = ttk.Treeview(tabelas, columns=colunas_tecnicos, show='headings')

    tree_tecnicos.column("cpf", width=80, anchor=CENTER,minwidth=80, stretch=NO)
    tree_tecnicos.column("nome_completo", width=173,anchor=CENTER, minwidth=173, stretch=NO)
    tree_tecnicos.column("telefone", width=80,anchor=CENTER, minwidth=80, stretch=NO)
    tree_tecnicos.column("turno", width=65, anchor=CENTER,minwidth=65, stretch=NO)
    tree_tecnicos.column("equipe", anchor=CENTER,width=85, minwidth=85, stretch=NO)

    tree_tecnicos.heading("cpf", text='CPF')
    tree_tecnicos.heading("nome_completo", text='Nome')
    tree_tecnicos.heading("telefone", text='Telefone')
    tree_tecnicos.heading("turno", text='Turno')
    tree_tecnicos.heading("equipe", text='Equipe')
    tree_tecnicos.place(x=3000, y=3000, height=224, width=485)

    scrollbar_tecnicos = ttk.Scrollbar(
        tabelas, orient='horizontal', command=tree_tecnicos.xview)

    tree_tecnicos.configure(xscrollcommand=scrollbar_tecnicos.set)
    scrollbar_tecnicos.place(x=23, y=252, width=500)

    # TABELA DE RESERVAS

    colunas_reservas= ('id_ferramenta', 'cpf_tecnico_responsavel', 'nome_tecnico_responsavel', 'data_hor_retirada', 'data_hor_devolucao')
    tree_reservas = ttk.Treeview(tabelas, columns=colunas_reservas, show='headings')

    tree_reservas.column("id_ferramenta", width=95, anchor=CENTER,minwidth=95, stretch=NO)
    tree_reservas.column("cpf_tecnico_responsavel", width=110,anchor=CENTER, minwidth=110, stretch=NO)
    tree_reservas.column("nome_tecnico_responsavel", width=173,anchor=CENTER, minwidth=173, stretch=NO)
    tree_reservas.column("data_hor_retirada", width=118, anchor=CENTER,minwidth=118, stretch=NO)
    tree_reservas.column("data_hor_devolucao", anchor=CENTER,width=118, minwidth=118, stretch=NO)

    tree_reservas.heading("id_ferramenta", text='ID da ferramenta')
    tree_reservas.heading("cpf_tecnico_responsavel", text='CPF do Técnico')
    tree_reservas.heading("nome_tecnico_responsavel", text='Nome do Técnico')
    tree_reservas.heading("data_hor_retirada", text='Data da Retirada')
    tree_reservas.heading("data_hor_devolucao", text='Data da Devolução')
    tree_reservas.place(x=3000, y=3000, height=224, width=485)

    scrollbar_reservas = ttk.Scrollbar(tabelas, orient='horizontal', command=tree_reservas.xview)

    tree_reservas.configure(xscrollcommand=scrollbar_reservas.set)
    scrollbar_reservas.place(x=23, y=252, width=500)


    # FRAME DOS TÉCNICOS

    frame_tecnicos = LabelFrame(janela, text='Técnicos', border=2, borderwidth=1,        relief='solid', font=('Alien League Bold', 12), fg='black')
    frame_tecnicos.place(x=22, y=340, width=260, height=200)

    cpf_label_deleta = Label(frame_tecnicos, text='CPF',    font=('Athiti', '13'), fg='#363636')
    cpf_label_deleta.pack(fill='x', side=TOP)

    entry_cpf_consulta = Entry(frame_tecnicos, font=('Arial', 12), relief='solid')
    entry_cpf_consulta.place(x=31, y=35, width=195)

    botao_consultar_tecnicos = Button(frame_tecnicos,text='Consultar',command=tecnicos_consultar, relief="raised", borderwidth=1, highlightthickness=0)
    botao_consultar_tecnicos.place(x=136, y=68, width=90)

    botao_mostrartodos_tecnicos = Button(frame_tecnicos,command=todos_tecnicos_consulta,text='Mostrar Todos', relief="raised", borderwidth=1, highlightthickness=0)
    botao_mostrartodos_tecnicos.place(x=32, y=68, width=90)

    botao_inserir_tecnicos = Button(frame_tecnicos,text='Inserir',command=inserir_tecnico, relief="raised", borderwidth=1, highlightthickness=0)
    botao_inserir_tecnicos.place(x=84, y=146, width=90)

    botao_deletar_tecnicos = Button(frame_tecnicos,text='Deletar',command=deletar_cpf_tecnico, relief="raised", borderwidth=1, highlightthickness=0)
    botao_deletar_tecnicos.place(x=84, y=110, width=90)

    # FRAME FERRAMENTAS

    frame_ferramentas = LabelFrame(janela, text='Ferramentas', border=1,borderwidth=1, relief='solid', font=('Alien League Bold', 12), fg='black')
    frame_ferramentas.place(x=312, y=340, width=260, height=200)

    id_label_deleta = Label(frame_ferramentas, text='ID',font=('Athiti', '13'), fg='#363636')
    id_label_deleta.pack(fill='x', side=TOP)

    entry_id_consulta = Entry(frame_ferramentas,font=('Arial', 12), relief='solid')
    entry_id_consulta.place(x=31, y=35, width=195)

    botao_consultar_ferramentas = Button(frame_ferramentas,text='Consultar',command=ferramenta_consultar, relief="raised", borderwidth=1, highlightthickness=0)
    botao_consultar_ferramentas.place(x=136, y=68, width=90)

    botao_mostrartodos_ferramentas = Button(frame_ferramentas,command=todas_ferramenta_consulta,text='Mostrar Todos', relief="raised", borderwidth=1, highlightthickness=0)
    botao_mostrartodos_ferramentas.place(x=32, y=68, width=90)

    botao_inserir_ferramentas = Button(frame_ferramentas,text='Inserir',command=inserir_ferramenta, relief="raised", borderwidth=1, highlightthickness=0)
    botao_inserir_ferramentas.place(x=84, y=146, width=90)

    botao_deletar_ferramentas = Button(frame_ferramentas,command=deletar_id_ferramenta,text='Deletar', relief="raised", borderwidth=1, highlightthickness=0)
    botao_deletar_ferramentas.place(x=84, y=110, width=90)

    # FRAME DE RESERVA 

    frame_reservas = LabelFrame(janela, text='Reservas', border=1,borderwidth=1, relief='solid', font=('Alien League Bold', 12), fg='black')
    frame_reservas.place(x=170, y=570, width=260, height=200)

    id_label_deleta = Label(frame_reservas, text='ID ou CPF',font=('Athiti', '13'), fg='#363636')
    id_label_deleta.pack(fill='x', side=TOP)

    entry_id_consulta_reserva = Entry(frame_reservas, font=('Arial', 12), relief='solid')
    entry_id_consulta_reserva.place(x=31, y=35, width=195)

    botao_consultar_reservas = Button(frame_reservas,text='Consultar',command=consultar_reserva_id_cpf, relief="raised", borderwidth=1, highlightthickness=0)
    botao_consultar_reservas.place(x=136, y=68, width=90)

    botao_mostrartodos_reservas = Button(frame_reservas,command=consultar_reservas,text='Reservas', relief="raised", borderwidth=1, highlightthickness=0)
    botao_mostrartodos_reservas.place(x=32, y=68, width=90)

    botao_inserir_reservas = Button(frame_reservas,text='Reservar',command=janela_reserva, relief="raised", borderwidth=1, highlightthickness=0)
    botao_inserir_reservas.place(x=84, y=146, width=90)

    botao_deletar_reservas = Button(frame_reservas,command=deletar_reserva,text='Deletar', relief="raised", borderwidth=1, highlightthickness=0)
    botao_deletar_reservas.place(x=84, y=110, width=90)

    botao_voltar_principal = Button(janela, text='Voltar',command=voltar_pra_principal,relief="raised", borderwidth=1, highlightthickness=0)
    botao_voltar_principal.place(x=22, y=750, width=90)
    
    deletar_reserva_automatico()

def reservar_ferramenta():
    email_empresa = 'videojfxcolaboradores@gmail.com'
    acesso123 = 'wrppyitugzedpfjo'

    corpo_email = (f"""
    <p><b>RESERVAR FERRAMENTA<b></p>
    <p>ID da ferramenta: {entry_id_ferramenta_solicitar.get()}</p>
    <p>CPF do técnico: {entry_cpf_tecnico_solicitar.get()}<p>
    <p>Email do técnico: {entry_email_tecnico_solicitar.get()}<p>
    <p>Desc. da solicitação: {entry_desc_solicitacao.get('1.0', 'end')}<p>
    <p>Data de retirada: {caixa_combo_dias_retirada_solicitacao.get()}/{caixa_combo_meses_retirada_solicitacao.get()}/{caixa_combo_anos_retirada_solicitacao.get()} as {entry_retirada_horario_solicitacao.get()}:00:00<p>
    <p>Data de devolução: {caixa_combo_dias_devolucao_solicitacao.get()}/{caixa_combo_meses_devolucao_solicitacao.get()}/{caixa_combo_anos_devolucao_solicitacao.get()} as {entry_devolucao_horario_solicitacao.get()}:00:00<p>
    """)

    msg = email.message.Message()
    msg['Subject'] = "Reserva de ferramenta"
    msg['From'] = 'videojfxcolaboradores@gmail.com'
    msg['To'] = 'janderjr2004@gmail.com'
    password = 'wrppyitugzedpfjo'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    messagebox.showinfo('','Reserva solicitada, aguarde retorno no seu email')

def tela_principal_colaboradores():
    global entry_id_ferramenta_solicitar,entry_cpf_tecnico_solicitar,entry_email_tecnico_solicitar,entry_desc_solicitacao,caixa_combo_dias_retirada_solicitacao,caixa_combo_meses_retirada_solicitacao,caixa_combo_anos_retirada_solicitacao,entry_retirada_horario_solicitacao,caixa_combo_dias_devolucao_solicitacao,caixa_combo_meses_devolucao_solicitacao,caixa_combo_anos_devolucao_solicitacao,entry_devolucao_horario_solicitacao,solicitar_reserva
    janela_login.withdraw()
    solicitar_reserva = Toplevel()
    solicitar_reserva.title(' ')
    solicitar_reserva.geometry('442x425')
    solicitar_reserva.resizable(width=FALSE,height=FALSE)

    frame1_reservas = Frame(solicitar_reserva,width=225,height=400)
    frame2_reservas = Frame(solicitar_reserva,width=217,height=400)
    frame1_reservas.place(x=0,y=50)
    frame2_reservas.place(x=225,y=50)

    img_videojfx_reserva = PhotoImage(file='VIDEOJFX.png')

    label_reservas_solicitar = Label(solicitar_reserva,text='RESERVAR',font=('Athiti SemiBold','19'),fg='#363636')
    label_reservas_solicitar.pack(side=TOP)

        # FRAME 1

    label_id_ferramenta_reservar = Label(frame1_reservas,text='ID da Ferramenta *',font=('Athiti','13'),fg='#363636')
    label_id_ferramenta_reservar.place(x=15,y=10)

    entry_id_ferramenta_solicitar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_id_ferramenta_solicitar.place(x=18,y=40,width = 180)


    label_cpf_tecnico_reservar = Label(frame1_reservas,text='CPF do Técnico *',font=('Athiti','13'),fg='#363636')
    label_cpf_tecnico_reservar.place(x=15,y=75)

    entry_cpf_tecnico_solicitar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_cpf_tecnico_solicitar.place(x=18,y=105,width = 180)


    label_email_tecnico_reservar = Label(frame1_reservas,text='Email do Técnico *',font=('Athiti','13'),fg='#363636')
    label_email_tecnico_reservar.place(x=15,y=135)

    entry_email_tecnico_solicitar = Entry(frame1_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_email_tecnico_solicitar.place(x=18,y=165,width = 180)

    botao_sair_reservar = Button(frame1_reservas,command=voltar_pra_principal_colaboradores,text='Sair',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_sair_reservar.place(x=18,y=340,width=90)

        # FRAME 2

    label_retirada = Label(frame2_reservas,text='Data da Retirada *',font=('Athiti','13'),fg='#363636')
    label_retirada.place(x=15,y=10)

    label_devolucao = Label(frame2_reservas,text='Data da Devolução *',font=('Athiti','13'),fg='#363636')
    label_devolucao.place(x=15,y=100)


    botao_reservar_ferramenta = Button(frame2_reservas,command=reservar_ferramenta,text='Reservar',relief = "raised",borderwidth = 1,highlightthickness = 0)
    botao_reservar_ferramenta.place(x=108,y=340,width=90)


    escolher_dia_retirada_solicitacao = StringVar()
    caixa_combo_dias_retirada_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_dia_retirada_solicitacao)
    caixa_combo_dias_retirada_solicitacao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    caixa_combo_dias_retirada_solicitacao.place(x=18,y=39,width = 45,height=28)

    escolher_meses_retirada_solicitacao = StringVar()
    caixa_combo_meses_retirada_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_meses_retirada_solicitacao)
    caixa_combo_meses_retirada_solicitacao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12']
    caixa_combo_meses_retirada_solicitacao.place(x=85,y=39,width = 45,height=28)

    escolher_anos_retirada_solicitacao = StringVar()
    caixa_combo_anos_retirada_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_anos_retirada_solicitacao)
    caixa_combo_anos_retirada_solicitacao['values']= ["2021","2022","2023"]
    caixa_combo_anos_retirada_solicitacao.place(x=152,y=39,width = 50,height=28)
        
        
        
    escolher_dia_devolucao_solicitacao = StringVar()
    caixa_combo_dias_devolucao_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_dia_devolucao_solicitacao)
    caixa_combo_dias_devolucao_solicitacao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    caixa_combo_dias_devolucao_solicitacao.place(x=18,y=129,width = 45,height=28)

    escolher_meses_devolucao_solicitacao = StringVar()
    caixa_combo_meses_devolucao_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_meses_devolucao_solicitacao)
    caixa_combo_meses_devolucao_solicitacao['values']= ['01','02','03','04','05','06','07','08','09','10','11','12']
    caixa_combo_meses_devolucao_solicitacao.place(x=85,y=129,width = 45,height=28)

    escolher_anos_devolucao_solicitacao = StringVar()
    caixa_combo_anos_devolucao_solicitacao = ttk.Combobox(frame2_reservas,textvariable=escolher_anos_devolucao_solicitacao)
    caixa_combo_anos_devolucao_solicitacao['values']= ["2021","2022","2023"]
    caixa_combo_anos_devolucao_solicitacao.place(x=152,y=129,width = 50,height=28)
        
    label_retirada_horario_reservar = Label(frame2_reservas,text='Horário:',font=('Athiti','13'),fg='#363636')
    label_retirada_horario_reservar.place(x=15,y=67)

    entry_retirada_horario_solicitacao = Entry(frame2_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_retirada_horario_solicitacao.place(x=85,y=75,width = 45)
        
        
        
    label_devolucao_horario_reservar = Label(frame2_reservas,text='Horário:',font=('Athiti','13'),fg='#363636')
    label_devolucao_horario_reservar.place(x=15,y=157)

    entry_devolucao_horario_solicitacao = Entry(frame2_reservas,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_devolucao_horario_solicitacao.place(x=85,y=165,width = 45)

    label_desc_reservar = Label(frame1_reservas,text='Desc. da Solicitação *',font=('Athiti','13'),fg='#363636')
    label_desc_reservar.place(x=15,y=195)

    entry_desc_solicitacao = Text(solicitar_reserva,highlightthickness = 0,font=('Arial',10),relief='solid')
    entry_desc_solicitacao.place(x = 18, y = 275,width = 180,height = 85)

    image_videojfx = Label(frame2_reservas,image=img_videojfx_reserva)
    image_videojfx.place(x=2,y=188)

    solicitar_reserva.mainloop()

def voltar_pra_principal():
    janela.withdraw()
    janela_login.deiconify()

def voltar_pra_principal_colaboradores():
    solicitar_reserva.withdraw()
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


label_acesso123 = Label(janela_login,fg='black', text='Palavra passe', font=estilo_da_fonte_widgets,background='white')
label_acesso123.place(x=46,y=220)

input_acesso123 = Entry(janela_login, width=25, justify='left',font=('',14),highlightthickness=1, relief='solid',show='*',fg='black',background='white')
input_acesso123.place(x=50,y=250,width=300)

botao_entrar = Button(janela_login,command=LoginBDD, text='Entrar',relief='flat',bg='black',fg='white',width=13,font=estilo_da_fonte_widgets)
botao_entrar.place(x=130,y=310)

janela_login.mainloop()