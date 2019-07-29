import cv2
import math
import numpy as np


def TonemapDurand(file_path):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    tonemapDurand = cv2.createTonemapDurand(1.5,4,1.0,1,1)
    ldrDurand = tonemapDurand.process(im)
    # im2_8bit = np.clip(ldrDurand * 255, 0, 255).astype('uint8')

    return  ldrDurand

def TonemapDrago(file_path):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    tonemapDrago = cv2.createTonemapDrago(1.0, 0.7)
    ldrDrago = tonemapDrago.process(im)

    return ldrDrago



def TonemapReinhard(file_path):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    tonemapReinhard = cv2.createTonemapReinhard(1.5, 0, 0, 0)
    ldrReinhard = tonemapReinhard.process(im)

    return ldrReinhard


def TonemapMantiuk(file_path):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    tonemapMantiuk = cv2.createTonemapMantiuk(2.2, 0.85, 1.2)
    ldrMantiuk = tonemapMantiuk.process(im)

    return ldrMantiuk

def load_image(file_path):
    filename = "leadenhall_market_2k.hdr"

def ACESToneMapping(file_path, adapted_lum):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    A = 2.51
    B = 0.03
    C = 2.43
    D = 0.59
    E = 0.14
    im *= adapted_lum;

    return pow((im * (A * im + B)) / (im * (C * im + D) + E),1/2.2)

def factor(image):
    A = 0.22
    B = 0.30
    C = 0.10
    D = 0.20
    E = 0.01
    F = 0.30

    return  ((image * (A * image + C * B) + D * E) / (image * (A * image + B) + D * F)) - E / F

def Uncharted2ToneMapping(file_path, adapted_lum):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    WHITE = 11.2
    return pow(factor(1.6 * adapted_lum * im) / factor(WHITE), 1/2.2)


def ReinhardSimpleToneMapping(file_path, adapted_lum):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)

    MIDDLE_GREY = 0.18
    im = im * MIDDLE_GREY / adapted_lum

    return pow(im/(1.0+im),1/2.2)

def ReinhardOriginalToneMapping(file_path, adapted_lum):
    im = cv2.imread(file_path, cv2.IMREAD_ANYDEPTH)
    rows = im.shape[0] # height
    cols = im.shape[1] # width

    factor = 0.09/adapted_lum


    for i in range(rows):
        for j in range(cols):
            im[i,j] = pow(im[i,j] * (factor/(1+factor * (im[i,j][0] * 0.2126 + im[i,j][1] * 0.7152 +  im[i,j][2] * 0.0722) )),1/2.2)

    return im

def getAverageLum(image):

    # dst = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    rows = image.shape[0] # height
    cols = image.shape[1] # width

    Lum_sum = 0.0
    for i in range(rows):
        for j in range(cols):
            Lum_sum += math.log(0.0001 + image[i,j][0] * 0.2126 + image[i,j][1] * 0.7152 +  image[i,j][2] * 0.0722)

    return math.exp( Lum_sum/(rows*cols))








def main():
    filename = "the_sky_is_on_fire_1k.hdr"

    widname_prev = "the_sky_is_on_fire_1k"
    im = cv2.imread(filename, cv2.IMREAD_ANYDEPTH)

    cv2.imshow(widname_prev, im)
    x = getAverageLum(im)
    #
    cv2.imshow(widname_prev + '_TonemapDurand', TonemapDurand(filename) * 3)
    cv2.imshow(widname_prev + '_TonemapDrago', TonemapDrago(filename)*3)
    cv2.imshow(widname_prev + '_TonemapMantiuk', TonemapMantiuk(filename)*3)
    cv2.imshow(widname_prev + '_TonemapReinhard', TonemapReinhard(filename)*3)
    cv2.imshow(widname_prev + '_Uncharted2ToneMapping', Uncharted2ToneMapping(filename, x))
    cv2.imshow(widname_prev + '_ACESToneMapping', ACESToneMapping(filename,x))
    cv2.imshow(widname_prev + '_ReinhardSimpleToneMapping', ReinhardSimpleToneMapping(filename, x))
    cv2.imshow(widname_prev + '_ReinhardOriginalToneMapping', ReinhardOriginalToneMapping(filename, x))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # cv2.imwrite(widname_prev + '_TonemapDurand' + ".jpg", np.clip(TonemapDurand(filename) * 3 * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_TonemapDrago' + ".jpg", np.clip(TonemapDrago(filename) *3 * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_TonemapMantiuk' + ".jpg", np.clip(TonemapMantiuk(filename) * 3 * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_TonemapReinhard' + ".jpg", np.clip(TonemapReinhard(filename)* 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_Uncharted2ToneMapping' + ".jpg", np.clip(Uncharted2ToneMapping(filename, x) * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_ACESToneMapping' + ".jpg", np.clip(ACESToneMapping(filename,x) * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_ReinhardSimpleToneMapping' + ".jpg", np.clip(ReinhardSimpleToneMapping(filename, x) * 255, 0, 255).astype('uint8'))
    # cv2.imwrite(widname_prev + '_ReinhardOriginalToneMapping' + ".jpg",  np.clip(ReinhardOriginalToneMapping(filename, x) * 255, 0, 255).astype('uint8'))
    print("tone mapping over")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__== '__main__':
    main()
