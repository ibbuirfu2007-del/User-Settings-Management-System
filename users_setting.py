"""
User Settings Management System

This program allows users to:
- Add new settings
- Update existing settings
- Delete settings
- View all settings
"""


# Initial user settings
test_settings = {
    "theme": "light",
    "language": "english",
    "notifications": "enabled"
}


def add_setting(settings, setting_tuple):
    """
    Add a new setting to the dictionary.
    """

    # Extract key and value from the tuple
    key, value = setting_tuple

    # Convert key and value to lowercase
    key_lower = key.lower()
    value_lower = value.lower()

    # Check if the setting already exists
    if key_lower in settings:
        return (
            f"Setting '{key_lower}' already exists! "
            "Cannot add a new setting with this name."
        )

    # Add the new setting
    settings[key_lower] = value_lower

    return (
        f"Setting '{key_lower}' added with value "
        f"'{value_lower}' successfully!"
    )


def update_setting(settings, setting_tuple):
    """
    Update an existing setting.
    """

    # Extract key and value from the tuple
    key, value = setting_tuple

    # Convert key and value to lowercase
    key_lower = key.lower()
    value_lower = value.lower()

    # Check if the setting exists
    if key_lower in settings:
        settings[key_lower] = value_lower

        return (
            f"Setting '{key_lower}' updated to "
            f"'{value_lower}' successfully!"
        )

    return (
        f"Setting '{key_lower}' does not exist! "
        "Cannot update a non-existing setting."
    )


def delete_setting(settings, key):
    """
    Delete an existing setting.
    """

    # Convert the key to lowercase
    key_lower = key.lower()

    # Check if the setting exists
    if key_lower in settings:
        del settings[key_lower]

        return f"Setting '{key_lower}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):
    """
    Display all current user settings.
    """

    # Check if the dictionary is empty
    if not settings:
        return "No settings available."

    result = "Current User Settings:\n"

    # Loop through all settings
    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result


# Example usage
if __name__ == "__main__":

    # Add a new setting
    print(add_setting(test_settings, ("font", "arial")))

    # Update an existing setting
    print(update_setting(test_settings, ("theme", "dark")))

    # Delete an existing setting
    print(delete_setting(test_settings, "language"))

    # View all settings
    print(view_settings(test_settings))