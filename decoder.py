from PIL import Image

NUM = int(input("Enter the step size for pixel modification (e.g., 10): "))
path = input("Enter the path to decode into the text: ")

Encrypted_img = Image.open(path)

width , hight = Encrypted_img.size
list_numbers = []

for i in range(0 , width, NUM):
    for j in range(0 , hight, NUM):
            pixel = Encrypted_img.getpixel((i,j))
            if pixel[0] != 0:  # Assuming non-black pixels contain encoded ASCII values
                list_numbers.append(pixel[0])
                print(f"list_numbers.append({pixel[0]}) at pixel ({i},{j})")
            else:
                break

def ASCII_to_text(list_numbers):
    """
    Convert ASCII values to text 
    """
    text = [chr(num) for num in list_numbers]
    
    return text

text = ASCII_to_text(list_numbers)

print("the decoded text is: ", ''.join(text)) 