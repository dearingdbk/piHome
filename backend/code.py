""" Basic todo list using webpy 0.3 """
import web
import model
import lib.thermo
import lib.pincushion

t = lib.thermo.ThermoThread()
t.daemon = True
t.start()

### Url mappings
urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/on/(\d+)', 'On',
    '/off/(\d+)', 'Off'
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
        try:
            model.new_pin(form.d.title, form.d.room, form.d.id, form.d.active)
            raise web.seeother('/')
        except:
            return render.error()


class Delete:
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_pin(id)
        raise web.seeother('/')

class On:
    def POST(self, id):
        id = int(id)
        model.turn_on(id)
        raise web.seeother('/')

class Off:
    def POST(self, id):
        model.turn_off(id)
        raise web.seeother('/')


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()

