# Path  of a charged particle

The Runge Kutta method of order 4 is used to solve for the path of a charged particle in an electromagnetic field.

A charged particle in an electromagnetic field is a second order system. Its governing differential equation is given by the Lorentz force equation -

$ \large m\frac{\text{d}^2\textbf{r}}{\text{d}t^2} = q(\textbf{E} + \frac{\text{d}\textbf{r}}{\text{d}t}\times\textbf{B}) $

Assuming $ \textbf{E} = E_0\hat{\textbf{x}} $ and $ \textbf{B} = -B_0\hat{\textbf{z}} $, we get - 

$ \large \ddot{x} = \frac{q}{m}(E_0 - \dot{y}B_0) \\
\large \ddot{y} = \frac{q}{m}\dot{x}B_0 $

Now, to apply the Runge-Kutta method, the two coupled second order equations must be converted to four first order equations. We decouple them by considering $x=y_1$, $y=y_2$, $\dot{x}=y_3$ and $\dot{y}=y_4$. Then, we define the functions as - 

$ \large f_1 = \dot{y_1} = y_3 \\
\large f_2 = \dot{y_2} = y_4 \\
\large f_3 = \dot{y_3} = \frac{q}{m}(E_0 - y_4B_0) \\
\large f_4 = \dot{y_4} = \frac{q}{m}(y_3B_0) $

These functions and the initial positions and velocities are passed to the RK44 function, which returns the updated
position and velocity vectors along the path.
