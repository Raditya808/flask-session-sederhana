from flask import Flask, redirect ,request,url_for,session

app = Flask(__name__)

# secret_key
app.secret_key = 'wjdhdjsh'


@app.route('/')
def index():
    # session username akan dikirim hasil nya kesini
    if 'username' in session:
        return f"""
            <!DOCTYPE html>
            <html>
                <head>
                <title>Hasil session</title>
                </head>
                    <body>
                    <h1>Hasil</h1>
                    <p>Halo {session['username']}</p>
                    
                    <button>
                   <a href="{url_for('logout')}">Logout</a> 
                   </button>
                    </body>
            </html>
            """
    return f"""
    <!DOCTYPE html>
        <html>
            <head>
                <title>Session form</title>
            </head>
            <body>
            <h1>Logged session</h1>
                <button>
                    <!-- button ke function login -->
                    <a href="{url_for('login')}">Login</a>
                </button>
            </body>
        </html>
    
    """

# login 
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        # mengirim menggunakan syntax session bernama username yang akan di kirim ke index 
        session['username'] = request.form['nama']
        return redirect(url_for('index'))
    return f"""
    <form method="POST">
        <h1>Silahkan Masukan Sesuatu</h1>
        <input type="text" name="nama" placeholder="Masukan nama:">
        <input type="submit" value="kirim">
    </form>
    """


# logout
@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True,port=5000)
