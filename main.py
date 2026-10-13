from pyscript import document

def add_names(e):
    name1 = document.getElementById("input1").value
    name2 = document.getElementById("input2").value

    members = ["Cheree Mendoza", "Princess Schwab", "Zoey Ledres", "Therese Reyes", "Elise Ramos"]

    fullname = name1 + " " + name2

    if fullname in members:
        document.getElementById("output1").innerHTML = "Congratulations! You are now part of the School's Volleyball Varsity, " + fullname
    else:
        document.getElementById("output1").innerHTML = "Sorry! your name is NOT on the list, " + fullname
