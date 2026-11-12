from pyscript import document


# desserts i picked out :p
desserts = {
    "Mochi": ("Japan", "Soft and chewy"),
    "Tiramisu": ("Italy", "Creamy with coffee and cocoa"),
    "Macaron": ("France", "Crisp outside, soft and sweet inside"),
    "Cupcake": ("USA", "Fluffy cake with sweet frosting"),
    "Donut": ("USA", "Fluffy and glazed"),
    "Ice Cream": ("Italy", "Cold and creamy"),
    "Pudding": ("England", "Smooth and silky with caramel"),
    "Churros": ("Spain", "Crunchy and cinnamon-sugar coated"),
    "Halo-Halo": ("Philippines", "Icy and colorful"),
    "Leche Flan": ("Philippines", "Rich, creamy caramel custard"),
    "Brownie": ("USA", "Fudgy and chocolatey"),
    "Crepe": ("France", "Thin, soft and filled with sweet cream"),
}

# checks if the dessert inputted by the user is apart of my list
def dessert_checker(event):
    name = document.getElementById("dessert").value.strip().title()
    result = desserts.get(name, ("-", "Dessert not found"))

    document.getElementById("result").innerHTML = f"""
<b>Dessert:</b> {name}<br>
<b>Origin:</b> {result[0]}<br>
<b>Taste:</b> {result[1]}<br>
"""