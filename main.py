def main():
    with open("books/frankenstein.txt") as f:

        #print the report header
        print("--- Begin Report ---")
        
        #turns the contents of the file into a string
        file_contents = f.read()

        #prints the book
        #print(file_contents)

        #counts the words
        word_count = len(file_contents.split())
        print(f"There are {word_count} words in this book")

        #counts the characters
        def count_letter(text):
            text_lowered = text.lower()
            letter_dict = {}
            for i in text_lowered:
                if i.isalpha():
                    if i in letter_dict:
                        letter_dict[i] += 1
                    else:
                        letter_dict[i] = 1
            return letter_dict
          
        letter_count = count_letter(file_contents)

        #sort the letters 
        def sort_by_number(letter):
            return letter[1]
        
        letter_sorted_by_number = sorted(letter_count.items(), key=sort_by_number, reverse=True)

        for letter, count in letter_sorted_by_number:
            print(f"The letter {letter} was found {count} times")

        print("--- End Report ---")
      
 
main()