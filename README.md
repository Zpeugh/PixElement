#PixElement Code Challenge#

###Project specifics:
1. If you're using any 3rd-party libraries, please include instructions for including/running them.
2. When run, the software should open an .obj file. I will be using this one to test your code. (Picture)
3. The code should, by default, rotate all the vertices of the 3D model 90 degrees along some axis that intersects the model.
4. The program should then save a new, valid .obj file to disk with the rotated model.

###Bonus points (entirely optional; pick-and-choose):
| Bonus Task Description                                                                                                                                       |  Status  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Use Python                                                                                                                                                   | Done     |
| Use git, and commit frequently.                                                                                                                              | Done     |
| Let me know how much time the project took. (No need to rush it.)                                                                                            | 4.5 hrs |
| Use CloudCompare, Blender, or another tool to take a screenshot of the input and output.                                                                     | Blender  |
| Rotate around either the mean of the vertex coordinates, or around the center of the object's volume (the box containing the points) based on a boolean flag | Done     |
| Let the user specify what input file to use via command-line argument.                                                                                       | Done     |
| Let the user specify how many degrees of rotation to apply (also via argument).                                                                              | Done     |
| Let the user specify which center (mass or volume) to rotate around.                                                                                         |          |
| Let the user specify the axis of rotation as a vector.                                                                                                       | Done     |
| Write automated tests for your code (or, even better, test-drive your code)                                                                                  |          |
| Don't use any (explicit) loops. (a.k.a. map/reduce paradigm)                                                                                                 |          |

###Dependencies
numpy (`pip install numpy`)

###Running the program
By default, objects are rotated around the mean of the vertices, and at 90 degrees counter clockwise.
The simplest way to run the program is from the terminal, when in this directory, using the command
<br />
`python rotate.py <input file> <output file>`
<br />
<br />
To get a list of all of the optional flags and arguments, type
<br />
`python rotate.py -h`
<br />

####Results
To see sample results, check the directory 'blender_screenshots' of blender before and after snips


