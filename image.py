import argparse
import cv2
import math

y = 333.0
x = 500.0

def mmethod():
   img = cv2.imread(FLAGS.img)
   cv2.imshow('img', img)
   cv2.waitKey(0)
   h = img.shape[0]
   w = img.shape[1]
   ratio = float(h)/float(w)
   dim = (0,0)
   r = 0.0
   if ratio > y/x:
       v = y/float(h)
       dim = (int(v*w), int(y))
   else:
       v = x/float(w)
       dim = (int(x), int(h*v))
   print(h, w, dim)
   im = cv2.resize(img, dim)
   cv2.imshow('im', im)

   side = FLAGS.box_size + side%2 # even box size for 50% overlap on  
sliding occluder
   cut_x = im.shape[0] % side
   cut_y = im.shape[1] % side

   i = im[0:im.shape[0]-cut_x,0:im.shape[1]-cut_y] # final tensor  
divisible by side in both dimensions


   for j in range(i.shape[0]*2/side-1):
       cj = -side/2
       cj += side/2
       for k in range(i.shape[1]*2/side-1):
           ck = -side/2
           ck += side
           i[j*side/2:(j+1)*side/2, k*side/2:(k+1)*side/2] = [0.5, 0.5, 0.5]



   cv2.imshow('i', i)
   cv2.waitKey(0)

def blend(img_a, alpha=0.5, img_b):
     if alpha > 1.0 or alpha < 0.0:
     img_c = cv2.addWeighted(img_a, alpha, )


if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument(
       '--img',
       type=str,
       default='',
       help='Path to image.'
   )
   parser.add_argument(
       '--box_size',
       type=int,
       default=25,
       help='Side length of occlusion box.'
   )
   FLAGS, unparsed = parser.parse_known_args()
   mmethod()
