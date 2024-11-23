# *Wallpaper Roll Calculation Program*
## *Description*
+ This program is designed to calculate the number of rolls of wallpaper needed to cover a room, taking into account the size of walls, windows and doors. The user enters the dimensions of the room, windows, doors and the size of wallpaper rolls, and the program calculates the area to be wallpapered and displays the required number of rolls.
## *Functionality*
### **1. Calculation of the total wall area of a room:**
+ the length, width and height of the walls are taken into account.
### **2. Accounting for windows and doors:**
+ the user enters the count of windows and doors and their dimensions;
+ the program automatically subtracts the area of windows and doors from the total wall area.
### **3. Calculating the quantity of wallpaper rolls:**
+ the user specifies the dimensions of the wallpaper roll;
+ the program calculates the number of rolls required to wallpaper the room.
## *Features*
+ check for correctness of entered data (for example, the area of windows and doors cannot exceed the total wall area);
+ interactive data entry via console;
+ provides error messages for incorrect inputs.
## *Requirements*
+ **Python 3.7** or higher.
## *Project structure*
+ **get_sizes_of_room_class.py**: contains classes to handle room, windows, doors and wallpaper sizes;
+ **wallpaper_roll_calculation_program.py**: the main program file that implements data input and calculation logic.