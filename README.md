# Advancing Multimodal Large Language Models in Chart Question Answering with Visualization-Referenced Instruction Tuning

## Release
* We have released all the code and datasets used in our paper.
* The generated data and selected benchmark can be downloaded in the [huggingface link](https://huggingface.co/datasets/lewy666/ChartInstructionData).
* Our model weights are available at the [huggingface link](https://huggingface.co/lewy666/llava-hr-ChartInstruction/tree/main).
## To-dos
- [ ] Write a walk-through tutorial about this repo.
- [ ] Need fix: some library paths and relevant file paths may be wrong. 

## Evaluation
You can run our evaluation bash scripts `scripts/*.sh`.


## CLI Inference
Here is the command for chatting with our model without the need for a Gradio interface.
```
python -m model/high_resolution/llava_hr.serve.cli \
    --model-path ./checkpoints/llava-hr-ChartInstruction \
    --image-file "*.jpg" 
```
## Usage and License Notices: 
* For the base model llava: This project utilizes certain datasets and checkpoints that are subject to their respective original licenses. Users must comply with all terms and conditions of these original licenses, including but not limited to the OpenAI Terms of Use for the dataset and the specific licenses for base language models for checkpoints trained using the dataset (e.g. Llama community license for LLaMA-2 and Vicuna-v1.5). 

## Acknowledgement
- [Vicuna](https://github.com/lm-sys/FastChat): the codebase LLaVA built upon. LLaVA's base language model is Vicuna-13B.
- [LLaVA](https://github.com/haotian-liu/LLaVA): the codebase we built upon. LLaVA was the only open-sourced project with all training code open-sourced when we started this work.
- [LLaVA-HR](https://github.com/luogen1996/LLaVA-HR): the high-resolution version model we built upon. 
- [SemDeDup](https://github.com/facebookresearch/SemDeDup): the sampling module we are based on. SemDeDup is designed for hundred million of image sampling.
- [WYTIWYR](https://github.com/SerendipitysX/WYTIWYR): Part of data our classification are collected from here.
- [Unichart](https://github.com/vis-nlp/UniChart): Part of existing data are first collected by Unichart.

## Contact
If you have any questions about this work, please email Xingchen Zeng at xingchen.zeng@outlook.com.
