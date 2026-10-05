# PH 306 Week 6: Roots

## Overview

This assignment focuses on finding roots of physics equations using [`scipy.optimize`](https://docs.scipy.org/doc/scipy/reference/optimize.html) (*e.g.*, `root_scalar`, `root`). You will implement the functions in `roots.py`.

Public and private tests call each function with different numerical arguments, so your implementation must work generally for the given parameters, not just for one hard-coded case.

Several problems below ask you to find where two curves intersect, such as $f(x) = g(x)$. This is still a root-finding problem: move every term to one side so the equation reads $f(x) - g(x) = 0$, and then find the input(s) that make that expression zero.

## Problems

### Projectile Flight Time

A ball is launched straight up from height `h0` with initial velocity `v0`
under gravitational acceleration `g`. Its height is

$$y(t) = h_0 + v_0 t - \tfrac{1}{2} g t^2.$$

Return the positive time `t > 0` at which `y(t) = 0` (the ball lands).
Assume parameters are such that exactly one positive root exists.

### Wien's Displacement Law

Wien's displacement law constant comes from the root of

$$x e^{x} = c\left(e^{x} - 1\right)$$

where $c$ is a coefficient from the blackbody radiation equation (in reality $c=5$). Return the positive root `x`.

### Radioactive Decay

A radioactive sample starts with `N0` nuclei and decays as

$$N(t) = N_0 \left(\tfrac{1}{2}\right)^{t / \tau}$$

where $\tau$ is the half life.

Return the time `t > 0` at which `N(t) = N_target`.

### Finite Square Well

For a particle of mass `m` in a finite square well of depth `V0` and width
`L`, the lowest even bound state's wavenumber `k` (inside the well) satisfies
the transcendental equation

$$k \tan\!\left(\frac{k L}{2}\right) = \sqrt{\frac{2 m V_0}{\hbar^2} - k^2}$$

valid for $0 < k < \sqrt{2 m V_0} / \hbar$. Return the root `k` in that range.

### Damped Oscillations

A damped harmonic oscillator $m\ddot{x} + c\dot{x} + k x = 0$ has a
characteristic equation

$$m s^2 + c s + k = 0$$

whose two roots `s` may be real or complex, depending on `m`, `c`, and `k`.
Return both roots as a 2-tuple of `complex` values (use `complex(...)` to
wrap purely real roots). Use a root-finding routine on the real and
imaginary parts rather than the quadratic formula.

### Circle Intersections

Two circular regions (e.g. sensor range circles) are centered at `(0, 0)`
and `(d, 0)` with radii `r1` and `r2`, respectively:

$$x^2 + y^2 = r_1^2 \qquad (x - d)^2 + y^2 = r_2^2$$

Return the intersection point `(x, y)` with `y >= 0`. Assume parameters are
such that an intersection exists.

### Two Masses on Three Strings

**Note**: Adapted from Landau's *Computational Physics* (see Section&nbsp;7.1).

Two weights `W1` and `W2` hang from three massless strings. String 1 (length
`L1`) connects the left support to weight 1, string 2 (length `L2`) connects
weight 1 to weight 2, and string 3 (length `L3`) connects weight 2 to the
right support. The supports are at the same height, separated by a horizontal
distance `L`. The inputs are

- `L`: spacing between the supports,
- `lengths = (L1, L2, L3)`: the string lengths,
- `weights = (W1, W2)`: the weights.

Return `((theta1, theta2, theta3), (T1, T2, T3))` (see the book). This can be done with nine equations where the $\sin$ and $\cos$ of an angle are treated independently as in the book (avoids cyclic nature of the parameters) or with six equations where the independent values are only the angles and the tensions. Assume parameters are such that an equilibrium exists with all tensions positive.

## Running the Public Tests

```bash
pytest test_public.py
```
