# Shooting method

For the ODE <img src="https://render.githubusercontent.com/render/math?math=y''=f(x,y,y')">, given <img src="https://render.githubusercontent.com/render/math?math=a<x<b">, the boundary conditions are defined as <img src="https://render.githubusercontent.com/render/math?math=y(a)=y_a"> and <img src="https://render.githubusercontent.com/render/math?math=y(b)=y_b">. The shooting method is used to convert the boundary value problem to an initial value problem with initial conditions <img src="https://render.githubusercontent.com/render/math?math=y(a)=y_a"> and <img src="https://render.githubusercontent.com/render/math?math=y'(a)=\alpha^{(k)}">, where <img src="https://render.githubusercontent.com/render/math?math=\alpha^{(k)}"> is such that it satisfies <img src="https://render.githubusercontent.com/render/math?math=y(b)=y_b">.

<img src="https://render.githubusercontent.com/render/math?math=\alpha^{(0)}"> is initially chosen as the slope between points <img src="https://render.githubusercontent.com/render/math?math=(a,y_a)"> and <img src="https://render.githubusercontent.com/render/math?math=(b,y_b)">. This trial <img src="https://render.githubusercontent.com/render/math?math=\alpha"> is passed as the argument <img src="https://render.githubusercontent.com/render/math?math=y_b"> to the Runge-Kutta function, which returns a vector <img src="https://render.githubusercontent.com/render/math?math=y"> whose last element is an updated value of <img src="https://render.githubusercontent.com/render/math?math=y_b">. This is not likely to be the correct answer as <img src="https://render.githubusercontent.com/render/math?math=\alpha"> was chosen incorrectly. <img src="https://render.githubusercontent.com/render/math?math=\alpha^{(1)}"> is chosen as <img src="https://render.githubusercontent.com/render/math?math=2\alpha^{(0)}">.

Now, we must solve for <img src="https://render.githubusercontent.com/render/math?math=\alpha^{(k)}"> iteratively until <img src="https://render.githubusercontent.com/render/math?math=y_b^{(k)}"> is within the margin of error of the actual <img src="https://render.githubusercontent.com/render/math?math=y_b">. The recurrence relation is given by comparing slopes - 

<img src="https://render.githubusercontent.com/render/math?math=\large\alpha^{(k)} = \alpha^{(k-2)} %2B (y_b - y_b^{(k-2)})\cfrac{\alpha^{(k-1)} - \alpha^{(k-2)}}{y_b^{(k-1)} - y_b^{(k-2)}}">

## Legendre polynomials

Using the shooting method, we solve the <img src="https://render.githubusercontent.com/render/math?math=n^{th}"> order Legendre differential equation - 

<img src="https://render.githubusercontent.com/render/math?math=\large (1-x^2)y'' - 2xy' %2B n(n%2B1)y = 0">

The boundary conditions are <img src="https://render.githubusercontent.com/render/math?math=y(-1)=(-1)^n"> and <img src="https://render.githubusercontent.com/render/math?math=y(1)=1">.

Plotted below are the solutions for n = 5 and n = 6.
