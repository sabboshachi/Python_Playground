def print_models(unprinted_designs, completed_models):
    """Simulate printing each design , untill none are left.
    Move each design to completed_design after printing."""

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all models taht were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model.title())

unprinted_designs = ["iphone case", "robot pendant", "didecahedron"]

completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

