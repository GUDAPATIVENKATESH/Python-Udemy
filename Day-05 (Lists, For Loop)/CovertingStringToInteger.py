List_of_Strings = input("Enter the list of strings").split()
for s in range(0, len(List_of_Strings)) :
    List_of_Strings[s] = int(List_of_Strings[s])
print(List_of_Strings)