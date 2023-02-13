# Speech_to_Image

## Synthesizing high-quality images from text descriptions


### Create 3 folders (test, weights,results_stage2) in your current working directory.
1. <b>weights </b> (your model weights will be saved here)
2. <b>test </b> (generated images from our stage I GAN)
3. <b>results_stage2 </b> (generated images from stage II fo GAN)
---
## About Dataset

#### Dataset Name: CUB_200_2011

Download from : https://data.caltech.edu/records/65de6-vp158

#### Text Embedding Model
Download char-CNN-RNN text embeddings for birds from : https://github.com/hanzhanggit/StackGAN

1. char-CNN-RNN-embeddings.pickle — Dataframe for the pre-trained embeddings of the text.
2.  filenames.pickle — Dataframe containing the filenames of the images.
3. class_info.pickle — Dataframe containing the info of classes for each image.

---
## Architecture
<img src="./Images/text_to_image_architecture.jpg" width="850px" height="370px"/>

- Stage 1
	- Text Encoder Network
		- Text description to a 1024 dimensional text embedding
		- Learning Deep Representations of Fine-Grained Visual Descriptions [Arxiv Link](https://arxiv.org/abs/1605.05395)
	- Conditioning Augmentation Network
		- Adds randomness to the network
		- Produces more image-text pairs
	- Generator Network
	- Discriminator Network
	- Embedding Compressor Network
	- Outputs a 64x64 image
#
- Stage 2
	- Text Encoder Network
	- Conditioning Augmentation Network
	- Generator Network
	- Discriminator Network
	- Embedding Compressor Network
	- Outputs a 256x256 image

---
#### Reference Papers
1. **StackGAN: Text to photo-realistic image synthesis** [[Arxiv Link](https://arxiv.org/pdf/1612.03242.pdf)]
---
