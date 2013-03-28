import web

db = web.database(dbn='sqlite', db='pinRegister.db')

def get_pins():
    return db.select('pins', order='id')

def new_pin(my_title, my_room, my_id, my_active):
   try:
<<<<<<< HEAD
        db.insert('pins', id=my_id, title=my_title, status='0', 
=======
        db.insert('pins', id=my_id, title=my_title, status='0',
>>>>>>> cf1b73b952bf510f96f1951a45b3a8a3ababe5b6
              room=my_room, active=my_active)
   except:
       print "BAD PIN NUMBER"
def del_pin(id):
    db.delete('pins', where="id=$id", vars=locals())
