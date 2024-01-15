# https://youtu.be/CUFjAS1qvbU?list=PLSiLeKadTQ7n8wFp1e1dKdtCYTy6DZTAL
from  pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def Rak():
 
    put_html('<center><h3>application for student</h3></center>').style('background-color:#030637;color:gold;padding:25px;')
    put_html('<p>CV for accepted students rita</p> ').style('color:gold;background-color:#030637;text-align:center;font-weight:bold;')
    put_html('<button>press</button>').style('background-color:#FF6868;')
    put_html('<center><img src="https://images.unsplash.com/photo-1571260899304-425eee4c7efc?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8dW5pdmVyc2l0eSUyMHN0dWRlbnR8ZW58MHx8MHx8fDA%3D" width=""</center>')
    data = input_group(
      'apllication for acepted student',[
      input('Student name',name='Student'),
      input('Student address',name='country'),
      input('email address',name='email'),
      input('phone number',name='phone', type=NUMBER),
      radio('student experience',options=['words','excel','powerpoint'],name='certi'),
      checkbox('language',options=['eng','french','esp'],inline=True,name='lang'),
      ]
       )
                       
start_server(Rak,port=3335,debug=True)