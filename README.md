<div align="center">
<h1>Python Art 🎨</h1>
</div>
This is a command line application that allows you to turn a image into characters art. See the demo below.

# Result
![demo](https://github.com/hongmei-codes/python_art/blob/master/demo/demo.jpg)

Image is turned into characters that is based on pixle density of the original image.

# How this works
The programme goes through a few steps to convert an image into a character representation.

1. Resize picture while maintaining aspect ratio
2. Change image color scheme to greyscale
3. Convert each greyscale pixle to a character


# Techonology Used
## Python Image Library (PIL)
Read documentation [here](https://pillow.readthedocs.io/en/stable/).

You can install PIL using pip by running the following command.
```console
python -m pip install --upgrade Pillow
```
### Resizing image
To resize image, the method [.resize()](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.resize) can be used. This method takes one required parameter: size in pixles. The size parameter has to be a tuple of (width, height). The method then returns a copy of the resized 'Image' object. This function is used to resize the user specified image in the following way.

```python
resize_image = original_image.resize((new_width, new_height))
```

### Greyscale
To change image color to greyscale, the [.covert()](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.convert) method can be used. This method is capable of many forms of color conversions. However, for the purpose of this project, it is used just for greyscale conversion which requires a parameter of `"L"`.

```python
greyed_image = original_image.convert('L')
```

### Pixle conversion
The pixle value of each pixle is needed for pixle conversion. Pixle value will indicate pixle intensity which ranges from 0 to 255. 0 is black and 255 is white. Since 11 characters are used, the value range has to be reduced. This is done by dividing the pixle value by 25 such that the maximum value in the range is 11 which points to the last element of the character list (**`"."`** the least dense character).

[.getdate()](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.getdata) method returns the pixle values of an image. The characters are then obtained in the following way.

```python
CHARACTERS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

pixle_values = image.getdata()
characters = ''
for pv in pixle_values:
    character = CHARACTERS[pv // 25]
    characters += character

```

# Try it your self
1. Download the scripts [here](https://github.com/hongmei-codes/python_art/archive/master.zip)
2. Install all the requirements by running the following command line
```console
$ pip install -r requirements.txt
```
3. Run the script by executing:
```console
$ python art.py
```
4. The result is saved in  `python_art.txt`.
