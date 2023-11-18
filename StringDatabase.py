# This class reads the contain of a text file and stores it into a list

class StringDatabase:
    def WordFile():
        # Opens text file in read mode
        with open("four_letters.txt","r") as four_letters:
            # Reads the number of lines in the file
            lines = four_letters.readlines()
            words = []

            # Loop looks through each line and of the file and stores each element in the list
            for I in lines:
                as_list = I.split(" ") # splits spaces within a line and treats the strings as individual elements
                for J in range(14):
                    words.append(as_list[J].replace("\n","")) # store content in list
            
            # Randomly selects a new word within the entire list of 4018 words
            import random
            word = words[random.randint(0,4018)]

            return word

    if __name__ == "__WordFile__":
        WordFile()
