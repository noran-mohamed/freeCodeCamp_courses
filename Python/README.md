# freeCodeCamp_courses
In this repo, I will put the code that I worked on during my learning at the freeCodeCamp courses!

# Python Course
## caesar.py -> Caesar Encryption Application  
This mini project is used to encrypt plaintext or decrypt encrypted_text 
The user can input the text that they wanna encrypt or decrypt, and also specify the shift amount.

<img src="logo/caesar_encryption.png" alt="Logo" width="150" height="150">

## RPG_char_builder.py -> An RPG Character Builder
A small program that creates an RPG character after validating the character name and three stats (Strength, Intelligence, and Charisma). The function must ensure the name follows specific rules (type, length, no spaces, etc.), the stats are valid integers within the range, and their total equals 7. If everything is valid, it returns a formatted character sheet displaying the character name and stat bars using full and empty dots.

<img src="Python/logo/rbg_character_builder.png" alt="Logo" width="150" height="150">

## pin_extractor.py -> A Pin Extractor from Poems
Given a poem or more, this mini project is used to extract the hidden pins in the input poems, where the nth digit of the pin is hidden as the length of the nth word in the nth line, e.g., the first digit of the pin is hidden as the length of the first word in the first line.

<img src="Python/logo/extractor.png" alt="Logo" width="150" height="150">

## medical_data_validator.py -> A Medical Data Validator
A small program that validates a list of medical records to ensure they follow a consistent format. Each record is checked to confirm it is a dictionary containing the required fields (patient ID, age, gender, diagnosis, medications, and last visit ID). If any record or field is invalid, the program reports detailed error messages indicating the unexpected format and the position of the faulty record; otherwise, it confirms that all records are valid.

<img src="Python/logo/med.png" alt="Logo" width="150" height="150">

## build_a_user_configuration_manager.py -> A User Configuration Manager
This program allows users to manage their settings such as theme, language, and notifications. I implemented functions to add, update, delete, and view user settings.

<img src="Python/logo/user.png" alt="Logo" width="150" height="150">

## ISBN_validator.py -> AN ISBN validator
The ISBN (International Standard Book Number) is a unique identifier assigned to commercial books. It can be either 10 or 13 digits long, and the last digit is a check digit calculated from the other digits. When the user runs the program, it will show the prompt **Enter ISBN and length:** The user can enter the ISBN code they want to validate in **ISBN,length** format. The ISBN code should not contain hyphens, followed by its length (10 or 13), separated by a comma.

Example inputs: 1530051126,10 for ISBN-10 codes. 9781530051120,13 for ISBN-13 codes.

<img src="Python/logo/isbn.png" alt="Logo" width="150" height="150">

## planet_class.py -> A Planet Class
This Python exercise defines a Planet class that represents a planet and its basic properties, along with simple validation to ensure all attributes are valid.  It provides methods to display planet information and simulate orbital behavior.

<img src="Python/logo/planet.png" alt="Logo" width="150" height="150">

## email_simulator.py -> An Email Simulator 
This mini program simulates sending, receiving, and managing emails between different users, by implementing classes, objects, and how to organize code in an object-oriented way.

<img src="Python/logo/email.png" alt="Logo" width="150" height="150">

## budget_app.py -> A Budget App 
This simple budget app tracks spending in different categories and can show the relative spending percentage on a graph.

<img src="Python/logo/budget_app.png" alt="Logo" width="150" height="150">

## salary_tracker.py -> A Salary Tracker System
A salary tracking system for employees.

<img src="Python/logo/salary.png" alt="Logo" width="150" height="150">

## discount_calculator_function.pthon -> A Discount Calculator Function
A function that calculates the final price of an item after applying a percentage discount.

## report_card_printer.py -> Report Card Printer
A simple report card printer.

## movie_ticket_booking_calculator.py -> Movie Ticket Booking Calculator
A mini program to handle the movie ticket booking process.

## game_char_stats_tracker.py -> A Game Character Stats Tracker
A game character stats tracker. The program will allow you to create a character with specific attributes, update those attributes, and retrieve the current stats of the character.

## media_catalogue.py -> A Media Catalogue System
A media catalogue system that manages movies and TV series using object-oriented principles, with validation, inheritance, custom exceptions, and categorized display of media items.

## discount_calculator.py -> A Discount Calculator
A discount calculator that can apply different discount strategies to products. The system will determine the best price for a customer based on multiple discount rules.

## player_interface.py -> A Player Interface
A simple game system in which a character moves randomly on a grid, keeps track of where it has been, and gains additional movement options as it levels up.

## polygon_calculator.py -> A Polygon Area Calculator
This mini program defines Rectangle and Square classes to model basic geometric shapes. It calculates area, perimeter, and diagonal length; it can draw the shape using stars. This program also demonstrates how many times one shape can fit inside another without rotation.

## linked_list_implementation.py -> A LinkedList Implementation 
This singly linked list implementation allows adding elements to the end of the list, removing a specific element, checking whether the list is empty, and tracking the number of elements using a length variable.

## hash_table.py -> A Hash Table Implementation from Scratch 
A hash table implementation from scratch. A hash table is a data structure that stores the key as an input and then hashes this key according to a specific hashing function. The hashing function used is summing the Unicode values of each character in the key. The hash value will then be used as the actual key to store the associated value; the same hash value would also be used to retrieve and delete the value associated with the key.

## binary_search.py -> A Binary Search Implementation from Scratch
A simple implementation of binary search from scratch.

## bisection_method.py -> A Bisection Method
The bisection method, also known as the binary search method, uses a binary search to find the roots of a real-valued function. It works by narrowing down an interval where the square root lies until it converges to a value within a specified tolerance.

## merge_sort.py -> An Implementation of Merge Sort 
Merge sort is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data. That is, it "divides" a collection into smaller sub-parts, and "conquers" the sub-parts by sorting them independently, then merges the sorted sub-parts.

## quick_sort.py -> An Implementation of Quick Sort
A simple implementation of the Quick Sort Algorithm 

## selection_sort.py -> An Implementation of Selection Sort
A simple implementation of the Selection Sort Algorithm 

## luhn_algorithm.py -> An Implementation of the Luhn Algorithm 
The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, like credit card numbers. This is a simple implementation of a credit card validator using the Luhn algorithm.

## tower_of_hanoi.py -> Tower of Hanoi Algorithm
This implementation is the solution to the mathematical puzzle known as the Tower of Hanoi.

## shortest_path.py -> Shortest Path Algorithm 
An implementation of the shortest path algorithm by writing a function that computes the shortest path between the nodes in a graph, and also returns the path taken.

## adjList2adjMat_converter.py -> An Adjacency List to Matrix Converter
A function that converts an adjacency list representation of a graph into an adjacency matrix.

## bfs.py -> Bredth-First Search Algorithm 
A function that generates all valid combinations of parentheses using a breadth-first search (BFS) approach.

## dfs.py -> Depth-First Search Algorithm 
A function that implements the depth-first search algorithm to output a list of all nodes reachable from the node passed to it.

## nQueens.py -> The N-Queens Algorithm
An implementation for the N-Queens problem that asks to place N queens on an N×N chessboard so that no two queens attack each other (no two share a row, column, or diagonal). This problem is solved using the DFS approach

## fibonacci.py -> Fibonacci Number Calculator
An Nth Fibonacci Number Calculator
