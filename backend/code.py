<<<<<<< HEAD
""" Basic todo list using webpy 0.3 """
import web
import model
import lib.thermo
import lib.pincushion
=======
"""
 * File:     code.py
 * Author:   
 * Date:     2013/03/23
 * Version:  1.0
 *
 * Purpose:  Starts and handles calls/posts/requests to the webservice.
"""
import web          # web.py import # 
import model        # handles calls to the database #
import lib.thermo   # intelligent agent for climate control #
import lib.pincushion
import signal, os

cushion = lib.pincushion.Cushion()
pins = model.get_todos()
for pin in pins:
    cushion.add_pin(pin.id, pin.active)
>>>>>>> cf1b73b952bf510f96f1951a45b3a8a3ababe5b6

"""cushion = lib.pincushion.Cushion()
pins = model.get_todos()
for pin in pins:
    cushion.add_pin(pin.id, pin.active)

t = lib.thermo.ThermoThread()
t.start()"""


### Url mappings
urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete'
)


### Templates
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull,
                         description="Description:"),
        web.form.Textbox('room', web.form.notnull,
                         description="Location:"),
        web.form.Dropdown('id', ['4', '17', '18', '21',
                                '22', '23', '24', '25'],
                         description="Pin:"),
<<<<<<< HEAD
        web.form.Dropdown('active', [('LOW', 'Low'), ('HIGH', 'High')], 
=======
        web.form.Dropdown('active', [('LOW', 'Low'), ('HIGH', 'High')],
>>>>>>> cf1b73b952bf510f96f1951a45b3a8a3ababe5b6
                          description="Active State:"),
        web.form.Button('Add Device'),

    )

    def GET(self):
        """ Show page """
        pins = model.get_pins()
        form = self.form()
        return render.index(pins, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            pins = model.get_pins()
            return render.index(pins, form)
        model.new_pin(form.d.title, form.d.room, form.d.id, form.d.active)
        raise web.seeother('/')



class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_pin(id)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()



<<<<<<< HEAD
#import web
#import view, config
#from view import render

#db = web.database(dbn="sqlite", db='pinRegister')

#urls = (
 #   '/', 'index'
#)

#class index:
 #   def GET(self):
  #      print db.query("23").list()
   #     todos = db.select('*')
    #    return render.index(todos)
      # return render.base(view.listing())

#if __name__ == "__main__":
#    app = web.application(urls, globals())
#    app.internalerror = web.debugerror
#    app.run()
#import web
#import RPi.GPIO as GPIO
#import view, config
#from view import render
#from subprocess import call

#GPIO.setmode(GPIO.BCM)


#urls = (
#     '/(.*)', 'index'
#)

#class index:
 #   def GET(self, pin):
#        GPIO.setup(17, GPIO.OUT)
#        if pin in ('off'):
#            GPIO.output(17, GPIO.LOW)
#        else:
#            GPIO.output(17, GPIO.HIGH)
        #call("echo " + pin + " > /sys/class/gpio/export", shell=True)
        #call("echo 1 " + " > /sys/class/gpio/gpio" + pin + "/active_low", shell=True)
        #call("echo \"out\" " + " > /sys/class/gpio/gpio" + pin + "/direction", shell=True)
        #call("echo 0 " + " > /sys/class/gpio/gpio" + pin + "/value", shell=True)
#        return render.index(GPIO.input(17))


#if __name__ == "__main__":
#    app = web.application(urls, globals())
#    app.internalerror = web.debugerror
#    app.run()
=======



def handler(signum, frame):
    t.join()

signal.signal(signal.SIGINT, handler)
signal.signal(signal.SIGQUIT, handler)
>>>>>>> cf1b73b952bf510f96f1951a45b3a8a3ababe5b6
