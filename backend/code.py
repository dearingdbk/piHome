import web
import json
import model
import lib.thermo
import lib.pincushion

t = lib.thermo.ThermoThread()
t.daemon = True
t.start()

### Url mappings
urls = (
    '/', Index
    '/controllers/', Controllers,
    '/devices/(\d+)?', Devices,
    '/rooms/(\d+)?', Rooms
"""
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/on/(\d+)', 'On',
    '/off/(\d+)', 'Off'
"""
)


"""
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
        "" Show page ""
        pins = model.Device.get_pins()
        form = self.form()
        return render.index(pins, form)

    def POST(self):
        "" Add new entry ""
        form = self.form()
        if not form.validates():
            pins = model.Device.get_pins()
            return render.index(pins, form)
        try:
            model.Device.new_pin(form.d.title, form.d.room, form.d.id, form.d.active)
            raise web.seeother('/')
        except:
            return render.error()

class Delete:
    def POST(self, id):
        "" Delete based on ID ""
        id = int(id)
        model.Device.del_pin(id)
        raise web.seeother('/')

class On:
    def POST(self, id):
        id = int(id)
        model.Device.turn_on(id)
        raise web.seeother('/')

class Off:
    def POST(self, id):
        model.Device.turn_off(id)
        raise web.seeother('/')
"""

class Index:
    def GET(self):
        raise web.seeother('/static/index.html')

"""Deliver controller information."""
class Controllers:
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps([{
                'id': 1,
                'name': 'Raspberry Pi GPIO',
                'connections': [
                    {
                        'id': 4
                        'name': 'Pin 4'
                    },
                    {
                        'id': 17
                        'name': 'Pin 17'
                    },
                    {
                        'id': 18
                        'name': 'Pin 18'
                    },
                    {
                        'id': 21
                        'name': 'Pin 21'
                    },
                    {
                        'id': 22
                        'name': 'Pin 22'
                    },
                    {
                        'id': 23
                        'name': 'Pin 23'
                    },
                    {
                        'id': 24
                        'name': 'Pin 24'
                    },
                    {
                        'id': 25
                        'name': 'Pin 25'
                    }
                ]
            }])

"""Handle device requests."""
class Devices:
    def GET(self, id = None):
        web.header('Content-Type', 'application/json')

        if id != None:
            return json.dumps(model.Debice.get_device(id))
        return json.dumps(model.Device.get_devices())

    def PUT(self):
        web.header('Content-Type', 'application/json')
        input = web.input()

        try:
            model.Device.new_device(input.controller, input.connection, input.type, input.active)
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False, 'message': 'Failure adding device to database!'})

    def POST(self, id):
        web.header('Content-Type', 'application/json')

        try:
            model.Device.get_device(id)
        except:
            return json.dumps({'success': False, 'message': 'Nonexistant device!'})

        model.Device.update_device(id, web.input())

    def DELETE(self, id):
        web.header('Content-Type', 'application/json')

        try:
            model.Device.delete_device(id)
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False, 'message': 'Failure removing device from database!'})

"""Handle rooms."""
class Rooms:
    def GET(self):
        web.header('Content-Type', 'application/json')

        return json.dumps(model.Room.get_rooms())

    def PUT(self):
        web.header('Content-Type', 'application/json')
        input = web.input()

        try:
            model.Room.new_room()
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False, 'message': 'Failure adding room to database!'})

    def POST(self, id):
        web.header('Content-Type', 'application/json')

        try:
            model.Room.update_room(id, web.input())
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False, 'message': 'Failure updating room!'})

    def DELETE(self, id):
        web.header('Content-Type', 'application/json')

        try:
            model.Room.delete_room(id)
            return json.dumps({'success': True})
        except:
            return json.dumps({'success': False, 'message': 'Failure removing room from database!'})

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()