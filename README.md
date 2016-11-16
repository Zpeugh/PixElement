#PixElement Code Challenge#

###Project specifics:
1. If you're using any 3rd-party libraries, please include instructions for including/running them.
2. When run, the software should open an .obj file. I will be using this one to test your code. (Picture)
3. The code should, by default, rotate all the vertices of the 3D model 90 degrees along some axis that intersects the model.
4. The program should then save a new, valid .obj file to disk with the rotated model.

###Bonus points (entirely optional; pick-and-choose):
| Bonus Task Description                                                                                                                                       | Status |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| Use Python                                                                                                                                                   | Done   |
| Use git, and commit frequently.                                                                                                                              |        |
| Let me know how much time the project took. (No need to rush it.)                                                                                            |3 hours |
| Use CloudCompare, Blender, or another tool to take a screenshot of the input and output.                                                                     |        |
| Rotate around either the mean of the vertex coordinates, or around the center of the object's volume (the box containing the points) based on a boolean flag |        |
| Let the user specify what input file to use via command-line argument.                                                                                       |        |
| Let the user specify how many degrees of rotation to apply (also via argument).                                                                              |        |
| Let the user specify which center (mass or volume) to rotate around.                                                                                         |        |
| Let the user specify the axis of rotation as a vector.                                                                                                       |        |
| Write automated tests for your code (or, even better, test-drive your code)                                                                                  |        |
| Don't use any (explicit) loops. (a.k.a. map/reduce paradigm)                                                                                                 |        |



####Running the program
From a terminal, when in this directory use the command
`python rotate.py -h`
to get a list of all of the options for rotating a .obj file
