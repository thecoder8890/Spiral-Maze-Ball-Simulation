import unittest
import simulation # Assuming your main simulation file is simulation.py

class TestSimulation(unittest.TestCase):

    def test_simulation_runs(self):
        """
        Test if the simulation can initialize and run for a few frames.
        """
        try:
            # If main_loop is designed to run indefinitely,
            # you might need to modify it or this test.
            # For example, main_loop could take a parameter for number of frames.
            # Or, we can run it in a way that we can stop it after a few frames.
            # For now, let's assume simulation.main_loop() runs for a fixed short duration
            # or can be interrupted.

            # Attempt to run the main loop.
            # This is a basic check for runtime errors.
            # Note: Pygame might require a display, which can be an issue in some CI environments.
            # If simulation.main_loop() opens a window and runs indefinitely,
            # this test will hang or fail in CI.
            # The main_loop in simulation.py has been modified to run for 200 frames.
            simulation.main_loop()
            self.assertTrue(True) # If it completes without error, test passes
        except Exception as e:
            self.fail(f"Simulation run failed with an error: {e}")

if __name__ == '__main__':
    unittest.main()
