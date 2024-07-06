@echo off
REM Create the first directory
mkdir test
REM Change directory to the newly created directory
cd test
REM Create the second directory inside the first one
mkdir test2
REM Change directory to the second directory
cd test2
REM Create a new file hello.txt and write "Hello World" into it
echo Hello World > hello.txt
REM Go back to the original directory
cd ../..
REM Display a completion message
echo Folder and file have been created successfully.
