players = ["renaldo",'messi','Osel','shoemacher']

print(players[:3])
# displays the first three values.
print(players[2:])
# displays values from 2 onwards
print(players[1:4])
# Displays values between 1 and 4

print('Here are some of the players on the world rankings:')
for player in players[:3]:
	print(f'\t{player.title()}')