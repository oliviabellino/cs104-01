first_name = ["Olivia", "Natalie", "Mikayla", "Isabella", "Charli", "Dianna", "Ashley", "Caitlin", "Tahlia", "Rachael"]
names = []
for i in range(0,10):
    names.append(random.choice(first_name))
for i in range(0,len(names)):
    print(names.pop(0))
