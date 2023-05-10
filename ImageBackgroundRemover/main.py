from rembg import remove

input_path = "cr7.jpg"
output_path = "output.png" #should be png

with open(input_path, 'rb') as i: #rb --> read as a byte
    with open(output_path, 'wb') as a: #wb --> write as a byte
        input_file = i.read() #read from input_path
        output_file = remove(input_file) #remove background
        a.write(output_file) #write into output_file
