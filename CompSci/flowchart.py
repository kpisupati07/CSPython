import schemdraw
import schemdraw.elements as elm

d = schemdraw.Drawing()

# Define the nodes
start = d.add(elm.RBox(w=6, h=2).label('Manufacturer'))
sol_clarity = d.add(elm.RBox(w=8, h=2).label('Sol-Clarity'))
contractor = d.add(elm.RBox(w=8, h=2).label('Contractor'))
overseas = d.add(elm.RBox(w=8, h=2).label('Overseas'))
profit = d.add(elm.RBox(w=6, h=2).label('Profit'))

# Connect the nodes with arrows
d.add(elm.Line().right().at(start.E))
d.add(elm.Arrow().down())
d.add(elm.Line().down().at(sol_clarity.S))
d.add(elm.Arrow().down())
d.add(elm.Line().down().at(contractor.S))
d.add(elm.Arrow().down())
d.add(elm.Line().down().at(overseas.S))
d.add(elm.Arrow().down())
d.add(elm.Line().down().at(profit.S))

# Encircle the nodes
phase1 = d.add(elm.EncircleBox([start, sol_clarity, contractor], padx=.8).linestyle('--').linewidth(2).color('red'))
phase2 = d.add(elm.EncircleBox([overseas], padx=.8).linestyle('--').linewidth(2).color('blue'))

# Save the flowchart as a PNG file
d.save('flowchart.png')
