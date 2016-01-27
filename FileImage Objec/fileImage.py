Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cImage;
>>> from cImage import *;
>>> myWin=ImageWin("Viet",300,400);
>>> myFile=FileImage('');
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myFile=FileImage('');
  File "C:\Python34\lib\cImage.py", line 398, in __init__
    super(FileImage, self).__init__(fname = thefile)
  File "C:\Python34\lib\cImage.py", line 258, in __init__
    self.width = self.im.width()
AttributeError: 'FileImage' object has no attribute 'im'
>>> myFile=FileImage
