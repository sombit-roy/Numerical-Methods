# Path  of a charged particle

The Runge Kutta method of order 4 is used to solve for the path of a charged particle in an electromagnetic field.

A charged particle in an electromagnetic field is a second order system. Its governing differential equation is given by the Lorentz force equation -

<img src="https://render.githubusercontent.com/render/math?math=\large m\frac{\text{d}^2\textbf{r}}{\text{d}t^2} = q(\textbf{E}%2B\frac{\text{d}\textbf{r}}{\text{d}t}\times\textbf{B})">

Assuming <img src="https://render.githubusercontent.com/render/math?math=\textbf{E} = E_0\hat{\textbf{x}}"> and <img src="https://render.githubusercontent.com/render/math?math=\textbf{B} = -B_0\hat{\textbf{z}}">, we get - 

<img src="https://render.githubusercontent.com/render/math?math=\large \ddot{x} = \frac{q}{m}(E_0 - \dot{y}B_0)">
<img src="https://render.githubusercontent.com/render/math?math=\large \ddot{y} = \frac{q}{m}\dot{x}B_0">

Now, to apply the Runge-Kutta method, the two coupled second order equations must be converted to four first order equations. We decouple them by considering <img src="https://render.githubusercontent.com/render/math?math=x=y_1">, <img src="https://render.githubusercontent.com/render/math?math=y=y_2">, <img src="https://render.githubusercontent.com/render/math?math=\dot{x}=y_3"> and <img src="https://render.githubusercontent.com/render/math?math=\dot{y}=y_4">. Then, we define the functions as - 

<img src="https://render.githubusercontent.com/render/math?math=\large f_1 = \dot{y_1} = y_3">
<img src="https://render.githubusercontent.com/render/math?math=\large f_2 = \dot{y_2} = y_4">
<img src="https://render.githubusercontent.com/render/math?math=\large f_3 = \dot{y_3} = \frac{q}{m}(E_0 - y_4B_0)">
<img src="https://render.githubusercontent.com/render/math?math=\large f_4 = \dot{y_4} = \frac{q}{m}(y_3B_0)">

These functions and the initial positions and velocities are passed to the RK44 function, which returns the updated
position and velocity vectors along the path.
