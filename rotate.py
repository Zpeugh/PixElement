'''
    Author: Zach Peugh
    Date: 11/2/2016
    Description:  This is a script that takes an object file
                  and given an input of number of degrees,
                  outputs a new object file rotated along
                  the center axis that number of degrees
'''

import argparse
import numpy as np
import math
import re

VERTEX_MARKER = 'v'
OBJ_EXT = ".obj"


'''
    Given a line of three numbers seperated by spaces, return a
    numpy array of three floats
'''
def read_three_floats(line):
    line = line.strip()
    return np.array([float(x) for x in line.split()[1:4]])

'''
    Given a file name, load in the .obj file returning
    <numpy array of vertices>, <all other lines in the file>
'''
def load_object(file_name):

    vertices = np.array([])
    other_lines = []
    with open(file_name) as f:
        for line in f:
            if line[0] == VERTEX_MARKER and line[1] == ' ':
                if len(vertices) == 0:
                    vertices = read_three_floats(line)
                    print(vertices)
                else:
                    vertices = np.vstack((vertices, read_three_floats(line)))
            else:
                other_lines.append(line)
    return vertices, other_lines


'''
    Returns a rotation matrix as a numpy array with shape (3,3)

    axis    an arraylike object with length 3, indicating the axis
            of rotation
    deg     the number of degrees to rotate the object counterclockwise
'''
def rotation_matrix(axis, deg):
    rad = math.radians(deg)
    axis = np.array(axis)
    axis_dot = np.dot(axis, axis)
    if axis_dot == 0:
        raise Exception("Invalid axis of rotation {0}".format(axis))
    axis = axis/math.sqrt(axis_dot)
    a = math.cos(rad/2.0)
    b, c, d = -axis*math.sin(rad/2.0)
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c+a*d), 2*(b*d-a*c)],
                     [2*(b*c-a*d), a*a+c*c-b*b-d*d, 2*(c*d+a*b)],
                     [2*(b*d+a*c), 2*(c*d-a*b), a*a+d*d-b*b-c*c]])


'''
    Given a 3D vertex point, write out the appropriate line for .obj files
'''
def create_vertex_line(vertex):
    return "{0} {1} {2} {3}\n".format(VERTEX_MARKER, vertex[0], vertex[1], vertex[2])


'''
    Write an array of vertices and the accompanying other lines to the
    specified file name in a .obj format
'''
def write_object(file_name, vertices, other_lines):

    if (OBJ_EXT not in file_name):
        file_name = file_name + OBJ_EXT

    f = open(file_name, 'w')

    for line in other_lines:
        f.write(line)

    f.write("\n")

    for vertex in vertices:
        f.write(create_vertex_line(vertex))

    f.close()


'''
    Returns the 3D axis of the mean vertex coordinates
'''
def mean_axis(vertices):
    return np.mean(vertices, axis=0)


'''
    Returns the volumetric center coordinates of the box containing the object
'''
def center_volume_axis(vertices):
    x_max, y_max, z_max = np.max(vertices, axis=0)
    x_min, y_min, z_min = np.min(vertices, axis=0)
    return np.array([(x_max+x_min) / 2.0, (y_max+y_min) / 2.0, (z_max+z_min) / 2.0])

'''
    Takes a string like '[1, 2.0, -1.1]' and returns an array of floats
'''
def parse_string_as_array(string):
    return map(float, re.findall(r"[-+]?\d*\.\d+|\d+", string))


'''
    Return correct axis based on input parameters
'''
def get_axis(args, vertices):
    if args.mean_ax:
        axis = mean_axis(vertices)
    elif args.volume_ax:
        axis = center_volume_axis(vertices)
    elif args.ax is not None:
        axis = parse_string_as_array(args.ax)
    else:
        axis = args.ax

    return axis

'''
    Set up the commandline arguments for running the script.  Return a Namepace object
    containing all of the arguments properly formatted
'''
def get_arguments():
    parser = argparse.ArgumentParser(prog='rotate', description='Rotate a .obj file object about an axis and write the output to disk')

    # positional, mandatory arguments
    parser.add_argument('input_file', help="The input .obj file name")
    parser.add_argument('output_file', help="The output file name")

    # optional arguments with input
    parser.add_argument('-deg', type=float, default=90.0, help="The number of degrees to rotate the object counterclockwise by")
    parser.add_argument('-ax', type=str, help="3D array of axis to rotate by.  i.e. [0,0,1]")

    # boolean arguments
    parser.add_argument('--mean_ax', default=False, action="store_true", help="Boolean flag to rotate around the mean of the vertice coordinates")
    parser.add_argument('--volume_ax', default=False, action="store_true", help="Boolean flag to rotate around the volumetric center of the box containing the object")
    args = parser.parse_args()

    return args


################################### Begin Script ###################################

args = get_arguments()
vertices, other_lines = load_object(args.input_file)
axis = get_axis(args, vertices)
rot_mat = rotation_matrix(axis, args.deg)
vertices = np.dot(vertices, rot_mat)

write_object(args.output_file, vertices, other_lines)
