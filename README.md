# Reinforcement learning :notebook_with_decorative_cover:

> Jupyter notebooks of the algorithms developed in the Self-Optimizing Systems ([HAW hamburg](https://www.haw-hamburg.de/studium/studiengaenge-a-z/studiengaenge-detail/course/courses/show/informatik/)) class.

## V2 pygame simulation

Restricted to one pedestrian with rectilinear motion.

![v2sim](https://github.com/JHermosillaD/Reinforcement_learning/blob/main/environment_simulator_V2/output/test_1.gif)

Experience buffer composed by the position and speed of 4 observations.
$Experience = ((p_{1x}, p_{1y}, v_{1x},v_{1y}), (p_{2x}, p_{2y}, v_{2x},v_{2y}), (p_{3x}, p_{3y}, v_{3x},v_{3y}), (p_{4x}, p_{4y}, v_{4x},v_{4y})) $

<p float="left">
  <img src="environment_simulator_V2/output/experience_buffer.png"/>
</p>

### References

David Silver. (2015). Lectures on Reinforcement Learning.

Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press.
