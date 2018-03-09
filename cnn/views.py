# Create your views here.
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.http import JsonResponse
import os
from PIL import Image
from django.views.decorators.http import require_POST
from base64 import b64encode
from .transform_django import main

UPLOADE_DIR = os.path.dirname(os.path.abspath(__file__)) + '/static/images/post/'
@require_POST
@csrf_exempt
def api(request):
    if request.method != 'POST':
        c = {}
        c.update(csrf(request))
        return JsonResponse({"status": "Your request is not post request."})

    file = request.FILES["image"]
    path = os.path.join(UPLOADE_DIR, file.name)
    img = Image.open(file)
    img.save(path)
    style = "yasei"
    input_file = path
    output = None  # output file name without extension
    original_color = 0  # 0~1
    blend_alpha = 0  # 0~1
    image_size = 256  # default: 256

    # 画風変換後の画像のパスが返ってくる
    img_path = main(style=style, input_file=input_file, output_file=output, original_color=original_color, blend_alpha=blend_alpha)
    #img_path = os.path.dirname(os.path.abspath(__file__))+"/transfer/" + img_path
    with open("/home/junichi200123/cnn-django/cnn/output.jpg", "rb") as f:
        byte_content = f.read()
    base64_bytes = b64encode(byte_content)
    base64_string = base64_bytes.decode("utf-8")
    return JsonResponse({"image":base64_string})

def line(request):
    return HttpResponse('This is a response for request from LINE Messaging API.')
