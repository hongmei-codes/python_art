import PIL.Image



CHARACTERS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]



def resize_image(image, new_width=100):
    """
    Resizes image to desired dimensions while maintaining aspect ratio.
    Default width is set to 100.

    :param image: image for processing.
    :param new_width: default image width is 100.
    :returns: resized image with same aspect ratio.
    """
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio)
    resized_image = image.resize((new_width, new_height))

    return resized_image


def grey_image(image):
    """
    Converts image color scheme to greyscale.

    :param image: image for processing.
    :returns: image coverted to greyscale.
    """
    return image.convert("L")


def to_character(image):
    """
    Converts each pixle of the image into a character based on
    the color density of the pixle.

    :param image: image for processing.
    :returns: string of characters in accordance with pixle density.
    """
    pixle_values = image.getdata()
    characters = ''

    for pv in pixle_values:
        character = CHARACTERS[pv//25]
        characters += character
    
    return characters



def main(new_width=100):
    # get image
    path = input("Enter path to image: ")
    # catch get image errors
    try:
        image = PIL.Image.open(path)
    except:
        print(f'{path} is not a valid path.')

    resized = resize_image(image)  # get resized image
    greyed = grey_image(resized)  # get resized and greyscale image
    characters = to_character(greyed) # get a list of characters

    # format characters
    length = len(characters)
    formatted_characters = '\n'.join(characters[i:(i + new_width)] for i in range(0, length, new_width))

    # save result
    with open('python_art.txt', 'w') as f:
        f.write(formatted_characters)


main()