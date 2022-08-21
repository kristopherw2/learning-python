# Create a list of names and use a for loop to output the length of each name (len())
# Add an if check inside the loop to only output names longer than 5
# Add another if check to see wether a name includes a 'n' or 'N' character.
# Use a while loop to empty the list of names (via pop())


names = ['Kristopher', 'Zoe', 'Evan', 'Maximillion']

for name in names:
    if len(name) > 5 and ('n' in name or 'N' in name):
        print(name)
while len(names) > 0:
    names.pop()

print(names)