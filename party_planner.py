import cgi

party_items = {
    0: ("Cake", 20),
    1: ("Balloons", 21),
    2: ("Music System", 10),
    3: ("Lights", 5),
    4: ("Catering Service", 8),
    5: ("DJ", 3),
    6: ("Photo Booth", 15),
    7: ("Tables", 7),
    8: ("Chairs", 12),
    9: ("Drinks", 6),
    10: ("Party Hats", 9),
    11: ("Streamers", 18),
    12: ("Invitation Cards", 4),
    13: ("Party Games", 2),
    14: ("Cleaning Service", 11),
}

form = cgi.FieldStorage()
selected_indices_str = form.getfirst("items", "")

try:
    selected_indices = [int(i.strip()) for i in selected_indices_str.split(",") if i.strip().isdigit()]
except Exception:
    selected_indices = []

selected_items = []
values = []

for idx in selected_indices:
    if idx in party_items:
        name, val = party_items[idx]
        selected_items.append(name)
        values.append(val)

base_code = values[0] if values else 0
for val in values[1:]:
    base_code &= val

adjusted_code = base_code
if base_code == 0:
    adjusted_code += 5
    message = "Epic Party Incoming!"
elif base_code > 5:
    adjusted_code -= 2
    message = "Let's keep it classy!"
else:
    message = "Chill vibes only!"


print("Content-Type: text/html\n")
print("<html><head><title>Digital Party Planner</title></head><body>")
print("<h2>🎉 Digital Party Planner Results 🎉</h2>")

if selected_items:
    print("<p><strong>Selected Items:</strong> " + ", ".join(selected_items) + "</p>")
    print("<p><strong>Base Party Code:</strong> {}</p>".format(base_code))
    print("<p><strong>Final Party Code:</strong> {}</p>".format(adjusted_code))
    print("<p><strong>Message:</strong> {}</p>".format(message))
else:
    print("<p>No valid items selected.</p>")

print("</body></html>")