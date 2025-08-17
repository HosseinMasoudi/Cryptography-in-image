from PIL import Image

NUM = int(input("Enter the step size for pixel modification (e.g., 10): "))
TEXT = input("Enter the text to encode into the image: ")

def text_to_ASCII(text):
    """
    Convert text to ASCII values
    """
    ascii_values = [ord(char) for char in text]
    
    return ascii_values

ASCII_values = text_to_ASCII(TEXT)

Encrypted_img = Image.new("RGB", (300,300), (0,0,0))
width , hight = Encrypted_img.size

k = 0
for i in range(0 , width, NUM):
    for j in range(0 , hight, NUM):
        if k < len(ASCII_values):
            pixel = Encrypted_img.getpixel((i,j))
            new_pixel = (ASCII_values[k],pixel[1],pixel[2])
            
            Encrypted_img.putpixel((i,j), new_pixel)

            print(f"Pixel ({i},{j}) updated → {new_pixel} \b new value: {Encrypted_img.getpixel((i,j))}")
            k += 1
            
Encrypted_img.show()
Encrypted_img.save("encrypted_image.png")
print("Image saved as 'encrypted_image.png'.") 