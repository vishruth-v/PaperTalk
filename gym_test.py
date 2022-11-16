import gym
import highway_env
from matplotlib import pyplot as plt
# %matplotlib inline
import pprint 

env = gym.make('highway-v0')
env.config["lanes_count"] = 3
env.config['centering_position'] = [0.3, 0.5]
env.config['screen_height'] = 180*2
env.config['screen_height'] = 45*2
env.config['simulation_frequency'] = 10
pprint.pprint(env.config)

env.reset()
for _ in range(100):
    action = env.action_type.actions_indexes["IDLE"]
    obs, reward, done, info = env.step(action)
    env.render()

plt.imshow(env.render(mode="rgb_array"))
plt.show()