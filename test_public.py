import numpy as np
import pytest

import roots


@pytest.mark.parametrize(
    "h0, v0, g", [(0.0, 10.0, 9.81), (5.0, 3.0, 9.81), (20.0, -2.0, 1.62)]
)
def test_projectile_time_lands_at_zero_height(h0, v0, g):
    t = roots.root_quadratic_projectile_time(h0, v0, g)
    assert t > 0
    np.testing.assert_allclose(h0 + v0 * t - 0.5 * g * t**2, 0.0, atol=1e-8)


def test_projectile_time_known_value():
    t = roots.root_quadratic_projectile_time(0.0, 10.0, 10.0)
    assert np.isclose(t, 2.0)


def test_wien_displacement_physical_constant():
    x = roots.root_wien_displacement_x(5.0)
    assert np.isclose(x, 4.965114231744276, rtol=1e-6)


@pytest.mark.parametrize("c", [2.0, 3.0, 5.0, 8.0])
def test_wien_displacement_general_coefficient(c):
    x = roots.root_wien_displacement_x(c)
    assert x > 1e-3
    assert np.isclose(x * np.exp(x), c * (np.exp(x) - 1.0), rtol=1e-8)


def test_radioactive_decay_one_half_life():
    t = roots.root_radioactive_decay_time(1000.0, 500.0, 3.0)
    assert np.isclose(t, 3.0)


@pytest.mark.parametrize(
    "N0, Nt, tau", [(1e6, 1e3, 5730.0), (200.0, 50.0, 1.5), (1.0, 0.1, 10.0)]
)
def test_radioactive_decay_general(N0, Nt, tau):
    t = roots.root_radioactive_decay_time(N0, Nt, tau)
    assert t > 0
    assert np.isclose(N0 * 0.5 ** (t / tau), Nt, rtol=1e-8)


@pytest.mark.parametrize(
    "V0, m, hbar, L",
    [(10.0, 1.0, 1.0, 2.0), (50.0, 1.0, 1.0, 1.0), (5.0, 2.0, 1.5, 3.0)],
)
def test_finite_square_well_even_state(V0, m, hbar, L):
    k = roots.root_finite_square_well_even_state(V0, m, hbar, L)
    k_max = np.sqrt(2 * m * V0) / hbar
    assert 0 < k < k_max
    # Lowest even state lies on the first branch of tan
    assert k * L / 2 < np.pi / 2
    lhs = k * np.tan(k * L / 2)
    rhs = np.sqrt(2 * m * V0 / hbar**2 - k**2)
    assert np.isclose(lhs, rhs, rtol=1e-6)


def test_damped_oscillator_complex_roots():
    m, c, k = 1.0, 2.0, 5.0
    roots_ = roots.roots_damped_oscillator(m, c, k)
    assert len(roots_) == 2
    assert all(isinstance(s, complex) for s in roots_)
    expected = sorted([complex(-1, 2), complex(-1, -2)], key=lambda z: z.imag)
    got = sorted(roots_, key=lambda z: z.imag)
    np.testing.assert_allclose(got, expected, atol=1e-6)


def test_damped_oscillator_real_roots():
    m, c, k = 1.0, 5.0, 6.0
    roots_ = roots.roots_damped_oscillator(m, c, k)
    assert all(isinstance(s, complex) for s in roots_)
    got = sorted(s.real for s in roots_)
    np.testing.assert_allclose(got, [-3.0, -2.0], atol=1e-6)
    np.testing.assert_allclose([s.imag for s in roots_], 0.0, atol=1e-6)


@pytest.mark.parametrize("m, c, k", [(2.0, 1.0, 8.0), (1.0, 4.0, 4.0), (0.5, 3.0, 1.0)])
def test_damped_oscillator_satisfies_characteristic_equation(m, c, k):
    for s in roots.roots_damped_oscillator(m, c, k):
        assert abs(m * s**2 + c * s + k) < 1e-6


def test_circle_intersection_known_point():
    x, y = roots.root_circle_intersection(5.0, 5.0, 6.0)
    assert np.isclose(x, 3.0, atol=1e-6)
    assert np.isclose(y, 4.0, atol=1e-6)


@pytest.mark.parametrize("r1, r2, d", [(3.0, 4.0, 5.0), (2.0, 3.0, 4.0), (10.0, 6.0, 8.0)])
def test_circle_intersection_general(r1, r2, d):
    x, y = roots.root_circle_intersection(r1, r2, d)
    assert y >= 0
    assert np.isclose(x**2 + y**2, r1**2, rtol=1e-6)
    assert np.isclose((x - d) ** 2 + y**2, r2**2, rtol=1e-6)


def test_two_masses_three_strings():
    L = 8.0
    lengths = (3.0, 4.0, 4.0)
    weights = (10.0, 20.0)
    (th1, th2, th3), (T1, T2, T3) = roots.root_two_masses_three_strings(
        L, lengths, weights
    )
    L1, L2, L3 = lengths
    W1, W2 = weights
    assert T1 > 0 and T2 > 0 and T3 > 0

    # Geometry
    assert np.isclose(L1 * np.cos(th1) + L2 * np.cos(th2) + L3 * np.cos(th3), L, atol=1e-6)
    assert np.isclose(L1 * np.sin(th1) + L2 * np.sin(th2) - L3 * np.sin(th3), 0.0, atol=1e-6)
    # Force balance (angles measured from the horizontal, as in Landau)
    assert np.isclose(T1 * np.sin(th1) - T2 * np.sin(th2), W1, atol=1e-6)
    assert np.isclose(T1 * np.cos(th1) - T2 * np.cos(th2), 0.0, atol=1e-6)
    assert np.isclose(T2 * np.sin(th2) + T3 * np.sin(th3), W2, atol=1e-6)
    assert np.isclose(T2 * np.cos(th2) - T3 * np.cos(th3), 0.0, atol=1e-6)
