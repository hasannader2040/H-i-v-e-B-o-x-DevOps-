import sys

def print_app_version_and_exit():
    # Define the current version of the application
    app_version = "v0.0.1"

    # Print the current version
    print(f"Current application version: {app_version}")

    # Exit the application
    sys.exit(0)

# Example of calling the function
if __name__ == "__main__":
    print_app_version_and_exit()
