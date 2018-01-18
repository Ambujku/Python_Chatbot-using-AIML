import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")

else:
    kernel.bootstrap(learnFiles = "Standard.aiml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

kernel.respond("load aiml b")

while True:
	print kernel.respond(raw_input("Please enter your Messages \n"))