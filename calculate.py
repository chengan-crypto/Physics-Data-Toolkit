import numpy as np

def read_data(filename, delimiter=','):
  data = np.genfromtxt(filename, dtype='float', delimiter=delimiter, skip_header=0)
  return data

def linspace(start, stop, num_points):
    return np.linspace(start, stop, num_points)

def save_data(filename, data, delimiter=',', decimal_places=4):
  fmt_string = f'%.{decimal_places}e'
  np.savetxt(filename, data, delimiter=delimiter, fmt=fmt_string)

