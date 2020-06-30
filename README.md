
# Video_animations_using_python

#This repo consists of codes , to create video animations using "MANIM" 
A library developed by CREATOR OF 3BLUE 1BROWN YOUTUBE CHANNEL.\\
This library doesn't have enough documentation . If you wanted to learn it as I used to, visit "THEOREM OF BEETHOVEN"  youtube channel for some brief tutorials.



Make sure you take out the images out of images folder.

IF you are here for the code for mid-evaluation report video : 
The corresponding source code is "MIDTERM_EVAL_IDP2020.py"

The video result after compiling "final.py" is :
```
```


This code is used to generate the YouTube video in this link. In order to compile this code you have to install manim. Move this code to the root directory of manim and execute the below provided command to compile the code and preview the video in Low resolution
```sh
$ python – m manim FILENAME.py -pl  
```
To preview the file in high resolution, exectute the below given command:
```sh
$ python – m manim FILENAME.py -p  
```
This is a brief explanation on the manim commands used in the python script provided:
  - TextMobject -> Used for introducing text in the video. 
  - TexMobject -> Used to insert Formulae in the video.
  - ImageMobject -> Used to insert Images in the video.
  - .add-> Used to add the objects created in the video.
  - .Play-> Used to play the animations created.
  - Write-> A style of playing the animation. Creates the borders first and then fills in the remaining parts.
  - FadeIn-> Another way of playing the animation. Name explains the way it animates.
  - .remove-> Used to remove the objects created from the screen.
  - FadeOut->Used to remove the objects as an animation.
  - .edge_to->Places the object near an edge.
  -	.next_to->Places the object adjacent to another object.
  -	.shift()->Shifts the object from its previous position by specified distance.
  -	Vgroup()->To group multiple object inorder to arrange them.
  -	Group()->Similar function as Vgroup(), but is compatible with ImageMobject.
  -	Transform->Used to Transfom one object into another object.
  -	ReplacementTransform->Similar function as transform, but different in its implementation.
  -	Arrow()->Used to create an arrow between the specified position co-ordinates.
  -	Brace()->Used to create Braces over the specified object.
  -	SurroundingRectangle()-> Used to create a framebox over the specified object.
  -	MovinCameraScene()->Passed as an argument to render scenes with mobile camera focus.
  -	.camera_frame.save_state()->Save the current state of camera.
  -	.camera_frame.set_width,Object.get_width()->Set the size with the width of a object.
  -	Restore(self.camera_frame)->Restore the saved state of camera.
