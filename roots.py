"""Student assignment implementation file.

Complete the TODOs in this file.
"""

# --- Imports --- #


# --- Problem 1: Quadratic (Projectile Fall Time) --- #
def root_quadratic_projectile_time(h0, v0, g):
    """Find the positive time at which a vertically launched projectile returns to height 0."""
    raise NotImplementedError


# --- Problem 2: Transcendental (Wien's Displacement Law) --- #
def root_wien_displacement_x(coef):
    """Find the positive root x of x * exp(x) = coef * (exp(x) - 1)."""
    raise NotImplementedError


# --- Problem 3: Transcendental (Radioactive Decay) --- #
def root_radioactive_decay_time(N0, N_target, half_life):
    """Find the elapsed time at which a sample of N0 nuclei decays to N_target nuclei."""
    raise NotImplementedError


# --- Problem 4: Non-Trivial Transcendental (Finite Square Well) --- #
def root_finite_square_well_even_state(V0, m, hbar, L):
    """Find the bound-state wavenumber k of the lowest even state in a finite square well."""
    raise NotImplementedError


# --- Problem 5: Complex Roots (Damped Harmonic Oscillator) --- #
def roots_damped_oscillator(m, c, k):
    """Find both roots s of the characteristic equation m*s**2 + c*s + k = 0."""
    raise NotImplementedError


# --- Problem 6: Multivariate (Circle Intersection / Trilateration) --- #
def root_circle_intersection(r1, r2, d):
    """Find the (x, y) point above the baseline where two circles of radii r1, r2 intersect."""
    raise NotImplementedError


# --- Problem 7: Multivariate Statics (Two Masses, Three Strings) --- #
def root_two_masses_three_strings(
    L, lengths, weights
):
    """Find the equilibrium angles and tensions of two weights hung from three strings."""
    raise NotImplementedError
