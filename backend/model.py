import web
import lib.pincushion
import pprint

cushion = lib.pincushion.Cushion()

db = web.database(dbn='sqlite', db='pinRegister.db')

class Device(object):
  @staticmethod
  def get_devices():
    return db.select('devices', order='id').list()

  @staticmethod
  def get_device(id):
    return db.select('devices', where='id = ' + str(id)).list()[0]

  @staticmethod
  def new_device(controller, connection, type, active):
    active = 'high' if active == 'high' else 'low'
    type = type if type == 'sensor' or type == 'dimmer' else 'onoff'

    try:
      device = db.insert('devices',
        controller=controller, connection=connection,
        type=type, active=active,
        state='off',
        floor=0.0, ceiling=0.0, reading=0.0,
        x=0, y=0)
      cushion.add_pin(connection, active)
    except:
      raise

  @staticmethod
  def update_device(id, parameters):
    dictP = dict(parameters)
    db.update('devices', where='id = ' + str(id), vars=dictP, **dictP)

    try:
      if (parameters.state == 'on'):
        Device.turn_on(id);
      else:
        Device.turn_off(id);
    except AttributeError:
      pass

  @staticmethod
  def delete_device(id):
      cushion.del_pin(Device.get_device(id).connection)
      db.delete('devices', where='id = ' + str(id))

  @staticmethod
  def turn_on(id):
      cushion.get_val(Device.get_device(id).connection).turn_on()
      db.update('devices', where='id = ' + str(id), state='on')

  @staticmethod
  def turn_off(id):
      cushion.get_val(Device.get_device(id).connection).turn_off()
      db.update('devices', where='id = ' + str(id), state='off')

class Room(object):
  @staticmethod
  def get_rooms():
    return db.select('rooms', order='id').list()

  @staticmethod
  def new_room():
    db.insert('rooms', x=-100, y=-100, width=200, height=200)

  @staticmethod
  def update_room(id, parameters):
    dictP = dict(parameters)
    db.update('rooms', where='id = ' + id, vars=dictP, **dictP)

  @staticmethod
  def delete_room(id):
    db.delete('rooms', where='id = ' + id)

devices = Device.get_devices()
for device in devices:
   cushion.add_pin(device.connection, device.active)