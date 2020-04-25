#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# read image

image = cv2.imread("D:\Study\DataScience\OpenCV\messi1.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# read logo
logo = cv2.imread("D:\Study\DataScience\OpenCV\logo.jpg")
logo = cv2.cvtColor(logo, cv2.COLOR_BGR2RGB)
logo = cv2.resize(logo, (160, 80))


# In[1]:


class PlaceImageLogo:
    
    def __init__(self):
        self
    
    def place_logo(self, image, logo, loc = None):
        
        self.image = image
        self.logo = logo
        self.loc = loc
            
        self.x_offset = 50
        self.y_offset = 50
        
        assert image.shape[0] > logo.shape[0], "Height of main image is less than logo image"
        assert image.shape[1] > logo.shape[1], "Width of main image in less than logo image"
        
        if self.loc is None:
            self.loc == 'bc'
            
            self.image[self.image.shape[0]-self.logo.shape[0]-self.y_offset:self.image.shape[0]-self.y_offset,
              int(self.image.shape[1]-self.logo.shape[1])//2:int(self.image.shape[1]-self.logo.shape[1])//2 + self.logo.shape[1]] = self.logo
            
        else:
 
            assert self.loc in ['tl', 'bl', 'tr', 'br'], "Please specify corrent location from 'tl', 'bl', 'tr', 'br'"
        
          
            if self.loc == 'br':
                self.image[self.image.shape[0]- self.logo.shape[0]-self.y_offset:self.image.shape[0]-self.y_offset, 
                  self.image.shape[1]- self.logo.shape[1]-self.x_offset:self.image.shape[1]-self.x_offset] = self.logo
            
            elif self.loc == 'tl':
                self.image[self.y_offset:self.y_offset+self.logo.shape[0], self.x_offset:self.x_offset+self.logo.shape[1]] = self.logo
            
            elif self.loc == 'bl':
                self.image[self.image.shape[0]- logo.shape[0]-self.y_offset:self.image.shape[0]-self.y_offset, 
                  self.x_offset:self.x_offset+self.logo.shape[1]] = self.logo
            
            elif self.loc == 'tr':
                self.image[self.y_offset:self.y_offset+self.logo.shape[0], 
                  self.image.shape[1]- self.logo.shape[1]-self.x_offset:self.image.shape[1]-self.x_offset] = self.logo
 

        return self.image
 


# In[ ]:




