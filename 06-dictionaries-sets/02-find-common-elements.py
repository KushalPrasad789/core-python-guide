# Use sets to find common friends between alice_friends = {"Bob", "Charlie"} and bob_friends = {"Charlie", "Diana"}.

alice_friends = {"Bob", "Charlie"}
bob_friends = {"Charlie", "Diana"}

common_friends = alice_friends.intersection(bob_friends)
print(common_friends)