Module07 Website
[Google Homepage](https://www.google.com "Google's Homepage")
[GitHub Webpage Code CheatSheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


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

