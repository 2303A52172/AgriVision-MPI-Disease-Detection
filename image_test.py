from mpi4py import MPI
import numpy as np
import cv2
import os
import socket

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print("Process", rank, "running on", socket.gethostname())

if rank == 0:
    print("Master loading image...")

    # Automatically get project root folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    image_path = os.path.join(project_root, "data", "crop.jpg")

    print("Looking for image at:", image_path)

    image = cv2.imread(image_path)

    if image is None:
        print("Image not found!")
        exit()

    split_image = np.array_split(image, size, axis=0)
else:
    split_image = None

local_image = comm.scatter(split_image, root=0)

print(f"Process {rank} received part with shape {local_image.shape}")

local_gray = cv2.cvtColor(local_image, cv2.COLOR_BGR2GRAY)

gathered = comm.gather(local_gray, root=0)

if rank == 0:
    final_image = np.vstack(gathered)
    output_path = os.path.join(project_root, "data", "output_gray.jpg")
    cv2.imwrite(output_path, final_image)
    print("Parallel grayscale image saved!")
