# For Ms.Mendez:
#Hit run

#These are to import dependencies
from replit import db
from flask import *
from flask_restful import *

import random
from werkzeug.security import *
import traceback
try:
  from googlesearch import search
except:
  print("Oops, you forgot to go to shell and type pip install google!")

#This is to allow javascript to send web request as this is a diffrent domain!
from flask_cors import *

#This is to initizize
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

#A intager generator
def randomnums():
    firstdig = random.randint(0,9)
    seconddig = random.randint(0,9)
    thirddig = random.randint(0,9)
    all3dig = str(firstdig) + str(seconddig) + str(thirddig)
    return all3dig

class Operations(Resource):
    def get(self,name):
        return jsonify({'error':'NO GET ALLOWED!!!!!!!!'})
    def post(self,name):
        try:
          #Athentication
            username = request.authorization["username"]
            password = request.authorization["password"]
            username = username.replace("'","")
            password = password.replace("'","")
            
            proceed = True
            value = db[f"{username}:{password}"]
          
            
            
            if proceed == True:
              #If correct url
              
                if name == "add":
                  #First get json body!
                    lol = request.get_json()
                    #d = json.dumps(lol)
                    #Set default uuid = 0
                    uuid = 0

                    #Infinately try to see if variable is same
                    while True:
                        try:
                          value = db[f"{uuid}"]
                          uuid = randomnums()
                        except:
                          break
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) + int(secondvar)
                        }
                    print("Putting into database")
                   
                    db[f"{uuid}"] = str(uuid) + str(lol) + str(result)
                    
                    return jsonify(result)

                if name == "sub":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        try:
                          value = db[f"{uuid}"]
                          uuid = randomnums()
                        except:
                          break

                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) - int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    db[f"{uuid}"] = str(uuid) + str(lol) + str(result)
                    
                    return jsonify(result)

                if name == "mul":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        try:
                          value = db[f"{uuid}"]
                          uuid = randomnums()
                        except:
                          break
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) * int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    db[f"{uuid}"] = str(uuid) + str(lol) + str(result)
                    
                    return jsonify(result)

                if name == "mod":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        try:
                          value = db[f"{uuid}"]
                          uuid = randomnums()
                        except:
                          break

                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) % int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    db[f"{uuid}"] = str(uuid) + str(lol) + str(result)
                    
                    return jsonify(result)

                if name == "div":
                    lol = request.get_json()
                    d = json.dumps(lol)
                    uuid = 0
                    while True:
                        try:
                          value = db[f"{uuid}"]
                          uuid = randomnums()
                        except:
                          break
                    firstvar = lol["arg1"]
                    secondvar = lol["arg2"]
                    result = {
                        "result": int(firstvar) / int(secondvar)
                        }
                    print("Putting into database")
                    data = json.dumps(lol, indent=2).encode('utf-8')
                    parody = {
                        "arg1":lol["arg1"],
                        "arg2":lol["arg2"]
                    }
                    db[f"{uuid}"] = str(uuid) + str(lol) + str(result)
                    
                    return jsonify(result)
                else:
                    return jsonify({"error":"Wrong operator"})
        #Error if none is inputed
        except:
            traceback.print_exc()
            return jsonify({"error":"Wrong username;Wrong password! If you have no account, use /signup!"})

#This is to create accounts
class SignUp(Resource):
    def get(self):
        return jsonify({"error":"No GET!!!!!"})
    def post(self):
        username = request.authorization["username"]
        password = request.authorization["password"]
        username = username.replace("'","")
        password = password.replace("'","")
        db[f"{username}:{password}"] = f"{username}:{password}"
        return "Signed you up!"



class LogIn(Resource):
    def post(self):
        return jsonify({"error":"No POST!!!!!"})
    def get(self):
        username = request.authorization["username"]
        password = request.authorization["password"]
        username = username.replace("'","")
        print(username)
        print(password)
        try:
            value = db[f"{username}:{password}"]
        
            print("checkmate")
           
            return jsonify({"success":"Logged in!"})
        except:
            return jsonify({"error":"Wrong username or password!"})
            
   
 #These are to route the classes
api.add_resource(Operations,'/api/operation/<string:name>') #localhost/api/operattion/add
api.add_resource(SignUp,'/api/signup')
api.add_resource(LogIn,"/api//testlogin")

#Now, this is a help page
@app.route('/', methods=['GET','POST'])
def index():
    return """
        /api/operation/add - addition
        /api/operation/sub - subtraction
        /api/operation/mul - multiplication
        /api/operation/div - division
        /api/operation/mod - modulo
        /api/signup - create account!
        /api/search/ - search
        /api/forgotpassword - forgot password
        /api/testlogin - Test login!
        EVERY REQUEST HAS TO BE POST!!!!!!!! BUT /api/search has to be GET

        for math operations:
            body:
            {
                "arg1":number,
                "arg2":number
            }(IN JSON MODE!)
        
        for search:
            /api/search/<query>
        YOU NEED TO AUTHENTICATE!!!!!!
        
    """

@app.route('/api/search/<string:query>')
def searchman(query):
    try:

            username = request.authorization["username"]
            password = request.authorization["password"]
            username = username.replace("'","")
            password = password.replace("'","")
            print(username)
            print(password)
            value = db[f"{username}:{password}"]
            searchlist = []
            for i in search(query,num=10,stop=10):
                searchlist.append(i)
            x = f"""
            {searchlist[0]}
            {searchlist[1]}
            {searchlist[2]}
            {searchlist[3]}
            {searchlist[4]}
            {searchlist[5]}
            {searchlist[6]}
            {searchlist[7]}
            {searchlist[8]}
            {searchlist[9]}
            """
            print(x)
            urls = {
                    "url1":searchlist[0],
                    "url2":searchlist[1],
                    "url3":searchlist[2],
                    "url4":searchlist[3],
                    "url5":searchlist[4],
                    "url6":searchlist[5],
                    "url7":searchlist[6],
                    "url8":searchlist[7],
                    "url9":searchlist[8],
                    "url10":searchlist[9]
                }
            return jsonify(urls)
    except:
        traceback.print_exc()
        return jsonify({"error":"Wrong username or password! If you have no account, use /signup!"})
   
if __name__ == '__main__':
    app.run(port=80,host='0.0.0.0')