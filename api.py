from rivescript import RiveScript
bot = RiveScript()
bot.load_file("brain.rive")	
bot.sort_replies()
while True:
	try:
		msg = input("You> ")
		reply = bot.reply("localuser", msg)
		print("Bot>", reply)

	except(KeyboardInterrupt, EOFError, SystemExit):
		break


