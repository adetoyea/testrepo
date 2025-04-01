#Just testing the superlinter

def predict_gender(name):
    male_names = {"John", "Michael", "William", "James", "Robert"}
    female_names = {"Mary", "Jennifer", "Linda", "Elizabeth", "Emily"}

    if name in male_names:
        return "Male"
    elif name in female_names:
        return "Female"
    else:
        return "Unknown"

# Example usage
name = input("Enter child's name: ")
print(f"Predicted Gender: {predict_gender(name)}")
