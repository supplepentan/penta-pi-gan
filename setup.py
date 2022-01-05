# 学習済みモデルのダウンロード
import gdown
import subprocess

gdown.download('https://drive.google.com/uc?id=1bRB4-KxQplJryJvqyEa8Ixkf_BVm4Nn6', './CelebA.zip', quiet=False)
subprocess.run(["unzip", "CelebA.zip"])
gdown.download('https://drive.google.com/uc?id=1WBA-WI8DA7FqXn7__0TdBO0eO08C_EhG', './Cats.zip', quiet=False)
subprocess.run(["unzip", "Cats.zip"])
gdown.download('https://drive.google.com/uc?id=1n4eXijbSD48oJVAbAV4hgdcTbT3Yv4xO', './CARLA.zip', quiet=False)
subprocess.run(["unzip", "CARLA"])