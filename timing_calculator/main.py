import random
from pyscript import document

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
units = [['hours', .125], ['days', 1], ['weeks', 5]]

print("Work times:")
total_step_time=0
total_wait_time=0
for x in range(8):
  unit = random.choice(units)
  step_time = random.choice(numbers)
  total_step_time += step_time * unit[1]
  print(str(step_time) + f" {unit[0]}")

print("\nWait times:")
for x in range(7):
  unit = random.choice(units)
  wait_time = random.choice(numbers)
  total_wait_time += wait_time * unit[1]
  print(str(wait_time) + f" {unit[0]}")

print("\nTotal Step Time: " + f"{round(total_step_time, 1)} days")
print("Total Wait Time: " + f"{round(total_wait_time, 1)} days")
total_lead_time = total_step_time + total_wait_time
print("Total Lead Time: " + f"{round(total_lead_time, 1)} days")
print("Step Time as a % of Lead Time: " +f"{total_step_time/total_lead_time:.0%}")


# Set the height of the terminal
terminal = document.querySelector('.xterm-screen')
terminal.style.height = '500px'
terminal = document.querySelector('.xterm-rows')
terminal.style.height = '500px'
