import os
import torch
DATA_DIR = '../input/'
OUT_DIR = '../result/'
MODEL_DIR = '../models/'
GAN_CHECKPOINT_DIR = '../checkpoint/'
AE_CHECKPOINT_DIR = '../ae_checkpoint'

TRAIN_DIR = DATA_DIR+"asoul128/"  # UPDATE
TEST_DIR = DATA_DIR+"test/" # UPDATE

os.makedirs(TRAIN_DIR, exist_ok=True)
os.makedirs(TEST_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(GAN_CHECKPOINT_DIR, exist_ok=True)
os.makedirs(AE_CHECKPOINT_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

# DATA INFORMATION
IMAGE_SIZE = 128 #初始是224
BATCH_SIZE = 1
GRADIENT_PENALTY_WEIGHT = 10
NUM_EPOCHS = 1000#初始是10
KEEP_CKPT = 2 #init 2
# save_model_path = MODEL_DIR

if torch.cuda.is_available():
  DEVICE = torch.device('cuda')
  print(DEVICE)
else:
  assert False
  DEVICE = 'cpu'

