"""
| File: gust_wind.py
| Author: [Your Name]
| Description: Implementation of a steady wind with sinusoidal gusts
| License: BSD-3-Clause
"""
import numpy as np
from pegasus.simulator.logic.wind import Wind
from pegasus.simulator.logic.state import State

class GustWind(Wind):
    """
    Implements a wind model with a constant base velocity and a periodic gust.
    """

    def __init__(self, mean_velocity=[0.0, 0.0, 0.0], gust_amplitude=[0.0, 0.0, 0.0], gust_frequency=0.5):
        """
        Args:
            mean_velocity (list[float]): Constant wind speed in World Frame [m/s].
            gust_amplitude (list[float]): Peak amplitude of the gust in World Frame [m/s].
            gust_frequency (float): How fast the gust oscillates (Hz).
        """
        super().__init__()

        self._mean_vel = np.array(mean_velocity)
        self._gust_amp = np.array(gust_amplitude)
        self._freq = gust_frequency
        
        self._curr_wind_world = np.array([0.0, 0.0, 0.0])
        self._time_elapsed = 0.0

    @property
    def wind_velocity_world(self):
        return self._curr_wind_world

    def update(self, state: State, dt: float):
        """
        Updates the wind vector. 
        Formula: V_wind = V_mean + V_gust * sin(2 * pi * f * t)
        """
        self._time_elapsed += dt
        
        # Calculate the gust component
        gust = self._gust_amp * np.sin(2 * np.pi * self._freq * self._time_elapsed)
        
        # Update current wind in world frame
        self._curr_wind_world = self._mean_vel + gust
        
        return self._curr_wind_world