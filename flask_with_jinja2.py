from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index_sub.html')
@app.route('/success/<int:score>')
def success(score):
    res=""
    gpa=""
    if score>=80:
        gpa="A+"
    elif score>=70:
        gpa='A'
    elif score>=60:
        gpa='A-'
    elif score>=50:
        gpa='B+'
    elif score>=40:
        gpa='B'
    else:
        gpa='F'
    
    if score>=50:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,
         'result':res,
         'total_gpa':gpa}
    return render_template('result.html',result=exp)


### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score=total_score))
if __name__=='__main__':
    app.run(debug=True)