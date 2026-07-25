# Slot machine in OOP

import time
import random

class SlotMachine:

    balance = 100
    symbols = ["🍊", "🍉", "🍍", "🍇"]

    def __init__(self, bet):
        self.bet = bet

    def spin(self):
        
        if SlotMachine.balance - SlotMachine.bet <= 0:
            print("You don't have enough money!")
            SlotMachine
        else:
            self.random1 = random.choice(SlotMachine.symbols)
            self.random2 = random.choice(SlotMachine.symbols)
            self.random3 = random.choice(SlotMachine.symbols)
        
    def payout(self):
        SlotMachine.spin()
        if SlotMachine.random1 == SlotMachine.random2 == SlotMachine.random3 == "🍇":
            print("YAY! You have won $100")
            SlotMachine.balance += 100
        elif SlotMachine.random1 == SlotMachine.random2 == SlotMachine.random3 == "🍍":
            print("YAY! You have won $1000")
            SlotMachine.balance += 1000
        elif SlotMachine.random1 == SlotMachine.random2 == SlotMachine.random3 == "🍉":
            print("YAY! You have won $10000")
            SlotMachine.balance += 10000
        elif SlotMachine.random1 == SlotMachine.random2 == SlotMachine.random3 == "🍊":
            print("YAY! You have won $100000")
            SlotMachine.balance += 100000
        else:
            print("You Lost!")

# The Build

while True:

    print("**************************************")
    print("         Welcome to Python Slots!     ")
    print("         Symbols: 🍊 🍉 🍍 🍇       ")
    print("**************************************")
    print(f"Current Balance: ${SlotMachine.balance}")
    bet = int(input("Enter the bet amount: "))

    print("Spining.........")
    time.sleep(3)

    slotmachine = SlotMachine(bet)
    slotmachine.spin()

    print("****************************")
    print(f"{slotmachine.random1} | {slotmachine.random2} | {slotmachine.random3}")
    print("****************************")
    slotmachine.payout()