#Get Api and Post parameters to Api
-----------------------------------

def login_api(request):
    if request.method == 'GET':
        url = 'example url'
        params = json.dumps({"userName":"root","userPwd":"pass"})
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(url,data=params, headers=headers)
        except Exception as e:
            response = None
            return HttpResponse(response.content,status=200) 

        print response.content
        return HttpResponse(response.content,status=200)





