# TFT-Swiss

IMPORTANT NOTES FOR THE CURRENT ITERATION OF THE PROGRAM:
-PLAYER COUNT MUST BE A MULTIPLE OF 8
-PLAYERS MUST BE IMPORTED IN A .xlsx FILE
-IT WILL NOT WORK UNLESS YOU CHANGE filename = "INSERT FILE NAME AND LOCATION" (ctrl+F for it)
-ONCE YOU END THE PROGRAM, NO DATA WILL BE SAVED. HIGHLY RECOMMEND YOU KEEP A PAPER (OR NOTEPAD) BACKUP (I'm currently working on a solution)

This program is designed to allow the user to run a TFT (Teamfight Tactics) tournament using a modified version Swiss system. I definitely recommend you to read this Wikipedia on the [Swiss System](https://en.wikipedia.org/wiki/Swiss-system_tournament) to become familiar with the concept of the Swiss system, as well as with some of the terms that I will use.

This program takes a list of names and generates lobbies based on them, at first based on a pre-determined seeding and then on the amount of points that each player has accrued.

This program REQUIRES the user to import the names in a .xlsx file (typical spreadsheet file). Inside that file, names must be listed top to bottom inside of the A column, with the first name being located in A1 and descending from there. The first name (the name in A1) will be the top seed, and the last name will be the final seed. A sample file (tft sample names.xlsx) is provided inside of the project folder as an example. 

The lobbies are generated similar to a snake draft. For example, if there are three lobbies, the third lobby will have both the third and fourth seeded players. This program is designed to be similar to a TFT version of McMahon System (including initial seeds), however, to run a more traditional unseeded Swiss, simply don't order (or randomize) the player list before you download the .xlsx file. 

The amount of points a player earns per round depending on placing is changable, simply adjust the values inside of the pointSpread array, where the first value is the points given to the first place of the lobby, and the final value is given to the last place of the lobby.

If you have any questions, or simply just want to talk about this system with me, feel free to DM me on Discord at Andrew H#6132. 

To-Do List:
-Allow for imperfect amount of players
-Save backup of values to .txt file
-General error catches/Bug Fixes
