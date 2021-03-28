from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def index():
  if request.method == 'POST':
      result = request.form
      return render_template('index.html',result = result)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
