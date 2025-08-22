import pickle
import numpy as np

def get_ordinal_columns_encodings():

    with open("./ordinal_columns_encodings.pkl","rb") as file_handle:
        ordinal_columns_encodings = pickle.load(file_handle)

    return ordinal_columns_encodings



def get_column_names():

    with open("./all_column_names.pkl","rb") as file_handle:
        all_X_columns = pickle.load(file_handle)

    return all_X_columns

"""
x_vec = list()

for idx, single_column in enumerate(all_X_columns):
    print("ENTER THE VALUE OF {}".format(single_column))
    print("PLEASE CHOOSE ANY OF THE VALUE FROM BELOW MENTIONED VALUES")

    if idx >= 9:
        print("Either 0 (No) or 1 (Yes)")
        value = float(input("Please enter the Value of is{}\n".format(single_column)))
        x_vec.append(value)
    else:
        if single_column not in ordinal_columns_encodings.keys():
            print("From 0 to Infinity")
            value = float(input("Please enter the Value of {}\n".format(single_column)))
            x_vec.append(value)
        else:
            print(list(ordinal_columns_encodings[single_column].keys()))
            value = str(input("Please enter the Value of {}\n".format(single_column)))
            x_vec.append(ordinal_columns_encodings[single_column][value])
    print("\n\n")

x_vec = np.array(x_vec)
x_vec = x_vec.reshape(1,x_vec.shape[0])
"""

def get_feature_mean_std():

    with open("./X_mean_std.pkl","rb") as file_handle:
        X_mean_std = pickle.load(file_handle)

    return X_mean_std


def get_trained_weights():

    with open("./weights.pkl","rb") as file_handle:
        ws = pickle.load(file_handle)

    return ws

"""
x_vec = (x_vec - X_mean_std[0])/X_mean_std[1]

log_yhat = ws[0] + np.matmul(x_vec,ws[1])
yhat = np.exp(log_yhat)[0][0]

print("\nThe predicted price of the laptop is {}".format(yhat))
"""