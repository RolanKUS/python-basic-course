#
# Example_1
#
text = "'Python Community'"
print(text, end=" -> ")
text = text.replace(" ", "")
text = text.strip("'")
text = "#" + text
print(text)
#
text_1 = "'i like python community!'"
print(text_1, end=" -> ")
text_1 = text_1.title()
text_1 = text_1.replace(" ", "")
text_1 = text_1.strip("'")
text_1 = text_1.rstrip("!")
text_1 = "#" + text_1
print(text_1)
#
text_2 = "'Should, I. subscribe? Yes!'"
print(text_2, end=" -> ")
text_2 = text_2.title()
text_2 = text_2.replace(",", "")
text_2 = text_2.replace(" ", "")
text_2 = text_2.replace("?", "")
text_2 = text_2.replace(".", "")
text_2 = text_2.strip("',!")
text_2 = "#" + text_2
print(text_2)
#
# Example_2
#
text_3 = "'Should, I. subscribe? Yes!'"
print(text_3, end=" -> ")
text_3 = text_3.title()
for char in [","," ","?",".","!","'"]:
    text_3 = text_3.replace(char, "")
text_3 = "#" + text_3
print(text_3)