#dictionary

Union_of_states = {
    "Andrapradesh": "Amaravathi",
    "Telangana": "Hyderabad",
    "Karnataka": "Bengalur"
}

#list in dictionary

Union_of_states = {
    "Andrapradesh": ["Amaravathi", "Karnool", "Vizag"],
    "Telangana": "Hyderabad",
    "Karnataka": "Bengalur"
}

#dictionary in a dictionary

Union_of_states = {
    "Andrapradesh": {
        "TDP": "Amaravathi",
        "YCP": "Vizag",
        "People": "fuck politicians"
    },
    "Telangana": "Hyderabad",
    "Karnataka": "Bengalur"
}
print(Union_of_states)
print(Union_of_states["Andrapradesh"])
print(Union_of_states["Andrapradesh"]["People"])