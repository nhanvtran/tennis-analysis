import re

def main():
    ### to make the raw rankings file, copy the rankings into a text file in batches of 100
    preprocess_rankings("data/rankings_raw_240906.dat","data/rankings_240906.dat")
    list_of_rankings = get_rankings("data/rankings_240906.dat")
    # print(list_of_rankings)

    ### get list of entrants, just copy the list from USTA webiste
    list_of_entrants = preprocess_tournament("data/tourn_raw_242109.dat")
    # print(list_of_entrants)

    list_of_entrants_with_points = []
    for entrant in list_of_entrants:
        first_name = entrant[0]
        last_name = entrant[1]

        entrant_found = False
        for ranking in list_of_rankings:
            if ranking[0] == first_name.lower() and ranking[1] == last_name.lower():
                entrant.append(int(ranking[2]))
                list_of_entrants_with_points.append(entrant)
                entrant_found = True
        if entrant_found == False:
            entrant.append(-1)
            list_of_entrants_with_points.append(entrant)
            print("Did not find", first_name, last_name, "in my rankings list...")

    # print(list_of_entrants_with_points)
    list_of_entrants_with_points.sort(key=lambda x: x[2], reverse=True)
    # print(list_of_entrants_with_points)
    counter = 1
    for entrant in list_of_entrants_with_points:
        # print(entrant)
        list_as_string = ' '.join(map(str, entrant))
        print(counter, list_as_string)
        counter += 1
        # print("Counter:", counter)

""" 
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
helper functions below
------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------
"""

def preprocess_rankings(rawfile, outfile):
    column_ctr = 0
    with open(rawfile, "r") as infile, open(outfile, "w") as outfile:
        # Loop through each line in the file
        for line in infile:
            # Check if the line is not blank
            if line.strip():
                # Write the line to the new file if it is not blank
                # Remove the new line from the string
                line = line.rstrip('\n')
                line += " "
                outfile.write(line)
                column_ctr += 1
                if column_ctr > 8:
                    outfile.write("\n")
                    column_ctr = 0

def get_rankings(rankingsfile):
    list_of_rankings = []   
    with open(rankingsfile, "r") as file:
        # Loop through each line in the file
        for line in file:
            if line.strip():
                line = line.rstrip('\n')    
                linelist = line.split()
                # print(line)
                list_of_rankings.append([linelist[3].lower(),linelist[4].lower(),linelist[5]]) 
    return list_of_rankings

def preprocess_tournament(rawfile):
    list_of_entrants = []
    # Open the file "tourn.dat" in read mode
    with open(rawfile, "r") as file:
        # Loop through each line in the file
        for line in file:
            # Check if the line has more than 5 characters
            if len(line) > 5:
                # Split the line by space or comma
                # columns = re.split(r'[ ,]', line)
                # # Print each column
                # for column in columns:
                #     print(column)
                last_name = line.split()[0][:-1]
                first_name = line.split()[1]
                last_name = last_name.lower()
                first_name = first_name.lower()
                # print(first_name, last_name)
                list_of_entrants.append([first_name,last_name])   
            # print(line, end='')
    
    #return a list of kids names
    return list_of_entrants

# Run the main function when the script is executed
if __name__ == "__main__":
    main()