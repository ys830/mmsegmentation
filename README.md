## Introduction
Our model comes from the MMSegmentation library.
In order to use MMsegmentation, please follow the official tutorial : https://github.com/open-mmlab/mmsegmentation#readme

## Download
### Dataset
* Stanford Healthcare provides an open source cardiac echocardiography dataset, containing 10,030 apical-4-chamber echocardiography videos. The dataset is publicly available at https://echonet.github.io/dynamic/

* Based on the video dataset, we proposed a dataset of 1047 images, each image was manually annotated left and right ventricles. The dataset is available [here](https://drive.google.com/file/d/1jaUxbOPbxAbNiGahtUG7x7pBTclfzAvv/view?usp=sharing)

* Download the dataset and extract it into `./data/`, without creating subfolders.

### Pretrained models
* Pretrained models can be downloaded [here](https://drive.google.com/file/d/1aL4No8AU27stPCk-_q1KDEVpTUtOlJoT/view?usp=sharing). To reproduce the results, the pretrained models(*.pth) should be placed in `./pretrained/`, and then test model directly

## Run code
### Training
* Train the `deeplabv3_unet_s5-d16` model:
```shell
python tools/train.py configs/unet/deeplabv3_unet_s5-d16_128x128_40k_Car_0505.py --work-dir=pretrained/2class_cardiac
```

### Testing
* For testing, run:
```shell
python tools/test.py configs/unet/deeplabv3_unet_s5-d16_128x128_40k_Car_0505.py\
    pretrained/2class_cardiac/latest.pth \
    --show-dir results
```
* To reproduce the results, move the pretrained models(*.pth) downloaded from [here](https://drive.google.com/file/d/1aL4No8AU27stPCk-_q1KDEVpTUtOlJoT/view?usp=sharing) to `./pretrained/`, and then test model directly.

## Other scripts
### Calculate mean & std
* Calculate the `mean` and `std` of custom dataset:
```shell
python ./get_mean.py ${img_pth} 
```
### Save video
* Save the output image sequence as a video:
```shell
python ./save_video.py ${original_pth} ${target_pth}
```


