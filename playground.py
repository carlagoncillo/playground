from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def play():
    return render_template("level1.html")

@app.route('/play/<int:num>')
def playx(num):
    return render_template("level2.html", num=num )

@app.route('/play/<int:num>/<color>')
def level3(num, color):
    return render_template('level3.html', num=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
