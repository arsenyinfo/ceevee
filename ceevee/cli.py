from fire import Fire
from tqdm import tqdm

from ceevee import MODELS
from ceevee.utils import jsonify, read_img


def main(task, *imgs):
    result = []
    model = MODELS[task]()
    for path in tqdm(imgs):
        img = read_img(path)
        pred = model(img)
        pred['path'] = path
        result.append(pred)

    print(jsonify(result))


if __name__ == '__main__':
    Fire(main)
