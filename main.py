text = 'History has known many great liars. Copernicus, Goebbels, St Ralph the Liar but there have been none quite so vile as the Tudor king Henry VII. It was he who rewrote history to portray his precessor Richard III as a deformed maniac who killed his nephews in the Tower. But the real truth is that Richard was a kind and thoughtful man who cherished his young wards. In particular: Richard, Duke of York, who grew into a big, strong boy. Henry also claimed he won the Battle of Bosworth Field and killed Richard III. Again, the truth is very different; for it was Richard, Duke of York, who became king after Bosworth Field, and reigned for thirteen glorious years. As for who really killed Richard III and how the defeated Henry Tudor escaped with his life, all is revealed in this, the first chapter of a history never before told: the history of The Black Adder! This was generated on a Maximus II 11.6” Laptop, Touchscreen, 2-in-1, Windows 10, Intel Bay Trail Z3735F Processor, 2GB RAM, 32GB Storage.'

#Task1/2a: The individual lines of text
def output_70(text):
    # Creates a null character for counting
    str_num = ''
    for i in text:
        str_num += i
        # When the length of the null character is greater than 70, the sentence is printed and then recalculated
        if len(str_num) >= 70:
            print(str_num)
            str_num = ''
    print(str_num)


output_70(text)

#Task 2b: Count of number of words
def word_num(text):
    # Create a new null character text2.
    # The purpose is to remove all punctuation from the sentence and to count the words.
    text2 = ''
    for i in text:
        # Use isalpha () to determine if a character is a letter and add it to text2.
        if i.isalpha():
            text2 += i
        else:
            # If it's not a letter, use a space instead
            text2 += ' '

    all_word = text2.split()  # To get the number of words, split () the space

    print('The number of words: ', len(all_word))


word_num(text)

#Task 2c: Count of number of sentences
def all_sentence_num(text):
    # First, determine whether the "." is a period or a decimal point.
    # If we found there are numbers before and after ".", then this "." is a decimal point instead of a period. Then replace the decimal point with a "*".
    temp = ''
    for i in range(len(text)):
        if text[i] == '.' and text[i - 1].isdigit() and text[i + 1].isdigit():
            temp += '*'
        else:
            temp += text[i]
    text = temp

    text2 = ''
    for i in text:
        if i in ['!', '?']:
            text2 += '.'
        else:
            text2 += i
    text = text2
    # Use split() to split the sentences to get the number of sentences according to the period
    data = text.split('.')
    # When using split() to split a sentence, the last period at the end of the text will also be split so that a null character will be generated,
    # but this null character is not a sentence, so reduce the number of sentences by one
    sentence_num = len(data) - 1
    print('The number of sentences: ', sentence_num)


all_sentence_num(text)






