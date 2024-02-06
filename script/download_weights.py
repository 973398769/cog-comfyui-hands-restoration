import os

# Clone ComfyUI repo
os.system("git clone https://github.com/comfyanonymous/ComfyUI.git")
os.system("mkdir -p models/checkpoints")

# TODO: See if linking from ComfyUI/models/checkpoints to models/checkpoints works
os.system("rm -rf ComfyUI/models/checkpoints")
os.system("ln -s /src/models/checkpoints ComfyUI/models/checkpoints")

# Download model weights
os.system("wget https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11p_sd15_openpose.pth -P models/checkpoints/")
os.system("wget https://huggingface.co/Justin-Choo/epiCRealism-Natural_Sin_RC1_VAE/blob/main/epicrealism_naturalSinRC1VAE.safetensors -P models/checkpoints/")

