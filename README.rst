MTCNN
#####

In this project, MTCNN was run for video using this implementation of MTCNN as baseline: https://github.com/ipazc/mtcnn  

INSTALLATION
############

Currently it is only supported Python3.4 onwards. It can be installed through pip:

.. code:: bash

    $ pip install mtcnn

This implementation requires OpenCV>=4.1 and Keras>=2.0.0 (any Tensorflow supported by Keras will be supported by this MTCNN package).
If this is the first time you use tensorflow, you will probably need to install it in your system:

.. code:: bash

    $ pip install tensorflow

or with `conda`

.. code:: bash

    $ conda install tensorflow

Note that `tensorflow-gpu` version can be used instead if a GPU device is available on the system, which will speedup the results.

USAGE
#####

Images
=========

The following example illustrates the ease of use of this package:

.. code:: bash

    python example.py

The detector returns a list of JSON objects. Each JSON object contains three main keys: 'box', 'confidence' and 'keypoints':

- The bounding box is formatted as [x, y, width, height] under the key 'box'.
- The confidence is the probability for a bounding box to be matching a face.
- The keypoints are formatted into a JSON object with the keys 'left_eye', 'right_eye', 'nose', 'mouth_left', 'mouth_right'. Each keypoint is identified by a pixel position (x, y).

Video
=========

.. code:: bash

    python example_video.py

Note: The path to the video should be provided in the example_video.py file

Notebook
=========

A Google Colab Notebook is also provided, named MTCNN.ipynb


LICENSE
#######

`MIT License`_.


REFERENCE
=========

.. [ZHANG2016] Zhang, K., Zhang, Z., Li, Z., and Qiao, Y. (2016). Joint face detection and alignment using multitask cascaded convolutional networks. IEEE Signal Processing Letters, 23(10):1499–1503.

.. _example.py: example.py
.. _MIT license: LICENSE
