# 34. Create a function that returns an array with words inside a text. 
def array_words_inside_text(text:str):
    result = text.split(" ")
    return result
print(array_words_inside_text("hola mundo"))