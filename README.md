# EyeStrain

## Description
Detects the amount of Digital Eye Strain for a person by checking the blink rate and the amount of time the person closes the eye

## Points to remember while executing
1. Remember to download these libraries (the pip install command is given with the library name
   - **imutils** - pip install imutils
   - **scipy** = pip install scipy
   - **cv2** = pip install opencv-python
   - **dlib** - 
     ### Windows installation is given below
     - First you have to install cmake. Refer https://cmake.org/download/ to download cmake. Make sure to add it to path variable for no further errors
     - Next, you have to download the C++ build tools. Download the visual studio through https://visualstudio.microsoft.com/visual-cpp-build-tools/ and make sure to download the C++ build tools, specifically the "C++ cmake tools for windows"
     - Next, we can install cmake with "pip install cmake" and then finally install dlib with "pip install dlib"
     ### For MacOS and Ubuntu installation
     - Refer the following link for installing dlib in MacOS or Ubuntu https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
2. Remember to have the 'shape_predictor_68_face_landmarks.dat' file in the same directory as the python file

## Execution of code
The code can be executed by typing 'python eye_strain_detection.py' in command line while being in the same directory as the code. An alternative would be to execute it through any other IDE
