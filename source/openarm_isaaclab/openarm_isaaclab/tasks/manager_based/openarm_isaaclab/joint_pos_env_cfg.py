# Copyright (c) 2022-2025, The Isaac Lab Project Developers.
# Copyright (c) 2025, Reazon Holdings, inc.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import math

from isaaclab.utils import configclass

from isaaclab.managers import EventTermCfg as EventTerm
import isaaclab_tasks.manager_based.manipulation.reach.mdp as mdp
from isaaclab_tasks.manager_based.manipulation.reach.reach_env_cfg import ReachEnvCfg

from openarm_isaaclab.assets.open_arm import OPEN_ARM_CFG

@configclass
class OpenArmEventCfg:
    """Configuration for events."""

    reset_robot_joints = EventTerm(
        func=mdp.reset_joints_by_scale,
        mode="reset",
        params={
            "position_range": (0.5, 1.5),
            "velocity_range": (0.0, 0.0),
        },
    )

@configclass
class OpenArmReachEnvCfg(ReachEnvCfg):

    events: OpenArmEventCfg = OpenArmEventCfg()
    
    def __post_init__(self):
        super().__post_init__()

        self.scene.robot = OPEN_ARM_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        self.rewards.end_effector_position_tracking.params["asset_cfg"].body_names = ["link8"]
        self.rewards.end_effector_position_tracking_fine_grained.params["asset_cfg"].body_names = ["link8"]
        self.rewards.end_effector_orientation_tracking.params["asset_cfg"].body_names = ["link8"]

        self.actions.arm_action = mdp.JointPositionActionCfg(
            asset_name="robot", 
            joint_names=[
                "rev1",
                "rev2",
                "rev3",
                "rev4",
                "rev5",
                "rev6",
                "rev7"], 
            scale=0.1, 
            use_default_offset=True
        )
        
        self.commands.ee_pose.body_name = "link8"
        # self.commands.ee_pose.ranges.pitch = (math.pi, math.pi)
        self.commands.ee_pose.ranges.pos_x = (0.15, 0.35)
        self.commands.ee_pose.ranges.pos_z = (0.15, 0.35)
        self.commands.ee_pose.ranges.roll = (0,0)#(-math.pi/2, math.pi/2)  # (0, 0)
        self.commands.ee_pose.ranges.pitch = (-math.pi/2,-math.pi/2)#(-math.pi/2, math.pi/2) # (0, 0)
        self.commands.ee_pose.ranges.yaw = (math.pi, math.pi)# (math.pi/2, 3*math.pi/2)  # (math.pi, math.pi)

@configclass
class OpenArmReachEnvCfg_PLAY(OpenArmReachEnvCfg):
    def __post_init__(self):
        super().__post_init__()
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        self.observations.policy.enable_corruption = False
