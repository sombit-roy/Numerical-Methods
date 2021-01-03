# Runge-Kutta method

Runge-Kutta method is a numerical technique to solve initial value ODEs by temporal discretization. The function RK44.py can be used to solve two coupled second order equations. The equations must be decoupled to four first order equations.

The RK method of order 4 is used to solve for the path of a charged particle in an electromagnetic field and simulating a double pendulum system.

## Path  of a charged particle

A charged particle in an electromagnetic field is a second order system. Its governing differential equation is given by the Lorentz force equation -

<img src="https://render.githubusercontent.com/render/math?math=\large m\frac{\text{d}^2\textbf{r}}{\text{d}t^2} = q(\textbf{E}%2B\frac{\text{d}\textbf{r}}{\text{d}t}\times\textbf{B})">

Assuming <img src="https://render.githubusercontent.com/render/math?math=\textbf{E} = E_0\hat{\textbf{x}}"> and <img src="https://render.githubusercontent.com/render/math?math=\textbf{B} = -B_0\hat{\textbf{z}}">, we get - 

<img src="https://render.githubusercontent.com/render/math?math=\large \ddot{x} = \frac{q}{m}(E_0 - \dot{y}B_0)">
<img src="https://render.githubusercontent.com/render/math?math=\large \ddot{y} = \frac{q}{m}\dot{x}B_0">

We decouple them by considering <img src="https://render.githubusercontent.com/render/math?math=x=y_1">, <img src="https://render.githubusercontent.com/render/math?math=y=y_2">, <img src="https://render.githubusercontent.com/render/math?math=\dot{x}=y_3"> and <img src="https://render.githubusercontent.com/render/math?math=\dot{y}=y_4">. Then, we define the functions as - 

<img src="https://render.githubusercontent.com/render/math?math=\large f_1 = \dot{y_1} = y_3">
<img src="https://render.githubusercontent.com/render/math?math=\large f_2 = \dot{y_2} = y_4">
<img src="https://render.githubusercontent.com/render/math?math=\large f_3 = \dot{y_3} = \frac{q}{m}(E_0 - y_4B_0)">
<img src="https://render.githubusercontent.com/render/math?math=\large f_4 = \dot{y_4} = \frac{q}{m}(y_3B_0)">

These functions and the initial positions and velocities are passed to the RK44 function, which returns the updated position and velocity vectors along the path. We call charge(0,1) and charge(1,1) to plot helix and cycloid trajectories respectively.

![](charge.png)

## Double Pendulum

Let the angles made by the vertical by the upper and lower pendulum be <img src="https://render.githubusercontent.com/render/math?math=\theta_1"> and <img src="https://render.githubusercontent.com/render/math?math=\theta_2"> respectively. The lagrangian of the double pendulum system is - 

<img src="https://render.githubusercontent.com/render/math?math=\large L = \left(\frac{m_1}{2} %2B \frac{m_2}{2}\right) l_1^2\dot\theta_1^2 %2B \frac{m_2}{2}l_2^2\dot\theta_2^2 %2B m_2l_1l_2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2) %2B (m_1%2Bm_2)gl_1\cos\theta_1 %2B m_2gl_2\cos\theta_2">

Using the Euler-Lagrange equation <img src="https://render.githubusercontent.com/render/math?math=\cfrac{\text{d}}{{\text{d}t}}\left(\cfrac{{\partial L}}{{\partial{{\dot\theta}_i}}}\right) = \cfrac{{\partial L}}{{\partial {\theta_i}}}">, we get the following equations -

<img src="https://render.githubusercontent.com/render/math?math=\large (m_1%2Bm_2)l_1\ddot\theta_1 %2B m_2l_2\ddot\theta_2\cos(\theta_1–\theta_2) %2B m_2l_2\dot\theta_2^2\sin(\theta_1–\theta_2) %2B (m_1+m_2)g\sin\theta_1 = 0">
<img src="https://render.githubusercontent.com/render/math?math=\large l_2\ddot\theta_2 %2B l_1\ddot\theta_1\cos(\theta_1–\theta_2) – l_1\dot\theta_1^2\sin(\theta_1-\theta_2) %2B g\sin\theta_2 = 0">

We decouple them as in the previous example and call the RK44 function with initial angles as 30 and 60 degrees. Below is the gif obtained using the matplotlib animation package -

![](doublependulum.gif)
