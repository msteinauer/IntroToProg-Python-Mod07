# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# Change Log:
# JMannisto, 8.19.2022, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ Saves data from a List to a File

            :param file_name: (string) with name of file:
            :param list_of_data: (list) you want filled with file data:
            :return: nothing
    """
    objFile = open(file_name, "ab")
    for row in list_of_data:
        pickle.dump(row, objFile)
    objFile.close()


def read_data_from_file(file_name):
    """ Reads data from File to a List

            :param file_name: (string) with name of file
            :return objFileData: (list) of file data
    """
    print(f"Reading data from {file_name}...")
    objFile = open(file_name, "rb+")
    objFileData = []
    while True:
        try:
            objFileData.append(pickle.load(objFile))
        except EOFError:
            print("No more data in file. Closing file...")
            break
    objFile.close()
    return objFileData

def get_id_and_name():
    """ Gets ID and Name input from a user

        :param: none
        :return input ID: (int) ID inputted by user, inputName: (str) Name inputted by user
    """
    try:
        inputID = int(input("Enter an Id: "))
    except ValueError:
        print("Please enter a number as an Id")
        inputID = int(input("Enter an Id: "))
    inputName = input("Enter a Name: ")
    return inputID, inputName

# Presentation ------------------------------------ #
id, name = get_id_and_name()
lstCustomer = [id, name]

save_data_to_file(strFileName, lstCustomer)

allCustomers = read_data_from_file(strFileName)
print("The current data is: ")
for i in range(0,len(allCustomers),2):
    print(allCustomers[i], allCustomers[i + 1])