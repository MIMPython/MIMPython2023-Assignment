import os

children_objects = os.listdir() # Specify a path if necessary.
for object in children_objects:
    if os.path.isdir(object):
        print(f"- Object {object}, type folder")
    else:
        print(f"- Object {object}, type file")