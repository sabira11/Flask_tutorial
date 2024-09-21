from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/members/<int:num>')
def members(num):
    return "there are total " + str(num) +" people present in the meeting"
@app.route('/attend/<int:num>')
def attend_mem(num):
    return render_template('attend.html',result=num) 
@app.route('/leave/<int:num2>')
def leave(num2):
    return "Total " +str(num2)+ " people need to leave the meeting"

@app.route('/meeting_state/<int:num1>')
def status(num1):
    results=""
    if num1<10:
        results="attend_mem"
    else:
        results="leave"
    return redirect(url_for(results,num=num1))
@app.route('/submit',methods=['POST','GET'])
def submit():
    present_mem=0
    extra_mem=0
    if request.method=='POST':
        expect=float(request.form['members'])
        present=float(request.form['attend'])
        leave=float(request.form['leave']) 
        present_mem=present-leave
        extra_mem=abs(expect - present_mem)
    res=""
    if present_mem>=expect:
        res="leave"
    else:
        res="attend_mem"
    return redirect(url_for(res,num=present_mem,num2=extra_mem))
if __name__=='__main__':
    app.run(debug=True)
   
