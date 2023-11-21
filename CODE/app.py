from flask import Flask, render_template, request
import  numpy as np
import pickle

app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result",methods=['POST','GET'])
def result():
    l=[]
    l.append(float(request.form['v1']))
    l.append(float(request.form['v2']))
    l.append(float(request.form['v3']))
    l.append(float(request.form['v4']))
    l.append(float(request.form['v5']))
    l.append(float(request.form['v6']))
    l.append(float(request.form['v7']))
    l.append(float(request.form['v8']))
    l.append(float(request.form['v9']))
    l.append(float(request.form['v10']))
    l.append(float(request.form['v11']))
    l.append(float(request.form['v12']))
    l.append(float(request.form['v13']))
    l.append(float(request.form['v14']))
    l.append(float(request.form['v15']))
    l.append(float(request.form['v16']))
    l.append(float(request.form['v17']))
    l.append(float(request.form['v18']))
    l.append(float(request.form['v19']))
    l.append(float(request.form['v20']))
    l.append(float(request.form['v21']))
    l.append(float(request.form['v22']))
    dbfile=open(r'D:/New folder (2)/knn.pkl', 'rb')
    db=pickle.load(dbfile)
    predicted_price = db.predict(np.array([l]).reshape(1,-1))
    t=int(predicted_price[0])
    if t==0:
        return render_template('noprakinson.html')
    else:
        return render_template('prakinson.html')

if __name__=="__main__":
    app.run(debug=True,port=7384)