from rest_framework.renderers import JSONRenderer


class AppJSONRenderer(JSONRenderer):
    # force DRF to add charset header to the content-type
    charset = 'utf-8'
