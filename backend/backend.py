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


hitPositions = []

auto.click(farmPos)
auto.click(breakPos)
auto.click(fistPos)
for number in range (farmHardness):
    auto.click(breakPos)

# left 466, 710   //magplant/block (farmPos)
# left 568, 429   //place block (breakPos)
# wait 100
# left 638, 422   //place block
# wait 100
# left 390, 709   //fist
# left_down 568, 429    //break
# wait 1000
# left_up 568, 429
# wait 100
# left_down 638, 422    //break
# wait 1000
# left_up 638,422