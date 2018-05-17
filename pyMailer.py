import smtplib
from tkinter import *
from smtplib import SMTPException


#enviar email via hotmail
def hotmail( ):

    usermail = usuario_email.get()
    receivermail = destinatario_email.get()           
    server = smtplib.SMTP('smtp-mail.outlook.com:587')
    pass_word = password.get()
    subject = assunto.get()
    main_message = body.get('1.0', 'end-1c')
    Body = '\r\n'.join([
        'De: %s' % usermail,
        'Para: %s' % receivermail,
        'Assunto: %s' % subject,
        '',
        '%s' % main_message ])


    try:
            server=smtplib.SMTP('smtp-mail.outlook.com:587')
            server.ehlo()
            server.starttls()
            server.login(usermail, pass_word  )
            server.sendmail(usermail,receivermail, Body)

            text.insert(1.0, 'Mensagen enviada')

    #caso de erro
    
    except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
        text.insert(1.0, 'Mensagen não enviada')
    finally:
           server.quit()





#Interface
root= Tk(className = " Hotmail App" )
root.config(bg = "blue", )

#usuario email
usuario_email = Label(root, text = "Entre com seu usuario do Hotmail: ")
usuario_email.pack()
usuario_email.config(bg = "black", fg = "white")

usuario_email = Entry(root, bd = 8)
usuario_email.pack(fill = X)


#destinatario email
destinatario_email = Label(root, text = ("Insira o email do remetente: "))
destinatario_email.pack()
destinatario_email.config(bg = "black", fg = "white")


destinatario_email = Entry(root, bd = 8)
destinatario_email.pack(fill = X)

#Assunto
assunto = Label(root, text = "Assunto da mensagen: ")
assunto.pack( )
assunto.config(bg = "black", fg = "white")


assunto = Entry(root, bd = 8)
assunto.pack(fill = X)

#Body da mensagen
body = Text(root, font = "Tahoma",  relief = SUNKEN , bd = 8)
body.config(bg = "cyan", height = 15)
body.pack(fill = BOTH, expand = True)

#password
password = Label(root, text = "Insira a senha para validar:  ")
password.pack()
password.config(bg = "black", fg = "white")

password= Entry(root, show = '*', bd = 8)
password.pack(fill = X)

#Butão de envio
submit_mail = Button(root, bd = 8, text = "Enviar", command = hotmail)
submit_mail.pack(fill = X)

#feed back
text = Text(root, font = "Tahoma",  relief = SUNKEN , bd = 8)
text.config(bg= "cyan",  height = 2)
text.pack(fill = BOTH, expand = True)


root.mainloop()