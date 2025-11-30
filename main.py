# Grade Calculator
from pyscript import display, document # pyright: ignore[reportMissingImports]

def calculate_gwa(e):
    document.getElementById('profile_info').innerHTML = ""  # Clear Output
    document.getElementById('gwa_result').innerHTML = ""    # Clear Output

    # Student Details
    first_name = document.getElementById("fname").value.strip()
    surname = document.getElementById("lname").value.strip()

    # Subjects
    fil = int(document.getElementById('filipino').value)
    eng = int(document.getElementById('english').value)
    math = int(document.getElementById('mathematics').value)
    sci = int(document.getElementById('science').value)
    ss = int(document.getElementById('ss').value)
    ict = int(document.getElementById('ict').value)

    grades = [fil, eng, math, sci, ss, ict] # List of subjects
    units = (3, 5 , 5, 4, 3, 1) # Units of each subject

    # Calculating the GWA
    total_units = sum(units)    # Getting the sum of the units
    weighted_sum = sum(grades[i] * units[i] for i in range(len(grades)))    # Multiplies each grade by its subject unit and sum to get the GWA
    gwa = round(weighted_sum / total_units, 2)    # Weighted sum divided by total units

    # Displaying the result of inputted values
    display(f"Name: {first_name} {surname}", target="profile_info")
    display(f"Your General Weighted Average is: {gwa}", target = 'gwa_result')

# School Club Information
club_data = {
    "Glee Club":{
        "Description":"The singing club of OBMC.",
        "Meeting Time":"Every Monday and Thursday 3:00-4:30 PM",
        "Location":"HS Music Room",
        "Club Moderator":"Mary Margery Loyola",
        "Number of Members":"38"
    },
    "Commarts Club":{
        "Description":"The communication and writing club of OBMC.",
        "Meeting Time":"Every Tuesday and Wednesday 3:00-4:30 PM",
        "Location":"HS Communication Room",
        "Club Moderator":"Roman Gerard Loreto",
        "Number of Members":"24"
    },
    "Dance Club":{
        "Description":"The dancing club of OBMC.",
        "Meeting Time":"Every Thursday and Friday 3:00-4:30 PM",
        "Location":"HS Dance Room",
        "Club Moderator":"Akihiro Marutani",
        "Number of Members":"28"
    }
}

def club_information(e):
    document.getElementById("club_name").innerHTML = "" # Clear Output
    document.getElementById("information").innerHTML = ""   # Clear Output

    # Getting the value from the selected club
    get_value = document.getElementById("clubDropdown").value

    # If nothing selected
    if get_value == "":
        display("Please choose a club first.", target="information")
        return

    # Checks which club you chose from the dropdown and, if it’s valid, shows that club’s information on the page
    subject_data = club_data[get_value]

    # Displaying the result of inputted values
    display(f"{get_value}", target="club_name")
    display(f"Description: {subject_data['Description']}", target="information")
    display(f"Meeting Time: {subject_data['Meeting Time']}", target="information")
    display(f"Location: {subject_data['Location']}", target="information")
    display(f"Club Moderator: {subject_data['Club Moderator']}", target="information")
    display(f"Number of Members: {subject_data['Number of Members']}", target="information")