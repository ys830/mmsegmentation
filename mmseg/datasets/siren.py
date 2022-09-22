# Copyright (c) OpenMMLab. All rights reserved.
import os.path as osp
from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class Siren(CustomDataset):
    CLASSES = ('background', 'LV')

    PALETTE = [[120, 120, 120], [6, 230, 230]]

    def __init__(self, **kwargs):
        super(Siren, self).__init__(
            img_suffix='.mat',
            seg_map_suffix='_label.png',
            reduce_zero_label=False,
            **kwargs)
        assert osp.exists(self.img_dir)