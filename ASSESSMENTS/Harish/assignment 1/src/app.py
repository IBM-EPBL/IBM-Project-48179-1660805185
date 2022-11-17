from flask import Flask,render_template ,url_for ,request, redirect
app= Flask(__name__)
@app.route('/success ')
def success(name):
    return "welcome " + name
@app.route('/')
def index():
    return render_template("registration.html")
@app.route('/registration', methods =["POST","GET"])
def registration():
    if request.method == "POST":
        name = request.form['name']
        return redirect(url_for('success' , name= name))
    

if __name__=='__main__':
    app.run (debug=True)
