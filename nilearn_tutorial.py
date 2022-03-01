from nilearn.connectome import ConnectivityMeasure
from nilearn import datasets
from nilearn import plotting

import scipy as sp
import scipy.io as sio
import numpy as np

"""
# download atlas, disk location is /home/dzjin/nilearn_data
dataset_ho = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')

# Nifit1Image:(91*109*91)
atlas_filename = dataset_ho.maps

# plot atlas
plotting.plot_roi(atlas_filename)
plotting.show()
"""


"""
mat = sio.loadmat('/home/dzjin/datasets/ABIDE/mat_800/matrix/0050004_ho_correlation.mat')['connectivity']
coords = np.loadtxt('/home/dzjin/datasets/ABIDE/mat_800/ho_coords.csv', delimiter=',', dtype=float)
coords = np.delete(coords, 82, axis=0)
# plot fc.
plotting.plot_connectome(mat, coords, edge_threshold="98%", colorbar=True)
plotting.show()
"""
