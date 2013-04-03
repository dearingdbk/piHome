import web
import lib.pincushion

cushion = lib.pincushion.Cushion()

db = web.database(dbn='sqlite', db='pinRegister.db')

class Device:
  def get_devices():
    return db.select('devices', order='id')

  def get_device(id):
    return db.select('devices', where='id = ' + str(id))

  def new_device(controller, connection, type, active):
    active = 'high' if active == 'high' else 'low'
    type = type if type == 'sensor' or type == 'dimmer' else 'onoff'

    try:
      device = db.insert('devices',
        controller=controller, connection=connection,
        type=type, active=active,
        status='off',
        floor=0.0, ceiling=0.0, reading=0.0,
        x=0, y=0)
      cushion.add_pin(connection, active)
     except:
         raise

  def update_device(id, parameters):
    db.update('devices', where='id = ' + str(id), vars=parameters)

    try:
      if (parameters.status == 'on'):
        turn_on(id);
      else:
        turn_off(id);
    except NameError:
      pass

  def delete_device(id):
      cushion.del_pin(get_device(id).connection)
      db.delete('devices', where='id = ' + str(id))

  def turn_on(id):
      cushion.get_val(get_device(id).connection).turn_on()
      db.update('devices', where='id = ' + str(id), status='on')

  def turn_off(id):
      cushion.get_val(get_device(id).connection).turn_off()
      db.update('devices', where='id = ' + str(id), status='off')

class Room:
  def get_rooms():
    return db.select('rooms', order='id')

  def new_room():
    db.insert('rooms', x=-100, y=-100, width=200, height=200)

  def update_room(id, parameters):
    db.update('rooms', where='id = ' + str(id), vars=parameters)

  def delete_room(id):
    db.delete('rooms', where='id = ' + str(id))

devices = Device.get_devices()
for device in devices:
   cushion.add_pin(device.connection, device.active)