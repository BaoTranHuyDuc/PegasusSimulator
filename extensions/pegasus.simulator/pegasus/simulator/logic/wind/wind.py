"""
| File: wind.py
| Author: [Your Name]
| Description: Base interface used to implement wind models that affect the environment
| License: BSD-3-Clause
"""
from pegasus.simulator.logic.state import State

class Wind:
    """
    Class that serves as a template for the implementation of Wind models.
    """

    def __init__(self):
        pass

    @property
    def wind_velocity_world(self):
        """ The wind velocity vector in the world frame (ENU)
        
        Returns:
            list: [vx, vy, vz] in m/s
        """
        return [0.0, 0.0, 0.0]

    def update(self, state: State, dt: float):
        """ Method to update the wind state based on time or vehicle position.
        
        Args:
            state (State): The current state of the vehicle (useful if wind depends on altitude).
            dt (float): The time elapsed (s).
        """
        return [0.0, 0.0, 0.0]