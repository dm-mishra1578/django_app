

class CustomHeaderMiddleware :
    def __init__(self,get_response):
        print("Custome__init__")
        self.get_response = get_response
    
    def __call__(self, request):
        print("Custome __call__")
        response = self.get_response(request)
        response['X-Custom-Header']="My Custome value"
        return response