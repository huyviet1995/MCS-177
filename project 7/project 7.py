from cImage import*
myImage=FileImage('touhou_Image.gif');

#Pixel -> Pixel
def brownishColor(originalPixel):
     '''take a pixel as input, return the corresponding pixel in sepia tone'''
     R=originalPixel.getRed();
     G=originalPixel.getGreen();
     B=originalPixel.getBlue();
     newR=min([int(R*0.393+G*0.769+B*0.189),255]);
     newG=min([int(R*0.349+G*0.686+B*0.168),255]);
     newB=min([int(R*0.272+G*0.534+B*0.131),255]);
     newPixel=Pixel(newR,newG,newB);
     return newPixel

#int->int
def check(value):
     '''take a value of one of three RGB as input, set that value to 0 or 255 if that value is greater than 255 or smaller than 0'''
     if value<0:
          value=0;
     elif value>255:
          value=255;
     return value;
     
#pixel,int->pixel
def gammaCorrection(originalPixel,gamma):
     '''take a pixel as input, return its associated YUV pixel'''
     R=originalPixel.getRed();
     G=originalPixel.getGreen();
     B=originalPixel.getBlue();
     Y =0.00117 * R + 0.00230 * G + 0.000447 * B
     U =-0.000577 * R - 0.00113 * G + 0.00171 * B
     V =0.00241 * R - 0.00202 * G - 0.00039 * B
     Y=Y**gamma;
     R = int(255 * (Y + 1.13983 * V));
     G = int(255 * (Y - 0.39465 * U - 0.58060 * V));
     B = int(255 * (Y + 2.03211 * U));
     newPixel=Pixel(check(R),check(G),check(B));
     return newPixel;

#pixel->function
def gammaTwo(originalPixel):
     '''take a pixel as input, return its YUV pixel with gamma's value of 2'''
     return gammaCorrection(originalPixel,2);

#pixel->function
def gammaHalf(originalPixel):
     '''take a pixel as input, return its YUV pixel with gamma's value of 0.5'''
     return gammaCorrection(originalPixel,0.5);

#image,function -> image
     '''take an image and a procedure as input, return the associated image after being processed by the given procedure'''
def transformPixels(image,procedure):
     myImage=image;
##     myWin=ImageWin('test',myImage.getWidth(),myImage.getHeight());
     ei=EmptyImage(image.getWidth(),image.getHeight());
     for i in range(myImage.getWidth()):
          for j in range(myImage.getHeight()):
               originalPixel=myImage.getPixel(i,j);
               newPixel=procedure(originalPixel);
               ei.setPixel(i,j,newPixel);
##     myImage.draw(myWin);
     return ei

#image->image
def rotateImage90(image):
     '''rotate an image 90 degree clockwise'''
     myImage=image;
     ei=EmptyImage(myImage.getHeight(),myImage.getWidth());
     for i in range(myImage.getWidth()):
          for j in range(myImage.getHeight()):
               originalPixel=myImage.getPixel(i,j);
               ei.setPixel(myImage.getHeight()-j,i,originalPixel);
     return ei;
     
     
#string,list->void
def drawImages(title,listOfImages):
     '''take a title and a list of images, return a canvas with all the images in the list locating next to each other'''
     totalWidth=0;
     totalHeight=0;
     maxHeight=0;
     for image in listOfImages:
          totalWidth=totalWidth+image.getWidth()+1;
          if (image.getHeight()>maxHeight):
               maxHeight=image.getHeight();
          
     myWin=ImageWin(title,totalWidth,maxHeight);
     totalWidth=0;
     for i in range (len(listOfImages)):
          listOfImages[i].setPosition(totalWidth,0);
          listOfImages[i].draw(myWin);
          totalWidth=totalWidth+listOfImages[i].getWidth()+1;
     myWin.exitOnClick();
     
drawImages('touhou_image', [transformPixels(myImage, gammaHalf), transformPixels(rotateImage90(myImage), gammaTwo)])
     
          
     
     
          
     
               
     
               
     
     
     
     
          
     
     
     
     
               
               
     
     
