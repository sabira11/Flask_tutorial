from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to the webpage"

@app.route('/members/<int:num>')
def members(num):
    return "There are total " + str(num) +" people present in the meeting"
@app.route('/dish/<int:num>')
def serve_dish(num):
    return "There are total " + str(num) + " dishes served in the meeting"

@app.route('/meeting_state/<int:num1>')
def status(num1):
    results=""
    if num1<10:
        results="members"
    else:
        results="serve_dish"
    return redirect(url_for(results,num=num1))
if __name__=='__main__':
    app.run(debug=True)
   
