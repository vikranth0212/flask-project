from flask import Flask
#from flask package we are using Flask class or func

#FAI is a flask application instance
#Application Instance is a object for Flask class
FAI=Flask(__name__)

#__name__ will define name of current module
#by using @ decorator we can add additional functionalities to func
#@FAI is a decorator
#route is use for urlmapping,route is a method
#in django we are using urlmapping,but in flask urls.py is not there,so we r using route method
#'/stringresponse' is a suffix

@FAI.route('/stringresponse')
def stringresponse():
    return 'This is a first function in flask'

@FAI.route('/multistring')
def multistring():
    return 'This is last function in flask'   

if __name__ == '__main__':
    FAI.run(debug=True)

#at the time of doing project debug=True
#at the time of hosting or delivering we need to give debug=False

#__name__=='__main__'
#here we are creating featues.py and in that 2 func we created,if we run it will give name as main
#Here cond is true
#for ex if we are creating another pythonfile dummy.py
#in dummy.py we will import (import feature)
#there it will give name as feature,so there debug will become false
#because __name__ will give name as a feature it is not equal to main


