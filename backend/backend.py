import pyautogui as auto
import keyboard as kb

print("Aim cursor at your fist and click enter")
kb.wait("enter")
fistPos= auto.position()

print("Aim cursor at your farmable and click enter")
kb.wait("enter")
farmPos = auto.position()


try:
    farmHardness = int(input("What is your farmable hardness?"))
except ValueError:
    print("Must Be An Integer!")

print("Aim cursor at Break position and click enter")
kb.wait("enter")
breakPos = auto.position()
#how many farmables position do you want to break?
# for num in range (jumlahFarmable):
# print("position?")
# currentPos = auto.position()
# hitPositions.append(currentPos)

hitPositions = []

auto.click(farmPos)
auto.click(breakPos)
auto.click(fistPos)
for number in range (farmHardness):
    auto.click(breakPos)