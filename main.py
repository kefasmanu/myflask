from flask import Flask, request
from datetime import datetime

app = Flask("MY FIRST APPLICATION")

@app.route('/')
def index():
    return """ <h1>Kefas Website</h1> 
               <p>My name is Kefas</p>
           """

@app.route('/contact')
def contact_page():
    return "Contact me at kefasmanu3@gmail.com"

@app.route('/date')
def show_date():
    date = str(datetime.now())
    return f'Today is {date}'

@app.route('/birthyear', methods =['POST','GET'])
def calc_birthyear():
    if request.method == 'POST': #User is posting or Submitting  his/her information
        return f"""
                        <form action = "/birthyear" method="POST">
                                        <input type ="number" name= "birthyear" placeholder ="Birthyear e.g 2020">
                                        <button type = "submit"> submit</button>
                                    </form>
                        your submission, your age is {2022 - int(request.form.get('birthyear'))}
                """
    elif request.method =='GET':# User is asking for this page
        return """From
                <form action = "/birthyear" method="POST">
                    <input type ="number" name= "birthyear" placeholder ="Birthyear e.g 2020">
                    <button type = "submit"> submit</button>
                </form>
    
               """

if __name__ == '__main__':
    app.run()