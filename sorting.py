user_input = input("Enter a dictionary (e.g., {'a': 3, 'c': 1, 'b': 2}): ")

try:
    user_dict = eval(user_input)
    
    if isinstance(user_dict, dict):
        sorted_dict = dict(sorted(user_dict.items()))
        
        
        print("Sorted dictionary in ascending order by keys:", sorted_dict)
    else:
        print("Input is not a valid dictionary.")
except:
    print("Invalid input. Please enter a dictionary in the correct format.")