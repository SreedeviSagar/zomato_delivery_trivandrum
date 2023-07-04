import pickle
from flask import Flask,request,app,url_for,render_template
import pandas as pd
import numpy as np

app=Flask(__name__)
#load pickle file

zomato_tvm=pd.read_pickle(open('zomato_tvm.pkl','rb'))

def dish_input(dish_name_req):
    zomato_df1=pd.DataFrame()
    dish_name_req=dish_name_req.lower()
    zomato_df1=zomato_tvm[zomato_tvm['dish_name'].str.contains(dish_name_req)]
    zomato_df1=zomato_df1.sort_values(by='dish_price_INR',ascending=False)
    lists1=zomato_df1['restaurant_name'].values
    lists2=zomato_df1['dish_name'].values
    lists3=zomato_df1['dish_price_INR'].values
    final_list=list(zip(lists1,lists2,lists3))
    return final_list

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods=['POST'])
def predict():
    dish_name_req=request.form.get('dish_name')
    result_list=dish_input(dish_name_req)
    return render_template('index.html',result_list=result_list)
    
if __name__=="__main__":
    app.run(debug=True)