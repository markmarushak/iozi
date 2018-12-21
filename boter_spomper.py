import vk_api

vk_session = vk_api.VkApi('markk.99@mail.ru', '12moroz12')
vk_session.auth()
vk = vk_session.get_api()

def addComment(post) :
    print(post)
    for p in post :
        vk.wall.createComment(owner_id=p.get(1),post_id=p.get(0), message='очень круто')

def postID(groups) :
    id_post=[]
    for grop in groups :
        data = vk.wall.get(owner_id=-grop, count=2, offset=0)
        item = data['items']
        for k in item :
            id_post.append({0:k.get('id'),1:k.get('owner_id')})

    return addComment(id_post)            
                               

''' здесь все работает - это поиск груп по запросу НИШТЯК ОЧЕНЬ ПРИЯТНО НАБЛЮДАТЬ '''                          
def searchGroupID(word) :
    id_group = []
    search = vk.groups.search(q=word, count=3, offset=0)
    for key in search['items'] :
        for name, data in key.items() :
            if name == 'id' :
                id_group.append(data)
    return postID(id_group)
    
searchGroupID('жизнь')
