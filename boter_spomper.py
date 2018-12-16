import vk_api
vk_session = vk_api.VkApi('markk.99@mail.ru', '12moroz12')
vk_session.auth()
vk = vk_session.get_api()

def addComment(post) :
    for id in post :
        vk.wall.createComment(post_id=id, message='очень круто')

def postID(groups) :
    id_post = {}
    c = 0
    
    for grop in groups :
        data = vk.wall.get(owner_id=-grop, count=5, offset=0)
        for key in data['items'] :
            print(key)
        
    print(id_post)             
                               

                          
def searchGroupID(word) :
    id_group = []
    search = vk.groups.search(q=word)
    for key in search['items'] :
        for name, data in key.items() :
            if name == 'id' :
                id_group.append(data)
    postID(id_group)
    
searchGroupID('жизнь')
