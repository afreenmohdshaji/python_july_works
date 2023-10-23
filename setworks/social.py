all_user=["mammooty","mohanlal","prithvi","nivin","dq","dhanush"]

nivin_friends=["dq","prithvi","dhanush"]
dq_friends={"prithvi","mammooty","nivin","mohanlal"}

all_user_set=set(all_user)
nivin_friends_set=set(nivin_friends)

# suggestions=all_user_set.difference(nivin_friends)
# suggestions.discard("nivin")
# print(suggestions)
mutual_friends=dq_friends.intersection(nivin_friends_set)
print(mutual_friends)