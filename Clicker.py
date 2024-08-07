#! python3
# Clicker.py - A simple (and not funny) clicker game

from tkinter import *
from tkinter import messagebox

# NOTE: The comments are the values that should be there. Feel free to increase or decrease them as you want
clicks = 0 # 0
coins = 0 # 0
click_multiplier = 1 # 1
coin_multiplier = 1 # 1
a = 1 # 1
b = 1 # 1
c = True # True
autoclick = False # False
aclick_speed = 2000 # 2000
buyed = False # False

notification = lambda: messagebox.showinfo("News", "A new level of\ncoin multiplier\nhas been unlocked!")

window = Tk()
window.geometry("500x550")
window.resizable(False, False)
window.title("Clicker")

def refresh_shop(coins, click_multiplier):
  global click_mult, click_mult_cost, coin_mult, coin_mult_cost, c

  if coins >= 500:
    coin_mult.config(text = "Coins per click + 10", command = lambda: coin_add(10, 500))
    coin_mult_cost.config(text = 500, command = lambda: coin_add(10, 500))

  if coins >= 5000:
    coin_mult.config(text = "Coins per click + 100", command = lambda: coin_add(100, 5000))
    coin_mult_cost.config(text = 5000, command = lambda: coin_add(100, 5000))

  if coins >= 10000:
    coin_mult.config(text = "Coins per click + 250", command = lambda: coin_add(250, 10000))
    coin_mult_cost.config(text = "10k", command = lambda: coin_add(250, 10000))

  if coins >= 20000:
    coin_mult.config(text = "Coins per click + 500", command = lambda: coin_add(500, 20000))
    coin_mult_cost.config(text = "20k", command = lambda: coin_add(500, 20000))

  if coins >= 50000:
    coin_mult.config(text = "Coins per click + 1000", command = lambda: coin_add(1000, 50000))
    coin_mult_cost.config(text = "50k", command = lambda: coin_add(1000, 50000))

  if coins >= 1000000:
    coin_mult.config(text = "Coins per click + 1000000", command = lambda: coin_add(1000000, 1000000))
    coin_mult_cost.config(text = "1mln", command = lambda: coin_add(1000000, 1000000)) 


  if click_multiplier >= 1.2 and c: # I use c later to disable the button 
    click_mult.config(text = "Click x 1.5", command = lambda: click_add(1.5, 10000))
    click_mult_cost.config(text = "7500", command = lambda: click_add(2, 7500))

  if click_multiplier >= 1.5 and c:
    click_mult.config(text = "Click x 2", command = lambda: click_add(2, 10000))
    click_mult_cost.config(text = "20k", command = lambda: click_add(2, 20000))

  if click_multiplier >= 2 and c:
    click_mult.config(text = "Click x 5", command = lambda: click_add(5, 10000))
    click_mult_cost.config(text = "100k", command = lambda: click_add(5, 100000))

  if click_multiplier == 5 and c:
    click_mult.config(text = "Click x 10", command = lambda: click_add(10, 250000))
    click_mult_cost.config(text = "250k", command = lambda: click_add(10, 250000))

  if click_multiplier == 10 and c:
    click_mult.config(text = "Click x 50", command = lambda: click_add(50, 1000000))
    click_mult_cost.config(text = "1mln", command = lambda: click_add(50, 1000000))

  if click_multiplier == 50 and c:
    click_mult.config(text = "Click x 500", command = lambda: click_add(500, 10000000))
    click_mult_cost.config(text = "10mln", command = lambda: click_add(500, 10000000))

  if click_multiplier == 500 and c:
    click_mult.config(text = "Max", state = DISABLED)
    c = False
    click_mult_cost.destroy()
    click_mult.place(x = 0, y = 75, width = 590)
  refresh_home(coins, clicks)

def refresh_stats(coin_multiplier, click_multiplier, aclick_speed):
  global coin_info, click_info, buyed, aclick_info, aclick_speed_info, autoclick

  try:
    coin_info.config(text=f"Coins per click: {coin_multiplier}")
    click_info.config(text=f"Click multiplier: {click_multiplier}")
    state_aclick = "Active" if autoclick else "Not active"        

    if buyed: # buyed refers to the autoclicker
      auto_speed = 1 / (aclick_speed / 1000)
      if int(auto_speed) == auto_speed:
        auto_speed = int(auto_speed)
    else:
      auto_speed = 0

    aclick_info.config(text=f"AutoClicker state: {state_aclick}")
    aclick_speed_info.config(text=f"AutoClicker speed: {auto_speed}click/s")

  except:
        pass

def refresh_home(coins, clicks):
  global number, coinindicator

  numbershown = round(clicks, 1) if clicks <= 5000 else round(clicks) # Only show the decimals if you have less than 5000 clicks
  number.config(text = f"You clicked me {numbershown} times!")
  coinsshown = round(coins, 1) if coins <= 5000   else round(coins) # Same but with coins
  coinindicator.config(text = f"{coinsshown} coins")

def click():
  global clicks, coins, a

  clicks += 1 
  coins += click_multiplier * coin_multiplier

  try: # Maybe stats aren't open 
    refresh_stats(coin_multiplier, click_multiplier)
  except:
      pass

  try: # Maybe shop isn't open
      refresh_shop(coins, click_multiplier)
  except:
    pass

  refresh_home(coins, clicks)

  if coins >= 500 and a == 1:
    a += 1
    notification()

  if coins >= 5000 and a == 2:
    a += 1
    notification()

  if coins >= 10000 and a == 3:
    a += 1
    notification()

  if coins >= 20000 and a == 4:
    a += 1
    notification()

  if coins >= 50000 and a == 5:
    a += 1
    notification()


def coin_add(added, cost):
  global coin_multiplier, coins, coin_mult_cost, coin_mult, aclick_speed

  if coins >= cost:
    coin_multiplier += added
    coins -= cost
    refresh_shop(coins, click_multiplier)
    refresh_home(coins, clicks)
    refresh_stats(coin_multiplier, click_multiplier, aclick_speed)

def click_add(new, cost):
  global click_multiplier, coins, aclick_speed

  if coins >= cost:
    click_multiplier = new
    coins -= cost
    refresh_shop(coins, click_multiplier)
    refresh_stats(coin_multiplier, click_multiplier, aclick_speed)
    refresh_home(coins, clicks)

def open_stats():
  global coin_multiplier, click_multiplier, coin_info, click_info, aclick_info,aclick_speed_info, autoclick, aclick_speed

  statsscreen = Toplevel(window)
  statsscreen.geometry("650x300")
  statsscreen.resizable(False, False)
  statsscreen.title("Stats")

  if not buyed:
    aclick_speed = 0

  state_aclick = "Active" if autoclick else "Not active"
  try:
    auto_speed = 1 / int(aclick_speed/1000)
    if int(auto_speed) == auto_speed:
      auto_speed = int(auto_speed) # This essencially removes the .0 if present
  except ZeroDivisionError:
    auto_speed = 0

  # Buttons
  coin_info = Label(statsscreen, text = f"Coins per click: {coin_multiplier}", font = ("consolas", 10), anchor = "w")
  click_info = Label(statsscreen, text = f"Click multiplier: {click_multiplier}", anchor = "w", font = ("consolas", 10))
  coin_info.place(width = 650, height = 75)
  click_info.place(y = 75, width = 650, height = 75)
  aclick_info = Label(statsscreen, text = f"AutoClicker state: {state_aclick}", anchor = "w", font = ("consolas", 10))
  aclick_info.place(y = 150, width = 650, height = 75)
  aclick_speed_info = Label(statsscreen, text = f"AutoClicker speed: {auto_speed} click/s", anchor = "w", font = ("consolas", 10))
  aclick_speed_info.place(width = 650, height = 75, y = 225)

def open_shop():
  global click_multiplier, coin_multiplier, coin_mult, click_mult, click_mult_cost, coin_mult_cost, coins, autoclicker_btn, autoclicker_cost, ac_speed_btn, ac_speed_cost

  shopscreen = Toplevel(window)
  shopscreen.resizable(False, False)
  shopscreen.geometry("590x300")
  shopscreen.title("Shop")

  # Buttons
  coin_mult = Button(shopscreen, text = "Coins per click + 1", font = ("consolas", 10), command = lambda: coin_add(1, 50))
  coin_mult_cost = Button(shopscreen, text = 50, font = ("consolas", 10), command = lambda: coin_add(1, 50), justify = CENTER)  
  click_mult = Button(shopscreen, text = "Click x 1.2", font = ("consolas", 10), command = lambda: click_add(1.2, 2000))
  click_mult_cost = Button(shopscreen, text = 2000, font = ("consolas", 10), command = lambda: click_add(1.2, 2000))    
  coin_mult.place(x = -10, y = 0, height = 75, width = 495)
  coin_mult_cost.place(x = 485, y = 0, height = 75, width = 105)  
  click_mult.place(x = -10, y = 75, height = 75, width = 495)
  click_mult_cost.place(x = 485, y = 75, height = 75, width = 105)

  autoclicker_btn = Button(shopscreen, text = "AutoClicker", command = lambda: enable_autoclicker(), font = ("consolas", 10))
  autoclicker_btn.place(x = -10, y = 150, width = 495, height = 75)
  autoclicker_cost = Button(shopscreen, text = "30k", command = lambda: enable_autoclicker(), font = ("consolas", 10))
  autoclicker_cost.place(x = 485, y = 150, width = 105, height = 75)
  ac_speed_btn = Button(shopscreen, text = "AutoClicker speed (1/s)", command = lambda: change_ac_speed(1000, 50000), font = ("consolas", 10))
  ac_speed_cost = Button(shopscreen, text = "50k", command = lambda: change_ac_speed(1000, 50000), font = ("consolas", 10))
  ac_speed_btn.place(x = -10, y = 225, width = 495, height = 75)
  ac_speed_cost.place(x = 485, y = 225, width = 105, height = 75)

  refresh_shop(coins, click_multiplier)

def change_ac_speed(value, cost): # Change AutoClicker Speed
  global aclick_speed, buyed, b, ac_speed_btn, ac_speed_cost, coins

  if coins >= cost:
    coins -= cost
    aclick_speed = value

    if b == 1:
      ac_speed_btn.config(text="AutoClicker speed (1.25/s)", command=lambda: change_ac_speed(750, 75000), font=("consolas", 10))
      ac_speed_cost.config(text="75k", command=lambda: change_ac_speed(750, 75000), font=("consolas", 10))
      b += 1

    elif b == 2:
      ac_speed_btn.config(text="AutoClicker speed (1.5/s)", command=lambda: change_ac_speed(666, 100000), font=("consolas", 10))
      ac_speed_cost.config(text="100k", command=lambda: change_ac_speed(666, 100000), font=("consolas", 10))
      b += 1

    elif b == 3:
      ac_speed_btn.config(text="AutoClicker speed (2/s)", command=lambda: change_ac_speed(500, 150000), font=("consolas", 10))
      ac_speed_cost.config(text="150k", command=lambda: change_ac_speed(500, 150000), font=("consolas", 10))
      b += 1

    elif b == 4:
      ac_speed_btn.config(text="AutoClicker speed (5/s)", command=lambda: change_ac_speed(200, 500000), font=("consolas", 10))
      ac_speed_cost.config(text="500k", command=lambda: change_ac_speed(200, 500000), font=("consolas", 10))
      b += 1

    elif b == 5:
      ac_speed_btn.config(text="AutoClicker speed (10/s)", command=lambda: change_ac_speed(100, 1000000), font=("consolas", 10))
      ac_speed_cost.config(text="1mln", command=lambda: change_ac_speed(100, 1000000), font=("consolas", 10))
      b += 1

    elif b == 6:
      ac_speed_btn.config(text="AutoClicker speed (50/s)", command=lambda: change_ac_speed(100, 2000000), font=("consolas", 10))
      ac_speed_cost.config(text="2mln", command=lambda: change_ac_speed(50, 2000000), font=("consolas", 10))
      b += 1

    elif b == 7:
      ac_speed_btn.config(text="AutoClicker speed (100/s)", command=lambda: change_ac_speed(10, 5000000), font=("consolas", 10))
      ac_speed_cost.config(text="5mln", command=lambda: change_ac_speed(10, 5000000), font=("consolas", 10))
      b += 1

    elif b == 8:
      ac_speed_btn.config(text="AutoClicker speed (500/s)", command=lambda: change_ac_speed(5, 7500000), font=("consolas", 10))
      ac_speed_cost.config(text="7.5mln", command=lambda: change_ac_speed(5, 7500000), font=("consolas", 10))
      b += 1

    elif b == 9:
      ac_speed_btn.config(text="AutoClicker speed (1000/s)", command=lambda: change_ac_speed(1, 10000000), font=("consolas", 10))
      ac_speed_cost.config(text="10mln", command=lambda: change_ac_speed(1, 10000000), font=("consolas", 10))
      b += 1

    elif b == 10:
      ac_speed_btn.config(text = "Max", state = DISABLED)
      ac_speed_btn.place(x = 0, y = 225, width = 590)
      ac_speed_cost.destroy()

  refresh_home(coins, clicks)
  refresh_stats(coin_multiplier, click_multiplier, aclick_speed)

def enable_autoclicker():
   global autoclick, coins, aclick_speed, autoclicker_btn, autoclicker_cost, buyed

   if coins >= 30000 and not buyed:
     coins -= 30000
     buyed = True
   if buyed:
     autoclick = True
     autoclicker()
     autoclicker_btn.config(command = disable_autoclicker)
     autoclicker_cost.config(text = "Deactivate", command = disable_autoclicker, font = ("consolas", 6))
     refresh_shop(coins, click_multiplier)
     refresh_stats(coin_multiplier, click_multiplier, aclick_speed)

def disable_autoclicker():
   global autoclick, aclick_speed

   autoclick = False # Given that autoclicker() checks the variable autoclick every time that it clicks the button, setting it to False will make it stop running
   autoclicker_btn.config(command = enable_autoclicker)
   autoclicker_cost.config(text = "Activate", command = enable_autoclicker, font = ("consolas", 10))
   refresh_shop(coins, click_multiplier)
   refresh_stats(coin_multiplier, click_multiplier, aclick_speed)

def autoclicker():
  global autoclick, aclick_speed, coin_multiplier, click_multiplier

  if autoclick:
    click()
    window.after(aclick_speed, autoclicker)
    refresh_stats(coin_multiplier, click_multiplier, aclick_speed)

# Buttons
button = Button(window, bg = "red", command = click, activebackground = "red", border = 5)
clickme = Label(window, text = "Click me!", font = ("consolas", 20))
number = Label(window, text = f'You clicked me {round(clicks, 1)} times!', font = ("consolas", 8))
coinindicator = Label(window, text = f"{round(coins, 1)} coins")
button.place(x = 125, y = 75, width = 250, height = 250)
clickme.place(x = 0, y = 350, width = 500)
number.place(x = 50, y = 440, width = 400)
coinindicator.place(x = 0, y = 0)

shop = Button(window, text = "Shop", command = open_shop, font = ("consolas", 8), width = 10)
shop.place(relx = 1.0, rely = 0.0, anchor='ne')

stats = Button(window, text = "Stats", command = open_stats, font = ("consolas", 8), width = 10)
stats.place(relx = 0.5, rely = 1.0, anchor='s')

window.mainloop()