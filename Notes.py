#Python Terminal Notes

def Write_Notes():
	
	#Naming a note
	f_name = input("\n Name your note: ")
	file = open(f_name + '.txt', 'w')
	#Specifying a title
	title = input("\n Specify the title: ")
	file.write(title)
	#Writing the actual note
	print("\n Write your note: \n")
	lines = ['\n']
	while True:
	    line = input("  ")
	    if line:
	        lines.append(line)
	    else:
	        break
	note = '\n'.join(lines)
	file.write(note)
	#Closing the file
	file.close()
	


	#Wanna see your note?
	ask = input("\n Wanna see your note? (y/n): ")
	if ask == "y":
		print("\n Here is Your Note: \n")
	elif ask == "n":
		exit()

	file = open(f_name + '.txt', "r")
	print(file.read())
	

if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Write_Notes()

