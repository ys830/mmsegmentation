# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class Cardiac(CustomDataset):
    CLASSES = ('background', 'LV')

    PALETTE = [[0], [1]]

    def __init__(self, **kwargs):
        super(Cardiac, self).__init__(
            img_suffix='.png',
            seg_map_suffix='_label.png',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)