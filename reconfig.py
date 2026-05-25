import json
import random
from pathlib import Path


SEED = 42
DEV_RATIO = 0.1

random.seed(SEED)


TRAIN_FILE = "train_vimqa.json"
TEST_FILE = "test_vimqa.json"


with open(
    TRAIN_FILE,
    encoding="utf8"
) as f:

    train_data = json.load(f)


random.shuffle(train_data)


n = len(train_data)

dev_size = int(
    n * DEV_RATIO
)


dev_data = train_data[:dev_size]

new_train_data = train_data[dev_size:]


with open(
    "vimqa_train.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        new_train_data,
        f,
        ensure_ascii=False,
        indent=2
    )


with open(
    "vimqa_dev.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        dev_data,
        f,
        ensure_ascii=False,
        indent=2
    )


with open(
    TEST_FILE,
    encoding="utf8"
) as f:

    test_data = json.load(f)


with open(
    "vimqa_test.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        test_data,
        f,
        ensure_ascii=False,
        indent=2
    )


print(
    "Train:",
    len(new_train_data)
)

print(
    "Dev:",
    len(dev_data)
)

print(
    "Test:",
    len(test_data)
)

print()

print(
    "Created:"
)

print(
    "vimqa_train.json"
)

print(
    "vimqa_dev.json"
)

print(
    "vimqa_test.json"
)