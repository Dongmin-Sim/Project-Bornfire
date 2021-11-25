from flask import redirect,url_for
import re



def password_validate(pw,pw2):
    validation_pw = re.compile('(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,50}$') 
    if pw != pw2:
        return redirect(url_for('login.get_login'))
        
    if validation_pw.match(pw) != None:
        pass
    else:
        return redirect(url_for('login.get_login'))

def email_validate(email):
    validation_email = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if validation_email.match(email) != None:
        pass
    else:
        return redirect(url_for('login.get_login'))