import random

player_keys = 0

# Генерация подземелья
def generate_dungeon():
    n = random.randint(4, 10)
    m = random.randint(4, 10)

    room_types = ["пусто", "сундук", "монстр", "ключ", "портал", "ловушка"]

    dungeon = []
    for i in range(n):
        row = []
        for j in range(m):
            room = random.choice(room_types)
            row.append({"symbol": "*", "type": room})
        dungeon.append(row)

    # Случайная стартовая позиция
    x, y = random.randint(0, n-1), random.randint(0, m-1)
    dungeon[x][y]["symbol"] = "o"

    print(f"Размер подземелья: {n} x {m}")
    for row in dungeon:
        print(*(c["symbol"] for c in row))
    print(f"\nИгрок в комнате ({x},{y}): {dungeon[x][y]['type']}")

    return dungeon, n, m, x, y


#портал
def portal(dungeon, n, m, x, y):
    print("Вы попали в портал! Телепортация...")

    dungeon[x][y]["symbol"] = "-"
    dungeon[x][y]["type"] = "None"

    while True:
        nx = random.randint(0, n - 1)
        ny = random.randint(0, m - 1)
        if dungeon[nx][ny]["symbol"] == "*":
            dungeon[nx][ny]["symbol"] = "o"
            print(f"Телепортация в ({nx},{ny}) — {dungeon[nx][ny]['type']}")
            return nx, ny

#ключ
def key(dungeon, n, m, x, y):
    global player_keys

    print("Вы нашли ключ!")
    player_keys += 1
    print(f"Ключей: {player_keys}")

    return move_player(dungeon, n, m, x, y)

#монстр
def monster(dungeon, n, m, x, y, atk, health):
    monster_hp = random.randint(1, health + 1)
    print(f"Комната монстра! Монстр HP: {monster_hp}, ваш урон: {atk}, ваше HP: {health}")

    dmg = monster_hp - atk
    if dmg < 0:
        dmg = 0

    if health - dmg <= 0:
        print("Монстр убил вас!")
        return x, y, 0

    health -= dmg
    print(f"Монстр побежден! Потеряно {dmg} HP. Текущее здоровье: {health}")

    nx, ny = move_player(dungeon, n, m, x, y)
    return nx, ny, health

#ловушка
def trap(dungeon, n, m, x, y, health):
    dmg = random.randint(1, health // 2 + 2)
    print(f"Ловушка! Потеряно {dmg} HP.")

    if health - dmg <= 0:
        print("Ловушка убила вас!")
        return x, y, 0

    health -= dmg
    print(f"Ваше здоровье: {health}")

    nx, ny = move_player(dungeon, n, m, x, y)
    return nx, ny, health

#сундук
def chest(dungeon, n, m, x, y, health):
    global player_keys
    print("Вы нашли сундук!")

    opened = False

    # Если есть ключ — предложить использовать
    if player_keys > 0:
        ans = input("Использовать ключ? (y/n): ").lower()
        if ans == "y":
            player_keys -= 1
            reward = random.randint(15, 40)
            health += reward
            dungeon[x][y]['type'] = "пусто"
            print(f"Сундук открыт ключом. +{reward} HP. Теперь HP = {health}")
            print(f"Ключей осталось: {player_keys}")
            opened = True

    # Если ключ не использовали — мини-задача
    if not opened:
        number = random.randint(10000, 1000000)
        root = random.randint(2, 6)
        correct = round(number ** (1 / root), 2)

        print(f"Чтобы открыть сундук, вычислите корень {root}-й степени из {number}.")
        print("Округлите до двух знаков.")

        try:
            ans = float(input("Ответ: ").replace(",", "."))
        except:
            print("Ошибка ввода. Сундук закрыт.")
            return move_player(dungeon, n, m, x, y)

        if abs(ans - correct) < 0.05:
            reward = random.randint(1, 20)
            health += reward
            dungeon[x][y]['type'] = "пусто"
            print(f"Верно! Сундук открыт. +{reward} HP. Теперь HP = {health}")
        else:
            print(f"Неверно. Правильный ответ был {correct}. Сундук остался закрыт.")

    nx, ny = move_player(dungeon, n, m, x, y)
    return nx, ny, health

#пустая комната
def none(dungeon, n, m, x, y):
    print("Пустая комната.")
    return move_player(dungeon, n, m, x, y)


#перемещение игрока
def move_player(dungeon, n, m, x, y):
    while True:
        move = input("Куда идти? (w/a/s/d): ").lower()

        nx, ny = x, y

        if move == "w": nx -= 1
        elif move == "s": nx += 1
        elif move == "a": ny -= 1
        elif move == "d": ny += 1
        else:
            print("Неверная команда.")
            continue

        if not (0 <= nx < n and 0 <= ny < m):
            print("Выход за границу подземелья.")
            continue

        dungeon[x][y]["symbol"] = "*"
        dungeon[nx][ny]["symbol"] = "o"

        print(f"Перемещение в ({nx},{ny}) — {dungeon[nx][ny]['type']}")
        return nx, ny


#игровой цикл
dungeon, n, m, x, y = generate_dungeon()

health = 10
atk = 1

while health > 0:
    room = dungeon[x][y]['type']

    print(f"\nВы в комнате: {room}, HP = {health}")

    if room == "портал":
        x, y = portal(dungeon, n, m, x, y)

    elif room == "ключ":
        x, y = key(dungeon, n, m, x, y)

    elif room == "монстр":
        x, y, health = monster(dungeon, n, m, x, y, atk, health)
        if health == 0:
            break

    elif room == "ловушка":
        x, y, health = trap(dungeon, n, m, x, y, health)
        if health == 0:
            break

    elif room == "сундук":
        x, y, health = chest(dungeon, n, m, x, y, health)

    elif room == "пусто":
        x, y = none(dungeon, n, m, x, y)


print("\nИгра окончена!")
