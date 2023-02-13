# Speech-to-Image

<details>
  <summary>Table of Contents</summary>
    <ol>
        <li>
            <a href="#Introduction">Introduction</a>
        </li>
        <li>
          <a href="#Step-1 Speech to Text">Speech to Text</a>
	  <ul>
                <li><a href="##Transformer Model Architecture">Transformer Architecture</a></li>
          </ul>
        </li>
        <li>
            <a href="#Step-2 Text to Image">Text to Image</a>
            <ul>
                <li><a href="#About Dataset">Dataset</a></li>
                <li><a href="#Text Embedding Model">Text Embedding Model</a></li>
		<li><a href="## Architecture">Architecture</a></li>
            </ul>	
        </li>
        <li>
            <a href="#### References">References</a> 
        </li> 
    </ol>
</details>

# Introduction
In this project we attempt to translate the speech signals into image signals in two steps. The speech signal is converted into text with the help of Automatic speech recognition (ASR) and then high-quality images are generated from the text descriptions by using StackGAN.

# Step-1 Speech to Text
Automatic speech recognition (ASR) consists of transcribing audio speech segments into text. ASR can be treated as a sequence-to-sequence problem, where the audio can be represented as a sequence of feature vectors and the text as a sequence of characters, words, or subword tokens.

The Dataset we are using is the [<b>LJSpeech dataset</b>](https://keithito.com/LJ-Speech-Dataset/) from the LibriVox project. It consists of short audio clips of a single speaker reading passages from 7 non-fiction books. Our model is similar to the original Transformer (both encoder and decoder) as proposed in the paper,[<b> "Attention is All You Need"</b>](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf).

## Transformer Model Architecture
<img src="./Images/Transformer_Architecture.png" width="428px" height="521px"/>

# Step-2 Text to Image


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
#### References
1. <b>Attention is All You Need</b> [[Arxiv Link](https://arxiv.org/abs/1706.03762)]
2. <b>Very Deep Self-Attention Networks for End-to-End Speech Recognition</b> [[Arxiv Link](https://arxiv.org/pdf/1904.13377.pdf)]
3. <b>Speech-Transformer</b> [[IEEE Xplore](https://ieeexplore.ieee.org/document/8462506)]
4. **StackGAN: Text to photo-realistic image synthesis** [[Arxiv Link](https://arxiv.org/pdf/1612.03242.pdf)]
---
