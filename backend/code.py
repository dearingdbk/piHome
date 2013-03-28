""" Basic todo list using webpy 0.3 """
import web
import model
import lib.thermo
import lib.pincushion

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

        web.form.Dropdown('active', [('LOW', 'Low'), ('HIGH', 'High')], 

        web.form.Dropdown('active', [('LOW', 'Low'), ('HIGH', 'High')],
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

