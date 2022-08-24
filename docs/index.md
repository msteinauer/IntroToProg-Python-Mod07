# Pickling and Error Handling in Python
## 1 Introduction

In this knowledge documentation, I cover a description of how I completed Assignment 7. Assignment 7 was a much more freeform and was centered around the topics of Structured Error Handling and Pickling. 

Starter code was provided for this assignment which asked for the following to be done:
- For function save_data_to_file to be defined
- For function read_data_from_file to be defined
- Get an ID and name from the user, then store it in a list object
- Store a list object into a binary file
- Read the data saved in the binary file into a new list object and display the contents of the new list object. 

## 2 Writing the Pseudocode
To create the code for Assignment 7 I first opened the starter code in PyCharm. Given that there was so little code in the starter code, it didn’t take long to figure out what had already been written and how all the pieces interacted. Subsequently, I started drafting up pseudocode for these missing sections. 

### 2.1 Processing
First, I began by drafting up the code for the Processing section, specifically the two functions included in the starter code: *save_data_to_file* and *read_data_from_file*.


```Python
def save_data_to_file(file_name, list_of_data):
    """ Saves data from a List to a File

            :param file_name: (string) with name of file:
            :param list_of_data: (list) you want filled with file data:
            :return: nothing
    """
    pass #TODO: Add code here
    #open File
    #objFile = open(file_name, "ab")
    
    #dump
    #pickle.dump(list_of_data, objFile)
    
    #close file
    #objFile.close()
```
###### Figure 1: Pseudocode for the first function in the script: *save_data_to_file*

Figure 1 shows us the first instance of pseudocode drafted up under the Processing section in the script. Here we see the first function save_data_to_file with pseudocode and comments drafted up underneath it. Given the name of the function from the starter code, while no other guidance was provided, the actions the function was to perform seemed clear. My drafted pseudocode included opening the file in append mode in binary format, although I could also see this function writing over all the data currently in the file. After opening the file, we use the dump() function imported from the pickle class to dump all the data from the list identified as an argument in the function. After dumping the data in binary format, we close the file. 

I also drafted up comments for the function to summarize its purpose, its parameters, as well as what the function returns to make it clear for others reading the code to understand the function at a moment’s glance. 

```Python
def read_data_from_file(file_name):
    """ Reads data from a File to a List

            :param file_name: (string) with name of file:
            :return : (list) of file data
    """
    pass #TODO: Add code here
    #open File
    #objFile = open(file_name, "rb")
    
    #load data
    #objFileData = pickle.load(objFile)
        #note will only load one row of data!
    
    #close file
    #objFile.close()
```

###### Figure 2: Pseudocode for the second function in the script: *read_data_from_file*

Figure 2 shows us the pseudocode draft for the second function of the script in the Processing section of the code: *read_data_from_file*. Again, like with the function in Figure 1, there was not much guidance provided with the starter code. However, I felt like the purpose of the function was clear from its name. I drafted up some pseudocode to get started on tackling the task for this function. Given that we’re reading data from a file, I determined that first I needed to open the file. After opening the file I simply defined a new list *objFileData* to load the data that was pickled into. I did however note that this would simply load the first line that was pickled, not the entirety of data if there were multiple lines. I decided to tackle that later. Finally, I finished by closing the file and returning the list the previously pickled data was loaded onto. 

Like with the first function, I wrote up a summary in the beginning of the function to summarize its purpose, the parameters it takes, as well as what it returns. 

### 2.2 Presentation
The next section of the script is the Presentation. Here I was provided with three tasks by the starter code: 
1.	Get an ID and name from the user, then store it in a list object
2.	Store a list object into a binary file
3.	Read the data saved in the binary file into a new list object and display the contents of the new list object. 

```Python
#TODO: Get ID and NAME from user, then store it in a list object
#get input ID
#inputID = int(input("Enter an Id: "))

#get input Name
#inputName = str(input("Enter a Name: "))

#save in list
#lstCustomer = [inputID, inputName]
```
###### Figure 3: Pseudocode written for the first TODO of the Presentation Section

Figure 3 shows the pseudocode for the first task listed above. To get an ID and name from a user, I first defined two variables *inputID* and *inputName* and initialized them using the *input()* function. After assigning values to these two variables from the user’s input, these variables are then saved into a list *lstCustomer*, declared under the Data section of the script.

```Python
#TODO: store the list object into a binary file
#call save data to file
#save_data_to_file(strFileName, lstCustomer)
```
###### Figure 4: Pseudocode written for the second TODO of the Presentation Section

The second task under the Presentation section of the script was to store the list, lstCustomer, into a binary file. To do so, I simply drafted pseudocode (along with actual Python) to call the previously defined function *save_list_to_file()*.The pseudocode drafted can be seen in Figure 4 where you can see the commented out Python code underneath the pseudocode.

```Python
#TODO: Read the data from the file into a new list object and display the contents

#call read file function
#allCustomers = read_data_from_file(strFileName)

#read the list
#print(allCustomers)
```
###### Figure 5: Pseudocode written for the final TODO of the Presentation Section

The final drafted pseudocode was for the last task under the Presentation section of the script. This can be seen in Figure 5. The task here was to read the data from a file into a new list object and to then print out the contents of the list. To me it seemed clear that this was a place to call the *read_data_from_file* function previously. However, that function returns a list, so I needed to have a place to put the data from the function. This led me to initialize a new variable *allCustomers* with the data from calling the function *read_data_from_file*. After assigning data to that variable, I then needed to read the list, most likely with some sort of print function. 

## 3 Writing the Code
After drafting up the pseudocode, as described in [2 Writing the Pseudocode](https://jmannisto.github.io/IntroToProg-Python-Mod07/#2-writing-the-pseudocode) I started writing full statements out in Python. 

### 3.1 Data
The first section of our code is Data. Here, variables and constants are initialized, if relevant to the section. Variables had already been declared in the data section and I did not see any need to add any more variables to the code than what had already been included. 

### 3.2 Processing
Under the Processing section of the script is where the functions are defined for this script.  

In our Processing section we have two functions: 
- *save_data_to_file(file_name, list_of_data)*
- *Read_data_from_file(file_name)* 

Both functions required editing for the assignment. 

#### 3.2.1 Saving Data to a File
The first function in the starter code was the function *save_data_to_file(file_name, list_of_data)*. This function takes two parameters: the file name we want to save data to and the list that holds the data we want to save. 

The code for this function can be seen in Figure 6. Here, I opened the file in append mode in binary format, so that any data added would add the data to the end of the file rather than writing over the file. After opening the file, I made some additional edits to the pseudocode. Originally there was simply a *dump()* function imported from the pickle class to dump all the data from the list identified as an argument in the function. However, I added a for loop to loop through the *list_of_data*. For each row, we perform the *dump()* function so that we are able to add multiple lines of data to the file of binary data if needed. I added this so that there is flexibility for the program to be able to store multiple lines of data in the initial list populated by the user. After dumping the data in binary format, we close the file.

```Python
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
```
###### Figure 6: Code for function *save_data_to_file(file_name, list_of_data)*
Figure 6 shows the code for the function *save_data_to_file(file_name, list_of_data)*. 


#### 3.2.2 Reading Data From a File 



