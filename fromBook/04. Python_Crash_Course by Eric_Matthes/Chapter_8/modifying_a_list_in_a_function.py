## start with some design that need to be printed


unprinted_design = ["iphone case", "robot pendant", "didecahedron"]

completed_models = []

## Simulate printing each design, untill none are left

## move each design to cpmpleted models after printing

while unprinted_design:
    current_design = unprinted_design.pop()
    print("Printing model: " + current_design.title())
    completed_models.append(current_design)
### display all completed models.

print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model.title())


