import math, random  # for the euclidean distance


def init():
    return("🌮")

# Movements
def left(row):
    return(row[0]-1)


def right(row):
    return(row[0]+1)


def up(row):
    return(row[1]-1)


def down(row):
    return(row[1]+1)


# euclidean distance
def euclidean_distance(row, food_location):
    return math.sqrt(pow(food_location[0] - row[0], 2) + pow(food_location[1] - row[1], 2))


def run(db_cursor, state):

    food_location = []
    enemy_location = []

    food = db_cursor.execute(
        f"SELECT x,y from main_game_field as taco, owner where is_flag = FALSE and taco.owner_id = owner.owner_id and owner.name = 'Food'")

    for i in food.fetchall():
        food_location.append(i)

    enemy = db_cursor.execute(
        f"SELECT x,y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}'")

    for i in enemy.fetchall():
        enemy_location.append(i)

    rows = db_cursor.execute(
        f"SELECT x,y from main_game_field as gf, owner where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")

    for row in rows.fetchall():
        db_cursor.execute(logic(row, food_location, enemy_location))


def logic(row, food_location, enemy_location):

    food_location.sort(key=lambda x: euclidean_distance(row, x))

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

    enemy_location.sort(key=lambda x: euclidean_distance(row, x))

    for looking in enemy_location:
        # if the enemy is not in the same row
        if(looking[0] != row[0]):
            # if the enemy is to the left
            if(looking[0] < row[0]):
                return(f"insert into engine_orders values( {row[0]}, {row[1]}, {left(row)}, {row[1]}, 'MOVE')")
            # if the enemy is to the right
            else:
                return(f"insert into engine_orders values( {row[0]}, {row[1]}, {right(row)}, {row[1]}, 'MOVE')")
        # if the enemy is not in the same column
        elif(looking[1] != row[1]):
            # if the enemy is above
            if(looking[1] < row[1]):
                return(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]}, {up(row)}, 'MOVE')")
            # if the enemy is below
            else:
                return(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0]}, {down(row)}, 'MOVE')")

    while True:
      #dance 
      return(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + random.randint(-1,1)}, {row[1] + random.randint(-1,1)}, 'MOVE')")

