# Cryptography in Image

##Text to Image Encoder/Decoder
This project implements a simple system for hiding text inside images (Steganography).
The main idea is to convert text into ASCII values and store them inside the red channel (R) of image pixels. Later, we can read the values back and recover the original text.
The way the encoder works is that it takes a number (private key) and a text, and in the decoder you have to give it the same number and the path to the image.

##Requirements
You need Python 3 and the Pillow library:
pip install pillow

##project Structure
.
├── encoder.py   # Code for encoding text into image
├── decoder.py   # Code for decoding text from image
└── README.md    # Project description

For example:
If we encode the text "Hello":
ASCII values: [72, 101, 108, 108, 111]
These values are stored in the red channel of selected pixels in the image and is saved in a encrypted_image.png file
When decoding, we get back the original text "Hello"
