def main():
# get's the text from the book    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#recieves the text and counts the words
        def count_words(file_contents):
            words = file_contents.split()
            count = 0
            for i in words:
                count +=1

            return count
#get's the text, returns how many times a letter appears
        def count_characters(file_contents):
            list_of_words = file_contents
            lowered_string = list_of_words.lower()
            dict_out = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0
                        , 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0
                        ,'m':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0
                        , 's':0, 't':0, 'u':0, 'v':0, 'w':0
                        , 'x':0, 'y':0, 'z':0}
            for i in lowered_string:
                if i in dict_out:
                    dict_out[i] += 1
            return dict_out

    #count_words(file_contents)
    #count_characters(file_contents)

    #I ask myself 'wtf am i doing?' ,but i did it anyway...i am cooked!
        def print_report(count_words, count_characters):
            print("--- Begin report of books/frankenstein.txt ---")
            print(count_words, " words found in the document\n")
            for i in count_characters:
                print(f"The '{i}' character was found {count_characters[i]} times" )


    print_report(count_words(file_contents), count_characters(file_contents))
main()
    