_base_ = [
    '../_base_/models/deeplabv3_unet_s5-d16.py',
    '../_base_/datasets/Car_0505.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_40k.py'
]
model = dict(test_cfg=dict(crop_size=(160, 160), stride=(85, 85)))
evaluation = dict(metric='mDice')
