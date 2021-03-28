from flask import Flask, render_template, request, redirect
import requests
import json
from dotenv import dotenv_values
import pandas as pd
from bokeh.plotting import figure, show
#import .alpha_vantage# import make_graph


app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      #plot = make_graph(ticker_name, type_of_graph)
      #script, div = components(plot)
      return render_template("result.html",result = result)#, the_div=div, the_script=script)

if __name__ == '__main__':
  app.run(port=33507)