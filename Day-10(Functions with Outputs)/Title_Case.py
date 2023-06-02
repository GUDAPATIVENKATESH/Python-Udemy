def title_case():
    F_Name = input("Enter your first name\n:").lower()
    L_Name = input("Enter your last name\n:").lower()
    # F_Name = "first"
    # L_Name = "lower"
    High_F_Name = F_Name[0].upper()
    High_L_Name = L_Name[0].upper()
    R_F_Name = ""
    R_L_Name = ""
    for letter in range(1, len(F_Name)) :
        R_F_Name += F_Name[letter] 
    for letter in range(1, len(L_Name)) :
        R_L_Name += L_Name[letter]
    FF_Name = High_F_Name + R_F_Name
    FL_Name = High_L_Name + R_L_Name
    print(f"Your name in Title Case is '{FF_Name} {FL_Name}'")

title_case()
