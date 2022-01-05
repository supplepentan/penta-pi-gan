# Usage
git clone https://github.com/supplepentan/penta-pi-gan.git
cd penta-pi-gan
wsl
python -m venv venv-wsl
venv-wsl/bin/activate
python -m pip install -U pip setuptools
python -m pip install -r requirements.txt
python setup.py

# Command
## マルチビュー画像を作成（CelebA）
python render_multiview_images.py CelebA/generator.pth --curriculum CelebA --seeds 0 1 2 3
## ビデオを作成（CelebA）
python render_video.py CelebA/generator.pth --curriculum CelebA --seeds 0 1 2 3 --image_size 128
## 複数の動画補間ビデオを作成（CelebA）
python render_video_interpolation.py CelebA/generator.pth --curriculum CelebA --seeds 5 0 4 16 2 19 5 --image_size 128
## 複数の動画補間ビデオを作成（Cats）
python render_video_interpolation.py Cats/generator.pth --curriculum CelebA --seeds 0 4 8 5 9 1 0 --image_size 128
## 複数の動画補間ビデオを作成（CARLA）
python render_video_interpolation.py CARLA/generator.pth --curriculum CARLA --seeds 1 2 3 5 6 8 1 --image_size 64
 

# Original
https://marcoamonteiro.github.io/pi-GAN-website/