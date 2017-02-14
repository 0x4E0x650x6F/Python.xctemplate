___PROJECTNAME___  Module Repository.
=====================================

___PROJECTNAME___ Python project.

To make the project run on Xcode:

Product -> scheme -> edit scheme -> run -> info.
	* Set the Executable to Python:
	* Select "Other" on the Combo Box  press, Command-Shift-G and set the path to Python ()
	* Disable
		- Debug executable. 
	* enable
		Lauch automatically 
		
Product -> scheme -> edit scheme -> run -> Arguments.
	- On arguments Passed On launch press "+" to add new one and add:
	-m unittest discover -s $(SOURCE_ROOT)/$(PROJECT_NAME) 
	
NOTE:
The -s is should point to project root (at README level folder).
