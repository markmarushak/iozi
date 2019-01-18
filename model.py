import vk_api
from db import aut

id_group = []
id_post = []

def auth() :
    login,password = aut[0]['account'][aut[0]['count']]['login'],aut[0]['account'][aut[0]['count']]['pass']
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    v_k = vk_session.get_api()
    if aut[0]['count'] == 3 :
        aut[0]['count'] = 0
    else :
        aut[0]['count'] = aut[0]['count']+1
    print('connect account')
    return v_k

vk = auth()

def checkIsClose(key) :
    value = key.get('is_closed')
    if value == 0 :
        return 'true'
    else :
        return 'false'

def addComment(post) :
        print(post)
        # report.write('https://vk.com/'+id.get(2))
        # vk.wall.createComment(post_id=id, message='очень круто')

def postID(groups) :
    data = 0
    try:
        data = vk.wall.get(owner_id=-groups, count=10, offset=0)
    except :
        pass

    if data == 0:
        auth()
        data = vk.wall.get(owner_id=-groups, count=10, offset=0)

    for key in data['items'] :
        id_post.append({0: key.get('owner_id'), 1: key.get('id')})

def searchGroupID(word) :
    search = vk.groups.search(q=word, count=1000, offset=0)
    for key in search['items']:
        if (checkIsClose(key)) :
            id_group.append({0: key.get('id'), 1: key.get('screen_name')})

