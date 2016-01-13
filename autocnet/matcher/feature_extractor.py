import cv2

def extract_features(image_array, num_nodes=500):
    """
    Extracts keypoints and corresponding descriptors from a numpy array
    that represents an image. The extracted information is returned as a tuple whose first element is
    a list of KeyPoints and whose second element is a numpy array of geometric vector descriptors.

    Parameters
    ----------
    image_array : ndarray
                  a numpy array that represents an image
    num_nodes : int
                the number of best features to retain

    Returns
    -------
    : tuple
      This tuple is in the form (list of KeyPoints, array of descriptors)
    """
    sift = cv2.xfeatures2d.SIFT_create(num_nodes)
    return sift.detectAndCompute(image_array, None)