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


def run(db_cursor, state):
  
    food_location = []

    food = db_cursor.execute(
        f"SELECT x,y from main_game_field as taco, owner where is_flag = FALSE and taco.owner_id = owner.owner_id and owner.name = 'Food'")

    for i in food.fetchall():
        food_location.append(i)

    food_location.sort()
    
    rows = db_cursor.execute(
        f"SELECT x,y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")

    for row in rows.fetchall():
        db_cursor.execute(logic(row, food_location))


def logic(row, food_location):

    for looking in food_location: 

      # if the food is not in the same row
      if(looking[0] != row[0]):
          # if the food is to the left
          if(looking[0] < row[0]):
              return(f"insert into engine_orders values( {row[0]}, {row[1]}, {left(row)}, {row[1]}, 'MOVE')")
          # if the food is to the right
          else:
              return(f"insert into engine_orders values( {row[0]}, {row[1]}, {right(row)}, {row[1]}, 'MOVE')")
      # if the food is not in the same column
      elif(looking[1] != row[1]):
          # if the food is above
          if(looking[1] < row[1]):
              return(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]}, {up(row)}, 'MOVE')")
          # if the food is below
          else:
              return(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]}, {down(row)}, 'MOVE')")

    return(f"insert into engine_orders values( {row[0]}, {row[1]}, {left(row)}, {down(row)}, 'MOVE')")

# taco
