def add_setting(settings, pair):
    key = pair[0].lower()
    value = pair[1].lower()
    key_list = list(settings.keys())

    if key in key_list :
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else :
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    

def update_setting(settings, pair) :
    key = pair[0].lower()
    value = pair[1].lower()
    key_list = list(settings.keys())

    if key in key_list :
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else :
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key) :
    key = key.lower()
    key_list= list(settings.keys())

    if key in key_list:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else :
        return "Setting not found!"
        
def view_settings(settings) :
    if settings == {} :
        return "No settings available."
    else :
        output = ["Current User Settings:"]
        for key, value in settings.items():
            output.append(f"{key.capitalize()}: {value}")
        return '\n'.join(output) + '\n'
        

test_settings = {
    'theme': 'light', 
    'notifications': 'enabled', 
    'volume': 'low'
}
t2 = {}

print(view_settings(test_settings))
print("****")
print(view_settings(t2))


