import web
import lib.pincushion

cushion = lib.pincushion.Cushion()

db = web.database(dbn='sqlite', db='pinRegister.db')

def get_pins():
    return db.select('pins', order='id')

def new_pin(my_title, my_room, my_id, my_active):
   try:
        db.insert('pins', id=my_id, title=my_title, status='0', 
              room=my_room, active=my_active)
        cushion.add_pin(my_id, my_active)
   except:
       print "BAD PIN NUMBER"

def del_pin(id):
    db.delete('pins', where="id=$id",  vars=local())

def turn_on(id):
    cushion.get_val(id).turn_on()
    db.update('pins', where='id = ' + id , status='1')

def turn_off(id):
    cushion.get_val(id).turn_off()
    db.update('pins', where='id = ' + id , status='0')

pins = get_pins()
for pin in pins:
   cushion.add_pin(pin.id, pin.active)
