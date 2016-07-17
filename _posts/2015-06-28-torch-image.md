---
layout: post
title: "2015-06-28-Torch-Image"
tags:
    - python
    - notebook
--- 
## Tensor Image
Image패키지는 여러 type의 이미지 load, save 및 간단한 image processing 을 지원합니다. 

**In [1]:**

{% highlight python %}
require 'torch'
require 'image'
{% endhighlight %}
 
### Sample Image
Image패키지에서는 Image Processing에 단골로 등장하는 샘플 2개를 제공합니다.

* [Lena Image](https://en.wikipedia.org/wiki/Lenna)
* [Fabio Image](https://en.wikipedia.org/wiki/Fabio_Lanzoni)

두 이미지를 iTorch에서 이미지 출력을 위해 기본으로 제공하는 itorch.image() 함수를 이용해 출력해봅니다. 

**In [2]:**

{% highlight python %}
lena = image.lena()
itorch.image(lena)
print(lena:size())
{% endhighlight %}

 
![png]({{ BASE_PATH }}/images/2015-06-28-torch-image_3_0.png) 





    
       3
     512
     512
    [torch.LongStorage of size 3]
    



 
Lena이미지는 컬러 이미지로 3x512x512 3차원 Tensor로 저장되어 있습니다. 

**In [3]:**

{% highlight python %}
fabio = image.fabio()
itorch.image(fabio)
print(fabio:size())
{% endhighlight %}

 
![png]({{ BASE_PATH }}/images/2015-06-28-torch-image_5_0.png) 





    
     257
     271
    [torch.LongStorage of size 2]
    



 
Fabio이미지는 흑백 이미지로 257x271 2차원 Tensor로 저장되어 있습니다. 
