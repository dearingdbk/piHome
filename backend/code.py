""" Basic todo list using webpy 0.3 """
import web
import model
import lib.thermo
import lib.pincushion


###    This starts the temperature Thread as a Daemon.
###    pin 4 and pin 17 will be occupied when this thread
###    runs.
t = lib.thermo.ThermoThread()
t.daemon = True
t.start()

### Url mappings - This maps different urls to classes in code.py
### Any URL's that are not documented here will return a 404 not found error
urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/on/(\d+)', 'On',
    '/off/(\d+)', 'Off'
)


### Templates - This is where we direct code.py to the folder containing our html
### documents to compile and display online.
render = web.template.render('templates', base='base')


### Class which dispalys the root page of the website /
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
                          description="Active State:"),
        web.form.Button('Add Device'),
        
    )
    ### Handles GET requests
    def GET(self):
        """ Show page """
        pins = model.get_pins()
        form = self.form()
        return render.index(pins, form)

    ### Handles Post requests
    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates():
            pins = model.get_pins()
            return render.index(pins, form)
        try:
            model.new_pin(form.d.title, form.d.room, form.d.id, form.d.active)
            raise web.seeother('/')
        except:
            return render.error()

### Class which handles deleting a pin from the interface.
class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_pin(id)
        raise web.seeother('/')

### Class which turns on a pin.
class On:
    def POST(self, id):
        id = int(id)
        model.turn_on(id)
        raise web.seeother('/')

### Class which turns off a pin.
class Off:
    def POST(self, id):
        model.turn_off(id)
        raise web.seeother('/')


### sets app as the the main web.py application which starts the web server.
app = web.application(urls, globals())


### If this script is called as main run the app. 
if __name__ == '__main__':
    app.run()

