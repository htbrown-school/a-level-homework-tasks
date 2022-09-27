proverb = "A picture's worth a thousand words."
print(proverb)

proverb_image = proverb.replace("A picture's", "An image is")
print(proverb_image)

first_o = proverb.find("o")
print(f"The first \"o\" is at position {first_o}.")

proverb_upper = proverb.upper()
print(proverb_upper)

proverb_count = len(proverb)
print(f"There are {proverb_count} characters.")