"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Shikel Percell]
Date: [10/27/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
#==================================================================my code part 1==================================================================================
#Took inspo from my favorite game (metaphor refantazio)
def create_character(name, character_class): #Takes the tupple from calculate stats and turns it into a dictionary
    stats = calculate_stats(character_class, 1)
    if stats is None:
        return None  
    strength, magic, health = stats
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character
 
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass
#==================================================================my code part 2==================================================================================
def calculate_stats(character_class, level=1): #makes stats based of class and makes it into a tuple
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # Convert class name to lowercase so it's easier to compare
    character_class = character_class.lower() #makes it so the class you choose isn't case sensitive
    
    # Change stats based on class
    if character_class == "mage":
        strength, magic, health = 5, 15, 80
    elif character_class == "warrior":
        strength, magic, health = 12, 3, 120
    elif character_class == "rogue":
        strength, magic, health = 8, 5, 100
    elif character_class == "brawler":
        strength, magic, health = 18, 1, 150
    elif character_class == "cleric":
        strength, magic, health = 3, 12, 50
    elif character_class == "saiyans": #extra class for fun
        strength, magic, health = 9000, 20000, 10000
    else:
        return None  # If class doesn't match any above
    
    # Each level adds +1 to every stat(wasn't needed until later)
    strength += level - 1 
    magic += level - 1
    health += level - 1

    # Return the three stats as a tuple
    return (strength, magic, health)
    pass

def save_character(character, filename): #saves the dictionary from create character as a txt file
    """
    Saves a character to a text file.
    Returns True if successful, False otherwise.
    """
    # Attempt to open file safely
    file = open(filename, "w") if "/" not in filename else None
    if file is None:
        return False

    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()
    return True

#just copies everything into filename(or wtv you call it) 
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

def load_character(filename): #loads said txt file when called upon
    # Step 1: open/close in "a" mode — creates file if missing
    open(filename, "a").close() #uses a so it can load a file which doesn't exist first for test cases

    # Step 2: now safely open for reading from start
    file = open(filename, "r") #then opens real file using r so it only reads and doesn't write
    lines = file.readlines() #readlines so it reads every line in the txt file
    file.close()

    # If file is empty, return None
    if not lines:
        return None

    character = {} # makes a empty dict. SO basically turns the first sections list into a dict
    for line in lines: # goes line by line in said dict
        if ": " in line: # this makes it so it only checks lines with : in it. Just to make sure its formatted correctly
            key, value = line.strip().split(": ", 1) # the strip part removes spaces and newlines while split makes it so everything before : is they key and everything else the value
            key = key.lower()
            # Convert "character name" → "name"
            if key == "character name":
                key = "name"
            if value.isdigit():
                value = int(value) #converts string to int
            character[key] = value # saves key/value in dict
# then all this loops until there isn't any more lines to be read from the fisrt section of the code
    return character
#this returns the dict so we can print it
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character): #displays all characters current info
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    character["level"] += 1
    stats = calculate_stats(character["class"], character["level"])
    if stats:
        strength, magic, health = stats
        character["strength"] = strength
        character["magic"] = magic
        character["health"] = health
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
