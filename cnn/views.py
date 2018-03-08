# Create your views here.
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.http import JsonResponse
import os
from PIL import Image

from .transform_django import main

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/image/post/'
@csrf_exempt
def api(request):
    if request.method != 'POST':
        c = {}
        c.update(csrf(request))
        return JsonResponse({"status": "Your request is not post request."})

    file = request.FILES["image"]

    path = os.path.join(UPLOADE_DIR, file.name)
    destination = open(path, 'wb')
    extension = file.name
    extension = extension.split(".")
    if extension[1] != "jpg":  # jpgファイルじゃない時はメッセージを返す
        HttpResponse("The extension of this file is not .jpg")

    for chunk in file.chunks():
        destination.write(chunk)

    else:
        style = "yasei"
        input_file = file.name
        output = None  # output file name without extension
        original_color = 0  # 0~1
        blend_alpha = 0  # 0~1
        image_size = 256  # default: 256

        # 画風変換後の画像のパスが返ってくる
        img_path = main(style=style, input_file=path, output_file=output, original_color=original_color, blend_alpha=blend_alpha)
        img_path = os.path.abspath(os.path.join("static/images/post/" + img_path))
        with open(img_path, "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")

def line(request):
    return HttpResponse('This is a response for request from LINE Messaging API.')