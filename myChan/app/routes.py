from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : "SMW"}
    return '''
    <html>
        <head>
            <title>Home Page - SMW myChan</title>
        </head>
        <body> 
            <h1> Hello ''' + user['username'] + '''!</h1>
        </body>
                
    </html>
    '''