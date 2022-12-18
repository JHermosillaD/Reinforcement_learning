# Reinforcement learning :notebook_with_decorative_cover:

> Jupyter notebooks of the algorithms developed in the Self-Optimizing Systems ([HAW hamburg](https://www.haw-hamburg.de/studium/studiengaenge-a-z/studiengaenge-detail/course/courses/show/informatik/)) class.

The vehicle's task is to start from an initial position and speed and move towards a goal in a straight line, modifying its speed in order to not invade a person's personal space. 

The vehicle state ( $s^v$ ) is given by its position and velocity constrained to the y-axis.
The vehicle detects a human and stores 4 sequential positions to generate an observation.
These positions are points ( $\mathbf{P}$ ) in the plane recorded at arbitrary time intervals $\Delta t$.
While the human velocity ( $\dot{p}^h$ ) can be obtained from the positions and the elapsed time.

<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{matrix}Description&space;&space;&space;&space;&space;&space;&space;&&space;Symbol&space;&space;&space;&space;&space;&space;&&space;Content&space;\\&space;\mbox{Vehicle&space;state}&space;&space;&space;&space;&space;&&space;s^v&space;&space;&space;&space;&space;&space;&space;&space;&space;&&space;\{p_y^v,&space;\dot{p}_y^v\}&space;\\\mbox{Human&space;state}&space;&space;&space;&space;&space;&space;&space;&&space;s^h&space;&space;&space;&space;&space;&space;&space;&space;&space;&&space;\{p_x^h,&space;p_y^h,&space;\dot{p}^h\}&space;\\&space;\mbox{Observation&space;space}&space;&&space;\mathcal{O}&space;&&space;\{&space;\mathbf{P}_t^h,&space;\mathbf{P}_{t&plus;1}^h,&space;\mathbf{P}_{t&plus;2}^h,&space;\mathbf{P}_{t&plus;3}^h&space;\}&space;\\\mbox{Action&space;space}&space;&space;&space;&space;&space;&space;&&space;\mathcal{A}&space;&&space;\{\alpha_&plus;,&space;\alpha_{-}&space;\}\end{matrix}" title="https://latex.codecogs.com/svg.image?\begin{matrix}Description & Symbol & Content \\ \mbox{Vehicle state} & s^v & \{p_y^v, \dot{p}_y^v\} \\\mbox{Human state} & s^h & \{p_x^h, p_y^h, \dot{p}^h\} \\ \mbox{Observation space} & \mathcal{O} & \{ \mathbf{P}_t^h, \mathbf{P}_{t+1}^h, \mathbf{P}_{t+2}^h, \mathbf{P}_{t+3}^h \} \\\mbox{Action space} & \mathcal{A} & \{\alpha_+, \alpha_{-} \}\end{matrix}" />

Where $\mathcal{O}\in \Re^8$ and $\mathcal{A}\in \Re^2$. \\

The action $\alpha$ is a control variable that updates the current velocity.
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{align*}\dot{p}_y^v(t&plus;1)&space;&=&space;\alpha&space;\dot{p}_y^v(t)\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}\dot{p}_y^v(t+1) &= \alpha \dot{p}_y^v(t)\end{align*}" />

The reward ( $R$ ) is obtained by:
<p align="center">
<img src="https://latex.codecogs.com/svg.image?R&space;=&space;\Biggl\{\begin{align*}&space;&space;&space;&space;&space;&space;&r_g(s^v)&space;&plus;&space;r_h(s^h)&space;&\text{if&space;}&space;|\mathbf{P}^h&space;-&space;\mathbf{P}^v|^2&space;\geq&space;l^2\\&space;&space;&space;&space;&space;&space;&r_g(s^v)&space;&\text{else&space;}\end{align*}" title="https://latex.codecogs.com/svg.image?R = \Biggl\{\begin{align*} &r_g(s^v) + r_h(s^h) &\text{if } |\mathbf{P}^h - \mathbf{P}^v|^2 \geq l^2\\ &r_g(s^v) &\text{else }\end{align*}" />

where $l = 1 + \beta \dot{p}^h$. 

The vehicle receives a reward $r_g$ that increases as it gets closer to the goal. 
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{align*}r_g&space;=&space;\frac{1}{|\mathbf{P}^g&space;-&space;\mathbf{P}^v|&plus;1}\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}r_g = \frac{1}{|\mathbf{P}^g - \mathbf{P}^v|+1}\end{align*}" />

While it receives a penalty when it approaches the human 
<p align="center">
<img src="https://latex.codecogs.com/svg.image?\begin{align*}r_h&space;=&space;-\frac{l}{|\mathbf{P}^h&space;-&space;\mathbf{P}^v|}\end{align*}" title="https://latex.codecogs.com/svg.image?\begin{align*}r_h = -\frac{l}{|\mathbf{P}^h - \mathbf{P}^v|}\end{align*}" />

<p align="center">
<img src='https://github.com/JHermosillaD/Reinforcement_learning/blob/main/environment_simulator_V1/imgs/reward.png?raw=true' />

Rewards obtained in an instant of time, when $s^h = \{3,5,1.4\}$ and the goal is at $\mathbf{P}^g(8,-7.5)$.

The end of an episode is defined by the following terminal states:
  * The vehicle reaches the goal, i.e. $|\mathbf{P}^g - \mathbf{P}^v| \approx 0$
  * The vehicle invades personal space, i.e. $|\mathbf{P}^h - \mathbf{P}^v| < l^2$
  * The vehicle is moving backwards, i.e. $\dot{p}^h < 0$

## V2 pygame simulation

Restricted to one pedestrian with rectilinear motion.

![v2sim](https://github.com/JHermosillaD/Reinforcement_learning/blob/main/environment_simulator_V2/output/test_1.gif)

Experience buffer composed by the position and speed of 4 observations.
$Experience = ((p_{1x}, p_{1y}, v_{1x},v_{1y}), (p_{2x}, p_{2y}, v_{2x},v_{2y}), (p_{3x}, p_{3y}, v_{3x},v_{3y}), (p_{4x}, p_{4y}, v_{4x},v_{4y})) $

Execution example:
<p float="left">
  <img src="environment_simulator_V2/output/experience_buffer.png"/>
</p>

### References

David Silver. (2015). Lectures on Reinforcement Learning.

Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.
