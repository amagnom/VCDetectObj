from structure_code import utils


def __image(image_path):
    image_np = utils.load_image_into_numpy_array(image_path)

    # Flip horizontally
    utils.flip_image(image_np)

    # Convert image to grayscale
    utils.convert_gray_scale(image_np)
    return image_np


if __name__ == '__main__':
    # PASS THE PATH FROM IMAGE HERE:
    # image_path = "https://comparaplano.com.br/wp-content/uploads/2019/09/dog-tv.png"
    image_path = "./images/img1.jpg"
    image_np = __image(image_path)

    inference = utils.inference(image_np)
    utils.visualizing_result(image_np, inference)
    print("Resultado gerado na pasta results")
