import pyautogui as auto
import keyboard as kb
import time

# Input parameters
farmHardness = int(input('Input your farm hardness in number: '))
positionsToHit = int(input("How many positions of blocks do you have? "))

# Get fist position
print("Aim cursor at your fist and click Enter")
kb.wait("enter")
fistPos = auto.position()

print("Aim cursor at your farmable in your inventory")
kb.wait("enter")
farmableInvPos = auto.position()

# Get positions of farmables
hitPositions = []
for position in range(positionsToHit):
    print(f"Aim cursor at position {position + 1} of your farmable and click Enter")
    kb.wait("enter")
    farmablePos = auto.position()
    hitPositions.append(farmablePos)
# Initialize index
indexCounter = 0

# Loop to automate the process
while True:
    # Place blocks
    auto.click(farmableInvPos)
    time.sleep(0.2)
    for pos in hitPositions:
        auto.click(pos)

    # Break blocks
    time.sleep(0.1)
    auto.click(fistPos)
    for pos in hitPositions:
        for _ in range(farmHardness):  # Hit the block the required number of times
            auto.moveTo(pos)
            auto.mouseDown()
