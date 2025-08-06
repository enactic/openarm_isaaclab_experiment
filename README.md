> [!CAUTION]
> This repository is archived. We'll continue on https://github.com/enactic/openarm_isaac_lab .

## Installation Guide
### ① Install ISAAC SIM and ISAAC LAB
The required version of ISAAC SIM is 4.5.0.
From this point on, it is assumed that you have created a virtual environment named env_isaaclab using pyenv and will be working within that environment.

### ② Install openarm-isaaclab
Navigate to the same directory where IsaacLab is cloned and execute the following commands:

```bash
git clone https://github.com/reazon-research/openarm_isaaclab.git
cd openarm_isaaclab
python -m pip install -e exts/openarm_isaaclab
```

After completing this step, the directory structure should look like this:

```
|-IsaacLab
|-openarm_isaaclab
```

### ③ Edit train.py and play.py
When you clone IsaacLab, the scripts train.py and play.py will be located in:

```
IsaacLab/scripts/reinforcement_learning/rsl_rl/
```

These scripts are used for training reinforcement learning models and replaying trained models. However, to recognize the gym environment of openarm_isaaclab, you need to import openarm_isaaclab at the beginning of each script.

Specifically, add the following line at the beginning of train.py and play.py:

```bash
import openarm_isaaclab.tasks.manipulation
```

This ensures that the environment is properly registered and recognized.



### ④ Run Training
Run the following command to start training:

```bash
(env_isaaclab) reazon@reazon:~/isaac/openarm_isaaclab$ bash ../IsaacLab/isaaclab.sh -p ../IsaacLab/scripts/reinforcement_learning/rsl_rl/train.py --task Isaac-Reach-OpenArm-v0 --num_envs 2048
```

### ⑤ Replay Trained Model
To replay a trained model, use the following command:

```bash
(env_isaaclab) reazon@reazon:~/isaac/openarm_isaaclab$ bash ../IsaacLab/isaaclab.sh -p ../IsaacLab/scripts/reinforcement_learning/rsl_rl/play.py --task Isaac-Reach-OpenArm-v0 --num_envs 2048
```
