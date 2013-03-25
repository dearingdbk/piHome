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


t = lib.thermo.ThermoThread()   # create the thread to manage thermostat #
t.start()                       # start the thread #


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
        web.form.Dropdown('active', [('0', 'Low'), ('1', 'High')], 
                          description="Active State:"),
        web.form.Button('Add Device'),
        
    )

    def GET(self):
        """ Show page """
        todos = model.get_todos()
        form = self.form()
        return render.index(todos, form)

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            todos = model.get_todos()
            return render.index(todos, form)
        model.new_todo(form.d.title, form.d.room, form.d.id, form.d.active)
        raise web.seeother('/')



class Delete:

    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
