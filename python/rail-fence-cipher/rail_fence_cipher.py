def matrix_creation(message, rails):                    #this function is to create the matrix that is going to make the encoding for us
    size = len(message)                                 #but also, we are going to use it to decode
    encoding = [[""]*size for _ in range(rails)]
    i = -1                                      #these are for the indixes of the matrix and starting at -1
    j = -1                                      #because we want to add 1 to every interaction, so it will actually start at 0
    while True:
        if i <= 0:                              #in case we reach the first line we should start adding one to the lines (and the condition of < 0 is becuase of the first interaction)
            while True:
                if j == size - 1:               #if the number of the column == lenght of the code it means that we already finished
                    break
                j += 1
                i += 1
                encoding[i][j] = message[j]     #add the number in the desired position
                if i == rails - 1:              #if we reach the last line of the matrix
                    break
        if i == rails - 1:                      #we should enter here and start decreasing 1 to the lines
            while True:
                if j == size - 1:               #again, the encoding is done if number of column == lenght of the code
                    break
                j += 1
                i -= 1
                encoding[i][j] = message[j]
                if i == 0:                      #in case we reach the line 0
                    break
        if j == size - 1:
            break
    return encoding                             #give us the matrix

def encode(message, rails):                     #for enconding is pretty straight forward
    encoding = matrix_creation(message, rails)  #just take the matrix and join the letters
    return "".join(["".join(lists) for lists in encoding])



def decode(encoded_message, rails):             #but for the decoding it's a little bit more complicated
    number_of_letters = [i for i in range(len(encoded_message))]    #here I'm taking how many letters there are in the message
    matrix_comparison = matrix_creation(number_of_letters, rails)   #and creating a matrix with the position of each letter to compare it later
    lenght = len(matrix_comparison)
    location = []
    decoded_message = ""
    for i in range(lenght):
        if "" in matrix_comparison[i]:
            count_of_empty = matrix_comparison[i].count("")
            for j in range(count_of_empty):
                matrix_comparison[i].remove("")             #having the matrix, we should remove the empty values
        location += matrix_comparison[i]                    #and join everything in one list to have where each letter ended up in which position of the string
    for k in range(len(encoded_message)):
        decoded_message += encoded_message[location.index(k)]   #now search for them and put them together
    return decoded_message
