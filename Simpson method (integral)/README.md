# Simpson method

This method is used to approximate definite integrals by quadratic interpolation. The function Simpson.py takes in the function to be integrated, the integration limits and the number of discrete steps as arguments and returns the answer.

## Diffraction pattern

The parametric curve known as Cornu's spiral is given by -

<img src="https://render.githubusercontent.com/render/math?math=\large x(t) = \int_0^t \cos\left(\frac{\pi u^2}{2}\right)\text{d}u">
<img src="https://render.githubusercontent.com/render/math?math=\large y(t) = \int_0^t \sin\left(\frac{\pi u^2}{2}\right)\text{d}u">

with <img src="https://render.githubusercontent.com/render/math?math=t \in [-\infty,\infty]">. Here, we take <img src="https://render.githubusercontent.com/render/math?math=t \in [-50,50]">, which gives us enough data points.

The intensity due to diffraction at a sharp edge is plotted using - 

<img src="https://render.githubusercontent.com/render/math?math=\large I(t) = {\left(\frac{1}{2}-x(t)\right)}^2 %2B {\left(\frac{1}{2}-y(t)\right)}^2">

![](diffraction.png)
