# progress_bar.py
This program helps with using progress bars in python 3.



to import this modual, while in the same directory as it execute:
"from progress_bar import bar"
in python 3.

Then run:
"bar.progress_bar(percent, end, use_display=False, display='new', exact=False)"
in python 3.


Percent: This is the percent you are showing
end: Return True or False based on if this is the last itteration of using the progress bar (note: This is only necessessary to define if you are not using a display)
use_display: Return True or False based on weather you are going to use a display (note: if pygame modual is not installed the program will install it automatically) (note: if you do not use a display the progress bar will be shown in the terminal)
display='new': This defines if you are using a new window for the progress bar or an existing one. (note: leave as 'new' to make new display, or put in the display you are using without perenthisees)
exact=False: Return True or False based on weather you want to show decimals of the percentage (note: this will only have affect if you are using a display)
