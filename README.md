Image style transfer at Django
----------

This repository is Image style transfer processing at Django on WebAPI.

version:
- python3.x
- Keras2.1.5
- tensorflow1.6 

example:

run API
```
python manage.py runserver 0:8000
```

POST data
```
{
image:"Picture"
}
```

Response
```
{
image:"after processing image(base64encode)"
}
```

[Referrence repository](https://github.com/misgod/fast-neural-style-keras)


