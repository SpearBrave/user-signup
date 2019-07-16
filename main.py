from flask import Flask, request, redirect, render_template
import re


app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/',methods=["GET"])
           

def apple():

    return render_template("index.html")
@app.route('/',methods=["POST"])

def pear():
    input_username =request.form["username"]
    input_password =request.form["password"]        
    input_confirmationP = request.form["verify"]
    input_email = request.form["email"]
   
    erroruser=""        
    error_password=""
    verifyP=""        
    erroremail=""

    In_User=""
    
    
    In_Email=""

    
    


    if  re.search(" ", input_username):
        erroruser= "No Spaces!"
        In_User=input_username
    
    elif len(input_username) > 20 or len(input_username) <3:
    
        erroruser="3-20 characters !"
        In_User=input_username
    
    

    



    
    if  re.search(" ", input_password):
        error_password= "No Spaces!"
        

   
    elif len(input_password) > 20 or len(input_password) <3:
        error_password= "3-20 character !"
      
    
   
    
    
    
    
    if input_confirmationP != input_password:
        verifyP="Does not match !"
       
   

    if input_email != "":

        
        
        if input_email.count("@")!= 1 and input_email.count(".")!=1 :
            erroremail= "1 @ and ."

        elif re.search(" ", input_email):
            erroremail= "no spaces !"
            In_Email=input_email
        elif len(input_email) > 20 or len(input_email) <3:
            erroremail= "3- 20"
            In_Email=input_email
            
        return render_template("index.html",user_error=erroruser,pass_error=error_password,verify_error_=verifyP,email_error=erroremail)
    
    if erroruser =="" and error_password=="" and verifyP=="" and erroremail=="":
        return render_template("welcome.html", USER=input_username)
    input_username
  

    

    

app.run()