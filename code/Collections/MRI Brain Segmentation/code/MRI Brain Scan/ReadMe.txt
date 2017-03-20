Release Notes Update: May 8, 2006
---------------------------------
While I am pleased that so many have found this example helpful over the 
past two years, it was recently brought to my attention that some of the
old code in this example was not compatable with Release R2006a of MATLAB 
and the Image Processing Toolbox. This update should resolve both known 
problems.


1. In R2006a when line 49 of analyze_series8.m was executed the following 
error would occur:

??? Previously accessible file "D:\Applications\R2006a\toolbox\images\imuitools\private\reactToImageChangesInFig.m" is now inaccessible.

Error in ==> imtool at 238
    addImageToImtool(varargin{:});

Error in ==> analyze_series8 at 49
imtool(im,[0 max_level])

The problem traced back to some refactoring of IMTOOL. Follow the address
below for more information and a link to download a patch:
<http://www.mathworks.com/support/bugreports/details.html?rp=291909>


2. Line 62 of analyze_series8.m was previously hard coded to open a 
particular HTML page of the MATLAB Help. That line was changed to use the
programmatic DOCSEARCH command to find the Help page containing the 
appropriate keywords. This should be much more robust.


Please do not hesitate to Email if additional problems are detected with 
this example. Thanks!
						- rbemis@mathworks.com


Original Text
-------------
Welcome to Bob's case study on neuroimaging with MATLAB!

I believe this code is clean but if you find any bugs, please let me
know.  Or if you have any interesting comments or suggestions to make
it better, I'd love to hear from you.
						- rbemis@mathworks.com


This package contains a number of files so here is an index:
----------------------------------------------------------------------

 (1) ANALYZE_SERIES8.M (script M-file)

    - This is the main program which uses all the other files.
    - Don't just run this or everything will whiz by and look goofy.
    - My intent was to work through this example code step by step to 
      retrace the actual steps I followed when doing this work: 

	* accessing data 
	* visualizing 2D slices
	* exploring 3D volume using SLICEOMATIC
	* developing algorithm to segment different parts of head
	* computing volume fractions of white & gray matter
	* displaying 3D brain in head with transparent isosurfaces

    - I usually prefer to step through the code in chunks using the 
      debugger.  The STEPTHRU utility makes this easy:

           >> stepthru analyze_series8 base

    - You could also highlight chunks of code in the MATLAB Editor and 
      right-click to evaluate them immediately in the Command Window.

 (2) SERIES 8 (folder)

    - Contains a series of 60 DICOM images (coronal slices).  
    - The whole series constitutes an MRI scan of a patient.  
    - These files were previously anonymized to remove patient 
      information using the DICOMREAD and DICOMWRITE commands from 
      the Image Processing Toolbox.

 (3) UPDATE_SLICEOMATIC.M (function M-file)

    - Helper function used by ANALYZE_SERIES8 script.
    - Refreshes the current sliceomatic figure (gcf) with new data.
    - Requires SLICEOMATIC by Eric Ludlam, available at MATLAB Central.

<http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=764&objectType=file>

 (4) LIMITS.M (function M-file)

    - Helper function used by THRESH_TOOL.
    - Returns min & max values of matrix regardless of dimensionality 
      (size & shape).

 (5) STEPTHRU.M (function M-file)

    - Utility function to help you step through programs one section
      at a time using the debugger.  In this case:

           >> stepthru analyze_series8 base

 (6) THRESH_TOOL.M (function M-file)

    - Interactive thresholding tool with GUI (graphic user interface).
    - Provides both blocking and nonblocking behavior.  See M-file 
      help for more details:

           >> help thresh_tool

    - Requires VLINE by Brandon Kuczenski, available on MATLAB Central.

<http://www.mathworks.com/matlabcentral/fileexchange/loadFile.do?objectId=1039&objectType=file>

 (7) ISINTEGER.M (function M-file)

    - Helper function used by THRESH_TOOL.
    - Utility that returns TRUE if X is a legal integer (INT8, UINT8, 
      INT16, UINT16, INT32, UINT32, INT64, or UINT64).

 (8) MOVE_VLINE.M (function M-file)

    - Helper function implements horizontal movement of line.
    - Callback code used by THRESH_TOOL.

 (9) MOVEX_TEXT.M (function M-file)

    - Helper function implements horizontal movement of text.
    - Callback code used by THRESH_TOOL and MOVE_VLINE.

    
System Requirements:
----------------------------------------------------------------------
    This example was developed and tested using the following 
    MathWorks products:
    
       * MATLAB 6.5.1
       * Image Processing Toolbox 4.1

    In addition, as noted above, this example relies on other user-
    contributed MATLAB code, which is available on MATLAB Central.
    <www.matlabcentral.com>


System Recommendations:
----------------------------------------------------------------------
    The more physical memory you have, the better this example is
    likely to perform.  It was developed using a Windows 2000 PC with 
    a Pentium 4 processor and 512MB physical RAM.
