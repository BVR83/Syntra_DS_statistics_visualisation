import matplotlib

def standard_setup():
    matplotlib.rc('figure', figsize=(10, 6))
    matplotlib.rc('font', size = 16)
    matplotlib.rc('axes', edgecolor='black', facecolor='white')  # Set the default color
    matplotlib.rcParams['axes.spines.right'] = False
    matplotlib.rcParams['axes.spines.top'] = False
    matplotlib.rcParams['axes.spines.left'] = True
    matplotlib.rcParams['axes.spines.bottom'] = True
    matplotlib.rcParams['axes.grid'] = False
    return

# Define the color values
hist_color = '#074173'
hist_color2 = '#5DEBD7'
hist_color3 = '#fff400'
hist_edgecolor = '#1679AB'
median_color = '#074173'
mean_color = '#1679AB'

if __name__ == '__main__':
    pass