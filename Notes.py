#Python Terminal Notes

# for outputing only text files
import glob
# for centering output
import shutil
columns = shutil.get_terminal_size().columns

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
	
	#Asking if a user wants to see his note?
	ask = input("\n Wanna see your note? (y/n): ")
	if ask == "y":
		print("\n Here is Your Note: \n")
	elif ask == "n":
		return
	#Reading a note
	print("\n" + f_name.upper().center(columns) + "\n")
	file = open(f_name + '.txt', "r")
	print(file.read())

def Read_Notes():
	#to check if there's no .txt files
	if [] == glob.glob("*.txt"):
		print("Sorry, there are no notes to read, we suggest you to take a note first")
		return
	else:
	#to get the file name to output
		print("\n Please, choose which notes you want to read: \n")
		i = 1
		for note in glob.glob("*.txt"):
			print(str(i) + " - " + note.split('.txt')[0])
			i += 1

		#to get an index of a desired note
		while True:
			try:
				num = int(input("\n Type the number of the note: "))
				print("\n"+ glob.glob("*.txt")[num-1].split('.txt')[0].upper().center(columns) + "\n")
				break
			except ValueError:
				print("\n Please input integer only...")
				continue
				
	#grabbing the file name to read it
	f_name = glob.glob("*.txt")[num-1]		
	file = open(f_name, "r")
	print(file.read())

def Choose_Action():
	print("\n" + "TERMINAL NOTES".center(columns) + "\n")

	while(True):
		mode = input("\n Choose between Write mode and Read mode (W/R): ")
		if mode.lower() == "w":
			Write_Notes()
		if mode.lower() == "r":
			Read_Notes()

		ask = input("\n Wanna Continue? (y/n): ")
		if ask.lower() == "y":
			continue
		elif ask.lower() == "n":
			exit()


if __name__ == '__main__':
      
    # main method for executing
    # the functions
    Choose_Action()

