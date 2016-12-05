MODE = 'hs'

SOURCE_VOCAB_SIZE = 341 # 2492 # 5980
TARGET_VOCAB_SIZE = 556 # 2110 # 4830 #
RULE_NUM = 100 # 228
NODE_NUM = 70

NODE_EMBED_DIM = 256
EMBED_DIM = 256
RULE_EMBED_DIM = 256
QUERY_DIM = 256
LSTM_STATE_DIM = 256
DECODER_ATT_HIDDEN_DIM = 50
POINTER_NET_HIDDEN_DIM = 50

MAX_QUERY_LENGTH = 70
MAX_EXAMPLE_ACTION_NUM = 350

DECODER_DROPOUT = 0.2
WORD_DROPOUT = 0

# training
TRAIN_PATIENCE = 10
MAX_EPOCH = 70
BATCH_SIZE = 10
VALID_PER_MINIBATCH = 160
SAVE_PER_MINIBATCH = 160

# decoding
BEAM_SIZE = 50
DECODE_MAX_TIME_STEP = 350

from collections import OrderedDict
config_info = OrderedDict([(v, globals()[v]) for v in dir() if not v.startswith('__')])

# define actions
APPLY_RULE = 0
GEN_TOKEN = 1
COPY_TOKEN = 2
GEN_COPY_TOKEN = 3

ACTION_NAMES = {APPLY_RULE: 'APPLY_RULE',
                GEN_TOKEN: 'GEN_TOKEN',
                COPY_TOKEN: 'COPY_TOKEN',
                GEN_COPY_TOKEN: 'GEN_COPY_TOKEN'}