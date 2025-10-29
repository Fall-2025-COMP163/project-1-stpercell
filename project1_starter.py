"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Shikel Percell]
Date: [10/27/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""
#==================================================================my code part 1==================================================================================
    def calculate_stats(character_class):
    character_class = character_class.lower()
#Took inspo from my favorite game (metaphor refantazio)
    if character_class == "mage":#spells
        return {"strength": 5, "magic": 15,"agility": 3, "health": 80, "gold": 100}
    elif character_class == "warrior":#basic all rounder
        return {"strength": 12, "magic": 3,"agility": 8, "health": 120, "gold": 100}
    elif character_class == "rogue":#Speed
        return {"strength": 8, "magic": 5,"agility": 15, "health": 100, "gold": 100}
    elif character_class == "brawler":#as the name entails
        return {"strength": 18, "magic": 1,"agility": 5, "health": 150, "gold": 100}
    elif character_class == "cleric":#healer class
        return {"strength": 3, "magic": 12,"agility": 8, "health": 50, "gold": 100}
    elif character_class == "saiyans":#secret dbz class
        return {"strength": 9000, "magic": 20000,"agility": 9000, "health": 10000, "gold": 10000}#magic is ki and gold is zeni
#all stat calcs with diff classes
def create_character(name, character_class):
    stats = calculate_stats(character_class)
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": stats["strength"],
        "magic": stats["magic"],
        "agility": stats["agility"],
        "health": stats["health"],
        "gold": stats["gold"]
    }
    return character
character = create_character("Shikel", "saiyans")
print(character)
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



def calculate_stats(character_class):
    character_class = character_class.lower()
#Took inspo from my favorite game (metaphor refantazio)
    if character_class == "mage":#spells
        return {"strength": 5, "magic": 15,"agility": 3, "health": 80, "gold": 100}
    elif character_class == "warrior":#basic all rounder
        return {"strength": 12, "magic": 3,"agility": 8, "health": 120, "gold": 100}
    elif character_class == "rogue":#Speed
        return {"strength": 8, "magic": 5,"agility": 15, "health": 100, "gold": 100}
    elif character_class == "brawler":#as the name entails
        return {"strength": 18, "magic": 1,"agility": 5, "health": 150, "gold": 100}
    elif character_class == "cleric":#healer class
        return {"strength": 3, "magic": 12,"agility": 8, "health": 50, "gold": 100}
    elif character_class == "saiyans":#secret dbz class
        return {"strength": 9000, "magic": 20000,"agility": 9000, "health": 10000, "gold": 10000}#magic is ki and gold is zeni

    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, filename):
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

def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

def display_character(character):
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
