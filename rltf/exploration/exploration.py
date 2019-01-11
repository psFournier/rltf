from rltf.utils import seeding


class ExplorationNoise:

  def __init__(self):
    self.prng = seeding.get_prng()

  def sample(self, t):
    """Get a sample from the noise process for the given time step
    Args:
      t: Current time step
    Returns:
      float: the sampled noise value
    """
    raise NotImplementedError()

  def reset(self):
    """Reset the noise process"""
    raise NotImplementedError()
