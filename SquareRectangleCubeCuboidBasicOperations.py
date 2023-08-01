import math

# Requesting the shape from the user.
print("Shapes: 1-Square\n\t2-Rectangle\n\t3-Cube\n\t4-Cuboid\n")
op_bool = True

while op_bool:
    try:
        shape_input = int(input("Choose an option: "))
        #If the user chooses Square
        if (shape_input == 1):

            #Taking input of square's side
            square_side = int(input("Enter side of the square in cm: "))
            print("Operations available:   1-Area\n\t\t\t2-Perimeter\n\t\t\t3-Diagonal")
            
            while True:
                try:
                    operation_input = int(input("Choose an option(1-3): "))

                    #Calculations
                    square_area = square_side ** 2
                    square_perimeter = square_side * 4
                    square_diagonal = square_side * (math.sqrt(2))

                    #Printing Area of the square
                    if (operation_input == 1):
                        print(f"Area of square of side {square_side}cm is {square_area}cm^2.")
                        op_bool = False
                        break
                    #Printing Perimeter of the square
                    elif (operation_input == 2):
                        print(f"The perimeter of square of side {square_side}cm is {square_perimeter}cm")
                        op_bool = False
                        break
                    #Printing Diagonal of the square
                    elif (operation_input == 3):
                        print(f"The Diagonal of square of side {square_side}cm is {square_diagonal}cm")
                        op_bool = False
                        break
                except ValueError:
                    print("Invalid input. Please choose a valid option(1-3).")

        elif (shape_input == 2):
            
            #Taking input of rectangle's dimentions
            rectangle_length = int(input("Enter the length of the rectangle: ")) 
            rectangle_width = int(input("Enter the width of the rectangle:"))
            print("Operations available:   1-Area\n\t\t\t2-Perimeter\n\t\t\t3-Diagonal")

            while op_bool:
                try:
                    operation_input = int(input("Choose an option(1-3): "))

                    #Calculations
                    rectangle_area = rectangle_length * rectangle_width
                    rectangle_perimeter = 2 * (rectangle_length + rectangle_width)
                    rectangle_diagonal = math.sqrt((rectangle_length ** 2) + (rectangle_width ** 2))

                    #Printing area of the rectangle
                    if (operation_input == 1):
                        print(f"Area of rectangle is {rectangle_area}cm^2")
                        op_bool = False
                        break
                    #Printing the perimeter of the rectangle
                    elif (operation_input == 2):
                        print(f"Perimeter of rectangle is {rectangle_perimeter}cm")
                        op_bool = False
                        break
                    #Printing the Diagonal of rectangle
                    elif (operation_input == 3):
                        print(f"Diagonal of rectangle is {rectangle_diagonal}cm")
                        op_bool = False
                        break
                except ValueError:
                    print("Invalid input. Please choose a valid option(1-3).")

        elif (shape_input == 3):

            #Taking input of cube's side
            cube_side = int(input("Please enter the side of the cube: "))
            print("Operations available:   1-Surface Area\n\t\t\t2-Diagonal\n\t\t\t3-Volume")

            while op_bool == True:
                try:
                    operation_input = int(input("Choose an option(1-3): "))

                    #Calculations
                    cube_surface_area = 6 * (cube_side ** 2)
                    cube_diagonal = (math.sqrt(3) * cube_side)
                    cube_volume = cube_side ** 3

                    #Printing the surface area of the cube
                    if (operation_input == 1):
                        print(f"The surface area of the cube is {cube_surface_area}cm^2")
                        op_bool = False
                        break
                    
                    #Printing the Diagonal of the cube
                    if (operation_input == 2):
                        print(f"The diagonal of the cube is {cube_volume}cm")
                        op_bool = False
                        break

                    #Printing the Volume of the cube
                    if (operation_input == 3):
                        print(f"The volume of the cube is {cube_volume}cm^3")

                except ValueError:
                    print("Invalid Input. Please choose a valid option(1-3)")

        elif (shape_input == 4):
            #Taking in the cuboid's dimentions
            cuboid_length = int(input("Enter the lenth of cuboid: "))
            cuboid_width = int(input("Enter the width of cuboid: "))
            cuboid_hieght = int(input("Enter the hieght of the cuboid: "))

            #Calculations
            cuboid_surface_area = 2 * ((cuboid_length * cuboid_width) + (cuboid_width * cuboid_hieght) + (cuboid_length * cuboid_hieght))
            cuboid_diagonal = math.sqrt((cuboid_length ** 2) + (cuboid_width ** 2) + (cuboid_hieght ** 2))
            cuboid_volume = cuboid_length * cuboid_hieght * cuboid_width

            #Printing the surface area of the cuboid
            if (operation_input == 1):
                print(f"The surface are of cuboid is {cuboid_surface_area}cm^2")
                op_bool = False
                break
            elif (operation_input == 2):
                print(f"The diagonal of cube is {cuboid_diagonal}cm")
                op_bool = False
                break
            elif (operation_input == 3):
                print(f"The volume of cube is {cube_volume}cm^3")
                op_bool = False
                break



    except ValueError:
        print("Invalid input. Please choose a valid option(1-4).")



input("Press enter to exit;")
