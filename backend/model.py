import web

db = web.database(dbn='sqlite', db='todo.db')

def get_todos():
    return db.select('todo', order='id')

def new_todo(my_title, my_room, my_id, my_active):
   try:
        db.insert('todo', id=my_id, title=my_title, status='0',
              room=my_room, active=my_active)
   except:
       print "BAD PIN NUMBER"
def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())
