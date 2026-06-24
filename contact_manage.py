import json
import logging

# Name of our database file
FILE_NAME = "contact.json"
LOG_FILE = "app_activity.log"


#  CUSTOM EXCEPTION DEFINITIONS


class DuplicateContactError(Exception):
    """Custom error raised when attempting to add an existing name contact."""
    pass

class InvalidContactInputError(Exception):
    """Custom error raised when mandatory input rows are left blank."""
    pass



#  SYSTEM DIAGNOSTIC LOGGING CONFIGURATION


# Setting up our logger file stream pipeline cleanly
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


#  FILE HANDLING & SERIALIZATION CHANNELS


def load_contacts():
    """Loads contacts from the JSON file safely with error boundaries."""
    try:
        logging.info("Attempting to load data rows off local storage disk...")
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info(f"Database synced successfully. Loaded {len(data)} contacts.")
            return data
            
    except FileNotFoundError:
        #  Graceful handling of missing files
        logging.warning(f"'{FILE_NAME}' not found on disk. Initializing a clean memory array.")
        return []
        
    except json.JSONDecodeError:
        #  Graceful handling of corrupted files
        logging.error(f"Critical Error: '{FILE_NAME}' contains corrupted text lines.")
        print("⚠️ Warning: System detected corrupted file formatting on disk. Starting with a clean temporary database.")
        return []
        
    except Exception as general_error:
        # Catch-all safety net block for unexpected file block issues
        logging.error(f"Unexpected operational leak during load: {general_error}")
        return []


def save_contacts(contacts_list):
    """Saves the active contacts memory array list back down to the JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(contacts_list, file, indent=4)
        logging.info("Disk write committed successfully. Local changes synced to hard drive.")
    except Exception as write_error:
        logging.error(f"Failed to execute file write pipeline: {write_error}")
        print("❌ System Error: Unable to save changes permanently to file storage.")



#  CORE FEATURE PLATFORM FUNCTIONS


def add_new_contact(contacts_list):
    """Prompts user for inputs and safely commits a new contact entry map."""
    print("\n--- Create New Contact ---")
    name = input("Enter Full Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email Address: ").strip()
    category = input("Enter Category (e.g., Friends, Work, Family): ").strip()

    try:
        #  Custom Input Verification & Error Triggers
        if not name or not phone:
            raise InvalidContactInputError("Name and Phone Number are strictly mandatory fields.")

        #  Custom Duplicate Check & Error Triggers
        for contact in contacts_list:
            if contact["name"].lower() == name.lower():
                raise DuplicateContactError(f"A profile record under the name '{name}' already exists.")

    except InvalidContactInputError as error_msg:
        # Capture and log specific blank field operations
        print(f"❌ Input Validation Refusal: {error_msg}")
        logging.warning(f"Registration Refused: User left mandatory attributes empty.")
        return # Graceful return to loop grid

    except DuplicateContactError as error_msg:
        # Capture duplicate metrics and handle gracefully without crashing
        print(f"❌ Input Rejection: {error_msg}")
        logging.warning(f"Registration Replaced Attempt: Duplicate check hit for target name '{name}'.")
        return

    else:
        #  This block runs ONLY if no exceptions were thrown above
        if not category:
            category = "General"

        new_contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "category": category
        }

        contacts_list.append(new_contact)
        save_contacts(contacts_list)
        print(f"✅ Success: '{name}' added to your contacts!")
        logging.info(f"User Action: Successfully created new contact entry profile for '{name}'.")
        
    finally:
        #  This block runs no matter what happened before (Cleanups/Resets)
        print("System Notice: Completed contact creation routing check sequence.")


def view_all_contacts(contacts_list):
    """Displays all contacts neatly formatted onto terminal grids."""
    print("\n--- All Registered Contacts ---")
    if not contacts_list:
        print("Your database is empty.")
        return

    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25} | {'Category':<12}")
    print("-" * 78)
    for c in contacts_list:
        print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25} | {c['category']:<12}")


def search_contact(contacts_list):
    """Filters directory matching name, email, or category metrics."""
    print("\n--- Search Directory ---")
    query = input("Enter search keyword: ").strip().lower()

    if not query:
        print("❌ Search cancelled. Empty keyword string.")
        return

    found_any = False
    print(f"\nSearching database for queries matching: '{query}'...")
    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25} | {'Category':<12}")
    print("-" * 78)

    for c in contacts_list:
        if (query in c["name"].lower() or 
            query in c["email"].lower() or 
            query in c["category"].lower()):
            print(f"{c['name']:<20} | {c['phone']:<15} | {c['email']:<25} | {c['category']:<12}")
            found_any = True

    if not found_any:
        print("No matching contact entries found.")
        logging.info(f"Search Query run for filter parameter '{query}' with zero matches returned.")



#  MENU DASHBOARD RUNNER LOOP


def main():
    logging.info("--- Application Workspace System Session Started ---")
    my_contacts = load_contacts()
    
    print("⚡ ScholarOps Persistent JSON Database Platform (Day 3)")
    print(f"📁 Tracking Diagnostics Live on local file path: '{LOG_FILE}'")

    while True:
        print("\n=== Navigation Menu ===")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contacts")
        print("4. Exit System")
        
        choice = input("\nEnter option number (1-4): ").strip()

        if choice == "1":
            add_new_contact(my_contacts)
        elif choice == "2":
            view_all_contacts(my_contacts)
        elif choice == "3":
            search_contact(my_contacts)
        elif choice == "4":
            print("🚀 Secure database logging loop closed safely. Happy coding!")
            logging.info("--- Application Workspace System Session Closed Gracefully ---")
            break
        else:
            print("❌ Invalid entry option value! Please choose numbers 1 through 4.")
            logging.warning(f"User Interface Input Warn: Unrecognized choice input variant entered: '{choice}'")

if __name__ == "__main__":
    main()