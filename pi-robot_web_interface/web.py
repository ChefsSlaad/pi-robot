#!/usr/bin/python3

import threading
#import robo_car
from bottle import route, request, run, template, static_file



@route('/')
def page_get():
# simple return for for all pages
    html_page = '<body><p>the simplest page ever<p></body>'
    print ('returning main page')
    return static_file('index.html', root='html')

@route('/<filename:re:.*\.(js)$>')
def js_file_return(filename):
    return static_file(filename, root='js')

@route('/<filename:re:.*\.(css)$>')
def css_file_return(filename):
    return static_file(filename, root='css')

@route('/<filename:re:.*\.(jpg|jpeg|gif|png|bmp)$>')
def css_file_return(filename):
    return static_file(filename, root='image')

@route('/<filename:re:.*\.(html)$>')
def js_file_return(filename):
    print ('returning', filename)
    return static_file(filename, root='html')

@route('/action=<parameter>')
# the robot is expected to be driven through the web interface.
# this function maps a simple web api to functions on the robot
# class. 
def parse_api_string(parameter):
    error_returnstring = '''
       format for parameters is <br> 
       action={action} <br>
       action=stop|forward|backward|rotate_left|rotate_right|forward_left|forward_right|backward_left|backward_right <br> 
       eg <url>/action=rotate_right <br>

    '''
    valid_responses = ('stop', 'forward', 'backward', 
                       'rotate_left', 'rotate_right', 
                       'forward_left', 'forward_right', 
                       'backward_left', 'backward_right')
    print (parameter)
    if parameter not in valid_responses:
        return error_returnstring
    
    if parameter == 'stop':
        pass 


def main_thread():
    print('starting web interface')
    run (host='0.0.0.0', port=8080, debug=True)
    return print ('exiting')



main_thread()

