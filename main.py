from flask import Flask,render_template,request
app =Flask(__name__)## it tells flask where application is located
import joblib
model= joblib.load(r'C:\Users\Win 11\Desktop\data science\6-months-data-science\machine learning\bike_project\bike project\Model\bike_price_model')
##<<<<<<<<<<<<<<<day1>>>>>>>>>>>>>>>
# @app.route("/") ## it showsthe home route of the functionand @ is a decorator which runs this in a website 
# def home():  ## it is a function 
#     return "hello today we are learning flask"

# @app.route("/my_intro")
# def myintro():
#     return""" good morning i am saloni"""
# @app.route("/aboutme")
# def about():
#   return"""i am studying data science """

# if __name__=="__main__":
#     app.run(debug=True) ## automatically reads the server when we change the code

##<<<<<<<<<<<<<<<<<<<day2>>>>>>>>>>>>>>>>>>>
##task2  postman and api fatch method



@app.route("/")
def index():
 return render_template("index.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/predict",methods=["GET","POST"])
def predict():

  if request.method =="POST":
        kms_driven = float(request.form["kms_driven"])
        owner = int(request.form["owner"])
        age = int(request.form["age"])
        power = float(request.form["power"])
        brand = int(request.form["brand"])

        print("\n=====bike information=====")
        print("kms_driven:",kms_driven)
        print("owner:",owner)
        print("age:",age) 
        print("power:",power)
        print("brand:",brand)

        ## create input for model
        input_data = [[kms_driven, owner, age, power, brand]]
        print("input_data:",input_data)


        ## prediction
        prediction = model.predict(input_data)
        print("predicted bike price:",prediction[0])

        return render_template("index.html",prediction=round(prediction[0],2)) ## round is used to round the value upto 2 decimal places

if __name__=="__main__":
 app.run(debug=True) ## automatically reads the server when we change the code





## post method jab bi apan frontend sa backend ma aata ha toh apan post method ka use karta ha
