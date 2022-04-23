import random

my_dots = {}

def init():
  return("🌮")

def left(row):
  return(row[0]-1)
def right(row):
  return(row[0]+1)
def up(row):
  return(row[1]-1)
def down(row):
  return(row[1]+1)

def run(db_cursor , state): 
  
  food_location = []
  
  food = db_cursor.execute(f"SELECT x,y from main_game_field as taco, owner where is_flag = FALSE and taco.owner_id = owner.owner_id and owner.name = 'Food'")
  
  for i in food.fetchall():
    food_location.append(i)

  rows = db_cursor.execute(f"SELECT x,y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
  
  for row in rows.fetchall():
    db_cursor.execute(logic(row, food_location))
    print(row) 

def differenceX(a, b):
  return (a[0] - b[0])

def differenceY(a, b):
  return (a[1] - b[1])

#find the nearest food
def logic(row, food_location):  
  
  
  
  return(f"insert into engine_orders values( {row[0]}, {row[1]}, {left(row)}, {down(row)}, 'MOVE')")

#taco