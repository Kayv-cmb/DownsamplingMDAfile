# DownsamplingMDAfile
DownsamplingMDAfile
## Installation 



```
pip install numpy
pip install pandas
pip install scipy
```

You need to add the file mdaio to the python path

## Running the script
Directory = Path to file you want to downsample

Name = name of the mda file without the number of the tetrode (EXEMPLE = FILE NAME =
 'Rat_Hm_Ephys_Rat2_389237_20200915_postsleep.nt3.mda' -> 'Rat_Hm_Ephys_Rat2_389237_20200915_postsleep.nt'

You can modify the directory, the name of file and the list of number of tetrode according to the file you want to downsampled and run the script.


The output should be a mda file for each tetrode of your recording downsampled to 600Hz and bandpass filter 1-300Hz
