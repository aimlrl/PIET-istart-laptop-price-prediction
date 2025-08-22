import streamlit as st
from predict import get_column_names, get_ordinal_columns_encodings, get_feature_mean_std, get_trained_weights
import numpy as np

st.title("Used Laptop Price Predictor")

all_X_columns = get_column_names()
ordinal_columns_encodings = get_ordinal_columns_encodings()
k = ordinal_columns_encodings.keys()
v = ordinal_columns_encodings.values()

print(all_X_columns)

inputX = dict(zip(range(len(list(k))),list(k)))

company = st.radio("### **Please select brand of your laptop**",list(ordinal_columns_encodings[inputX[0]]),
                   horizontal=True)
typename = st.radio("### **Please select the type of your laptop**",list(ordinal_columns_encodings[inputX[1]]),
                    horizontal=True)
inches = st.text_input("### **Please enter the size of the screen in inches**",value="0")
screenresolution = st.radio("### **Please select the screen resolution as well as technology of the display**",
                            list(ordinal_columns_encodings[inputX[2]]),horizontal=True)
cpu = st.radio("### **Please select the CPU in your laptop**",list(ordinal_columns_encodings[inputX[3]]),
               horizontal=True)
ram = st.text_input("### **Please enter the RAM available in your laptop**",value="0")
hdd = st.radio("### **Please select the Hard drive configuration of your laptop**",list(ordinal_columns_encodings[inputX[4]]))
gpu = st.radio("### **Please select the type of GPU your laptop has**", list(ordinal_columns_encodings[inputX[5]]))
weight = st.text_input("### **Please enter the weight of your laptop**",value="0")
isandroid = st.text_input("### **Does your laptop has Andoid OS (Please enter \"yes\" or \"no\")**",value="no")

no_yes_dict = {"no":0.0, "yes": 1.0} 

input_features = [company,typename,float(inches),screenresolution,cpu, float(ram), hdd, gpu, float(weight), 
                  no_yes_dict[isandroid]]

all_input_features_mean_std = get_feature_mean_std()

x_vec = list()

for idx, input_feat in enumerate(input_features):

    if isinstance(input_feat) == str:
        x_vec.append((ordinal_columns_encodings[inputX[idx]][input_feat] -\
                       all_input_features_mean_std[0][idx])/all_input_features_mean_std[1][idx])
    else:
        x_vec.append((input_feat - all_input_features_mean_std[0][idx])/all_input_features_mean_std[1][idx])

x_vec = np.array(x_vec)
x_vec = x_vec.reshape(1,x_vec.shape[0])

ws = get_trained_weights()

log_y_hat = ws[0] + np.matmul(x_vec,ws[1])
y_hat = np.exp(log_y_hat)[0,0]

if st.button("Predict the Price"):
    st.success("The Price of the Laptop is {}".format(y_hat))




