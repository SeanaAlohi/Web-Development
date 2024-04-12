#import website function 
#grab create app function and use that to create the application and run it

from website import create_app 
#we can do this because website is a python package. 
#whenever you put __init__.py inside of a folder, it becomes a python package
#which means when you input the name of the folder, 
#it will by default run all the things in the init.py file
#which means we can import defined in the file, like "create_app"

app = create_app()

if __name__ == '__main__':
    #line 13 says, only if we run this file, not if we import, are we going to execute this line. HERE
    app.run(debug=True)
