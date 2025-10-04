import string

def first_char(n):
    return (5+n-1)//5

def second_char(n):
    return ((n-1)%5)+1

def get_letter_number (letter) :
    if(letter.capitalize() == "J"):
        letter_number=9
    else:

        for i in range(len(alphabet)) :
            
            
            if(alphabet[i]==letter.capitalize()):
                
                letter_number=i+1
                break
                
    return letter_number

def polybe(letters):
    result = ""
    for letter in letters :
        if letter == " ":
            result = result +" " 
        else :
            n = get_letter_number(letter)
            result = result + str(first_char(n))+str(second_char(n))
    
    return result


# =================================================================================

alphabet = string.ascii_uppercase

alphabet = alphabet.split("J")[0]+alphabet.split("J")[1]
print(alphabet)


letters = input("Entrez une chaîne de caractères : ")



print("Texte chiffré : "+polybe(letters))