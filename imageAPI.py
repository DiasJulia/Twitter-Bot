import numpy as np
import matplotlib.pyplot as plt

class ImageAPI:

    def gradient(self, color):
        picture = []
        for x in range(0, 250):
            arrayx = []
            for y in range(0, 250):
                arrayy = []
                for z in range(0, 3):
                    if(z == color):
                        val = (x * y * 2) / (5 * 10 ** 4 * 3)
                    else:
                        val = 0
                    arrayy.append(val)
                arrayx.append(arrayy)
            picture.append(arrayx)
        self.pic = np.array(picture)

    def saveImg(self, filename):
        plt.imsave(filename, self.pic)
