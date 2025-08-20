import pickle

with open("./ordinal_columns_encodings.pkl","rb") as file_handle:
    ordinal_columns_encodings = pickle.load(file_handle)

with open("./all_column_names.pkl","rb") as file_handle:
    all_X_columns = pickle.load(file_handle)

for idx, single_column in enumerate(all_X_columns):
    print("ENTER THE VALUE OF {}\n".format(single_column))
    print("PLEASE CHOOSE ANY OF THE VALUE FROM BELOW MENTIONED VALUES\n")

    if idx >= 9:
        print("Either 0 (No) or 1 (Yes)")

    if single_column not in ordinal_columns_encodings.keys():
        print("From 0 to Infinity")
    else:
        print(list(ordinal_columns_encodings[single_column].keys()))

    value = str(input("Please enter the Value of {}\n".format(single_column)))
    print("\n\n")