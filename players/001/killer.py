import random

def init():
    return("💀")


def run(db_cursor , state):
  
  
    #get all my dots
  i = 0
  rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
  
  for row in rows.fetchall():
    db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1 }, {row[1] + 1 }, 'MOVE')") 
    
    
def left(row):
  return("row[0]-1")
def right(row):
  return("row[0]+1")
def up(row):
  return("row[0]-1")
def down(row):
  return("row[0]+1")
# +1 down
# -1 up
# +1 right
# -1 left