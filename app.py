from flask import Flask, render_template, request

app  = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # For demonstration purposes, we use hardcoded credentials
        # In a real application, you would verify against a database
        trueUsername = "<script>alert(1)</script>"
        
        truePassword = "<script>alert(1)</script>"
        # Process the username and password as needed
        if not username or not password:
            return render_template('index.html' , message="Please provide both username and password." , trueUsername=trueUsername, color="red") 
        if username == trueUsername and password == truePassword:
            return render_template('index.html' , message="Welcome," ,trueUsername=trueUsername, color="green")
        else:
            return render_template('index.html' , message="Invalid credentials." , color="red")
        
          



if __name__ == "__main__":
    app.run(debug=True)