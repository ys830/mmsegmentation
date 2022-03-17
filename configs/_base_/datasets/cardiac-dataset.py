dataset_type = 'renewCardiac2'
data_root = './data/renewCardiacdataset2'
img_norm_cfg = dict(
    mean=[32.996, 32.714, 32.581, 32.996, 32.714, 32.581, 32.996, 32.714, 32.581],
    std=[50.182, 49.895, 49.808, 50.182, 49.895, 49.808, 50.182, 49.895, 49.808],
    to_rgb=False)
# img_scale = (960, 999)
img_scale = (112, 112)
# crop_size = (128, 128)
crop_size = (112, 112)
train_tif_pipeline = [
    dict(type='LoadTIFImageFromFile'),
    dict(type='LoadAnnotations'),
    dict(type='Resize', img_scale=img_scale, ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0),
    # dict(type='PhotoMetricDistortion'),
    # dict(type='TiffNormalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg'])
]
test_tif_pipeline = [
    dict(type='LoadTIFImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=img_scale,
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img'])
        ])
]

data = dict(
    samples_per_gpu=4,
    workers_per_gpu=4,
    train=dict(
        type='RepeatDataset',
        times=40000,
        dataset=dict(
            type=dataset_type,
            data_root=data_root,
            img_dir='img_dir/TRAIN',
            ann_dir='ann_dir/TRAIN',
            pipeline=train_tif_pipeline)),
    val=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/VAL',
        ann_dir='ann_dir/VAL',
        pipeline=test_tif_pipeline),
    test=dict(
        type=dataset_type,
        data_root=data_root,
        img_dir='img_dir/TEST',
        ann_dir='ann_dir/TEST',
        pipeline=test_tif_pipeline))