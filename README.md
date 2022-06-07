# **Description**
A simple python to get the queue times of the 2 terminals of Dublin Airport. It save the times in 2 seperate csv files in a directory named "data".


# Dependencies
1. bs4
1. requests
1. pandas
1. matplotlib

# Create the environment using conda
```
conda env create -f environment.yml
```

# Activate the conda environment
```
conda activate tqueues
```

# Run the script
By default the main script scrapes the data and appends them to the `.csv` files. However, two optional flags may be passed to no scrape the data and/or plot the data. To run it simply run:
```
python main.py [-p, --plot] [-n, --no-scrape]
```

# Plot the data
To plot the data without scrape run:
```
python plot.py
```
or
```
python main.py -np
```

# Linux only
You can make both scripts excutable by running the command in the root directory:
```
chmod +x main.py plot.py
```
After that you can run them like a normal excecutable file:
```
./<script-name>.py [options]
```
